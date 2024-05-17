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
    settings: Optional[titiler.pgstac.settings.PostgresSettings] = None,
    pool_kwargs: Optional[Dict[str, Any]] = None
) -> None
```

Connect to Database.