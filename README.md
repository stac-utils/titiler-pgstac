<p align="center">
  <img width="500" src="https://github.com/stac-utils/titiler-pgstac/assets/10407788/24a64ea9-fede-4ee8-ab8d-625c9e94db44"/>
  <p align="center">Connect PgSTAC and TiTiler.</p>
</p>

<p align="center">
  <a href="https://github.com/stac-utils/titiler-pgstac/actions?query=workflow%3ACI" target="_blank">
      <img src="https://github.com/stac-utils/titiler-pgstac/workflows/CI/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/stac-utils/titiler-pgstac" target="_blank">
      <img src="https://codecov.io/gh/stac-utils/titiler-pgstac/branch/main/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/titiler.pgstac" target="_blank">
      <img src="https://img.shields.io/pypi/v/titiler.pgstac?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/stac-utils/titiler-pgstac/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/stac-utils/titiler-pgstac.svg" alt="License">
  </a>
</p>

---

**Documentation**: <a href="https://stac-utils.github.io/titiler-pgstac/" target="_blank">https://stac-utils.github.io/titiler-pgstac/</a>

**Source Code**: <a href="https://github.com/stac-utils/titiler-pgstac" target="_blank">https://github.com/stac-utils/titiler-pgstac</a>

---

**TiTiler-PgSTAC** is a [TiTiler](https://github.com/developmentseed/titiler) extension that connects to a [PgSTAC](https://github.com/stac-utils/pgstac) database to create dynamic **mosaics** based on [search queries](https://github.com/radiantearth/stac-api-spec/tree/master/item-search).

## Installation

To install from PyPI and run:

```bash
# Make sure to have pip up to date
python -m pip install -U pip

# Install `psycopg` or `psycopg["binary"]` or `psycopg["c"]`
python -m pip install psycopg["binary"]

python -m pip install titiler.pgstac
```

To install from sources and run for development:

We recommand using [`uv`](https://docs.astral.sh/uv) as project manager for development.

See https://docs.astral.sh/uv/getting-started/installation/ for installation 

```
git clone https://github.com/stac-utils/titiler-pgstac.git
cd titiler-pgstac

uv sync --extra psycopg 
```

### `PgSTAC` version

`titiler.pgstac` depends on `pgstac >=0.3.4` (https://github.com/stac-utils/pgstac/blob/main/CHANGELOG.md#v034).

In theory, pgstac version `>=0.3.4` should be supported by titiler-pgstac but `old` version might fail or require old Postgres version (see https://github.com/stac-utils/titiler-pgstac/issues/252). 

Here are the versions **officially** (tested) supported:

| titiler-pgstac Version  |      pgstac |
|                       --|           --|
|                    <1.0 | >=0.7,<0.8  |
|              >=1.0,<2.1 | >=0.8,<0.10 |
|                   >=2.1 | >=0.9,<0.10 |

### `psycopg` requirement

`titiler.pgstac` depends on the `psycopg` library. Because there are three ways of installing this package (`psycopg` or , `psycopg["c"]`, `psycopg["binary"]`), the user must install this separately from `titiler.pgstac`.

- `psycopg`: no wheel, pure python implementation. It requires the `libpq` installed in the system.
- `psycopg["binary"]`: binary wheel distribution (shipped with libpq) of the `psycopg` package and is simpler for development. It requires development packages installed on the client machine.
- `psycopg["c"]`: a C (faster) implementation of the libpq wrapper. It requires the `libpq` installed in the system.

`psycopg[c]` or `psycopg` are generally recommended for production use.

In `titiler.pgstac` setup.py, we have added three options to let users choose which psycopg install to use:

- `python -m pip install titiler.pgstac["psycopg"]`: pure python
- `python -m pip install titiler.pgstac["psycopg-c"]`: use the C wrapper (requires development packages installed on the client machine)
- `python -m pip install titiler.pgstac["psycopg-binary"]`: binary wheels

### Prometheus metrics

Install the optional metrics extra and enable it:

```bash
python -m pip install titiler-pgstac[metrics]
export TITILER_PGSTAC_API_METRICS_ENABLED=TRUE
```

Once enabled, `/metrics` is available on startup and records:

- `titiler_pgstac_http_requests_total{operation,method,status}`
- `titiler_pgstac_http_request_duration_seconds{operation,method}`

`operation` values are low-cardinality labels such as `landing`, `conformance`,
`tiles`, `point`, `search`, `search_info`, `collection`, `item`, `register_search`,
`list_searches`, `external`, `tms`, `algorithms`, `colormaps`, `other`, and
`unknown`. `status` is grouped (`2xx`, `3xx`, `4xx`, `5xx`). `/healthz` and the
scrape endpoint are excluded from request counters. Untemplated paths (for example
bare 404s) are also ignored.

With `TITILER_PGSTAC_API_METRICS_ENABLED` left at its default (`FALSE`), `/metrics`
is not registered even if the extra is installed.

#### Multi-worker deployments

For multi-worker deployments (for example `uvicorn --workers N` or Gunicorn), set
`PROMETHEUS_MULTIPROC_DIR` to an existing writable directory **before** the
application is imported, and clear that directory before each server start.

```bash
export PROMETHEUS_MULTIPROC_DIR=/tmp/titiler-pgstac-prometheus
mkdir -p "$PROMETHEUS_MULTIPROC_DIR"
rm -rf "$PROMETHEUS_MULTIPROC_DIR"/*
```

With Gunicorn, also mark workers dead on exit so stale metric files are cleaned up:

```python
from prometheus_client import multiprocess


def child_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)
```

#### Custom apps

Custom apps can enable the same instrumentation:

```python
from titiler.pgstac.metrics import instrument_app

instrument_app(app)
```

## Launch

You'll need to have `PGUSER`, `PGPASSWORD`, `PGDATABASE`, `PGHOST`, `PGPORT` variables set in your environment pointing to your Postgres database where pgstac has been installed.

```
export PGUSER=username
export PGPASSWORD=password
export PGDATABASE=postgis
export PGHOST=database
export PGPORT=5432
```

```
$ python -m pip install uvicorn
$ uvicorn titiler.pgstac.main:app --reload
```

### Using Docker

```
$ git clone https://github.com/stac-utils/titiler-pgstac.git
$ cd titiler-pgstac
$ docker compose up --build tiler
# or
$ docker compose up --build tiler-uvicorn
```

## Contribution & Development

See [CONTRIBUTING.md](https://github.com//stac-utils/titiler-pgstac/blob/main/CONTRIBUTING.md)

## License

See [LICENSE](https://github.com//stac-utils/titiler-pgstac/blob/main/LICENSE)

## Authors

See [contributors](https://github.com/stac-utils/titiler-pgstac/graphs/contributors) for a listing of individual contributors.

## Changes

See [CHANGES.md](https://github.com/stac-utils/titiler-pgstac/blob/main/CHANGES.md).
