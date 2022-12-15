"""Setup titiler.pgstac."""

from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    long_description = f.read()

inst_reqs = [
    "titiler.core>=0.10.1,<0.11",
    "titiler.mosaic>=0.10.1,<0.11",
    "geojson-pydantic>=0.4,<0.5",
    "stac-pydantic==2.0.*",
]
extra_reqs = {
    "dev": ["pre-commit"],
    "test": [
        "pytest",
        "pytest-cov",
        "pytest-asyncio",
        "httpx",
        "pypgstac>=0.6,<0.7",
        "psycopg2",
        "pytest-pgsql",
    ],
    # https://www.psycopg.org/psycopg3/docs/api/pq.html#pq-module-implementations
    "psycopg": ["psycopg[pool]"],  # pure python implementation
    "psycopg-c": ["psycopg[c,pool]"],  # C implementation of the libpq wrapper
    "psycopg-binary": ["psycopg[binary,pool]"],  # pre-compiled C implementation
}


setup(
    name="titiler.pgstac",
    description="Connect PgSTAC and TiTiler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="COG STAC MosaicJSON FastAPI PgSTAC",
    author="Vincent Sarago",
    author_email="vincent@developmentseed.org",
    url="https://github.com/stac-utils/titiler-pgstac",
    license="MIT",
    packages=find_namespace_packages(exclude=["tests*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
)
