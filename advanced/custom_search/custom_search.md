Even though `TiTiler.PgSTAC` includes default FastAPI application,
it also can be used like a library if you want to extend or
override default behaviour.

Let's look at one such example. Imagine that we use JSON Web Token (JWT)
based approach for authorization and every token contains information
about area a user has access to:

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022,
  "scope": "zone_A"
}
```

We want our application to take this information into account while
registering a search query. It can be done in the following way:

```python
from typing import Tuple
import json
import jwt
from fastapi import FastAPI
from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from titiler.pgstac.factory import MosaicTilerFactory
from titiler.pgstac.model import RegisterMosaic, Metadata, PgSTACSearch


app = FastAPI()

AREAS = {
    "zone_A": {"type": "Point", "coordinates": [-41.93, -12.76]},
    "zone_B": {"type": "Point", "coordinates": [2.15, 41.39]},
}


def search_factory(request: Request, body: RegisterMosaic) -> Tuple[PgSTACSearch, Metadata]:
    authorization = request.headers.get("Authorization")
    scheme, token = get_authorization_scheme_param(authorization)
    payload = jwt.decode(token, algorithms=["HS256"], key="your-256-bit-secret")

    search = body.dict(exclude_none=True, exclude={"metadata"}, by_alias=True)
    search["filter"] = {
        "op": "and",
        "args": [
            {
                "op": "s_intersects",
                "args": [{"property": "geometry"}, AREAS[payload["scope"]]],
            },
            search["filter"],
        ],
    }

    return model.PgSTACSearch(**search), body.metadata


mosaic = MosaicTilerFactory(search_dependency=search_factory)
app.include_router(mosaic.router)
```

Checking:

```bash
$ curl -s -X 'POST' \
  'http://localhost:8081/register' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJzY29wZSI6InpvbmVfQSJ9.BelzluX7v7kYObix2KSyy1T5gEOQYQn_pyNO5Ri0gWo' \
  -H 'Content-Type: application/json' \
  -d '{"filter":{"op":"and","args":[{"op":"=","args":[{"property":"collection"},"l1"]}]}}' | jq '.searchid'
"bbc3c8f4c392436f74de6cd0308469f6"

$ curl -X 'GET' \
  'http://localhost:8081/bbc3c8f4c392436f74de6cd0308469f6/info' \
  -H 'accept: application/json'
{"hash":"bbc3c8f4c392436f74de6cd0308469f6","search":{"filter":{"op":"and","args":[{"op":"s_intersects","args":[{"property":"geometry"},{"type":"Point","coordinates":[-41.93,-12.76]}]},{"op":"and","args":[{"op":"=","args":[{"property":"collection"},"l1"]}]}]}},"_where":"(  ( st_intersects(geometry, '0101000020E6100000D7A3703D0AF744C085EB51B81E8529C0'::geometry) and  ( (collection_id = 'l1') )  )  )  ","orderby":"datetime DESC, id DESC","lastused":"2022-02-23T13:00:04.090757+00:00","usecount":3,"metadata":{"type":"mosaic"}}
```
