FROM tiangolo/uvicorn-gunicorn:python3.8

ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt

WORKDIR /tmp

COPY titiler/ titiler/
COPY setup.py setup.py
COPY setup.cfg setup.cfg
COPY README.md README.md

RUN pip install --no-cache-dir --upgrade .["psycopg-binary"]
RUN rm -rf titiler/ setup.py setup.cfg README.md

ENV MODULE_NAME titiler.pgstac.main
ENV VARIABLE_NAME app
