window.BENCHMARK_DATA = {
  "lastUpdate": 1715878157908,
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
          "id": "5f7e221cc2a456732a8cfd4b42713ddeb19032bb",
          "message": "Bump version: 0.4.0 → 0.4.1",
          "timestamp": "2023-06-21T10:25:06+02:00",
          "tree_id": "bd792663611e60810e4419c180df03a559dd0947",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/5f7e221cc2a456732a8cfd4b42713ddeb19032bb"
        },
        "date": 1687336289409,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.995069658892925,
            "unit": "iter/sec",
            "range": "stddev: 0.005185215285954201",
            "extra": "mean: 333.88205079999125 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.169577703758325,
            "unit": "iter/sec",
            "range": "stddev: 0.006003686868924205",
            "extra": "mean: 162.08564799999672 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.450681247931083,
            "unit": "iter/sec",
            "range": "stddev: 0.0021061648212365447",
            "extra": "mean: 134.21591485713893 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 15.774908844991838,
            "unit": "iter/sec",
            "range": "stddev: 0.0037614629889906152",
            "extra": "mean: 63.39180846154154 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.624423204894203,
            "unit": "iter/sec",
            "range": "stddev: 0.002021198306675405",
            "extra": "mean: 44.20002185000129 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.078244641517344,
            "unit": "iter/sec",
            "range": "stddev: 0.003718069148524975",
            "extra": "mean: 47.44228074999768 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.476961161972998,
            "unit": "iter/sec",
            "range": "stddev: 0.0029570836470616535",
            "extra": "mean: 51.34271161111156 msec\nrounds: 18"
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
          "id": "d4a058f26a0b8ff86de077aca505e0f9c2940070",
          "message": "fix tag",
          "timestamp": "2023-06-21T10:51:00+02:00",
          "tree_id": "81372185ec645a50ba056d71103045f45ffdf280",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/d4a058f26a0b8ff86de077aca505e0f9c2940070"
        },
        "date": 1687339229660,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.739122684970989,
            "unit": "iter/sec",
            "range": "stddev: 0.01303936245687109",
            "extra": "mean: 365.0803979999864 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.836691621396926,
            "unit": "iter/sec",
            "range": "stddev: 0.005282717440124118",
            "extra": "mean: 171.32993566664823 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.253256728331996,
            "unit": "iter/sec",
            "range": "stddev: 0.0041183495076076585",
            "extra": "mean: 137.86910314285348 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 14.802984688122168,
            "unit": "iter/sec",
            "range": "stddev: 0.0017136194636239476",
            "extra": "mean: 67.55394409090988 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 20.737799274904706,
            "unit": "iter/sec",
            "range": "stddev: 0.004073547360059846",
            "extra": "mean: 48.22112446667006 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 19.537377244581183,
            "unit": "iter/sec",
            "range": "stddev: 0.0031587750329522503",
            "extra": "mean: 51.1839428333379 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 17.837801827031083,
            "unit": "iter/sec",
            "range": "stddev: 0.005042955163693067",
            "extra": "mean: 56.06071923529378 msec\nrounds: 17"
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
          "id": "ba8bfc3bfca22b5051c4d68258cf36b09182fa44",
          "message": "update logo",
          "timestamp": "2023-07-19T08:10:23+02:00",
          "tree_id": "cbeda90d4ce70b6f4a3f6818e150d8c4072233de",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/ba8bfc3bfca22b5051c4d68258cf36b09182fa44"
        },
        "date": 1689747386440,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.8021463477085704,
            "unit": "iter/sec",
            "range": "stddev: 0.006314087955665145",
            "extra": "mean: 356.86929799999234 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.825609075730566,
            "unit": "iter/sec",
            "range": "stddev: 0.006537294650032025",
            "extra": "mean: 171.65587099999394 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.110696911886813,
            "unit": "iter/sec",
            "range": "stddev: 0.002057245982981864",
            "extra": "mean: 140.63319142858128 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 15.229474562595243,
            "unit": "iter/sec",
            "range": "stddev: 0.0019208748160136095",
            "extra": "mean: 65.66214716665779 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 21.16262128402774,
            "unit": "iter/sec",
            "range": "stddev: 0.0020577251415012784",
            "extra": "mean: 47.25312552631366 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.04534539874118,
            "unit": "iter/sec",
            "range": "stddev: 0.003509918072616615",
            "extra": "mean: 49.88689294736715 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.367561096159044,
            "unit": "iter/sec",
            "range": "stddev: 0.0028966000905907446",
            "extra": "mean: 54.44380964705849 msec\nrounds: 17"
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
          "id": "c5707d1dea39c081c3bf2a4df02e2cf4430ba022",
          "message": "Merge pull request #107 from stac-utils/updateTiTiler0.12\n\nupdate to titiler 0.12",
          "timestamp": "2023-07-19T11:32:27+02:00",
          "tree_id": "04b993024a8b06739528d0aa350d741b929fc77b",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/c5707d1dea39c081c3bf2a4df02e2cf4430ba022"
        },
        "date": 1689759425861,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.034431760914126,
            "unit": "iter/sec",
            "range": "stddev: 0.006349316001549449",
            "extra": "mean: 329.5509930000037 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.363395603599091,
            "unit": "iter/sec",
            "range": "stddev: 0.0035602935549318452",
            "extra": "mean: 157.148802666678 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.584837092626998,
            "unit": "iter/sec",
            "range": "stddev: 0.002314822863775267",
            "extra": "mean: 131.8419878750028 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.688431403678837,
            "unit": "iter/sec",
            "range": "stddev: 0.0028435205199221626",
            "extra": "mean: 59.92174913332823 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 23.032409983318857,
            "unit": "iter/sec",
            "range": "stddev: 0.0032555700693981775",
            "extra": "mean: 43.41708057143158 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.630438702890437,
            "unit": "iter/sec",
            "range": "stddev: 0.0028860472544148482",
            "extra": "mean: 46.23114740000034 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.711451019405104,
            "unit": "iter/sec",
            "range": "stddev: 0.002639221718564341",
            "extra": "mean: 50.73193236842593 msec\nrounds: 19"
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
          "id": "0397ffaa71be9201edba191efeeb9d297893f50d",
          "message": "Merge pull request #108 from stac-utils/removeStacPydantic\n\nremove stac-pydantic",
          "timestamp": "2023-07-19T12:02:21+02:00",
          "tree_id": "af32f61b17eef1a0ff1a92115c1e772e86ddc173",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/0397ffaa71be9201edba191efeeb9d297893f50d"
        },
        "date": 1689761248474,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.996231446153499,
            "unit": "iter/sec",
            "range": "stddev: 0.006056098751216021",
            "extra": "mean: 333.75258820001363 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.17571297901256,
            "unit": "iter/sec",
            "range": "stddev: 0.006415378161702739",
            "extra": "mean: 161.9246236666735 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.604638874905728,
            "unit": "iter/sec",
            "range": "stddev: 0.00260429014628532",
            "extra": "mean: 131.498683428593 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.401406860702224,
            "unit": "iter/sec",
            "range": "stddev: 0.003095725744893265",
            "extra": "mean: 60.97037946153268 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 23.113233127997486,
            "unit": "iter/sec",
            "range": "stddev: 0.0021509103629107915",
            "extra": "mean: 43.26525823809052 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.446613599521942,
            "unit": "iter/sec",
            "range": "stddev: 0.002398304202795905",
            "extra": "mean: 46.62740788234701 msec\nrounds: 17"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.546380947657823,
            "unit": "iter/sec",
            "range": "stddev: 0.002505596890127138",
            "extra": "mean: 51.16036583333994 msec\nrounds: 18"
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
          "id": "2de7ce042dd026e72643a58a4255cfc0727053dd",
          "message": "Merge pull request #111 from stac-utils/newApiDocsUrl\n\nchange openapi/docs url and update landing page",
          "timestamp": "2023-07-19T16:33:07+02:00",
          "tree_id": "bd95fe5e8ad7d0e0b3cd2c82f2ba81515162137b",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/2de7ce042dd026e72643a58a4255cfc0727053dd"
        },
        "date": 1689777468607,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.961546276808463,
            "unit": "iter/sec",
            "range": "stddev: 0.0053465609805415",
            "extra": "mean: 337.6614466000035 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.289423188347091,
            "unit": "iter/sec",
            "range": "stddev: 0.003792262593562554",
            "extra": "mean: 158.9970924285678 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.513652689664234,
            "unit": "iter/sec",
            "range": "stddev: 0.008734714204102944",
            "extra": "mean: 133.09105987499237 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.253358038579997,
            "unit": "iter/sec",
            "range": "stddev: 0.0035068863107501863",
            "extra": "mean: 61.525747333341016 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.170751492386643,
            "unit": "iter/sec",
            "range": "stddev: 0.003911057086868247",
            "extra": "mean: 45.104470200001856 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.786124336365873,
            "unit": "iter/sec",
            "range": "stddev: 0.0027635383414914136",
            "extra": "mean: 45.900775399999816 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.41598555649909,
            "unit": "iter/sec",
            "range": "stddev: 0.0024858474043812566",
            "extra": "mean: 51.503952611113846 msec\nrounds: 18"
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
          "id": "b5867579bd6c3ad4a9e5581551fed3ba7a6a2b8a",
          "message": "update logos",
          "timestamp": "2023-07-19T18:51:49+02:00",
          "tree_id": "1834d936e90544710b12e8ea4c460e5fcd8bcee4",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/b5867579bd6c3ad4a9e5581551fed3ba7a6a2b8a"
        },
        "date": 1689785827791,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.6627185197163636,
            "unit": "iter/sec",
            "range": "stddev: 0.011215616256177686",
            "extra": "mean: 375.55603140001494 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.712637417088481,
            "unit": "iter/sec",
            "range": "stddev: 0.0049600408757167974",
            "extra": "mean: 175.0504936666649 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.768170812990961,
            "unit": "iter/sec",
            "range": "stddev: 0.012971334512408237",
            "extra": "mean: 147.75040814285896 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 13.720310209128648,
            "unit": "iter/sec",
            "range": "stddev: 0.0050642845988278975",
            "extra": "mean: 72.88464945454817 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 18.084000437794664,
            "unit": "iter/sec",
            "range": "stddev: 0.0062587210932812274",
            "extra": "mean: 55.29749921428057 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 18.16192136767742,
            "unit": "iter/sec",
            "range": "stddev: 0.005211363671565577",
            "extra": "mean: 55.0602538000021 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 16.89887629094771,
            "unit": "iter/sec",
            "range": "stddev: 0.0035315529850574374",
            "extra": "mean: 59.17553231250494 msec\nrounds: 16"
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
          "id": "51dfe43a5d997d5002cde3960098f10e2710dbb8",
          "message": "Merge pull request #112 from stac-utils/LandingPage\n\nadd landing page",
          "timestamp": "2023-07-19T19:57:25+02:00",
          "tree_id": "2d06cbcdcbb7d897389ba46afc95ce266452e6bb",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/51dfe43a5d997d5002cde3960098f10e2710dbb8"
        },
        "date": 1689789747240,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.1725708735885716,
            "unit": "iter/sec",
            "range": "stddev: 0.01236151918647516",
            "extra": "mean: 460.2841785999999 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 4.537626463286613,
            "unit": "iter/sec",
            "range": "stddev: 0.012053151157960044",
            "extra": "mean: 220.37953279999556 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 5.618077669798333,
            "unit": "iter/sec",
            "range": "stddev: 0.014854275966249924",
            "extra": "mean: 177.9968271666661 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 11.830966189137149,
            "unit": "iter/sec",
            "range": "stddev: 0.005536240703839256",
            "extra": "mean: 84.52395045454284 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 15.716737088196846,
            "unit": "iter/sec",
            "range": "stddev: 0.005837632317882279",
            "extra": "mean: 63.62643813333194 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 15.627299768780256,
            "unit": "iter/sec",
            "range": "stddev: 0.0066831342638640065",
            "extra": "mean: 63.99058153333499 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 14.079614206341812,
            "unit": "iter/sec",
            "range": "stddev: 0.004228211035092095",
            "extra": "mean: 71.02467335714176 msec\nrounds: 14"
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
          "id": "b48732c97f6ea1b5e19c0cdc832f0bd26cf5cffd",
          "message": "Merge pull request #113 from stac-utils/FastAPILifespan\n\nFastAPI lifespan",
          "timestamp": "2023-07-20T11:34:26+02:00",
          "tree_id": "3cd9af9ad2a2fc0149f871054850dd7a4e871ef3",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/b48732c97f6ea1b5e19c0cdc832f0bd26cf5cffd"
        },
        "date": 1689845945150,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.9388076498681914,
            "unit": "iter/sec",
            "range": "stddev: 0.005156799989343685",
            "extra": "mean: 340.27405639999984 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.035702356400411,
            "unit": "iter/sec",
            "range": "stddev: 0.005207587434237345",
            "extra": "mean: 165.68080083332384 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.34122806202458,
            "unit": "iter/sec",
            "range": "stddev: 0.0030537638453376386",
            "extra": "mean: 136.21699142857275 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 15.63322751209617,
            "unit": "iter/sec",
            "range": "stddev: 0.003919426847718255",
            "extra": "mean: 63.966317846155086 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.202403628410224,
            "unit": "iter/sec",
            "range": "stddev: 0.002663377367138882",
            "extra": "mean: 45.04016847619141 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.63116585279347,
            "unit": "iter/sec",
            "range": "stddev: 0.0026876415603388957",
            "extra": "mean: 48.47035824999679 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.93757235375665,
            "unit": "iter/sec",
            "range": "stddev: 0.0021905702322014197",
            "extra": "mean: 52.80507877777848 msec\nrounds: 18"
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
          "id": "280fea21e32c9d8fe3e4e69745df27fa1093db35",
          "message": "Bump version: 0.4.1 → 0.5.0",
          "timestamp": "2023-07-20T12:41:41+02:00",
          "tree_id": "421b429ec5d141fcbfb8214eb5a019c33d88ae70",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/280fea21e32c9d8fe3e4e69745df27fa1093db35"
        },
        "date": 1689850071790,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.86281541136775,
            "unit": "iter/sec",
            "range": "stddev: 0.0090340497981933",
            "extra": "mean: 349.30648900001415 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.14721045137554,
            "unit": "iter/sec",
            "range": "stddev: 0.007500534272133854",
            "extra": "mean: 162.67541316667197 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.366458945889119,
            "unit": "iter/sec",
            "range": "stddev: 0.005107220371479777",
            "extra": "mean: 135.75043414285963 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 15.501332456381403,
            "unit": "iter/sec",
            "range": "stddev: 0.004072482901278997",
            "extra": "mean: 64.51058338461297 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.476180435113456,
            "unit": "iter/sec",
            "range": "stddev: 0.0030196050516694884",
            "extra": "mean: 44.49154530000783 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.699524662944935,
            "unit": "iter/sec",
            "range": "stddev: 0.004586866126104419",
            "extra": "mean: 48.31028810000362 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.519383175565512,
            "unit": "iter/sec",
            "range": "stddev: 0.004624631585999585",
            "extra": "mean: 53.99747877777057 msec\nrounds: 18"
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
          "id": "10e3906cebe0946612aa42c6f7555c8ba6cda2ab",
          "message": "Merge pull request #116 from stac-utils/dotEnv\n\nadd missing python-dotenv",
          "timestamp": "2023-08-03T16:29:32+02:00",
          "tree_id": "87868adda7c2230aa69f7ac384281c0faf204e17",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/10e3906cebe0946612aa42c6f7555c8ba6cda2ab"
        },
        "date": 1691073255476,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.4746714420671814,
            "unit": "iter/sec",
            "range": "stddev: 0.021343518322204193",
            "extra": "mean: 404.09404780000386 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.541887788589747,
            "unit": "iter/sec",
            "range": "stddev: 0.006294938997445834",
            "extra": "mean: 180.4439278000018 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.938120548320658,
            "unit": "iter/sec",
            "range": "stddev: 0.004442424298883562",
            "extra": "mean: 144.1312518333291 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 14.859573832474306,
            "unit": "iter/sec",
            "range": "stddev: 0.004832504620216971",
            "extra": "mean: 67.29668100000197 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 21.317599535071906,
            "unit": "iter/sec",
            "range": "stddev: 0.004140464970842513",
            "extra": "mean: 46.90959685000138 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 19.367600167205627,
            "unit": "iter/sec",
            "range": "stddev: 0.005038553714810359",
            "extra": "mean: 51.63262311111004 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.332209768372383,
            "unit": "iter/sec",
            "range": "stddev: 0.0032958483294578318",
            "extra": "mean: 54.54879758823448 msec\nrounds: 17"
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
          "id": "50e37883ffe12cc739467f25d370c00672fe9070",
          "message": "Bump version: 0.5.0 → 0.5.1",
          "timestamp": "2023-08-03T16:29:57+02:00",
          "tree_id": "da56ebb270bb095a3aa0da105acb224f35dac16f",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/50e37883ffe12cc739467f25d370c00672fe9070"
        },
        "date": 1691073314763,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.879286468771433,
            "unit": "iter/sec",
            "range": "stddev: 0.013211996095400262",
            "extra": "mean: 347.3082692000048 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.271762742326072,
            "unit": "iter/sec",
            "range": "stddev: 0.0028823049952351474",
            "extra": "mean: 159.4448070000046 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.526708376491893,
            "unit": "iter/sec",
            "range": "stddev: 0.003408155377725737",
            "extra": "mean: 132.8602026250003 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.249805583264287,
            "unit": "iter/sec",
            "range": "stddev: 0.00275905982552561",
            "extra": "mean: 61.539197799997204 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.3125802151195,
            "unit": "iter/sec",
            "range": "stddev: 0.0032480028098055423",
            "extra": "mean: 44.81776604762087 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.44334980563837,
            "unit": "iter/sec",
            "range": "stddev: 0.0025415738384909734",
            "extra": "mean: 48.915662526314314 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.560572752896785,
            "unit": "iter/sec",
            "range": "stddev: 0.0021054096105115982",
            "extra": "mean: 53.87764770588386 msec\nrounds: 17"
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
          "id": "89c3a3b5ca680cc66a9ca245e4baabacd60abe3d",
          "message": "Merge pull request #119 from zacharyDez/patch-1\n\nUpdate README.md",
          "timestamp": "2023-08-30T10:04:41+02:00",
          "tree_id": "506602585490a537d9fffbba1c47a5bf1b2d5568",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/89c3a3b5ca680cc66a9ca245e4baabacd60abe3d"
        },
        "date": 1693382973446,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.7324275979969377,
            "unit": "iter/sec",
            "range": "stddev: 0.012707413563187202",
            "extra": "mean: 365.97493040001154 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.7592581706884785,
            "unit": "iter/sec",
            "range": "stddev: 0.006559341046244687",
            "extra": "mean: 173.63347333332987 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.7409855508662115,
            "unit": "iter/sec",
            "range": "stddev: 0.0031443021459517475",
            "extra": "mean: 148.346260714281 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 14.719145207961454,
            "unit": "iter/sec",
            "range": "stddev: 0.0023848260989555235",
            "extra": "mean: 67.93872781818261 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 20.707433975422173,
            "unit": "iter/sec",
            "range": "stddev: 0.005004999927710939",
            "extra": "mean: 48.291835733336555 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 19.325711895730628,
            "unit": "iter/sec",
            "range": "stddev: 0.004370471954448542",
            "extra": "mean: 51.74453626315917 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 17.726585997318097,
            "unit": "iter/sec",
            "range": "stddev: 0.002499185487412704",
            "extra": "mean: 56.4124417499959 msec\nrounds: 12"
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
          "id": "4b9da631bf944b2f618aba6dfa8f582841d482c9",
          "message": "Merge pull request #120 from stac-utils/LayerLinks\n\nadd tilejson links for layers",
          "timestamp": "2023-08-31T15:46:56+02:00",
          "tree_id": "d0247a275701b3bc15e7c9245ef65143166ddad9",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/4b9da631bf944b2f618aba6dfa8f582841d482c9"
        },
        "date": 1693489928151,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.442886073566027,
            "unit": "iter/sec",
            "range": "stddev: 0.020980969112838893",
            "extra": "mean: 409.35187720000386 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 4.933284558540893,
            "unit": "iter/sec",
            "range": "stddev: 0.009481510623495136",
            "extra": "mean: 202.70470680000017 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.110388568978248,
            "unit": "iter/sec",
            "range": "stddev: 0.004319548589850206",
            "extra": "mean: 163.65571333333642 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 12.924497319366687,
            "unit": "iter/sec",
            "range": "stddev: 0.0059301780839550915",
            "extra": "mean: 77.37244825000289 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 17.477697256710208,
            "unit": "iter/sec",
            "range": "stddev: 0.00606105207525253",
            "extra": "mean: 57.2157753571381 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 16.86521675259895,
            "unit": "iter/sec",
            "range": "stddev: 0.004548249123654028",
            "extra": "mean: 59.29363462499815 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 15.415200005354357,
            "unit": "iter/sec",
            "range": "stddev: 0.004209226768718046",
            "extra": "mean: 64.87103635714472 msec\nrounds: 14"
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
          "id": "ef3507e3e3c7129bf9aa12e4fddeea0a58a298d7",
          "message": "Merge pull request #121 from stac-utils/multiWMTSLayers\n\nSupport multiple Layers in WMTS endpoint",
          "timestamp": "2023-09-18T21:13:37-06:00",
          "tree_id": "181994dce562396166e56c5d03ea73b5c639b137",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/ef3507e3e3c7129bf9aa12e4fddeea0a58a298d7"
        },
        "date": 1695093479357,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.038290002357341,
            "unit": "iter/sec",
            "range": "stddev: 0.003238014956494668",
            "extra": "mean: 329.13250520000474 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.317067822126652,
            "unit": "iter/sec",
            "range": "stddev: 0.004218642023103951",
            "extra": "mean: 158.30129233333898 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.68285178186055,
            "unit": "iter/sec",
            "range": "stddev: 0.0028395397336876244",
            "extra": "mean: 130.1600015714257 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.26481344314705,
            "unit": "iter/sec",
            "range": "stddev: 0.0031659671023007365",
            "extra": "mean: 61.48241438461355 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.69971009562324,
            "unit": "iter/sec",
            "range": "stddev: 0.0026626444592560915",
            "extra": "mean: 44.05342604762213 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.014611343687907,
            "unit": "iter/sec",
            "range": "stddev: 0.003012596873311212",
            "extra": "mean: 47.585938357140584 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.87212044953008,
            "unit": "iter/sec",
            "range": "stddev: 0.0031889231635406144",
            "extra": "mean: 52.98821627777923 msec\nrounds: 18"
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
          "id": "25de1bbecbcb9f3e71f2f810bbe7f294dbaf9419",
          "message": "Bump version: 0.5.1 → 0.6.0",
          "timestamp": "2023-09-18T21:20:33-06:00",
          "tree_id": "eb6b2a5718eef2cbd9e71aabe7f97940b7dbdc23",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/25de1bbecbcb9f3e71f2f810bbe7f294dbaf9419"
        },
        "date": 1695093918523,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.945081260281657,
            "unit": "iter/sec",
            "range": "stddev: 0.004452491919718538",
            "extra": "mean: 339.54920479999373 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.282939584187416,
            "unit": "iter/sec",
            "range": "stddev: 0.004419992734826145",
            "extra": "mean: 159.16116757142618 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.63826725261975,
            "unit": "iter/sec",
            "range": "stddev: 0.005556571358003374",
            "extra": "mean: 130.91974487499414 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.424447672104762,
            "unit": "iter/sec",
            "range": "stddev: 0.002842125277321381",
            "extra": "mean: 60.884847999996815 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.40012759112883,
            "unit": "iter/sec",
            "range": "stddev: 0.0037924838199335014",
            "extra": "mean: 44.64260285713874 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.861508447450568,
            "unit": "iter/sec",
            "range": "stddev: 0.0025000031959312935",
            "extra": "mean: 47.93517221053147 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.4740507867498,
            "unit": "iter/sec",
            "range": "stddev: 0.002869386186784479",
            "extra": "mean: 51.350384722237806 msec\nrounds: 18"
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
          "id": "41c706e4793b05497ea9585cf5b9fdf0604002b0",
          "message": "Merge pull request #115 from stac-utils/pydantic2.0\n\nupdate requirements for pydantic 2.0",
          "timestamp": "2023-09-22T15:21:40+02:00",
          "tree_id": "cb45c8d4480c56b2fb4d8d92fe28967cbb6ec1df",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/41c706e4793b05497ea9585cf5b9fdf0604002b0"
        },
        "date": 1695389226199,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.15764693933518,
            "unit": "iter/sec",
            "range": "stddev: 0.00992721707231194",
            "extra": "mean: 316.6915172000017 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.458667267960147,
            "unit": "iter/sec",
            "range": "stddev: 0.0033085454138861064",
            "extra": "mean: 154.83070399999596 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.600439130951908,
            "unit": "iter/sec",
            "range": "stddev: 0.00477557576962516",
            "extra": "mean: 131.57134512499624 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.600959258318746,
            "unit": "iter/sec",
            "range": "stddev: 0.0031253667582967774",
            "extra": "mean: 60.237482933337105 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.4641476135316,
            "unit": "iter/sec",
            "range": "stddev: 0.0036815048315675357",
            "extra": "mean: 44.51537699999958 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.639132756444816,
            "unit": "iter/sec",
            "range": "stddev: 0.004005384861075737",
            "extra": "mean: 46.21257290000074 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.508111550816285,
            "unit": "iter/sec",
            "range": "stddev: 0.0032492773625569836",
            "extra": "mean: 51.26072799999735 msec\nrounds: 19"
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
          "id": "a2bf3991f07c06a2c814503ead5f6630a8489d89",
          "message": "Merge pull request #124 from stac-utils/titiler014\n\nupdate titiler version",
          "timestamp": "2023-09-22T16:32:33+02:00",
          "tree_id": "f08fb8afbc326ea3371db78129a2a109927a89ec",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/a2bf3991f07c06a2c814503ead5f6630a8489d89"
        },
        "date": 1695393479014,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.6200497356704924,
            "unit": "iter/sec",
            "range": "stddev: 0.009416500863943219",
            "extra": "mean: 381.67214400000375 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.3569059135420165,
            "unit": "iter/sec",
            "range": "stddev: 0.00835073434494843",
            "extra": "mean: 186.67492319998473 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.581136000245921,
            "unit": "iter/sec",
            "range": "stddev: 0.004119807539699674",
            "extra": "mean: 151.94945066666796 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 13.835190847473365,
            "unit": "iter/sec",
            "range": "stddev: 0.0045807686026104084",
            "extra": "mean: 72.2794510769343 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 18.666984488546913,
            "unit": "iter/sec",
            "range": "stddev: 0.003613657172615757",
            "extra": "mean: 53.57051647059266 msec\nrounds: 17"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 17.486170930572285,
            "unit": "iter/sec",
            "range": "stddev: 0.005200775539944293",
            "extra": "mean: 57.18804900000324 msec\nrounds: 17"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 15.813937280399744,
            "unit": "iter/sec",
            "range": "stddev: 0.005291197253726885",
            "extra": "mean: 63.23535892857178 msec\nrounds: 14"
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
          "id": "7eba5ef20dc3502ad0617d7a423fa16ae9517feb",
          "message": "update pydantic for breaking changes",
          "timestamp": "2023-09-28T11:27:23+02:00",
          "tree_id": "9a51f933a8bd49ab4156d6594e63c5ae2aab8efb",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/7eba5ef20dc3502ad0617d7a423fa16ae9517feb"
        },
        "date": 1695893581882,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.031725446060777,
            "unit": "iter/sec",
            "range": "stddev: 0.02607030370434554",
            "extra": "mean: 329.8451715999988 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.406869570029232,
            "unit": "iter/sec",
            "range": "stddev: 0.0046013371089499095",
            "extra": "mean: 156.08246571428757 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.530972720939784,
            "unit": "iter/sec",
            "range": "stddev: 0.005123277130767127",
            "extra": "mean: 132.7849717499987 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.219167333164425,
            "unit": "iter/sec",
            "range": "stddev: 0.0030839819678126954",
            "extra": "mean: 61.65544626666701 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.1410312947633,
            "unit": "iter/sec",
            "range": "stddev: 0.0034269347433368226",
            "extra": "mean: 45.16501452380474 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.793610310038687,
            "unit": "iter/sec",
            "range": "stddev: 0.0026344352168050085",
            "extra": "mean: 48.09169668420797 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.104116105037168,
            "unit": "iter/sec",
            "range": "stddev: 0.0024963010572487203",
            "extra": "mean: 52.34474049999783 msec\nrounds: 18"
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
          "id": "54b597c40e6595f0684e0c53b78e397f9f787a6f",
          "message": "update changelog",
          "timestamp": "2023-09-28T11:35:23+02:00",
          "tree_id": "1258b8a8737c80a49931684e95dc5ef00babc4ff",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/54b597c40e6595f0684e0c53b78e397f9f787a6f"
        },
        "date": 1695894037637,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.8543808962068526,
            "unit": "iter/sec",
            "range": "stddev: 0.03947655610911104",
            "extra": "mean: 350.3386675999991 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.21230320611533,
            "unit": "iter/sec",
            "range": "stddev: 0.011789696373214012",
            "extra": "mean: 160.97089385714622 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.374179634892899,
            "unit": "iter/sec",
            "range": "stddev: 0.010017769710485862",
            "extra": "mean: 135.6083048571577 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.130445623318533,
            "unit": "iter/sec",
            "range": "stddev: 0.003192784548133087",
            "extra": "mean: 61.99456750000617 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 21.92289002917232,
            "unit": "iter/sec",
            "range": "stddev: 0.004435368775382933",
            "extra": "mean: 45.614423950004834 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.4578629074691,
            "unit": "iter/sec",
            "range": "stddev: 0.003685943336328094",
            "extra": "mean: 48.880961052627995 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.26205363754244,
            "unit": "iter/sec",
            "range": "stddev: 0.005084474374880506",
            "extra": "mean: 54.75835411764633 msec\nrounds: 17"
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
          "id": "606cb3591a5593c2607185135bc5e3e6df3720c2",
          "message": "Merge pull request #125 from stac-utils/FeaturePartEndpoints\n\nadd feature and bbox endpoints",
          "timestamp": "2023-10-03T12:37:03+02:00",
          "tree_id": "0c4f2531060019362cf0b4c91f8d86004cb8bda8",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/606cb3591a5593c2607185135bc5e3e6df3720c2"
        },
        "date": 1696329741357,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.0462650938430316,
            "unit": "iter/sec",
            "range": "stddev: 0.008192879959366534",
            "extra": "mean: 328.27083959999186 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.357742402166192,
            "unit": "iter/sec",
            "range": "stddev: 0.006362484984385347",
            "extra": "mean: 157.2885368333393 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.740915846154953,
            "unit": "iter/sec",
            "range": "stddev: 0.0016758707012305006",
            "extra": "mean: 129.1836805714297 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.053828040852938,
            "unit": "iter/sec",
            "range": "stddev: 0.0046010555158925515",
            "extra": "mean: 62.29043923077116 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 21.995854524881672,
            "unit": "iter/sec",
            "range": "stddev: 0.003563038060857666",
            "extra": "mean: 45.46311210000056 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.423116803801662,
            "unit": "iter/sec",
            "range": "stddev: 0.005003296642701113",
            "extra": "mean: 48.964122842104835 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.13948702582866,
            "unit": "iter/sec",
            "range": "stddev: 0.004850153287224805",
            "extra": "mean: 52.24800427777944 msec\nrounds: 18"
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
          "id": "2ff16eed4bfee95ae90ed740a83a4dae80311c6d",
          "message": "Bump version: 0.7.0 → 0.8.0",
          "timestamp": "2023-10-06T13:40:14+02:00",
          "tree_id": "555d0a097a3a8474dcc933eb89cbe8ca253b416d",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/2ff16eed4bfee95ae90ed740a83a4dae80311c6d"
        },
        "date": 1696592741269,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.0816598688095125,
            "unit": "iter/sec",
            "range": "stddev: 0.01071096989453002",
            "extra": "mean: 324.5004454000025 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.302701490384409,
            "unit": "iter/sec",
            "range": "stddev: 0.00711531559108007",
            "extra": "mean: 158.66212314285073 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.694440162007406,
            "unit": "iter/sec",
            "range": "stddev: 0.004847982357362645",
            "extra": "mean: 129.96397125000314 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 17.02542364481147,
            "unit": "iter/sec",
            "range": "stddev: 0.002687803411617809",
            "extra": "mean: 58.73568968750753 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.599890304437903,
            "unit": "iter/sec",
            "range": "stddev: 0.003358171759371079",
            "extra": "mean: 44.248002380951014 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.535696636631663,
            "unit": "iter/sec",
            "range": "stddev: 0.0033294599492440066",
            "extra": "mean: 46.434532250005134 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.799747397323173,
            "unit": "iter/sec",
            "range": "stddev: 0.0024947333490095477",
            "extra": "mean: 50.50569484210667 msec\nrounds: 19"
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
          "id": "c339baf3147b2cab42d3284b2a84ca95381ab4e4",
          "message": "Merge pull request #128 from stac-utils/PgSTACDepsAndPoolCheck\n\nadd database pool check and more params in dependency",
          "timestamp": "2023-10-10T12:42:23+02:00",
          "tree_id": "e106dbcae930117ee14498a6d8e3af9ed1cc09ab",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/c339baf3147b2cab42d3284b2a84ca95381ab4e4"
        },
        "date": 1696934906431,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.6242427607115917,
            "unit": "iter/sec",
            "range": "stddev: 0.007818249495675259",
            "extra": "mean: 381.06230680001545 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.299777263610542,
            "unit": "iter/sec",
            "range": "stddev: 0.005259479117779824",
            "extra": "mean: 188.68717500001821 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.140237950676635,
            "unit": "iter/sec",
            "range": "stddev: 0.005985429441653372",
            "extra": "mean: 162.86013799999446 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 12.92289489714579,
            "unit": "iter/sec",
            "range": "stddev: 0.005461343150587882",
            "extra": "mean: 77.38204233332151 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 17.81823951526004,
            "unit": "iter/sec",
            "range": "stddev: 0.0028530441779422125",
            "extra": "mean: 56.12226725000369 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 17.12604455385229,
            "unit": "iter/sec",
            "range": "stddev: 0.0040708121064947575",
            "extra": "mean: 58.390598999992825 msec\nrounds: 17"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 15.071114507084953,
            "unit": "iter/sec",
            "range": "stddev: 0.005686965951253884",
            "extra": "mean: 66.35209357144082 msec\nrounds: 14"
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
          "id": "9a6bd27f238a51129c77e2a37987912fb4c511ef",
          "message": "Merge pull request #129 from stac-utils/search_id\n\nreplace `searchid` by `search_id` in path parameters and `searchid` by `id` in response model",
          "timestamp": "2023-10-12T16:51:11+02:00",
          "tree_id": "b926834c3db3990f481b12f2c5549c5e4c18c164",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/9a6bd27f238a51129c77e2a37987912fb4c511ef"
        },
        "date": 1697122572614,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.9753880069608027,
            "unit": "iter/sec",
            "range": "stddev: 0.029654059131826525",
            "extra": "mean: 336.0906199999931 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.403382973820592,
            "unit": "iter/sec",
            "range": "stddev: 0.005611470560787215",
            "extra": "mean: 156.1674514999917 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.565791415217377,
            "unit": "iter/sec",
            "range": "stddev: 0.008427502799748897",
            "extra": "mean: 132.17387912501266 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.058480010658545,
            "unit": "iter/sec",
            "range": "stddev: 0.005589313483648777",
            "extra": "mean: 62.27239435714133 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.41819271610086,
            "unit": "iter/sec",
            "range": "stddev: 0.004257630257703472",
            "extra": "mean: 44.606628761907054 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.847431560937732,
            "unit": "iter/sec",
            "range": "stddev: 0.004078416342660557",
            "extra": "mean: 47.96753965000278 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.733678200220577,
            "unit": "iter/sec",
            "range": "stddev: 0.0044593596914140506",
            "extra": "mean: 53.379800235290986 msec\nrounds: 17"
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
          "id": "d777eca04770622982121daa2df42d429e8c244d",
          "message": "searchInfoExtension",
          "timestamp": "2023-10-13T14:23:05+02:00",
          "tree_id": "1a444c975e6a1d0b4d06cc825a685da02598cbec",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/d777eca04770622982121daa2df42d429e8c244d"
        },
        "date": 1697200130674,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.2723215010532107,
            "unit": "iter/sec",
            "range": "stddev: 0.007861939307219018",
            "extra": "mean: 305.593444800013 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.6446120790848715,
            "unit": "iter/sec",
            "range": "stddev: 0.005197516986349158",
            "extra": "mean: 150.4978752857044 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.662024835795435,
            "unit": "iter/sec",
            "range": "stddev: 0.008724028206309587",
            "extra": "mean: 130.51380299998527 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 17.22568643157563,
            "unit": "iter/sec",
            "range": "stddev: 0.002862940553459624",
            "extra": "mean: 58.05283893749191 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 23.849138391099096,
            "unit": "iter/sec",
            "range": "stddev: 0.0032162170662202354",
            "extra": "mean: 41.930235952390504 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.664186407983102,
            "unit": "iter/sec",
            "range": "stddev: 0.0032382046641884635",
            "extra": "mean: 46.15913015000217 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 20.32791181363287,
            "unit": "iter/sec",
            "range": "stddev: 0.002474674241939581",
            "extra": "mean: 49.19344442105224 msec\nrounds: 19"
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
          "id": "715fd697c91de71e2220678f729ca3052e71e64b",
          "message": "Merge pull request #130 from stac-utils/SearchInfoExtension\n\nadd searchInfoExtension",
          "timestamp": "2023-10-13T15:10:23+02:00",
          "tree_id": "272c15f3ae633d4ec2833fc8f16389847c7944bb",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/715fd697c91de71e2220678f729ca3052e71e64b"
        },
        "date": 1697202954593,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.5271376729553303,
            "unit": "iter/sec",
            "range": "stddev: 0.017116648776261626",
            "extra": "mean: 395.7045991999962 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.231181893438,
            "unit": "iter/sec",
            "range": "stddev: 0.0031931009284519624",
            "extra": "mean: 191.16138960000626 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.110155919488124,
            "unit": "iter/sec",
            "range": "stddev: 0.009331234766880527",
            "extra": "mean: 163.6619446666714 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 13.080680459815111,
            "unit": "iter/sec",
            "range": "stddev: 0.005424354965418072",
            "extra": "mean: 76.44862230769107 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 18.031357770819334,
            "unit": "iter/sec",
            "range": "stddev: 0.003908380490088699",
            "extra": "mean: 55.4589406249999 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 16.0860755769893,
            "unit": "iter/sec",
            "range": "stddev: 0.006107296173236817",
            "extra": "mean: 62.165566437501596 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 14.505132031196093,
            "unit": "iter/sec",
            "range": "stddev: 0.0067389203025451155",
            "extra": "mean: 68.94111669230632 msec\nrounds: 13"
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
          "id": "3650371c1c81d1f64ffdb3acbd44eaa29a2f6f72",
          "message": "Merge pull request #131 from stac-utils/refactorFactory\n\nrefactor factories to allow more custom prefixes",
          "timestamp": "2023-10-17T14:46:26+02:00",
          "tree_id": "d8788873c7b83e585b354e8d521661b21d6df9f4",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/3650371c1c81d1f64ffdb3acbd44eaa29a2f6f72"
        },
        "date": 1697547141511,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.278620562303842,
            "unit": "iter/sec",
            "range": "stddev: 0.013592144740952074",
            "extra": "mean: 438.86201000000256 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 4.794542881976636,
            "unit": "iter/sec",
            "range": "stddev: 0.006683809401733469",
            "extra": "mean: 208.57045700000754 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 5.450881560263683,
            "unit": "iter/sec",
            "range": "stddev: 0.011518470539314252",
            "extra": "mean: 183.45656366667149 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 11.35109296031433,
            "unit": "iter/sec",
            "range": "stddev: 0.0066077580730807195",
            "extra": "mean: 88.09724345454644 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 15.278091871209678,
            "unit": "iter/sec",
            "range": "stddev: 0.007480775089533665",
            "extra": "mean: 65.45319981249875 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 15.182324842681734,
            "unit": "iter/sec",
            "range": "stddev: 0.004016488297138821",
            "extra": "mean: 65.86606533333565 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 14.01078784751989,
            "unit": "iter/sec",
            "range": "stddev: 0.00515860578157767",
            "extra": "mean: 71.37357376923056 msec\nrounds: 13"
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
          "id": "66cb0d5b52a7ac0b5fbf2b7c1d4b3f742c98ed99",
          "message": "Merge pull request #132 from stac-utils/CollectionsMosaics\n\nadd /collections/{collection_id} endpoints",
          "timestamp": "2023-10-17T17:14:50+02:00",
          "tree_id": "0e7de542cb81c1b1671727300ceb050b37d24c35",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/66cb0d5b52a7ac0b5fbf2b7c1d4b3f742c98ed99"
        },
        "date": 1697555989082,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.0804917346568232,
            "unit": "iter/sec",
            "range": "stddev: 0.007985116383091496",
            "extra": "mean: 324.6234972000025 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.450482293207562,
            "unit": "iter/sec",
            "range": "stddev: 0.00419396923973442",
            "extra": "mean: 155.0271676666739 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.809855219986425,
            "unit": "iter/sec",
            "range": "stddev: 0.0037063355689232968",
            "extra": "mean: 128.0433467499975 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.551913884504916,
            "unit": "iter/sec",
            "range": "stddev: 0.002950624449941064",
            "extra": "mean: 60.415974066669754 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.594702394649662,
            "unit": "iter/sec",
            "range": "stddev: 0.003187085467861386",
            "extra": "mean: 44.258162047613254 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.56930023552218,
            "unit": "iter/sec",
            "range": "stddev: 0.0033505788172156466",
            "extra": "mean: 46.36219019999146 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.62314289067521,
            "unit": "iter/sec",
            "range": "stddev: 0.002541398467986311",
            "extra": "mean: 50.96023636841545 msec\nrounds: 19"
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
          "id": "0a953b00c2f79162ed29d90b159d24bad54c4b99",
          "message": "update changelog",
          "timestamp": "2023-10-17T18:37:10+02:00",
          "tree_id": "671982c8894e845a2f18cf48a4b7e0186aa3c5cb",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/0a953b00c2f79162ed29d90b159d24bad54c4b99"
        },
        "date": 1697560968822,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.561999013134244,
            "unit": "iter/sec",
            "range": "stddev: 0.004826094126186881",
            "extra": "mean: 390.3202128000203 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.35772300287066,
            "unit": "iter/sec",
            "range": "stddev: 0.009890558830028028",
            "extra": "mean: 186.64645399999245 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.6676705003355,
            "unit": "iter/sec",
            "range": "stddev: 0.005170591180102109",
            "extra": "mean: 149.97741714286607 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 13.756543503616,
            "unit": "iter/sec",
            "range": "stddev: 0.0068010833160209875",
            "extra": "mean: 72.69267892309891 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 19.12568810281359,
            "unit": "iter/sec",
            "range": "stddev: 0.00419137107708159",
            "extra": "mean: 52.28570049999348 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 18.199604294991655,
            "unit": "iter/sec",
            "range": "stddev: 0.005472619341552828",
            "extra": "mean: 54.9462495882501 msec\nrounds: 17"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 16.21248800124085,
            "unit": "iter/sec",
            "range": "stddev: 0.0038518185239742085",
            "extra": "mean: 61.68084749999281 msec\nrounds: 16"
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
          "id": "719f16b8785970ddd934a0c9e9577b6470596af2",
          "message": "Merge pull request #135 from stac-utils/feat/required-path-dependency\n\nmake `path_dependency` a required input to `MosaicTilerFactory` class",
          "timestamp": "2023-10-18T18:17:48+02:00",
          "tree_id": "c10c6795cc93b14013a3f0102f42c35a2e0dca51",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/719f16b8785970ddd934a0c9e9577b6470596af2"
        },
        "date": 1697646181474,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.012248647030877,
            "unit": "iter/sec",
            "range": "stddev: 0.0044750873463885055",
            "extra": "mean: 331.97790660000237 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.265700965505456,
            "unit": "iter/sec",
            "range": "stddev: 0.006232740628037028",
            "extra": "mean: 159.59906249999753 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.734649663451696,
            "unit": "iter/sec",
            "range": "stddev: 0.0031915533808914254",
            "extra": "mean: 129.28833800000916 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 15.978089224940529,
            "unit": "iter/sec",
            "range": "stddev: 0.003128456160816235",
            "extra": "mean: 62.58570633333799 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 21.58781027972297,
            "unit": "iter/sec",
            "range": "stddev: 0.00460577146521851",
            "extra": "mean: 46.3224378499973 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.56810658405284,
            "unit": "iter/sec",
            "range": "stddev: 0.003275168493760069",
            "extra": "mean: 48.61896236843378 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.60657675185482,
            "unit": "iter/sec",
            "range": "stddev: 0.004157908888417065",
            "extra": "mean: 53.74443742857287 msec\nrounds: 14"
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
          "id": "b4dc2a44a392b8ac556c51203e846dad863650c7",
          "message": "update docs",
          "timestamp": "2023-10-18T18:20:50+02:00",
          "tree_id": "1ef1865b106579c3baf2f72676bba6890fc21340",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/b4dc2a44a392b8ac556c51203e846dad863650c7"
        },
        "date": 1697646379927,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.4328043053753836,
            "unit": "iter/sec",
            "range": "stddev: 0.018594305332043235",
            "extra": "mean: 411.04826960000764 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.181418133002949,
            "unit": "iter/sec",
            "range": "stddev: 0.01154257622329996",
            "extra": "mean: 192.99735599999508 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.319006160444081,
            "unit": "iter/sec",
            "range": "stddev: 0.010035278125754419",
            "extra": "mean: 158.25273383334113 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 13.373898194324134,
            "unit": "iter/sec",
            "range": "stddev: 0.004607365247452833",
            "extra": "mean: 74.77251474999254 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 16.69539263080154,
            "unit": "iter/sec",
            "range": "stddev: 0.006026136098012846",
            "extra": "mean: 59.89676446153698 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 16.081908927479294,
            "unit": "iter/sec",
            "range": "stddev: 0.0057387134630660485",
            "extra": "mean: 62.18167286666396 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 15.147500047611144,
            "unit": "iter/sec",
            "range": "stddev: 0.004708490291997831",
            "extra": "mean: 66.01749442857445 msec\nrounds: 14"
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
          "id": "bd13261720cad13882d0de3ea35837b96367322f",
          "message": "fix docs",
          "timestamp": "2023-10-18T18:54:15+02:00",
          "tree_id": "52e6a165cde94c7d2bb707cdd0fa6de0fafa4afa",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/bd13261720cad13882d0de3ea35837b96367322f"
        },
        "date": 1697648405468,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.55076057285529,
            "unit": "iter/sec",
            "range": "stddev: 0.004679690831581262",
            "extra": "mean: 392.0399313999951 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.660928829087087,
            "unit": "iter/sec",
            "range": "stddev: 0.00941553755680749",
            "extra": "mean: 176.6494563333462 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.760322063171795,
            "unit": "iter/sec",
            "range": "stddev: 0.008519861003098126",
            "extra": "mean: 147.92194671429928 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 14.418363038413602,
            "unit": "iter/sec",
            "range": "stddev: 0.004245651369302783",
            "extra": "mean: 69.35600090910364 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 19.547849827904102,
            "unit": "iter/sec",
            "range": "stddev: 0.005619487771314775",
            "extra": "mean: 51.15652150000268 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 17.82832019391831,
            "unit": "iter/sec",
            "range": "stddev: 0.004235921487784439",
            "extra": "mean: 56.09053400000777 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 15.404313124698001,
            "unit": "iter/sec",
            "range": "stddev: 0.006322061233258118",
            "extra": "mean: 64.91688346666251 msec\nrounds: 15"
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
          "id": "ed26e44c951e97d6478609ea72b0de4f94c400d2",
          "message": "0.8.0 -> 1.0.0a0",
          "timestamp": "2023-10-20T00:41:19+02:00",
          "tree_id": "2902a0bc718f839c0ecd34d1f7d8309812c24dec",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/ed26e44c951e97d6478609ea72b0de4f94c400d2"
        },
        "date": 1697755653490,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.275313822590627,
            "unit": "iter/sec",
            "range": "stddev: 0.031018673699682676",
            "extra": "mean: 439.49981320001825 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.070000359280044,
            "unit": "iter/sec",
            "range": "stddev: 0.009576282425448666",
            "extra": "mean: 197.23864480001794 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 5.961090300464609,
            "unit": "iter/sec",
            "range": "stddev: 0.004196439838002592",
            "extra": "mean: 167.7545465000018 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 12.647999335915099,
            "unit": "iter/sec",
            "range": "stddev: 0.006120028801638101",
            "extra": "mean: 79.06388776922313 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 18.617179875411026,
            "unit": "iter/sec",
            "range": "stddev: 0.0033492882370994644",
            "extra": "mean: 53.71382812499803 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 17.163054858743457,
            "unit": "iter/sec",
            "range": "stddev: 0.005414625199886117",
            "extra": "mean: 58.26468587499534 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 14.92206223415983,
            "unit": "iter/sec",
            "range": "stddev: 0.005543148509597111",
            "extra": "mean: 67.01486592857009 msec\nrounds: 14"
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
          "id": "14e7c22c8ff9e40e4155b09edfbbb3e2e120d5f6",
          "message": "add API documentation",
          "timestamp": "2023-10-20T09:50:34+02:00",
          "tree_id": "82f61a0b02890012ef0e02e99452e922128e05ae",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/14e7c22c8ff9e40e4155b09edfbbb3e2e120d5f6"
        },
        "date": 1697788596069,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.3178437171843003,
            "unit": "iter/sec",
            "range": "stddev: 0.01045514372830979",
            "extra": "mean: 431.4354728000353 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 4.916722612496413,
            "unit": "iter/sec",
            "range": "stddev: 0.002847258850427448",
            "extra": "mean: 203.38751619999584 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 5.816189142432548,
            "unit": "iter/sec",
            "range": "stddev: 0.00594378712821577",
            "extra": "mean: 171.93388583332117 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 12.131534647978654,
            "unit": "iter/sec",
            "range": "stddev: 0.005434837082621646",
            "extra": "mean: 82.42980208333488 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 16.811827855446,
            "unit": "iter/sec",
            "range": "stddev: 0.005203989890387697",
            "extra": "mean: 59.48193192306935 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 16.068089928997587,
            "unit": "iter/sec",
            "range": "stddev: 0.004597870875271898",
            "extra": "mean: 62.235150812501416 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 14.474409915811279,
            "unit": "iter/sec",
            "range": "stddev: 0.00402919891678058",
            "extra": "mean: 69.08744507143183 msec\nrounds: 14"
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
          "id": "d08c2be14c6d29c7c227ef7bb44cc489d338cab2",
          "message": "add API documentation",
          "timestamp": "2023-10-20T09:51:23+02:00",
          "tree_id": "71c1a72c63fd9095ce8ef053fd4ac9b65c1e297c",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/d08c2be14c6d29c7c227ef7bb44cc489d338cab2"
        },
        "date": 1697788614475,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.1728814240964773,
            "unit": "iter/sec",
            "range": "stddev: 0.006620786318729979",
            "extra": "mean: 315.17093339999747 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.517209299584092,
            "unit": "iter/sec",
            "range": "stddev: 0.009710768480580145",
            "extra": "mean: 153.4399087142739 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.737051799371939,
            "unit": "iter/sec",
            "range": "stddev: 0.003262015147741317",
            "extra": "mean: 129.24819762498885 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.872042788555042,
            "unit": "iter/sec",
            "range": "stddev: 0.0027529624572952493",
            "extra": "mean: 59.26964579999397 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 23.53159246440274,
            "unit": "iter/sec",
            "range": "stddev: 0.003060171471657778",
            "extra": "mean: 42.49606147619391 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.53162084314477,
            "unit": "iter/sec",
            "range": "stddev: 0.0034324918934458995",
            "extra": "mean: 46.4433219999961 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.930171168601355,
            "unit": "iter/sec",
            "range": "stddev: 0.0025064241238868835",
            "extra": "mean: 50.17518372222677 msec\nrounds: 18"
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
          "id": "7da390e42d3abaace5ca9a7172c799289e4cacf7",
          "message": "add missing requirements for docs",
          "timestamp": "2023-10-20T09:55:36+02:00",
          "tree_id": "46e680a013b0399a9ca859674c009da0ba84483e",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/7da390e42d3abaace5ca9a7172c799289e4cacf7"
        },
        "date": 1697788822203,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.2642519944880277,
            "unit": "iter/sec",
            "range": "stddev: 0.005558203255794542",
            "extra": "mean: 306.3488975999974 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.681597848840124,
            "unit": "iter/sec",
            "range": "stddev: 0.00531424037106804",
            "extra": "mean: 149.6647991428566 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.817097140167826,
            "unit": "iter/sec",
            "range": "stddev: 0.005941497143954886",
            "extra": "mean: 127.92472475000238 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 17.08762719773413,
            "unit": "iter/sec",
            "range": "stddev: 0.002951705445805697",
            "extra": "mean: 58.521875999998585 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 23.55179942513349,
            "unit": "iter/sec",
            "range": "stddev: 0.003321362592470791",
            "extra": "mean: 42.45960072727361 msec\nrounds: 22"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.73804924812203,
            "unit": "iter/sec",
            "range": "stddev: 0.003091866473980786",
            "extra": "mean: 46.00228790476178 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 20.632595374171473,
            "unit": "iter/sec",
            "range": "stddev: 0.002465435793716597",
            "extra": "mean: 48.46700000000151 msec\nrounds: 19"
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
          "id": "89968616c11486e4fe781bc721d644ef475db342",
          "message": "Merge pull request #137 from stac-utils/ItemIdParams\n\nrename `dependencies.ItemPathParams` to `ItemIdParams`",
          "timestamp": "2023-10-20T10:47:29+02:00",
          "tree_id": "d7c9a2ce8bb1bad941be6167269c168a3b2b80f9",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/89968616c11486e4fe781bc721d644ef475db342"
        },
        "date": 1697791948994,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.1292546637224676,
            "unit": "iter/sec",
            "range": "stddev: 0.0037534285084698726",
            "extra": "mean: 319.56491480000864 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.3539461682824045,
            "unit": "iter/sec",
            "range": "stddev: 0.007262315398799213",
            "extra": "mean: 157.38251057142958 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.7128344604279,
            "unit": "iter/sec",
            "range": "stddev: 0.004404645505286308",
            "extra": "mean: 129.65402085714166 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.401495811170353,
            "unit": "iter/sec",
            "range": "stddev: 0.003489241366838052",
            "extra": "mean: 60.970048799996825 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 21.86456329917388,
            "unit": "iter/sec",
            "range": "stddev: 0.004395099386952481",
            "extra": "mean: 45.73610670000363 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 20.769246469984296,
            "unit": "iter/sec",
            "range": "stddev: 0.003209803752640471",
            "extra": "mean: 48.14811174999534 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.948333649168667,
            "unit": "iter/sec",
            "range": "stddev: 0.003172482567348697",
            "extra": "mean: 52.77508927777793 msec\nrounds: 18"
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
          "id": "e722f22a86f648bd54e3c72416eba22c2a40de9c",
          "message": "update migration guide",
          "timestamp": "2023-10-20T10:53:27+02:00",
          "tree_id": "bd196a6c74f7b1ef933061245c22b4d67393d687",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/e722f22a86f648bd54e3c72416eba22c2a40de9c"
        },
        "date": 1697792319815,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.5366392721851807,
            "unit": "iter/sec",
            "range": "stddev: 0.008155487162338932",
            "extra": "mean: 394.222391400001 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.676685399214859,
            "unit": "iter/sec",
            "range": "stddev: 0.008408904030293398",
            "extra": "mean: 176.15913683331996 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.974078587788827,
            "unit": "iter/sec",
            "range": "stddev: 0.009330520604605427",
            "extra": "mean: 143.3881174999859 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 14.07994222735474,
            "unit": "iter/sec",
            "range": "stddev: 0.0024866211868194983",
            "extra": "mean: 71.0230186923057 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 19.208937226974882,
            "unit": "iter/sec",
            "range": "stddev: 0.003151791395503009",
            "extra": "mean: 52.059100833320024 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 17.61841900172261,
            "unit": "iter/sec",
            "range": "stddev: 0.0038886897089550256",
            "extra": "mean: 56.75878181250127 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 18.237156927910696,
            "unit": "iter/sec",
            "range": "stddev: 0.0026842544061923003",
            "extra": "mean: 54.83310824998 msec\nrounds: 16"
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
          "id": "b600454d19b093bb966da09359e2cb3d6702b65d",
          "message": "release 1.0.0a1",
          "timestamp": "2023-10-20T10:59:06+02:00",
          "tree_id": "20f7d80bcea838218c809d447649e24ea2d09df9",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/b600454d19b093bb966da09359e2cb3d6702b65d"
        },
        "date": 1697792677542,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.5918519989144815,
            "unit": "iter/sec",
            "range": "stddev: 0.01306112472235142",
            "extra": "mean: 385.8244993999733 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.355767032321091,
            "unit": "iter/sec",
            "range": "stddev: 0.008717743793159732",
            "extra": "mean: 186.7146188333398 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.41382680810771,
            "unit": "iter/sec",
            "range": "stddev: 0.00393739037516865",
            "extra": "mean: 155.91315916667745 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 13.580170793693657,
            "unit": "iter/sec",
            "range": "stddev: 0.006003948187873971",
            "extra": "mean: 73.63677638460769 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 19.281931756049417,
            "unit": "iter/sec",
            "range": "stddev: 0.0035728310951774764",
            "extra": "mean: 51.86202361110759 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 17.72084827632397,
            "unit": "iter/sec",
            "range": "stddev: 0.0062857537643453264",
            "extra": "mean: 56.43070717647614 msec\nrounds: 17"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 16.70510581118353,
            "unit": "iter/sec",
            "range": "stddev: 0.004737518958473324",
            "extra": "mean: 59.86193750000268 msec\nrounds: 16"
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
          "id": "a930989f1b70cb2f8c71dc13b640f96797e72eaf",
          "message": "fix tests",
          "timestamp": "2023-10-26T09:19:49+02:00",
          "tree_id": "c19fe8c9f480d3a4e9143e5f5dfe8249308f7b22",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/a930989f1b70cb2f8c71dc13b640f96797e72eaf"
        },
        "date": 1698305208730,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.638475314992529,
            "unit": "iter/sec",
            "range": "stddev: 0.008539802250124334",
            "extra": "mean: 379.00676739999426 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.218189068352598,
            "unit": "iter/sec",
            "range": "stddev: 0.011762478253970062",
            "extra": "mean: 191.6373644000032 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.251834092752919,
            "unit": "iter/sec",
            "range": "stddev: 0.011646686829126602",
            "extra": "mean: 159.95306100000204 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 13.045953205816026,
            "unit": "iter/sec",
            "range": "stddev: 0.008093204488759227",
            "extra": "mean: 76.6521222500008 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 18.24978970792853,
            "unit": "iter/sec",
            "range": "stddev: 0.005643937056266276",
            "extra": "mean: 54.795151944438835 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 16.557847595383045,
            "unit": "iter/sec",
            "range": "stddev: 0.005179258651796023",
            "extra": "mean: 60.39432325001215 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 16.154306974093256,
            "unit": "iter/sec",
            "range": "stddev: 0.00463164191324969",
            "extra": "mean: 61.90299599999586 msec\nrounds: 15"
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
          "id": "fea688e66170146b7ea8b3a6c3c76352677e7646",
          "message": "fetch",
          "timestamp": "2023-10-26T09:23:53+02:00",
          "tree_id": "bbcac98fe3de74bba078340a568152f9ca0231ec",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/fea688e66170146b7ea8b3a6c3c76352677e7646"
        },
        "date": 1698305395125,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.103882645186873,
            "unit": "iter/sec",
            "range": "stddev: 0.007771199825156561",
            "extra": "mean: 322.1771291999971 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.427443458810929,
            "unit": "iter/sec",
            "range": "stddev: 0.009054492340125526",
            "extra": "mean: 155.58285442856297 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.808565329509389,
            "unit": "iter/sec",
            "range": "stddev: 0.006204269681076905",
            "extra": "mean: 128.06449812501342 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.58382130287634,
            "unit": "iter/sec",
            "range": "stddev: 0.0033537855678115354",
            "extra": "mean: 60.29973320000484 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 22.51450490545945,
            "unit": "iter/sec",
            "range": "stddev: 0.0039050087657066953",
            "extra": "mean: 44.415811238092736 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.57044716985367,
            "unit": "iter/sec",
            "range": "stddev: 0.004403934506586983",
            "extra": "mean: 46.35972505000154 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.965412341150813,
            "unit": "iter/sec",
            "range": "stddev: 0.003671157854089316",
            "extra": "mean: 50.08661894444799 msec\nrounds: 18"
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
          "id": "694e18552f0090d68fcb3d05d914ca32b70db6d4",
          "message": "update endpoints documentation",
          "timestamp": "2023-10-26T09:54:29+02:00",
          "tree_id": "2263245c279f30aa1f14e6cc34a2274c7910a25e",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/694e18552f0090d68fcb3d05d914ca32b70db6d4"
        },
        "date": 1698307249677,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.3807941443038305,
            "unit": "iter/sec",
            "range": "stddev: 0.017561085529793054",
            "extra": "mean: 420.02791480000496 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.005336284113745,
            "unit": "iter/sec",
            "range": "stddev: 0.0086034816441855",
            "extra": "mean: 199.78677620000553 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 5.750436314115982,
            "unit": "iter/sec",
            "range": "stddev: 0.0018364972249307393",
            "extra": "mean: 173.8998478333258 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 12.075857202006642,
            "unit": "iter/sec",
            "range": "stddev: 0.004537456199124991",
            "extra": "mean: 82.80985633333178 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 16.32577508510354,
            "unit": "iter/sec",
            "range": "stddev: 0.006707566889904753",
            "extra": "mean: 61.25283453846245 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 15.995684509347914,
            "unit": "iter/sec",
            "range": "stddev: 0.005806354531109036",
            "extra": "mean: 62.51686193332944 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 14.65432816784337,
            "unit": "iter/sec",
            "range": "stddev: 0.00472913341502751",
            "extra": "mean: 68.2392251999886 msec\nrounds: 15"
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
          "id": "8afd86b6ff5413408282a825ea6881db7a42865f",
          "message": "Merge pull request #138 from stac-utils/UpdateTitiler0.15.2\n\nupdate titiler dependency",
          "timestamp": "2023-11-02T13:52:20+01:00",
          "tree_id": "a3fa88cbb2f728ae96fae435fd9b56a4d6aaa577",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/8afd86b6ff5413408282a825ea6881db7a42865f"
        },
        "date": 1698929900699,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.6740378766929735,
            "unit": "iter/sec",
            "range": "stddev: 0.006899463786214864",
            "extra": "mean: 373.966280999997 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.465883581332426,
            "unit": "iter/sec",
            "range": "stddev: 0.006603600733097727",
            "extra": "mean: 182.95303679999506 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.732433922159408,
            "unit": "iter/sec",
            "range": "stddev: 0.0029619714426611056",
            "extra": "mean: 148.53469214284587 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 14.373125760985706,
            "unit": "iter/sec",
            "range": "stddev: 0.00714563872567039",
            "extra": "mean: 69.5742886153819 msec\nrounds: 13"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 20.142383954088288,
            "unit": "iter/sec",
            "range": "stddev: 0.0042187082110757826",
            "extra": "mean: 49.64655635000099 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 18.567683904911487,
            "unit": "iter/sec",
            "range": "stddev: 0.005568684245569398",
            "extra": "mean: 53.85701335294069 msec\nrounds: 17"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 17.718508164235388,
            "unit": "iter/sec",
            "range": "stddev: 0.0037433942414929686",
            "extra": "mean: 56.43816007142683 msec\nrounds: 14"
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
          "id": "dadfd91edcb6811787a088ff3a75ca24d6869d10",
          "message": "version update",
          "timestamp": "2023-11-02T13:53:31+01:00",
          "tree_id": "84db66be970fa5f025823960489f67cdd0c754e6",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/dadfd91edcb6811787a088ff3a75ca24d6869d10"
        },
        "date": 1698930013871,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 2.5015169549028413,
            "unit": "iter/sec",
            "range": "stddev: 0.008863373066375987",
            "extra": "mean: 399.75743439997586 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 5.17687922452723,
            "unit": "iter/sec",
            "range": "stddev: 0.010160423444970788",
            "extra": "mean: 193.16656939998893 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 6.237948887051647,
            "unit": "iter/sec",
            "range": "stddev: 0.0030383656891843826",
            "extra": "mean: 160.3091044999966 msec\nrounds: 6"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 13.423038605463663,
            "unit": "iter/sec",
            "range": "stddev: 0.004999019666810706",
            "extra": "mean: 74.49878000000415 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 17.740672620652187,
            "unit": "iter/sec",
            "range": "stddev: 0.0056780283371894395",
            "extra": "mean: 56.36764858824376 msec\nrounds: 17"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 16.810388943084043,
            "unit": "iter/sec",
            "range": "stddev: 0.0051613171014526",
            "extra": "mean: 59.48702337499512 msec\nrounds: 16"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 15.04207899758891,
            "unit": "iter/sec",
            "range": "stddev: 0.006122023471623946",
            "extra": "mean: 66.48017206665978 msec\nrounds: 15"
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
          "id": "32819c8294f99cdfa1655b5b30f9e87651975084",
          "message": "Merge pull request #139 from stac-utils/feat/remove-reverse\n\nremove reverse option",
          "timestamp": "2023-11-03T08:46:30+01:00",
          "tree_id": "3d08ed5e1c6f3af9897e6e7f4c0ccc5588adc506",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/32819c8294f99cdfa1655b5b30f9e87651975084"
        },
        "date": 1698997877544,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 4.353793047403886,
            "unit": "iter/sec",
            "range": "stddev: 0.002849179252438691",
            "extra": "mean: 229.6847803999981 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 8.807826711443738,
            "unit": "iter/sec",
            "range": "stddev: 0.004404224111827514",
            "extra": "mean: 113.53538537500185 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 9.859243351097607,
            "unit": "iter/sec",
            "range": "stddev: 0.0037641690896180876",
            "extra": "mean: 101.42766177778464 msec\nrounds: 9"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 22.30585451853073,
            "unit": "iter/sec",
            "range": "stddev: 0.0034349511654848787",
            "extra": "mean: 44.83127957143465 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 31.01473895407288,
            "unit": "iter/sec",
            "range": "stddev: 0.003019440149818666",
            "extra": "mean: 32.24273470367801 msec\nrounds: 27"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 28.553554077961213,
            "unit": "iter/sec",
            "range": "stddev: 0.0028231945989486717",
            "extra": "mean: 35.02190996152876 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 25.75150349778378,
            "unit": "iter/sec",
            "range": "stddev: 0.003189181777540428",
            "extra": "mean: 38.83268408332204 msec\nrounds: 24"
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
          "id": "6008d1bcff5a7c69e609a9bd6d749f61b23d7dfc",
          "message": "version update",
          "timestamp": "2023-11-03T09:10:43+01:00",
          "tree_id": "cf3c01de356157d251fe6990d80ccbb361ec7eb3",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/6008d1bcff5a7c69e609a9bd6d749f61b23d7dfc"
        },
        "date": 1698999368602,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.1434173194026047,
            "unit": "iter/sec",
            "range": "stddev: 0.009404552700213646",
            "extra": "mean: 318.1251161999853 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 6.5239078192188895,
            "unit": "iter/sec",
            "range": "stddev: 0.006179899103655339",
            "extra": "mean: 153.2823619999785 msec\nrounds: 7"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 7.829973265877381,
            "unit": "iter/sec",
            "range": "stddev: 0.006134704165426064",
            "extra": "mean: 127.71435687500343 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 16.844352443983887,
            "unit": "iter/sec",
            "range": "stddev: 0.0032825767132740077",
            "extra": "mean: 59.36707886667136 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 23.081416978086292,
            "unit": "iter/sec",
            "range": "stddev: 0.004078982380898048",
            "extra": "mean: 43.32489642856022 msec\nrounds: 21"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 21.508552825842923,
            "unit": "iter/sec",
            "range": "stddev: 0.0030551132213525365",
            "extra": "mean: 46.49313266667024 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 19.523241606968313,
            "unit": "iter/sec",
            "range": "stddev: 0.003894734876568537",
            "extra": "mean: 51.22100213332791 msec\nrounds: 15"
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
          "id": "bd2a5fe8a37bf76344cfb126eb59bf92421b9fd8",
          "message": "Merge pull request #143 from stac-utils/feat/algorithm-in-statistics-1.0\n\nenable algorithm in statistics endpoints",
          "timestamp": "2023-11-10T09:19:59+01:00",
          "tree_id": "a7dc62769e69bff4a0020ce3d1336812f6c25ca0",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/bd2a5fe8a37bf76344cfb126eb59bf92421b9fd8"
        },
        "date": 1699604717846,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 4.327855461364762,
            "unit": "iter/sec",
            "range": "stddev: 0.0024626709463587628",
            "extra": "mean: 231.06132099999854 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 8.913073653751589,
            "unit": "iter/sec",
            "range": "stddev: 0.003532731586328518",
            "extra": "mean: 112.1947421111113 msec\nrounds: 9"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 10.040542324310625,
            "unit": "iter/sec",
            "range": "stddev: 0.004707538951016666",
            "extra": "mean: 99.59621380000101 msec\nrounds: 10"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 22.23181408900801,
            "unit": "iter/sec",
            "range": "stddev: 0.0029555676197991878",
            "extra": "mean: 44.98058484999774 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 31.08850710664927,
            "unit": "iter/sec",
            "range": "stddev: 0.002507618787962129",
            "extra": "mean: 32.166227750000836 msec\nrounds: 28"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 27.960816842614,
            "unit": "iter/sec",
            "range": "stddev: 0.002487701097992809",
            "extra": "mean: 35.76433426923131 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 25.292231723716004,
            "unit": "iter/sec",
            "range": "stddev: 0.0030957151606665423",
            "extra": "mean: 39.53783165217171 msec\nrounds: 23"
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
          "id": "e06ec4271fc00b035b184bb34a2f258cf4111943",
          "message": "update version",
          "timestamp": "2023-11-10T09:21:50+01:00",
          "tree_id": "d7fb2a2ef4f3d282da3b2c577b4d5c2197fc42d3",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/e06ec4271fc00b035b184bb34a2f258cf4111943"
        },
        "date": 1699604827290,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 4.314994643494925,
            "unit": "iter/sec",
            "range": "stddev: 0.007890747356913783",
            "extra": "mean: 231.74999800000933 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 8.740640077378847,
            "unit": "iter/sec",
            "range": "stddev: 0.003516534579408925",
            "extra": "mean: 114.40809724999923 msec\nrounds: 8"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 9.94967056650729,
            "unit": "iter/sec",
            "range": "stddev: 0.004716384114961808",
            "extra": "mean: 100.50584019999746 msec\nrounds: 10"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 21.488583339689352,
            "unit": "iter/sec",
            "range": "stddev: 0.004147034418386272",
            "extra": "mean: 46.53633905000163 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 29.5003930590098,
            "unit": "iter/sec",
            "range": "stddev: 0.0028883472758721032",
            "extra": "mean: 33.897853428586345 msec\nrounds: 28"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 26.76836615693257,
            "unit": "iter/sec",
            "range": "stddev: 0.0031436629980399343",
            "extra": "mean: 37.35752844000217 msec\nrounds: 25"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 24.792826934135608,
            "unit": "iter/sec",
            "range": "stddev: 0.0030632689007942587",
            "extra": "mean: 40.33424678261138 msec\nrounds: 23"
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
          "id": "7070461600d123d6f1fb0b614b9b623e97ca562c",
          "message": "1.0.0a4 -> 1.0.0",
          "timestamp": "2023-12-12T15:09:36+01:00",
          "tree_id": "b60c99b2e13ecb130a260cc02326fd5f7d62b5e8",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/7070461600d123d6f1fb0b614b9b623e97ca562c"
        },
        "date": 1702390429672,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 3.8935354713251606,
            "unit": "iter/sec",
            "range": "stddev: 0.0030836871465401874",
            "extra": "mean: 256.83598040000675 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 9.319992018814338,
            "unit": "iter/sec",
            "range": "stddev: 0.0034898352749363594",
            "extra": "mean: 107.29622922222386 msec\nrounds: 9"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 12.519992550103066,
            "unit": "iter/sec",
            "range": "stddev: 0.003964977147196747",
            "extra": "mean: 79.87225200000363 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 21.740627371501,
            "unit": "iter/sec",
            "range": "stddev: 0.0032755230210969612",
            "extra": "mean: 45.99683270000128 msec\nrounds: 20"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 28.946581161941307,
            "unit": "iter/sec",
            "range": "stddev: 0.0029263554095512127",
            "extra": "mean: 34.54639407692092 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 24.064223486879328,
            "unit": "iter/sec",
            "range": "stddev: 0.0030825214558640674",
            "extra": "mean: 41.55546513043463 msec\nrounds: 23"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 24.049817310215587,
            "unit": "iter/sec",
            "range": "stddev: 0.003276621405447292",
            "extra": "mean: 41.58035743478318 msec\nrounds: 23"
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
          "id": "2b5014749770b7651f4b30d43720ff20bec913da",
          "message": "Merge pull request #148 from hrodmn/fix-map-endpoint\n\nuse the cellSize parameter instead of the _resolution method for the /map endpoint",
          "timestamp": "2024-01-08T22:17:10+01:00",
          "tree_id": "6a1597b52dc8b0e3144f63816acc3a5edb66d170",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/2b5014749770b7651f4b30d43720ff20bec913da"
        },
        "date": 1704748916023,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 4.856575392117585,
            "unit": "iter/sec",
            "range": "stddev: 0.005436810153753326",
            "extra": "mean: 205.90640919999714 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 11.951900666649422,
            "unit": "iter/sec",
            "range": "stddev: 0.003920029152197756",
            "extra": "mean: 83.66870072727424 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.626521684869685,
            "unit": "iter/sec",
            "range": "stddev: 0.0036145660949407805",
            "extra": "mean: 63.99376778571561 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 26.196962636393966,
            "unit": "iter/sec",
            "range": "stddev: 0.0031985936255481354",
            "extra": "mean: 38.172364249997294 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 31.881665635196065,
            "unit": "iter/sec",
            "range": "stddev: 0.003590330526987624",
            "extra": "mean: 31.365989827584187 msec\nrounds: 29"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 26.586197425334312,
            "unit": "iter/sec",
            "range": "stddev: 0.002950851975215706",
            "extra": "mean: 37.61350237499883 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 26.775912303179368,
            "unit": "iter/sec",
            "range": "stddev: 0.0027931364562379358",
            "extra": "mean: 37.347000120001894 msec\nrounds: 25"
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
          "id": "941af3fa99e556076f13662a155de884bc3db366",
          "message": "Merge pull request #149 from stac-utils/feature/update-titiler-version\n\nupdate titiler version and fix starlette breaking change",
          "timestamp": "2024-01-09T10:13:58+01:00",
          "tree_id": "ee0be11325a47a901e78bf5a07bec47d860c4e55",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/941af3fa99e556076f13662a155de884bc3db366"
        },
        "date": 1704792024523,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.012791189405806,
            "unit": "iter/sec",
            "range": "stddev: 0.005621021118485608",
            "extra": "mean: 199.4896580000045 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.01236517489271,
            "unit": "iter/sec",
            "range": "stddev: 0.005418514512999066",
            "extra": "mean: 83.24755245454246 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.497359005167606,
            "unit": "iter/sec",
            "range": "stddev: 0.003087450191802707",
            "extra": "mean: 64.5271235999985 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 25.81127717359301,
            "unit": "iter/sec",
            "range": "stddev: 0.0035024633596858",
            "extra": "mean: 38.74275547368418 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 32.08035171446338,
            "unit": "iter/sec",
            "range": "stddev: 0.0029693975631427372",
            "extra": "mean: 31.171728068964764 msec\nrounds: 29"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 26.335418009207118,
            "unit": "iter/sec",
            "range": "stddev: 0.0030205656064361914",
            "extra": "mean: 37.9716775199995 msec\nrounds: 25"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 26.513295074315955,
            "unit": "iter/sec",
            "range": "stddev: 0.0030409608099258036",
            "extra": "mean: 37.71692644000041 msec\nrounds: 25"
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
          "id": "be9cf4099667b3b327307a54dca99d52ec39b336",
          "message": "Merge pull request #150 from stac-utils/feature/add-point-endpoint\n\nFeature/add point endpoint",
          "timestamp": "2024-01-10T12:18:43+01:00",
          "tree_id": "9636c3d5ae48703feecf36e70255f5377282b4e9",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/be9cf4099667b3b327307a54dca99d52ec39b336"
        },
        "date": 1704885927663,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 4.990966380796493,
            "unit": "iter/sec",
            "range": "stddev: 0.005415693423719217",
            "extra": "mean: 200.36199880000254 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.073579621149442,
            "unit": "iter/sec",
            "range": "stddev: 0.002951458697033128",
            "extra": "mean: 82.82547772727546 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.89292338248027,
            "unit": "iter/sec",
            "range": "stddev: 0.002808726703149482",
            "extra": "mean: 62.921086066667925 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 27.74436702940725,
            "unit": "iter/sec",
            "range": "stddev: 0.0029178799983380797",
            "extra": "mean: 36.043352473677416 msec\nrounds: 19"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 33.43025834997434,
            "unit": "iter/sec",
            "range": "stddev: 0.003258647077933348",
            "extra": "mean: 29.913020399998423 msec\nrounds: 30"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 27.44777588262049,
            "unit": "iter/sec",
            "range": "stddev: 0.003261675792148392",
            "extra": "mean: 36.432824440000786 msec\nrounds: 25"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 27.612143878309155,
            "unit": "iter/sec",
            "range": "stddev: 0.0028993684189269255",
            "extra": "mean: 36.21594920000234 msec\nrounds: 25"
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
          "id": "d1493c445a2e8763dc61eaa486c8e967a29e87d3",
          "message": "Merge pull request #151 from stac-utils/patch/rename-point-endpoint\n\nrename point endpoint to with `/point` prefix",
          "timestamp": "2024-01-10T14:13:06+01:00",
          "tree_id": "56f51df8acf6fc5385d6d849cec9c505db4f7150",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/d1493c445a2e8763dc61eaa486c8e967a29e87d3"
        },
        "date": 1704892642917,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 4.979401103966184,
            "unit": "iter/sec",
            "range": "stddev: 0.0037012456178299796",
            "extra": "mean: 200.82736440000417 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.20536239912046,
            "unit": "iter/sec",
            "range": "stddev: 0.0031445362101981066",
            "extra": "mean: 81.93120099998521 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.809027846980646,
            "unit": "iter/sec",
            "range": "stddev: 0.0028356757171756463",
            "extra": "mean: 63.25499642857478 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 26.69318999899812,
            "unit": "iter/sec",
            "range": "stddev: 0.0040752970328014875",
            "extra": "mean: 37.4627386250026 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 31.292424634846117,
            "unit": "iter/sec",
            "range": "stddev: 0.004488607743465359",
            "extra": "mean: 31.956616071432062 msec\nrounds: 28"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 26.687571105168413,
            "unit": "iter/sec",
            "range": "stddev: 0.0035355440003900997",
            "extra": "mean: 37.47062615999312 msec\nrounds: 25"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 26.98616847609061,
            "unit": "iter/sec",
            "range": "stddev: 0.0031347898686231637",
            "extra": "mean: 37.056020045453536 msec\nrounds: 22"
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
          "id": "0c15e36ca08b2df011fda15da63eeb112fd6e29e",
          "message": "Bump version: 1.0.0 → 1.1.0",
          "timestamp": "2024-01-10T16:33:45+01:00",
          "tree_id": "0bbf99c4ca3955b37191735e4f9f79917adadfab",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/0c15e36ca08b2df011fda15da63eeb112fd6e29e"
        },
        "date": 1704901094358,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.104238065811779,
            "unit": "iter/sec",
            "range": "stddev: 0.004148457269953647",
            "extra": "mean: 195.9156268000129 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.451685372505162,
            "unit": "iter/sec",
            "range": "stddev: 0.0036361414610442543",
            "extra": "mean: 80.31041341665457 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 16.704273628938317,
            "unit": "iter/sec",
            "range": "stddev: 0.003719243054338092",
            "extra": "mean: 59.86491973333159 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 27.62822936481902,
            "unit": "iter/sec",
            "range": "stddev: 0.003932673987166917",
            "extra": "mean: 36.19486384000311 msec\nrounds: 25"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 34.881723395496955,
            "unit": "iter/sec",
            "range": "stddev: 0.002418855908285614",
            "extra": "mean: 28.66830829032647 msec\nrounds: 31"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 28.335614604601947,
            "unit": "iter/sec",
            "range": "stddev: 0.003512626831301473",
            "extra": "mean: 35.29127615384745 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 27.571996358080682,
            "unit": "iter/sec",
            "range": "stddev: 0.0028723734750446686",
            "extra": "mean: 36.26868316000355 msec\nrounds: 25"
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
          "id": "48ba85c8f90f77b7b064b8f3ec23258e99087390",
          "message": "Merge pull request #152 from stac-utils/feature/more-precise-statistics\n\nupdate titiler version and use new options for better statistics",
          "timestamp": "2024-01-17T11:48:03+01:00",
          "tree_id": "7854a220a76a07ddaaa7498f0257facc2490be03",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/48ba85c8f90f77b7b064b8f3ec23258e99087390"
        },
        "date": 1705488716296,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 4.9321008623541305,
            "unit": "iter/sec",
            "range": "stddev: 0.004853394836109235",
            "extra": "mean: 202.7533556000094 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.13865834940494,
            "unit": "iter/sec",
            "range": "stddev: 0.0025754004996904343",
            "extra": "mean: 82.38142727272836 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.526763557908586,
            "unit": "iter/sec",
            "range": "stddev: 0.00284600717688858",
            "extra": "mean: 64.40492226666568 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 24.494468498468112,
            "unit": "iter/sec",
            "range": "stddev: 0.003307791147951274",
            "extra": "mean: 40.825543941177585 msec\nrounds: 17"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 30.171978129776747,
            "unit": "iter/sec",
            "range": "stddev: 0.0032647706379280825",
            "extra": "mean: 33.143335703703805 msec\nrounds: 27"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 25.03736051463643,
            "unit": "iter/sec",
            "range": "stddev: 0.0038327167946783872",
            "extra": "mean: 39.94031237499721 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 25.53932659637953,
            "unit": "iter/sec",
            "range": "stddev: 0.0032707075984460057",
            "extra": "mean: 39.15530020833676 msec\nrounds: 24"
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
          "id": "7c798f0cdc039a11a1887e4558204bb2e55598e3",
          "message": "Bump version: 1.1.0 → 1.2.0",
          "timestamp": "2024-01-17T12:25:36+01:00",
          "tree_id": "575067ac34cd711383de4e64d383063d3764ceae",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/7c798f0cdc039a11a1887e4558204bb2e55598e3"
        },
        "date": 1705490989688,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.102793160694985,
            "unit": "iter/sec",
            "range": "stddev: 0.004157986335211631",
            "extra": "mean: 195.9711021999965 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 11.912170114297929,
            "unit": "iter/sec",
            "range": "stddev: 0.003978181195876896",
            "extra": "mean: 83.94776018180944 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.222597366462372,
            "unit": "iter/sec",
            "range": "stddev: 0.0033434819856290013",
            "extra": "mean: 65.69181171428389 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 25.599747660391174,
            "unit": "iter/sec",
            "range": "stddev: 0.003768633426614713",
            "extra": "mean: 39.06288504348169 msec\nrounds: 23"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 30.831349670909052,
            "unit": "iter/sec",
            "range": "stddev: 0.004311231959080733",
            "extra": "mean: 32.434519107139536 msec\nrounds: 28"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 25.858027283403576,
            "unit": "iter/sec",
            "range": "stddev: 0.003515999620646764",
            "extra": "mean: 38.672710375003305 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 26.21063905740468,
            "unit": "iter/sec",
            "range": "stddev: 0.0025026008741940316",
            "extra": "mean: 38.15244633333323 msec\nrounds: 21"
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
          "id": "8208cf7f6f2ff3651b44c91af6a26a8d10c61a0e",
          "message": "Merge pull request #153 from stac-utils/patch/fix-url-parsing-html-template\n\nbetter handle URL path when app if proxied",
          "timestamp": "2024-01-19T18:45:30+01:00",
          "tree_id": "f783b82fecbd3b7e1735f2c6354208fa7fac58ef",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/8208cf7f6f2ff3651b44c91af6a26a8d10c61a0e"
        },
        "date": 1705686567277,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.088402371450165,
            "unit": "iter/sec",
            "range": "stddev: 0.005637557271094072",
            "extra": "mean: 196.52533880000647 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.292915157712416,
            "unit": "iter/sec",
            "range": "stddev: 0.0035324322765405316",
            "extra": "mean: 81.34766954546276 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 16.29519704563624,
            "unit": "iter/sec",
            "range": "stddev: 0.003958892715529881",
            "extra": "mean: 61.36777586668055 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 27.183857230048186,
            "unit": "iter/sec",
            "range": "stddev: 0.0029119707340245953",
            "extra": "mean: 36.78653811110482 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 34.019379554369834,
            "unit": "iter/sec",
            "range": "stddev: 0.0031630857803134314",
            "extra": "mean: 29.395009935492745 msec\nrounds: 31"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 28.111914826073146,
            "unit": "iter/sec",
            "range": "stddev: 0.0029751986513337726",
            "extra": "mean: 35.572105499996866 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 28.233310631755995,
            "unit": "iter/sec",
            "range": "stddev: 0.0025538450527969867",
            "extra": "mean: 35.419154807698305 msec\nrounds: 26"
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
          "id": "18e573cdbd3ea90828dcf1e2cf87601e1eb1ccef",
          "message": "Bump version: 1.2.0 → 1.2.1",
          "timestamp": "2024-01-19T18:45:43+01:00",
          "tree_id": "c4fa2af128f054aabbd98b9a24b51a23961e936e",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/18e573cdbd3ea90828dcf1e2cf87601e1eb1ccef"
        },
        "date": 1705686570451,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.0925646759073695,
            "unit": "iter/sec",
            "range": "stddev: 0.0038671133035914802",
            "extra": "mean: 196.36471280000478 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.47896818100794,
            "unit": "iter/sec",
            "range": "stddev: 0.0042377145270750625",
            "extra": "mean: 80.13483050000285 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 16.41952567652884,
            "unit": "iter/sec",
            "range": "stddev: 0.0028064909142955976",
            "extra": "mean: 60.903099133336504 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 27.67752247221769,
            "unit": "iter/sec",
            "range": "stddev: 0.002883163733337853",
            "extra": "mean: 36.13040151999826 msec\nrounds: 25"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 35.08542168959403,
            "unit": "iter/sec",
            "range": "stddev: 0.0023121377686130986",
            "extra": "mean: 28.501866354839613 msec\nrounds: 31"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 28.39037596828859,
            "unit": "iter/sec",
            "range": "stddev: 0.0030141084942353646",
            "extra": "mean: 35.223203846154675 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 28.625590358897313,
            "unit": "iter/sec",
            "range": "stddev: 0.002518704007120946",
            "extra": "mean: 34.933777346156404 msec\nrounds: 26"
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
          "id": "61d5324da2879d0f6ab7b6a0fca03cd54dd2a471",
          "message": "Merge pull request #155 from smohiudd/fix/db-connect-kwargs\n\nChange db connection kwargs default",
          "timestamp": "2024-02-21T14:51:42-05:00",
          "tree_id": "495941c837309a9c3c9d45326e5e4f1d39c1b845",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/61d5324da2879d0f6ab7b6a0fca03cd54dd2a471"
        },
        "date": 1708545347191,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.119331017289979,
            "unit": "iter/sec",
            "range": "stddev: 0.0010996228140166802",
            "extra": "mean: 195.33802299999934 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.269228102559818,
            "unit": "iter/sec",
            "range": "stddev: 0.002728708448147003",
            "extra": "mean: 81.5047199091003 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 16.121430929085705,
            "unit": "iter/sec",
            "range": "stddev: 0.0028898489272486945",
            "extra": "mean: 62.029233285727514 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 27.74886941205431,
            "unit": "iter/sec",
            "range": "stddev: 0.00306338188580368",
            "extra": "mean: 36.03750427271797 msec\nrounds: 22"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 33.96709959187556,
            "unit": "iter/sec",
            "range": "stddev: 0.002582486879012987",
            "extra": "mean: 29.440252833338338 msec\nrounds: 30"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 27.904266206630588,
            "unit": "iter/sec",
            "range": "stddev: 0.003078875085988459",
            "extra": "mean: 35.83681407692351 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 27.941708647924816,
            "unit": "iter/sec",
            "range": "stddev: 0.003135115453876646",
            "extra": "mean: 35.78879203846642 msec\nrounds: 26"
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
          "id": "10b6a2aeb45b694b9027895369c93b46303da6fd",
          "message": "Bump version: 1.2.1 → 1.2.2",
          "timestamp": "2024-02-21T14:58:46-05:00",
          "tree_id": "fe01380a2148ec816f32d3fb0f8f05f9b0df3d04",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/10b6a2aeb45b694b9027895369c93b46303da6fd"
        },
        "date": 1708545939984,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.04929515268183,
            "unit": "iter/sec",
            "range": "stddev: 0.0025746970353627456",
            "extra": "mean: 198.04744419998315 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.341727152525785,
            "unit": "iter/sec",
            "range": "stddev: 0.004365214099198895",
            "extra": "mean: 81.02593645455417 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.490930610573725,
            "unit": "iter/sec",
            "range": "stddev: 0.0038377652164212754",
            "extra": "mean: 64.55390093332578 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 26.952944067839915,
            "unit": "iter/sec",
            "range": "stddev: 0.0036764008111911197",
            "extra": "mean: 37.10169833332581 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 33.497436597290225,
            "unit": "iter/sec",
            "range": "stddev: 0.004416116596813622",
            "extra": "mean: 29.85303060715085 msec\nrounds: 28"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 28.17735711603979,
            "unit": "iter/sec",
            "range": "stddev: 0.0035461165224051293",
            "extra": "mean: 35.48948880769077 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 28.26319832987422,
            "unit": "iter/sec",
            "range": "stddev: 0.0032392736981104618",
            "extra": "mean: 35.38169984615645 msec\nrounds: 26"
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
          "id": "144f2eae0f72a8fe7d08ea3aeb766a57b53029d0",
          "message": "Merge pull request #157 from stac-utils/patch/avoid-pydantic-settings-bug\n\nadd extra=ignore to pydantic settings",
          "timestamp": "2024-03-25T15:33:54+01:00",
          "tree_id": "1e6a1ef53ec529a3f177926cedcdff7ce0747d4a",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/144f2eae0f72a8fe7d08ea3aeb766a57b53029d0"
        },
        "date": 1711377496743,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.022558964218954,
            "unit": "iter/sec",
            "range": "stddev: 0.006997496505915478",
            "extra": "mean: 199.10169440001937 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.182858499466946,
            "unit": "iter/sec",
            "range": "stddev: 0.0035254663315692197",
            "extra": "mean: 82.08254245452777 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.869773921708907,
            "unit": "iter/sec",
            "range": "stddev: 0.004366993357865454",
            "extra": "mean: 63.01286993333027 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 28.145382238460762,
            "unit": "iter/sec",
            "range": "stddev: 0.0030722485384948013",
            "extra": "mean: 35.52980704001584 msec\nrounds: 25"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 34.719101080802425,
            "unit": "iter/sec",
            "range": "stddev: 0.0023158361111258485",
            "extra": "mean: 28.80258903226443 msec\nrounds: 31"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 28.274229384470924,
            "unit": "iter/sec",
            "range": "stddev: 0.0031340937170349407",
            "extra": "mean: 35.36789584614571 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 28.43797804685865,
            "unit": "iter/sec",
            "range": "stddev: 0.0026974187924028096",
            "extra": "mean: 35.16424403845629 msec\nrounds: 26"
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
          "id": "12794979d2f099dd58b6b8d83400a3c7d5a65051",
          "message": "Merge pull request #158 from stac-utils/dependabot/github_actions/all-ec64423157\n\nBump the all group with 7 updates",
          "timestamp": "2024-03-25T15:37:59+01:00",
          "tree_id": "1b9f0bb0c47165feb5a7d2288c1b6515a20a4f06",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/12794979d2f099dd58b6b8d83400a3c7d5a65051"
        },
        "date": 1711377760106,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.0729137348288,
            "unit": "iter/sec",
            "range": "stddev: 0.0028991515085876017",
            "extra": "mean: 197.1253706000084 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.34233237022318,
            "unit": "iter/sec",
            "range": "stddev: 0.004030763808497537",
            "extra": "mean: 81.02196327272603 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.891329377314417,
            "unit": "iter/sec",
            "range": "stddev: 0.004140305417437405",
            "extra": "mean: 62.927397466667884 msec\nrounds: 15"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 27.251667493771986,
            "unit": "iter/sec",
            "range": "stddev: 0.003017314037042696",
            "extra": "mean: 36.695002249992115 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 33.85828535661307,
            "unit": "iter/sec",
            "range": "stddev: 0.0026603681617030257",
            "extra": "mean: 29.53486833333348 msec\nrounds: 30"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 27.573737949854262,
            "unit": "iter/sec",
            "range": "stddev: 0.002858599266802289",
            "extra": "mean: 36.266392384616296 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 27.895450821920914,
            "unit": "iter/sec",
            "range": "stddev: 0.0025515025596013242",
            "extra": "mean: 35.848139052629186 msec\nrounds: 19"
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
          "id": "2d57d2e4c222f9a0ff274892e417a7235ab8e468",
          "message": "Bump version: 1.2.2 → 1.2.3",
          "timestamp": "2024-03-25T16:00:28+01:00",
          "tree_id": "88f0d93293654270872644dc48bd78cd88df86a2",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/2d57d2e4c222f9a0ff274892e417a7235ab8e468"
        },
        "date": 1711379092868,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 4.974077164115252,
            "unit": "iter/sec",
            "range": "stddev: 0.0044826507406381085",
            "extra": "mean: 201.04231739996976 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 11.866346470207704,
            "unit": "iter/sec",
            "range": "stddev: 0.00317668678887008",
            "extra": "mean: 84.27193681818194 msec\nrounds: 11"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.174468719656778,
            "unit": "iter/sec",
            "range": "stddev: 0.00318269928961086",
            "extra": "mean: 65.90016550000298 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 26.341154908302666,
            "unit": "iter/sec",
            "range": "stddev: 0.002907428735636284",
            "extra": "mean: 37.96340758334793 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 32.548510209536296,
            "unit": "iter/sec",
            "range": "stddev: 0.0028920657511911393",
            "extra": "mean: 30.72337239284804 msec\nrounds: 28"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 26.12685731623673,
            "unit": "iter/sec",
            "range": "stddev: 0.0028539808936295704",
            "extra": "mean: 38.274790875002886 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 26.328050781812138,
            "unit": "iter/sec",
            "range": "stddev: 0.003345351826497996",
            "extra": "mean: 37.98230291666016 msec\nrounds: 24"
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
          "id": "ffe0b68c56eac9c2d5040d61a9022d4705807881",
          "message": "Merge pull request #160 from stac-utils/feature/deprecated-default-tilematrixset\n\nDeprecate default tilematrixset",
          "timestamp": "2024-03-25T20:16:55+01:00",
          "tree_id": "ff6343fa089ecd84ac255160699eec3244cec047",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/ffe0b68c56eac9c2d5040d61a9022d4705807881"
        },
        "date": 1711394483547,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 5.10452425071258,
            "unit": "iter/sec",
            "range": "stddev: 0.001433847366731103",
            "extra": "mean: 195.90464280004198 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 12.33383856538999,
            "unit": "iter/sec",
            "range": "stddev: 0.0036339775719132455",
            "extra": "mean: 81.07775975000209 msec\nrounds: 12"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 15.756844676814199,
            "unit": "iter/sec",
            "range": "stddev: 0.0035799453737043",
            "extra": "mean: 63.46448292858245 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 26.883790403683744,
            "unit": "iter/sec",
            "range": "stddev: 0.0036397371971827945",
            "extra": "mean: 37.19713570832539 msec\nrounds: 24"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 34.53819699225926,
            "unit": "iter/sec",
            "range": "stddev: 0.0026400516406208715",
            "extra": "mean: 28.953451166664003 msec\nrounds: 30"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 28.02523343297698,
            "unit": "iter/sec",
            "range": "stddev: 0.002950446847462082",
            "extra": "mean: 35.68212919230536 msec\nrounds: 26"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 28.252318884554242,
            "unit": "iter/sec",
            "range": "stddev: 0.0025331957190563846",
            "extra": "mean: 35.39532468418752 msec\nrounds: 19"
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
          "id": "a1ace2fc74b143205d1dcd2155fb81b20683b193",
          "message": "Merge pull request #163 from stac-utils/feature/add-render-support\n\nadd render extension support",
          "timestamp": "2024-05-16T18:45:15+02:00",
          "tree_id": "bdde4b95ccf8fe08d47099e78ec8495c7ef41683",
          "url": "https://github.com/stac-utils/titiler-pgstac/commit/a1ace2fc74b143205d1dcd2155fb81b20683b193"
        },
        "date": 1715878157524,
        "tool": "pytest",
        "benches": [
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[0/0/0]",
            "value": 4.6434969603530485,
            "unit": "iter/sec",
            "range": "stddev: 0.001516196462355559",
            "extra": "mean: 215.35493799999585 msec\nrounds: 5"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[1/1/1]",
            "value": 11.149548125260704,
            "unit": "iter/sec",
            "range": "stddev: 0.003202849388461052",
            "extra": "mean: 89.68973349999487 msec\nrounds: 10"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[2/2/1]",
            "value": 14.531004823675413,
            "unit": "iter/sec",
            "range": "stddev: 0.002665187438381134",
            "extra": "mean: 68.81836542856945 msec\nrounds: 14"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[3/5/0]",
            "value": 25.15182662597152,
            "unit": "iter/sec",
            "range": "stddev: 0.0028485413144167674",
            "extra": "mean: 39.758543777787104 msec\nrounds: 18"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[4/5/9]",
            "value": 31.173785626094276,
            "unit": "iter/sec",
            "range": "stddev: 0.003272496029873164",
            "extra": "mean: 32.0782343214339 msec\nrounds: 28"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[5/16/5]",
            "value": 25.374557147784707,
            "unit": "iter/sec",
            "range": "stddev: 0.003807133877650444",
            "extra": "mean: 39.40955478260647 msec\nrounds: 23"
          },
          {
            "name": ".github/workflows/tests/benchmarks.py::test_benchmark_tile[6/43/31]",
            "value": 25.879405908600916,
            "unit": "iter/sec",
            "range": "stddev: 0.0030696846627961",
            "extra": "mean: 38.64076337500677 msec\nrounds: 24"
          }
        ]
      }
    ]
  }
}