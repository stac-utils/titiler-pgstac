"""Setup titiler.pgstac."""

from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    long_description = f.read()

inst_reqs = [
    "titiler.core>=0.3.8,<0.4",
    "titiler.mosaic",
    "geojson-pydantic>=0.3.1,<0.4",
    "rio-tiler>=2.1.2,<2.2",
    "stac-pydantic==2.0.*",
]
extra_reqs = {
    "test": [
        "pytest",
        "pytest-cov",
        "pytest-asyncio",
        "requests",
        "pypgstac",
        "asyncpg",
    ],
    "psycopg2": ["psycopg2"],
    "psycopg2-binary": ["psycopg2-binary"],
}


setup(
    name="titiler.pgstac",
    description=u"Connect PgSTAC and TiTiler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="COG STAC MosaicJSON FastAPI PgSTAC",
    author=u"Vincent Sarago",
    author_email="vincent@developmentseed.org",
    url="https://github.com/stac-utils/titiler-pgstac",
    license="MIT",
    packages=find_namespace_packages(exclude=["tests*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
)
