# Module titiler.pgstac.db

Database connection handling.

## Functions

    
### close_db_connection

```python3
def close_db_connection(
    app: fastapi.applications.FastAPI
) -> None
```

Close Pool.

    
### connect_to_db

```python3
def connect_to_db(
    app: fastapi.applications.FastAPI,
    settings: Union[titiler.pgstac.settings.PostgresSettings, NoneType] = None
) -> None
```

Connect to Database.