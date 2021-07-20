FROM tiangolo/uvicorn-gunicorn:python3.8

ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt

# TMP, waiting for stac-fastapi release
RUN pip install -e git+https://github.com/stac-utils/stac-fastapi.git#egg=stac_fastapi&subdirectory=stac_fastapi/api \
    && pip install git+https://github.com/stac-utils/stac-fastapi.git#egg=stac_fastapi.types&subdirectory=stac_fastapi/types \
    && pip install git+https://github.com/stac-utils/stac-fastapi.git#egg=stac_fastapi.extensions&subdirectory=stac_fastapi/extensions \
    && pip install git+https://github.com/stac-utils/stac-fastapi.git#egg=stac_fastapi.pgstac&subdirectory=stac_fastapi/pgstac

RUN pip install titiler.core titiler.mosaic

# TiTiler
COPY src/titiler/ /tmp/titiler/
RUN pip install /tmp/titiler/pgstac --no-cache-dir

RUN rm -rf /tmp/titiler

ENV MODULE_NAME titiler.pgstac.main
ENV VARIABLE_NAME app
