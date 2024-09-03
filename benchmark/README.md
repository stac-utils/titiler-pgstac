
### Start DB
```bash
$ docker compose up database
```

### Add items/collections to the db

```bash
$ pypgstac load collections benchmark/stac/collection.json --dsn postgresql://username:password@localhost:5439/postgis --method insert
$ pypgstac load items benchmark/stac/items.json --dsn postgresql://username:password@localhost:5439/postgis --method insert
```

### Start API
```bash
# This should be done at the repo root level
$ uvicorn titiler.pgstac.main:app --port 8081
```

## Get Mosaic ID

```bash
$ curl -X 'POST' 'http://127.0.0.1:8081/mosaic/register' \-H 'accept: application/json' \-H 'Content-Type: application/json' \
-d '{"collections":["world"]}' | jq

>>> {
  "searchid": "a813b9d9afdb8ee44eb42ecdbe245e41",
  "metadata": "http://127.0.0.1:8081/mosaic/a813b9d9afdb8ee44eb42ecdbe245e41/info",
  "tiles": "http://127.0.0.1:8081/mosaic/a813b9d9afdb8ee44eb42ecdbe245e41/tilejson.json"
}
```

### Create urls

```bash
$ cd benchmark/
$ python -m create_urls --maxzoom 6
```

**edit urls.txt** with the mosaic id and path
```
PROT=http
HOST=localhost
PORT=8081
PATH=mosaic/a813b9d9afdb8ee44eb42ecdbe245e41/tiles/WebMercatorQuad/
$(PROT)://$(HOST):$(PORT)/$(PATH)0/0/0?assets=asset
...
```

### Environment Variable
```
# DB_MIN_CONN_SIZE=1
# DB_MAX_CONN_SIZE=10
# DB_MAX_QUERIES=10
# DB_MAX_IDLE=10
# WEB_CONCURRENCY=10
```

### Siege
```
# 50 concurrents / repeat 10 times (500 tiles)
$ siege --file benchmark/urls.txt -b -c 50 -r 10

Transactions:                    500 hits
Availability:                 100.00 %
Elapsed time:                  21.34 secs
Data transferred:               6.13 MB
Response time:                  1.88 secs
Transaction rate:              23.43 trans/sec
Throughput:                     0.29 MB/sec
Concurrency:                   44.10
Successful transactions:         500
Failed transactions:               0
Longest transaction:            3.84
Shortest transaction:           0.29


# 10 concurrents / repeat 100 times (1000 tiles)
$ siege --file benchmark/urls.txt -b -c 10 -r 100

Transactions:                   1000 hits
Availability:                 100.00 %
Elapsed time:                  65.78 secs
Data transferred:              11.61 MB
Response time:                  0.43 secs
Transaction rate:              15.20 trans/sec
Throughput:                     0.18 MB/sec
Concurrency:                    6.55
Successful transactions:        1000
Failed transactions:               0
Longest transaction:            1.47
Shortest transaction:           0.07


# 200 concurrents / repeat 1 time (200 tiles)
$ siege --file benchmark/urls.txt -b -c 200 -r 1

Transactions:                    194 hits
Availability:                  97.00 %
Elapsed time:                   8.43 secs
Data transferred:               2.28 MB
Response time:                  4.81 secs
Transaction rate:              23.01 trans/sec
Throughput:                     0.27 MB/sec
Concurrency:                  110.66
Successful transactions:         194
Failed transactions:               6
Longest transaction:            8.43
Shortest transaction:           0.52
```
