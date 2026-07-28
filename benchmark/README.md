
### Start application

```bash
$ docker compose up titiler-uvicorn
```

### Add items/collections to the db

```bash
uv run pypgstac load collections benchmark/stac/collection.json --dsn postgresql://username:password@0.0.0.0:5439/postgis --method upsert
uv run pypgstac load items benchmark/stac/items.json --dsn postgresql://username:password@0.0.0.0:5439/postgis --method upsert

curl http://127.0.0.1:8083/collections/world/info | jq
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
PORT=8083
PATH=collections/world/tiles/WebMercatorQuad/
$(PROT)://$(HOST):$(PORT)/$(PATH)0/0/0?assets=asset
...
``` 

### Siege
```
# 50 concurrents / repeat 10 times (500 tiles)
$ siege --file urls.txt -b -c 50 -r 10

Transactions:                 500    hits
Availability:                 100.00 %
Elapsed time:                   6.39 secs
Data transferred:               5.40 MB
Response time:                534.70 ms
Transaction rate:              78.25 trans/sec
Throughput:                     0.84 MB/sec
Concurrency:                   41.84
Successful transactions:      500
Failed transactions:            0
Longest transaction:         2220.00 ms
Shortest transaction:          50.00 ms


# 10 concurrents / repeat 100 times (1000 tiles)
$ siege --file urls.txt -b -c 10 -r 100

Transactions:                1000    hits
Availability:                 100.00 %
Elapsed time:                  17.31 secs
Data transferred:              11.45 MB
Response time:                127.95 ms
Transaction rate:              57.77 trans/sec
Throughput:                     0.66 MB/sec
Concurrency:                    7.39
Successful transactions:     1000
Failed transactions:            0
Longest transaction:          520.00 ms
Shortest transaction:          30.00 ms


# 200 concurrents / repeat 1 time (200 tiles)
$ siege --file urls.txt -b -c 200 -r 1

Transactions:                 200    hits
Availability:                 100.00 %
Elapsed time:                   2.85 secs
Data transferred:               2.08 MB
Response time:               1673.80 ms
Transaction rate:              70.18 trans/sec
Throughput:                     0.73 MB/sec
Concurrency:                  117.46
Successful transactions:      200
Failed transactions:            0
Longest transaction:         2840.00 ms
Shortest transaction:         470.00 ms
```