FROM tiangolo/uvicorn-gunicorn:python3.8

ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt

# Install TiTiler pgstac
COPY titiler/ /tmp/titiler/
COPY setup.py /tmp/setup.py
COPY setup.cfg /tmp/setup.cfg
COPY README.md /tmp/README.md

RUN cd /tmp && pip install .[psycopg2] --no-cache-dir
RUN rm -rf /tmp/titiler

ENV MODULE_NAME titiler.pgstac.main
ENV VARIABLE_NAME app
