<p align="center">
  <img src="https://user-images.githubusercontent.com/10407788/132182694-52cd3d02-5b80-4bb0-9102-b98272fae0f9.png"/>
  <p align="center">Connect PgSTAC and TiTiler.</p>
</p>

<p align="center">
  <a href="https://github.com/stac-utils/titiler-pgstac/actions?query=workflow%3ACI" target="_blank">
      <img src="https://github.com/developmentseed/titiler/workflows/CI/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/stac-utils/titiler-pgstac" target="_blank">
      <img src="https://codecov.io/gh/stac-utils/titiler-pgstac/branch/master/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/titiler.pgstac" target="_blank">
      <img src="https://img.shields.io/pypi/v/titiler.pgstac?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/stac-utils/titiler-pgstac/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/stac-utils/titiler-pgstac.svg" alt="License">
  </a>
</p>

---

**Documentation**: <a href="https://stac-utils.github.io/titiler-pgstac/" target="_blank">https://stac-utils.github.io/titiler-pgstac/</a>

**Source Code**: <a href="https://github.com/stac-utils/titiler-pgstac" target="_blank">https://github.com/stac-utils/titiler-pgstac</a>

---

`TiTiler.PgSTAC` is a [titiler](https://github.com/developmentseed/titile) extension which connect to [pgstac](https://github.com/stac-utils/pgstac) STAC database in order to create **mosaics** in response to a STAC-api `search` query.


## Installation

To install from PyPI and run:

```bash
$ pip install -U pip
$ pip install titiler.pgstac
```

To install from sources and run for development:

```
$ git clone https://github.com/stac-utils/titiler-pgstac.git
$ cd titiler-pgstac
$ pip install -e .
```

### Launch

You'll need to have `POSTGRES_USER`, `POSTGRES_PASS`, `POSTGRES_DBNAME`, `POSTGRES_HOST_READER`, `POSTGRES_HOST_WRITER`, `POSTGRES_PORT` variables set in your environment pointing to your Postgres database where pgstac has been installed.

```
export POSTGRES_USER=username
export POSTGRES_PASS=password
export POSTGRES_DBNAME=postgis
export POSTGRES_HOST_READER=database
export POSTGRES_HOST_WRITER=database
export POSTGRES_PORT=5432
```

```
$ pip install uvicorn
$ uvicorn titiler.pgstac.main:app --reload
```

### Using Docker

```
$ git clone https://github.com/stac-utils/titiler-pgstac.git
$ cd titiler-pgstac

$ docker-compose build
$ docker-compose up
```

## Contribution & Development

See [CONTRIBUTING.md](https://github.com//stac-utils/titiler-pgstac/blob/master/CONTRIBUTING.md)

## License

See [LICENSE](https://github.com//stac-utils/titiler-pgstac/blob/master/LICENSE)

## Authors

See [contributors](https://github.com/stac-utils/titiler-pgstac/graphs/contributors) for a listing of individual contributors.

## Changes

See [CHANGES.md](https://github.com/stac-utils/titiler-pgstac/blob/master/CHANGES.md).
