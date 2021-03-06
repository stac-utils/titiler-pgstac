
For some users, it might be useful to search or list `mosaic` registered via `titiler-pgstac`.

We can extend the default factory to add a `/list` endpoint:

```python
import re
from dataclasses import dataclass
from typing import Generator, List, Optional

from psycopg import sql
from psycopg.rows import class_row
from pydantic import BaseModel, validator

from fastapi import Query
from starlette.datastructures import QueryParams
from starlette.requests import Request
from titiler.pgstac import factory as TitilerPgSTACFactory
from titiler.pgstac import model


class Context(BaseModel):
    """Context Model."""

    returned: int
    limit: Optional[int]
    matched: Optional[int]

    @validator("limit")
    def validate_limit(cls, v, values):
        """validate limit."""
        if values["returned"] > v:
            raise ValueError(
                "Number of returned items must be less than or equal to the limit"
            )
        return v


class Infos(BaseModel):
    """Response model for /list endpoint."""

    searches: List[model.Info]
    links: Optional[List[model.Link]]
    context: Context


@dataclass
class MosaicTilerFactory(TitilerPgSTACFactory.MosaicTilerFactory):
    """Custom endpoints factory."""

    def register_routes(self) -> None:
        """This Method register routes to the router."""
        super().register_routes()

        @self.router.get(
            "/list",
            responses={200: {"description": "List Mosaics in PgSTAC."}},
            response_model=Infos,
            response_model_exclude_none=True,
        )
        def list_mosaic(
            request: Request,
            limit: int = Query(
                10,
                ge=1,
                le=10000,
                description="Page size limit",
            ),
            offset: int = Query(
                0,
                ge=0,
                description="Page offset",
            ),
            sortby: Optional[str] = Query(
                None,
                description="Sort the response items by a property (ascending (default) or descending).",
            ),
        ):
            """List a Search query."""
            # Default filter to only return `metadata->type == 'mosaic'`
            mosaic_filter = sql.SQL("metadata->>'type' = 'mosaic'")

            # additional metadata property filter passed in query-parameters
            # <propname>=val - filter for a metadata property. Multiple property filters are ANDed together.
            qs_key_to_remove = ["limit", "offset", "sortby"]
            additional_filter = [
                sql.SQL("metadata->>{key} = {value}").format(
                    key=sql.Literal(key), value=sql.Literal(value)
                )
                for (key, value) in request.query_params.items()
                if key.lower() not in qs_key_to_remove
            ]
            filters = [
                sql.SQL("WHERE"),
                sql.SQL("AND ").join([mosaic_filter, *additional_filter]),
            ]

            def parse_sort_by(sortby: str) -> Generator[sql.Composable, None, None]:
                """Parse SortBy expression."""
                for s in sortby.split(","):
                    parts = re.match(
                        "^(?P<dir>[+-]?)(?P<prop>.*)$", s
                    ).groupdict()  # type:ignore
                    prop = parts["prop"]
                    if parts["prop"] in ["lastused", "usecount"]:
                        prop = sql.Identifier(parts["prop"])
                    else:
                        prop = sql.SQL("metadata->>{}").format(
                            sql.Literal(parts["prop"])
                        )

                    if parts["dir"] == "-":
                        order = sql.SQL("{} DESC").format(prop)
                    else:
                        order = sql.SQL("{} ASC").format(prop)

                    yield order

            # sortby=[+|-]PROP - sort the response items by a property (ascending (default) or descending).
            order_by = []
            if sortby:
                sort_expr = list(parse_sort_by(sortby))

                print(sort_expr)
                if sort_expr:
                    order_by = [
                        sql.SQL("ORDER BY"),
                        sql.SQL(", ").join(sort_expr),
                    ]

            with request.app.state.dbpool.connection() as conn:
                with conn.cursor() as cursor:
                    # Get Total Number of searches rows
                    query = [
                        sql.SQL("SELECT count(*) FROM searches"),
                        *filters,
                    ]
                    cursor.execute(sql.SQL(" ").join(query))
                    nb_items = int(cursor.fetchone()[0])

                    # Get rows
                    cursor.row_factory = class_row(model.Search)
                    query = [
                        sql.SQL("SELECT * FROM searches"),
                        *filters,
                        *order_by,
                        sql.SQL("LIMIT %(limit)s OFFSET %(offset)s"),
                    ]
                    cursor.execute(
                        sql.SQL(" ").join(query), {"limit": limit, "offset": offset}
                    )

                    searches_info = cursor.fetchall()

            qs = QueryParams({**request.query_params, "limit": limit, "offset": offset})
            links = [
                model.Link(
                    rel="self",
                    href=self.url_for(request, "list_mosaic") + f"?{qs}",
                ),
            ]

            if len(searches_info) < nb_items:
                next_token = offset + len(searches_info)
                qs = QueryParams(
                    {**request.query_params, "limit": limit, "offset": next_token}
                )
                links.append(
                    model.Link(
                        rel="next",
                        href=self.url_for(request, "list_mosaic") + f"?{qs}",
                    ),
                )

            if offset > 0:
                prev_token = offset - limit if (offset - limit) > 0 else 0
                qs = QueryParams(
                    {**request.query_params, "limit": limit, "offset": prev_token}
                )
                links.append(
                    model.Link(
                        rel="prev",
                        href=self.url_for(request, "list_mosaic") + f"?{qs}",
                    ),
                )

            return Infos(
                searches=[
                    model.Info(
                        search=search,
                        links=[
                            model.Link(
                                rel="metadata",
                                href=self.url_for(
                                    request, "info_search", searchid=search.id
                                ),
                            ),
                            model.Link(
                                rel="tilejson",
                                href=self.url_for(
                                    request, "tilejson", searchid=search.id
                                ),
                            ),
                        ],
                    )
                    for search in searches_info
                ],
                links=links,
                context=Context(
                    returned=len(searches_info),
                    matched=nb_items,
                    limit=limit,
                ),
            )
```

Code from [eoAPI.raster](https://github.com/developmentseed/eoAPI/blob/2c8b8b19151e2e1e552021fe2010d9b5a7133e39/src/eoapi/raster/eoapi/raster/factory.py)

!!! Important
    To avoid bad performances, it's recommanded to add an Index in the PgSTAC database:

    ```sql
    CREATE INDEX IF NOT EXISTS searches_mosaic ON searches ((true)) WHERE metadata->>'type'='mosaic';
    ```
