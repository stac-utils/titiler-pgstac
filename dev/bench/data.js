window.BENCHMARK_DATA = {
  "lastUpdate": 1686248240596,
  "repoUrl": "https://github.com/stac-utils/titiler-pgstac",
  "entries": {
    "TiTiler-pgSTAC Benchmarks": [
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "Vincent Sarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "30a21ecbd3ef78fc04332dbb620f40694dfd137c",
          "message": "Merge pull request #102 from stac-utils/addBenchmark\n\nadd simple benchmark",
          "timestamp": "2023-06-08T19:04:34+02:00",
          "tree_id": "fdd23c647bf81bac9c75c40a06e7e6f5c40e5e3d",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/30a21ecbd3ef78fc04332dbb620f40694dfd137c"
        },
        "date": 1686244205523,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.836427762281342,
            "unit": "iter/sec",
            "range": "stddev: 0.004751084014841288",
            "extra": "mean: 352.5561317999859 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.917599503984506,
            "unit": "iter/sec",
            "range": "stddev: 0.007658743672032181",
            "extra": "mean: 168.9874414999982 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.267368168204441,
            "unit": "iter/sec",
            "range": "stddev: 0.0058431185355074305",
            "extra": "mean: 137.60139528572577 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 15.068761581061713,
            "unit": "iter/sec",
            "range": "stddev: 0.0011903244145160692",
            "extra": "mean: 66.3624541818215 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 20.54597228552386,
            "unit": "iter/sec",
            "range": "stddev: 0.003797368674634331",
            "extra": "mean: 48.67133986667417 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 19.537290109263058,
            "unit": "iter/sec",
            "range": "stddev: 0.002932352142793612",
            "extra": "mean: 51.18417111111424 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 17.792929326977454,
            "unit": "iter/sec",
            "range": "stddev: 0.005404172069647886",
            "extra": "mean: 56.20210037499618 msec\nrounds: 16"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "distinct": true,
          "id": "3952b81efb3bbdb343db3f3925b069469fe3b83a",
          "message": "publish docker",
          "timestamp": "2023-06-08T20:12:21+02:00",
          "tree_id": "b1a3496353b789c87afb88badc901f1bee3560ed",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/3952b81efb3bbdb343db3f3925b069469fe3b83a"
        },
        "date": 1686248240101,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.8689126631485315,
            "unit": "iter/sec",
            "range": "stddev: 0.005216384016774406",
            "extra": "mean: 348.5641138000119 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.074991013417379,
            "unit": "iter/sec",
            "range": "stddev: 0.004006033948614887",
            "extra": "mean: 164.60929700000784 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.384512260469682,
            "unit": "iter/sec",
            "range": "stddev: 0.0018443344808471232",
            "extra": "mean: 135.41855775000045 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 15.445866460293967,
            "unit": "iter/sec",
            "range": "stddev: 0.0027737597263819426",
            "extra": "mean: 64.74224042857405 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 21.67631924723492,
            "unit": "iter/sec",
            "range": "stddev: 0.003800665136358353",
            "extra": "mean: 46.13329359999909 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.12482961524685,
            "unit": "iter/sec",
            "range": "stddev: 0.0029632115097030683",
            "extra": "mean: 49.68986168421452 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.521442344075286,
            "unit": "iter/sec",
            "range": "stddev: 0.004576092395664916",
            "extra": "mean: 53.991475470585264 msec\nrounds: 17"
          }
        ]
      }
    ]
  }
}