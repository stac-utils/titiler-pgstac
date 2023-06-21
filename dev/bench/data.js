window.BENCHMARK_DATA = {
  "lastUpdate": 1687336174907,
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
          "id": "62aec6a64427f4909d66b05534260fde2db13932",
          "message": "fix name",
          "timestamp": "2023-06-08T20:20:51+02:00",
          "tree_id": "7824df3354d8ba55aa88640304b664bf886504e3",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/62aec6a64427f4909d66b05534260fde2db13932"
        },
        "date": 1686248801741,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.373412498133809,
            "unit": "iter/sec",
            "range": "stddev: 0.007715098733043546",
            "extra": "mean: 421.3342605999969 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 4.856247021924921,
            "unit": "iter/sec",
            "range": "stddev: 0.007761471437185086",
            "extra": "mean: 205.92033219999166 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.141078901198113,
            "unit": "iter/sec",
            "range": "stddev: 0.00484299147272101",
            "extra": "mean: 162.83783616668757 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 12.673483139002064,
            "unit": "iter/sec",
            "range": "stddev: 0.005430939955922097",
            "extra": "mean: 78.9049063333304 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 17.657737639989207,
            "unit": "iter/sec",
            "range": "stddev: 0.005733009206104463",
            "extra": "mean: 56.63239653846229 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 16.76821191880671,
            "unit": "iter/sec",
            "range": "stddev: 0.00552982023967614",
            "extra": "mean: 59.63665087500658 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 15.243951005882336,
            "unit": "iter/sec",
            "range": "stddev: 0.0057357263388900384",
            "extra": "mean: 65.59979099999207 msec\nrounds: 15"
          }
        ]
      },
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
          "id": "b176727e847f892231660377d5229f16d57ff789",
          "message": "Merge pull request #103 from charalamm/patch-1\n\nAdd required dependencies for demo notebook",
          "timestamp": "2023-06-09T14:53:02+02:00",
          "tree_id": "864ef654e1cc1773011f2a8683c89d50e9f10b45",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/b176727e847f892231660377d5229f16d57ff789"
        },
        "date": 1686315505095,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.5070024413901737,
            "unit": "iter/sec",
            "range": "stddev: 0.008836828279008382",
            "extra": "mean: 398.8827388000004 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.097253335559231,
            "unit": "iter/sec",
            "range": "stddev: 0.01103327559318889",
            "extra": "mean: 196.18408860000045 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.2613379002251595,
            "unit": "iter/sec",
            "range": "stddev: 0.005228575425339361",
            "extra": "mean: 159.71027533333407 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 13.09157278604271,
            "unit": "iter/sec",
            "range": "stddev: 0.0038222967940035753",
            "extra": "mean: 76.38501625000534 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 18.556870956114302,
            "unit": "iter/sec",
            "range": "stddev: 0.0045818700674059975",
            "extra": "mean: 53.88839542856821 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 17.377877236533855,
            "unit": "iter/sec",
            "range": "stddev: 0.0036751510654468326",
            "extra": "mean: 57.544427687501454 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 15.437570637756767,
            "unit": "iter/sec",
            "range": "stddev: 0.0037015064515485857",
            "extra": "mean: 64.77703153333134 msec\nrounds: 15"
          }
        ]
      },
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
          "id": "3abc5df15ed0425b7b5abf7218d8afbf133bf7f1",
          "message": "Merge pull request #104 from stac-utils/FixTemplateName\n\nupdate titiler and fix template name",
          "timestamp": "2023-06-21T10:24:47+02:00",
          "tree_id": "e69659093b1c3e0f2e93ab223ba2c414594d6bc9",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/3abc5df15ed0425b7b5abf7218d8afbf133bf7f1"
        },
        "date": 1687336174225,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.975981790781622,
            "unit": "iter/sec",
            "range": "stddev: 0.004622722818727696",
            "extra": "mean: 336.02356140000325 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.251995402482495,
            "unit": "iter/sec",
            "range": "stddev: 0.00499436284787555",
            "extra": "mean: 159.94893400000385 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.444703837424361,
            "unit": "iter/sec",
            "range": "stddev: 0.0032860658917885314",
            "extra": "mean: 134.3236778571395 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 15.65304992682078,
            "unit": "iter/sec",
            "range": "stddev: 0.0038199177565773007",
            "extra": "mean: 63.88531338461689 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.406851090107544,
            "unit": "iter/sec",
            "range": "stddev: 0.0018802023739444083",
            "extra": "mean: 44.629207200001986 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.617073703619738,
            "unit": "iter/sec",
            "range": "stddev: 0.003363616482584565",
            "extra": "mean: 48.503488631581604 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.8702325120234,
            "unit": "iter/sec",
            "range": "stddev: 0.00292692913263053",
            "extra": "mean: 52.99351766666563 msec\nrounds: 18"
          }
        ]
      }
    ]
  }
}