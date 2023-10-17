window.BENCHMARK_DATA = {
  "lastUpdate": 1697547142378,
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
      }
    ]
  }
}