

| Method | URL                                                                       | Output                            | Description
| ------ | --------------------------------------------------------------------------|-----------------------------------|--------------
| `GET`  | `/tileMatrixSets`                                                         | JSON ([TMS list][tms_list_model]) | return the list of supported TileMatrixSet
| `GET`  | `/tileMatrixSets/{TileMatrixSetId}`                                       | JSON ([TileMatrixSet][tms_model]) | return the TileMatrixSet JSON document

### List TMS

`:endpoint:/tileMatrixSets` - Get the list of supported TileMatrixSet

```bash
curl https://myendpoint/tileMatrixSets | jq
>> {
  "tileMatrixSets": [
    {
      "id": "LINZAntarticaMapTilegrid",
      "title": "LINZ Antarctic Map Tile Grid (Ross Sea Region)",
      "links": [
        {
          "href": "https://myendpoint/tileMatrixSets/LINZAntarticaMapTilegrid",
          "rel": "item",
          "type": "application/json"
        }
      ]
    },
    ...
  ]
}
```

### Get TMS info

`:endpoint:/tileMatrixSets/{TileMatrixSetId}` - Get the TileMatrixSet JSON document

- PathParams:
    - **TileMatrixSetId**: TileMatrixSet name

```bash
curl http://127.0.0.1:8000/tileMatrixSets/WebMercatorQuad | jq
>> {
  "type": "TileMatrixSetType",
  "title": "Google Maps Compatible for the World",
  "identifier": "WebMercatorQuad",
  "supportedCRS": "http://www.opengis.net/def/crs/EPSG/0/3857",
  "wellKnownScaleSet": "http://www.opengis.net/def/wkss/OGC/1.0/GoogleMapsCompatible",
  "boundingBox": {
    "type": "BoundingBoxType",
    "crs": "http://www.opengis.net/def/crs/EPSG/0/3857",
    "lowerCorner": [
      -20037508.3427892,
      -20037508.3427892
    ],
    "upperCorner": [
      20037508.3427892,
      20037508.3427892
    ]
  },
  "tileMatrix": [
    {
      "type": "TileMatrixType",
      "identifier": "0",
      "scaleDenominator": 559082264.028717,
      "topLeftCorner": [
        -20037508.3427892,
        20037508.3427892
      ],
      "tileWidth": 256,
      "tileHeight": 256,
      "matrixWidth": 1,
      "matrixHeight": 1
    },
    ...
```

[tms_list_model]: https://github.com/developmentseed/titiler/blob/f88e6e2fcbe5748cec91cfec160c08d5244183c6/src/titiler/core/titiler/core/models/OGC.py#L40-L48
[tms_model]: https://github.com/developmentseed/morecantile/blob/aafdbfdc943d88203664b231bb027a1fe8227b14/morecantile/models.py#L119-L130
