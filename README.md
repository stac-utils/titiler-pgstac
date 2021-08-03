**WORK IN PROGRESS / EXPERIMENTAL**

## titiler.pgstac

Connect PgSTAC and TiTiler

---

**Documentation**:

**Source Code**: <a href="https://github.com/stac-utils/titiler-pgstac" target="_blank">https://github.com/stac-utils/titiler-pgstac</a>

---

### Overview

1. Mosaic Creation

<img width="995" alt="Screen Shot 2021-07-20 at 4 47 46 PM" src="https://user-images.githubusercontent.com/10407788/126345041-df19a42a-bd6a-44cc-b26c-40f44d5035a6.png">

2. Tile Request

<img width="973" alt="Screen Shot 2021-07-20 at 4 47 51 PM" src="https://user-images.githubusercontent.com/10407788/126345102-eb521670-bac0-4283-a396-95620db3ff5c.png">

## Installation

```
$ git clone https://github.com/stac-utils/titiler-pgstac.git
$ cd titiler-pgstac
$ pip install -e src/titiler/pgstac
$ pip install uvicorn
$ uvicorn titiler.pgstac.main:app --reload --port 8082 --host 0.0.0.0
```

## Docker

- Built the docker locally
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
