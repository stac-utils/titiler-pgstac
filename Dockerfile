FROM tiangolo/uvicorn-gunicorn:python3.8

ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt

# Install TiTiler pgstac
COPY src/titiler/ /tmp/titiler/
RUN pip install /tmp/titiler/pgstac --no-cache-dir
RUN rm -rf /tmp/titiler

ENV MODULE_NAME titiler.pgstac.main
ENV VARIABLE_NAME app
