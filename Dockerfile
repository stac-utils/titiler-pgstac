FROM tiangolo/uvicorn-gunicorn:python3.8

ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt

# Install stac-fastapi. This is optional but enables to launch a stac api in parallel
RUN pip install stac-fastapi.api~=2.0 stac-fastapi.types~=2.0 stac-fastapi.extensions~=2.0 stac-fastapi.pgstac~=2.0

# Install TiTiler pgstac
COPY src/titiler/ /tmp/titiler/
RUN pip install /tmp/titiler/pgstac --no-cache-dir

RUN rm -rf /tmp/titiler

ENV MODULE_NAME titiler.pgstac.main
ENV VARIABLE_NAME app
