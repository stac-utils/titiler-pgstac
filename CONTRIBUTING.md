# Development - Contributing

Issues and pull requests are more than welcome: https://github.com/stac-utils/titiler-pgstac/issues

We recommand using [`uv`](https://docs.astral.sh/uv) as project manager for development.

See https://docs.astral.sh/uv/getting-started/installation/ for installation 

**dev install**

```bash
git clone https://github.com/stac-utils/titiler-pgstac.git
cd titiler-pgstac

uv sync --extra psycopg
```

You can then run the tests with the following command:

```sh
uv run pytest --cov titiler.pgstac --cov-report term-missing
```

This repo is set to use `pre-commit` to run *isort*, *flake8*, *pydocstring*, *black* ("uncompromising Python code formatter") and mypy when committing new code.

```bash
uv run pre-commit run --all-files
```
