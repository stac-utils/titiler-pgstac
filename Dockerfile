FROM cgr.dev/chainguard/wolfi-base:latest@sha256:28c39be5a5e1e9b85081c10740e8495f6518a865b23bc6a486637c4b21e74b43 AS base

ARG PYTHON_VERSION=3.14

ENV PYTHONUNBUFFERED=1

# Install runtime dependencies. Versions deliberately unpinned: Wolfi rolls
# forward and garbage-collects old versions, so an "=<version>" pin breaks the
# build within days. The guardrails are the version-scoped names plus the
# digest above. No pip: uv (below) installs everything.
#   libstdc++  NOT optional: the rasterio/pyproj/duckdb manylinux wheels list
#              libstdc++.so.6 in DT_NEEDED and auditwheel does not vendor it.
#   bash, tzdata, curl  parity with the old Debian base: /bin/sh is busybox,
#              Wolfi ships no /usr/share/zoneinfo, curl is for in-pod debugging.
#   libpq-18   for psycopg[c], compiled in the builder stage: an OS package,
#              so Wolfi patches it. Same major as postgresql-18-dev below.
RUN apk add --no-cache \
      python-${PYTHON_VERSION} \
      libstdc++ bash tzdata curl libexpat1 libpq-18

# uv as a pass-through stage rather than a direct COPY --from=<image>:
# Dependabot only parses FROM lines (dependabot/dependabot-core#5103), so this
# keeps the version pinned *and* auto-updated by the docker ecosystem.
FROM ghcr.io/astral-sh/uv:0.13.10@sha256:a3ea1357342c1a4bf9a0c53a3deb1b55379aefa037338d8113d5771efa01774f AS uv

# Build stage
FROM base AS builder

ARG PYTHON_VERSION

# Builder only, to compile psycopg[c] from its sdist: C toolchain, Python
# headers, and libpq headers + pg_config (via postgresql-18-dev).
RUN apk add --no-cache build-base python-${PYTHON_VERSION}-dev postgresql-18-dev

# Install uv
COPY --from=uv /uv /uvx /usr/local/bin/

# Configure uv-managed virtual environment
#   UV_PYTHON: the apk python's version, but resolved by uv (not the apk
#     binary itself: Wolfi's rolling python-3.14 build has repeatedly required
#     a newer glibc than the glibc package available in the same repo snapshot,
#     making /usr/bin/python3.14 unable to import stdlib extension modules).
#     uv instead downloads its own self-contained, statically-linked build.
#   UV_PYTHON_INSTALL_DIR: put that managed interpreter next to /opt/venv (both
#     get copied into the runtime stage below) — otherwise it lands under
#     /root/.local/share/uv, which never reaches the runtime stage, leaving
#     /opt/venv/bin/python (and every venv script's shebang, eg uvicorn) a
#     dangling symlink: `exec .../uvicorn: no such file or directory`.
#   UV_COMPILE_BYTECODE: .pyc at install time, as pip did, so cold starts
#     don't pay the compile on first import
ENV UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    UV_PYTHON=${PYTHON_VERSION} \
    UV_PYTHON_INSTALL_DIR=/opt/uv-python \
    UV_COMPILE_BYTECODE=1 \
    PATH="/opt/venv/bin:${PATH}"

# Copy project metadata and dependencies
COPY pyproject.toml uv.lock README.md LICENSE ./
RUN uv sync --frozen --no-dev --group server --extra psycopg-c --extra metrics --extra telemetry --no-install-project

# Copy and install runtime source code to the builder image
COPY titiler/ titiler/
RUN uv pip install --no-deps --no-editable .

# uv skips downloading its own managed interpreter when the apk python already
# satisfies UV_PYTHON, leaving UV_PYTHON_INSTALL_DIR absent. Make sure it
# exists (even empty) so the unconditional COPY below never fails.
RUN mkdir -p /opt/uv-python

# Runtime stage
FROM base

# Set runtime labels
LABEL org.opencontainers.image.source="https://github.com/stac-utils/titiler-pgstac"
LABEL org.opencontainers.image.description="TiTiler PgSTAC"
LABEL org.opencontainers.image.licenses="MIT"

# The chart execs `command: ["uvicorn"]` — a bare binary, resolved against the
# image's PATH.
ENV PATH="/opt/venv/bin:${PATH}"

# Copy virtual environment and its interpreter from builder
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /opt/uv-python /opt/uv-python

# Fail the build if psycopg is not the C implementation or cannot load libpq
RUN python -c "import psycopg; assert psycopg.pq.__impl__ == 'c', psycopg.pq.__impl__; print('libpq', psycopg.pq.version())"

WORKDIR /tmp

# Run as the wolfi-base nonroot user (uid 65532). On Kubernetes the chart sets 
# the net.ipv4.ip_unprivileged_port_start sysctl per pod. 
# Other deployments must allow unprivileged low ports the same way,
# or override PORT to something >=1024.
USER nonroot

###################################################
# For compatibility (might be removed at one point)
ENV MODULE_NAME=titiler.pgstac.main
ENV VARIABLE_NAME=app
ENV HOST=0.0.0.0
ENV PORT=80
ENV WEB_CONCURRENCY=1
CMD gunicorn -k uvicorn.workers.UvicornWorker ${MODULE_NAME}:${VARIABLE_NAME} --bind ${HOST}:${PORT} --workers ${WEB_CONCURRENCY}
