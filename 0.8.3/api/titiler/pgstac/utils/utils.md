# Module titiler.pgstac.utils

titiler.pgstac utilities.

## Functions

    
### retry

```python3
def retry(
    tries: int,
    exceptions: Union[Type[Exception], Sequence[Type[Exception]]] = <class 'Exception'>,
    delay: float = 0.0
)
```

Retry Decorator