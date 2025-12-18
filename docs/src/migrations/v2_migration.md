# Migration Guide: titiler-pgstac 1.9 to 2.0

This guide covers the breaking changes and new features when upgrading from titiler-pgstac 1.9 to 2.0.

## Breaking Changes

### Python Version Requirement

**Impact:** High - Affects deployment and development environments

titiler-pgstac 2.0 requires Python 3.11 or higher. Python 3.10 and earlier versions are no longer supported.

```bash
# Ensure you're using Python 3.11+
python --version  # Should show 3.11 or higher
```

**Action Required:**

- Update your Python environment to 3.11, 3.12, 3.13, or 3.14
- Update CI/CD pipelines and Docker base images
- Test your application with the new Python version

### TiTiler Dependency Update

**Impact:** High - Affects all functionality

titiler-pgstac 2.0 requires titiler `>=1.0,<1.1`, which includes several breaking changes. Please refer to the [TiTiler v1 Migration Guide](https://developmentseed.org/titiler/migrations/v1_migration/) for detailed information.

Key titiler 1.0 changes that affect titiler-pgstac:

- WMTS endpoints now provided via extension
- Point endpoint response model changes
- Updated mosaic backend requirements

**Action Required:**
- Review the TiTiler v1 migration guide
- Test all tile and metadata endpoints
- Update client code parsing responses

### Point Endpoint Response Model

**Impact:** High - Affects `/point` endpoint consumers

The response model for the `/point` endpoint has been restructured to provide clearer asset information.

```python
# Before (1.9)
class Point(BaseModel):
    coordinates: List[float]
    values: List[Tuple[str, List[Optional[float]], List[str]]]

# Now (2.0)
class AssetPoint(BaseModel):
    name: str
    values: list[float | None]
    band_names: list[str]
    band_descriptions: list[str] | None = None

class Point(BaseModel):
    coordinates: list[float]
    assets: list[AssetPoint]
```

**Migration Example:**

```python
# Before (1.9)
response = {
    "coordinates": [-122.5, 37.5],
    "values": [
        ("red", [100.0, 200.0], ["B1", "B2"]),
        ("green", [150.0, 250.0], ["B1", "B2"])
    ]
}

# Accessing values:
for asset_name, values, bands in response["values"]:
    print(f"{asset_name}: {values}")

# Now (2.0)
response = {
    "coordinates": [-122.5, 37.5],
    "assets": [
        {
            "name": "red",
            "values": [100.0, 200.0],
            "band_names": ["B1", "B2"],
            "band_descriptions": None
        },
        {
            "name": "green",
            "values": [150.0, 250.0],
            "band_names": ["B1", "B2"],
            "band_descriptions": None
        }
    ]
}

# Accessing values:
for asset in response["assets"]:
    print(f"{asset['name']}: {asset['values']}")
```

**Action Required:** Update all client code that parses `/point` endpoint responses to use the new structure.

### CQL Filter Changes

**Impact:** Medium - Affects search filtering functionality

Support for `cql-text` (CQL1) has been removed. Only CQL2 is now supported.

```python
# Before (1.9) - Both supported
search = {
    "collections": ["my-collection"],
    "filter-lang": "cql-text",  # No longer supported
    "filter": "landcover='urban'"
}

# Or
search = {
    "collections": ["my-collection"],
    "filter-lang": "cql2-json",  # Still supported
    "filter": {...}
}

# Now (2.0) - Only CQL2 supported
search = {
    "collections": ["my-collection"],
    "filter-lang": "cql2-json",
    "filter": {
        "op": "=",
        "args": [
            {"property": "landcover"},
            "urban"
        ]
    }
}
```

**Action Required:**
- Convert any `cql-text` filters to `cql2-json` or `cql2-text` format
- Update API calls that use the `filter-lang` parameter
- Test all search queries with filters

### Collection Endpoint Filter Support

**Impact:** Medium - New functionality for collection endpoints

The `/collections/{collection_id}` endpoints now support `filter` and `filter-lang` parameters for more advanced querying.

```python
# New in 2.0 - Filter support for collections
response = httpx.get(
    "/collections/my-collection/tiles/0/0/0",
    params={
        "filter-lang": "cql2-json",
        "filter": json.dumps({
            "op": "=",
            "args": [{"property": "cloud_cover"}, 10]
        })
    }
)
```

**Action Required:** Consider using these new filtering capabilities to improve collection queries.

### Searches List Endpoint Deprecation

**Impact:** Low - Endpoint path change

The `/searches/list` endpoint is deprecated and replaced with `/searches/`.

```python
# Before (1.9)
response = httpx.get("/searches/list")

# Now (2.0)
response = httpx.get("/searches/")
```

**Action Required:** Update any code using `/searches/list` to use `/searches/` instead.

### WMTS Endpoint Changes

**Impact:** High - Affects WMTS consumers

WMTS endpoints have been updated to match the latest titiler implementation:

- Removed `{tileMatrixSetId}` prefix from paths
- All available TileMatrixSets now included in layers
- WMTS functionality moved to an extension

```python
# Before (1.9)
# WMTS at: /searches/{search_id}/{tileMatrixSetId}/WMTSCapabilities.xml

# Now (2.0)
from titiler.pgstac.extensions import wmtsExtension

factory = MosaicTilerFactory(
    extensions=[wmtsExtension()]
)
# WMTS at: /searches/{search_id}/WMTSCapabilities.xml
```

**Action Required:**
- Add `wmtsExtension` to your factory if using WMTS
- Update WMTS client URLs to remove TileMatrixSet prefix
- Update code expecting single TMS to handle multiple TileMatrixSets

### Mosaic Backend Switch

**Impact:** Medium - Internal implementation change

titiler-pgstac now uses the rio-tiler mosaic backend instead of cogeo-mosaic.

This is primarily an internal change, but may affect:
- Custom backend implementations
- Performance characteristics
- Error handling behavior

**Action Required:**
- Test mosaic operations thoroughly
- Review any custom backend implementations for compatibility
- Monitor performance and adjust caching as needed

### Docker Image Changes

**Impact:** High - Affects container deployments

The container image now uses a non-root user for improved security.

```dockerfile
# Before (1.9)
# Container runs as root

# Now (2.0)
# Container runs as user:user (UID 1000, GID 1000)
RUN groupadd -g 1000 user && \
    useradd -u 1000 -g user -s /bin/bash -m user
USER user
```

Default python version has also been upgraded to 3.14

**Action Required:**
- Review file permissions if mounting volumes
- Update Kubernetes security contexts if needed
- Adjust any scripts assuming root user
- Test container deployments thoroughly

## Development Changes

### Build System Update

**Impact:** Medium - Affects package building

titiler-pgstac now uses [Hatch](https://hatch.pypa.io/) as the build backend instead of pdm-backend.

```toml
# Before (1.9)
[build-system]
requires = ["pdm-backend"]
build-backend = "pdm.backend"

# Now (2.0)
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

**Action Required:**
- Update build scripts to use `hatch` if building from source
- No action needed if installing via pip

### Development Environment

**Impact:** Low - Affects contributors

The project now uses [uv](https://github.com/astral-sh/uv) for dependency management during development.

```bash
# Before (1.9)
pip install -e ".[dev]"

# Now (2.0) - Recommended for development
uv sync

# Or traditional pip still works
pip install -e ".[dev]"
```

**Action Required:** Consider using `uv` for faster dependency resolution, but traditional pip still works.

## New Features

### Enhanced Type Hints

Type hints have been updated and improved throughout the codebase for better IDE support and type checking.

```python
# Modern Python 3.11+ type syntax now used
def get_collection_id(
    pool: ConnectionPool,
    collection_id: str,
    ids: str | None = None,  # Instead of Optional[str]
    bbox: str | None = None,
) -> str:
    ...
```

### CQL2 Library Integration

The project now uses the [cql2](https://pypi.org/project/cql2/) library for better CQL2 support and text-to-JSON conversion.

```python
from cql2 import Expr

# Automatic conversion from cql2-text to cql2-json
filter_text = "landcover='urban' AND cloud_cover < 10"
filter_json = Expr(filter_text).to_json()
```

## Migration Checklist

Use this checklist to ensure a smooth migration:

- [ ] Update Python to 3.11 or higher
- [ ] Update titiler-pgstac installation: `pip install "titiler-pgstac>=2.0,<2.1"`
- [ ] Review and apply TiTiler v1 migration changes
- [ ] Update `/point` endpoint response parsing
- [ ] Convert all `cql-text` filters to CQL2 format
- [ ] Update `/searches/list` references to `/searches/`
- [ ] Add `wmtsExtension` if using WMTS endpoints
- [ ] Update WMTS client URLs (remove TileMatrixSet prefix)
- [ ] Test Docker containers with non-root user
- [ ] Update volume mount permissions if needed
- [ ] Test all mosaic operations
- [ ] Update CI/CD for Python 3.11+
- [ ] Review build processes if building from source
- [ ] Test all endpoints with real data

## Testing Your Migration

After completing the migration, test these key areas:

1. **Basic Tile Access**
   ```bash
   # Test tile endpoints
   curl "/searches/{search_id}/tiles/WebMercatorQuad/0/0/0"
   ```

2. **Point Queries**
   ```bash
   # Test point endpoint and verify response structure
   curl "/searches/{search_id}/point/-122.5,37.5?assets=visual"
   ```

3. **Search with Filters**
   ```bash
   # Test CQL2 filter support
   curl -X POST "/searches/register" \
     -H "Content-Type: application/json" \
     -d '{
       "collections": ["my-collection"],
       "filter-lang": "cql2-json",
       "filter": {"op": "=", "args": [{"property": "cloudCover"}, 0]}
     }'
   ```

4. **WMTS**
   ```bash
   # Test WMTS capabilities
   curl "/searches/{search_id}/WMTSCapabilities.xml?assets=visual"
   ```

5. **Docker Container**
   ```bash
   # Test container starts and serves requests
   docker run -p 8000:8000 \
     -e DATABASE_URL=postgresql://... \
     ghcr.io/stac-utils/titiler-pgstac:2.0.0 \
     uvicorn titiler.pgstac.main:app --host 0.0.0.0 --port 8000
   ```

## Getting Help

If you encounter issues during migration:

1. Check the [GitHub Issues](https://github.com/stac-utils/titiler-pgstac/issues)
2. Review the [full CHANGELOG](https://stac-utils.github.io/titiler-pgstac/release-notes/)
3. Review the [TiTiler v1 Migration Guide](https://developmentseed.org/titiler/migrations/v1_migration/)
4. Join discussions in the [titiler-pgstac repository](https://github.com/stac-utils/titiler-pgstac)

## Summary

Version 2.0 represents a significant update to titiler-pgstac with modernized dependencies, improved type safety, enhanced security, and better CQL2 support. While there are several breaking changes, they primarily affect:

- Response models (Point endpoint)
- Filter syntax (CQL2 only)
- Python version requirements
- Container security (non-root user)

Most applications can migrate by updating Python, converting CQL filters, and updating response parsing logic. The improvements in type safety, security, and standards compliance make this a worthwhile upgrade.

---

*This migration guide was generated with assistance from Claude AI and should be reviewed for accuracy and completeness.*