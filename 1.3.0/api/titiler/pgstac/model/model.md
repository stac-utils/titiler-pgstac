# Module titiler.pgstac.model

Titiler.pgstac models.

Note: This is mostly a copy of https://github.com/stac-utils/stac-fastapi/blob/master/stac_fastapi/pgstac/stac_fastapi/pgstac/types/search.py

## Variables

```python3
FilterLang
```

```python3
Operator
```

## Classes

### Context

```python3
class Context(
    /,
    **data: 'Any'
)
```

Context Model.

#### Ancestors (in MRO)

* pydantic.main.BaseModel

#### Class variables

```python3
model_computed_fields
```

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of<br>`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class<br>`Model` with 2 type variables and a concrete model `Model[str, int]`,<br>the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.<br>If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### model_validate_strings

```python3
def model_validate_strings(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate the given object contains string data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object contains string data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

    
#### validate_limit

```python3
def validate_limit(
    v,
    info: pydantic_core.core_schema.ValidationInfo
)
```

validate limit.

#### Instance variables

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep-copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated<br>before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the output will only contain JSON serializable types.<br>If mode is 'python', the output may contain non-JSON-serializable Python objects. | None |
| include | None | A set of fields to include in the output. | None |
| exclude | None | A set of fields to exclude from the output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. | None |
| exclude | None | Field(s) to exclude from the JSON output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### Info

```python3
class Info(
    /,
    **data: 'Any'
)
```

Response model for /info endpoint.

#### Ancestors (in MRO)

* pydantic.main.BaseModel

#### Class variables

```python3
model_computed_fields
```

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of<br>`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class<br>`Model` with 2 type variables and a concrete model `Model[str, int]`,<br>the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.<br>If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### model_validate_strings

```python3
def model_validate_strings(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate the given object contains string data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object contains string data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

#### Instance variables

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep-copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated<br>before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the output will only contain JSON serializable types.<br>If mode is 'python', the output may contain non-JSON-serializable Python objects. | None |
| include | None | A set of fields to include in the output. | None |
| exclude | None | A set of fields to exclude from the output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. | None |
| exclude | None | Field(s) to exclude from the JSON output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### Infos

```python3
class Infos(
    /,
    **data: 'Any'
)
```

Response model for /list endpoint.

#### Ancestors (in MRO)

* pydantic.main.BaseModel

#### Class variables

```python3
model_computed_fields
```

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of<br>`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class<br>`Model` with 2 type variables and a concrete model `Model[str, int]`,<br>the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.<br>If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### model_validate_strings

```python3
def model_validate_strings(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate the given object contains string data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object contains string data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

#### Instance variables

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep-copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated<br>before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the output will only contain JSON serializable types.<br>If mode is 'python', the output may contain non-JSON-serializable Python objects. | None |
| include | None | A set of fields to include in the output. | None |
| exclude | None | A set of fields to exclude from the output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. | None |
| exclude | None | Field(s) to exclude from the JSON output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### Link

```python3
class Link(
    /,
    **data: 'Any'
)
```

Link model.

Ref: https://github.com/opengeospatial/ogcapi-tiles/blob/master/openapi/schemas/common-core/link.yaml

Code generated using https://github.com/koxudaxi/datamodel-code-generator/

#### Ancestors (in MRO)

* pydantic.main.BaseModel

#### Class variables

```python3
model_computed_fields
```

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of<br>`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class<br>`Model` with 2 type variables and a concrete model `Model[str, int]`,<br>the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.<br>If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### model_validate_strings

```python3
def model_validate_strings(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate the given object contains string data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object contains string data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

#### Instance variables

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep-copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated<br>before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the output will only contain JSON serializable types.<br>If mode is 'python', the output may contain non-JSON-serializable Python objects. | None |
| include | None | A set of fields to include in the output. | None |
| exclude | None | A set of fields to exclude from the output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. | None |
| exclude | None | Field(s) to exclude from the JSON output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### Metadata

```python3
class Metadata(
    /,
    **data: 'Any'
)
```

Metadata Model.

#### Ancestors (in MRO)

* pydantic.main.BaseModel

#### Class variables

```python3
model_computed_fields
```

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of<br>`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class<br>`Model` with 2 type variables and a concrete model `Model[str, int]`,<br>the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.<br>If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### model_validate_strings

```python3
def model_validate_strings(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate the given object contains string data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object contains string data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

#### Instance variables

```python3
defaults_params
```

Return defaults in a form compatible with TiTiler dependencies.

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep-copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated<br>before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the output will only contain JSON serializable types.<br>If mode is 'python', the output may contain non-JSON-serializable Python objects. | None |
| include | None | A set of fields to include in the output. | None |
| exclude | None | A set of fields to exclude from the output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. | None |
| exclude | None | Field(s) to exclude from the JSON output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### PgSTACSearch

```python3
class PgSTACSearch(
    /,
    **data: 'Any'
)
```

Search Query model.

Notes/Diff with standard model:
    - 'fields' is not in the Model because it's defined at the tiler level
    - we don't set limit

#### Ancestors (in MRO)

* pydantic.main.BaseModel

#### Descendants

* titiler.pgstac.model.RegisterMosaic

#### Class variables

```python3
model_computed_fields
```

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of<br>`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class<br>`Model` with 2 type variables and a concrete model `Model[str, int]`,<br>the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.<br>If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### model_validate_strings

```python3
def model_validate_strings(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate the given object contains string data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object contains string data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

    
#### validate_bbox

```python3
def validate_bbox(
    v: Union[Tuple[float, float, float, float], Tuple[float, float, float, float, float, float]]
)
```

Validate BBOX.

    
#### validate_datetime

```python3
def validate_datetime(
    v
)
```

Pgstac does not require the base validator for datetime.

    
#### validate_query_fields

```python3
def validate_query_fields(
    values: Dict
) -> Dict
```

Pgstac does not require the base validator for query fields.

    
#### validate_spatial

```python3
def validate_spatial(
    v: Optional[Annotated[Union[geojson_pydantic.geometries.Point, geojson_pydantic.geometries.MultiPoint, geojson_pydantic.geometries.LineString, geojson_pydantic.geometries.MultiLineString, geojson_pydantic.geometries.Polygon, geojson_pydantic.geometries.MultiPolygon, geojson_pydantic.geometries.GeometryCollection], FieldInfo(annotation=NoneType, required=True, discriminator='type')]],
    info: pydantic_core.core_schema.ValidationInfo
)
```

Make sure bbox is not used with Intersects.

#### Instance variables

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep-copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated<br>before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the output will only contain JSON serializable types.<br>If mode is 'python', the output may contain non-JSON-serializable Python objects. | None |
| include | None | A set of fields to include in the output. | None |
| exclude | None | A set of fields to exclude from the output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. | None |
| exclude | None | Field(s) to exclude from the JSON output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### RegisterMosaic

```python3
class RegisterMosaic(
    /,
    **data: 'Any'
)
```

Model of /register endpoint input.

#### Ancestors (in MRO)

* titiler.pgstac.model.PgSTACSearch
* pydantic.main.BaseModel

#### Class variables

```python3
model_computed_fields
```

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of<br>`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class<br>`Model` with 2 type variables and a concrete model `Model[str, int]`,<br>the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.<br>If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### model_validate_strings

```python3
def model_validate_strings(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate the given object contains string data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object contains string data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

    
#### validate_bbox

```python3
def validate_bbox(
    v: Union[Tuple[float, float, float, float], Tuple[float, float, float, float, float, float]]
)
```

Validate BBOX.

    
#### validate_datetime

```python3
def validate_datetime(
    v
)
```

Pgstac does not require the base validator for datetime.

    
#### validate_query_fields

```python3
def validate_query_fields(
    values: Dict
) -> Dict
```

Pgstac does not require the base validator for query fields.

    
#### validate_spatial

```python3
def validate_spatial(
    v: Optional[Annotated[Union[geojson_pydantic.geometries.Point, geojson_pydantic.geometries.MultiPoint, geojson_pydantic.geometries.LineString, geojson_pydantic.geometries.MultiLineString, geojson_pydantic.geometries.Polygon, geojson_pydantic.geometries.MultiPolygon, geojson_pydantic.geometries.GeometryCollection], FieldInfo(annotation=NoneType, required=True, discriminator='type')]],
    info: pydantic_core.core_schema.ValidationInfo
)
```

Make sure bbox is not used with Intersects.

#### Instance variables

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep-copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated<br>before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the output will only contain JSON serializable types.<br>If mode is 'python', the output may contain non-JSON-serializable Python objects. | None |
| include | None | A set of fields to include in the output. | None |
| exclude | None | A set of fields to exclude from the output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. | None |
| exclude | None | Field(s) to exclude from the JSON output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### RegisterResponse

```python3
class RegisterResponse(
    /,
    **data: 'Any'
)
```

Response model for /register endpoint.

#### Ancestors (in MRO)

* pydantic.main.BaseModel

#### Class variables

```python3
model_computed_fields
```

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of<br>`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class<br>`Model` with 2 type variables and a concrete model `Model[str, int]`,<br>the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.<br>If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### model_validate_strings

```python3
def model_validate_strings(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate the given object contains string data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object contains string data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

#### Instance variables

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep-copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated<br>before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the output will only contain JSON serializable types.<br>If mode is 'python', the output may contain non-JSON-serializable Python objects. | None |
| include | None | A set of fields to include in the output. | None |
| exclude | None | A set of fields to exclude from the output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. | None |
| exclude | None | Field(s) to exclude from the JSON output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### Search

```python3
class Search(
    /,
    **data: 'Any'
)
```

PgSTAC Search entry.

ref: https://github.com/stac-utils/pgstac/blob/3499daa2bfa700ae7bb07503795c169bf2ebafc7/sql/004_search.sql#L907-L915

#### Ancestors (in MRO)

* pydantic.main.BaseModel

#### Class variables

```python3
model_computed_fields
```

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of<br>`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class<br>`Model` with 2 type variables and a concrete model `Model[str, int]`,<br>the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.<br>If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### model_validate_strings

```python3
def model_validate_strings(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

Validate the given object contains string data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object contains string data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: 'DeprecatedParseProtocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

    
#### validate_metadata

```python3
def validate_metadata(
    v
)
```

Set SearchType.search when not present in metadata.

#### Instance variables

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep-copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated<br>before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the output will only contain JSON serializable types.<br>If mode is 'python', the output may contain non-JSON-serializable Python objects. | None |
| include | None | A set of fields to include in the output. | None |
| exclude | None | A set of fields to exclude from the output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    context: 'dict[str, Any] | None' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: "bool | Literal['none', 'warn', 'error']" = True,
    serialize_as_any: 'bool' = False
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.7/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. | None |
| exclude | None | Field(s) to exclude from the JSON output. | None |
| context | None | Additional context to pass to the serializer. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. | None |
| warnings | None | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,<br>"error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. | None |
| serialize_as_any | None | Whether to serialize fields with duck-typing serialization behavior. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.