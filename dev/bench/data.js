window.BENCHMARK_DATA = {
  "lastUpdate": 1689845945966,
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
      }
    ]
  }
}