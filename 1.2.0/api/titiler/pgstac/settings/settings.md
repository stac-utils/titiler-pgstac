# Module titiler.pgstac.settings

API settings.

## Functions

    
### RetrySettings

```python3
def RetrySettings(
    
) -> titiler.pgstac.settings._RetrySettings
```

This function returns a cached instance of the RetrySettings object.

## Classes

### ApiSettings

```python3
class ApiSettings(
    __pydantic_self__,
    _case_sensitive: 'bool | None' = None,
    _env_prefix: 'str | None' = None,
    _env_file: 'DotenvType | None' = PosixPath('.'),
    _env_file_encoding: 'str | None' = None,
    _env_nested_delimiter: 'str | None' = None,
    _secrets_dir: 'str | Path | None' = None,
    **values: 'Any'
)
```

API settings

#### Ancestors (in MRO)

* pydantic_settings.main.BaseSettings
* pydantic.main.BaseModel

#### Class variables

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
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

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
| strict | None | Whether to raise an exception on invalid fields. | None |
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

Usage docs: https://docs.pydantic.dev/2.5/concepts/json/#json-parsing

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

    
#### parse_cors_origin

```python3
def parse_cors_origin(
    v
)
```

Parse CORS origins.

    
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

    
#### settings_customise_sources

```python3
def settings_customise_sources(
    settings_cls: 'type[BaseSettings]',
    init_settings: 'PydanticBaseSettingsSource',
    env_settings: 'PydanticBaseSettingsSource',
    dotenv_settings: 'PydanticBaseSettingsSource',
    file_secret_settings: 'PydanticBaseSettingsSource'
) -> 'tuple[PydanticBaseSettingsSource, ...]'
```

Define the sources and their order for loading the settings values.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| settings_cls | None | The Settings class. | None |
| init_settings | None | The `InitSettingsSource` instance. | None |
| env_settings | None | The `EnvSettingsSource` instance. | None |
| dotenv_settings | None | The `DotEnvSettingsSource` instance. | None |
| file_secret_settings | None | The `SecretsSettingsSource` instance. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A tuple containing the sources and their order for loading the settings values. |

    
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
model_computed_fields
```

Get the computed fields of this model instance.

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
| include | None | Optional set or mapping<br>specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping<br>specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values<br>in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep copied. | None |

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

Usage docs: https://docs.pydantic.dev/2.5/concepts/serialization/#model_copy

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
    mode: "Literal[('json', 'python')] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.5/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the dictionary will only contain JSON serializable types.<br>If mode is 'python', the dictionary may contain any Python objects. | None |
| include | None | A list of fields to include in the output. | None |
| exclude | None | A list of fields to exclude from the output. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value from the output. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None` from the output. | None |
| round_trip | None | Whether to enable serialization and deserialization round-trip support. | None |
| warnings | None | Whether to log warnings when invalid fields are encountered. | None |

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
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.5/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. Can take either a string or set of strings. | None |
| exclude | None | Field(s) to exclude from the JSON output. Can take either a string or set of strings. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that have the default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | Whether to use serialization/deserialization between JSON and class instance. | None |
| warnings | None | Whether to show any warnings that occurred during serialization. | None |

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

### CacheSettings

```python3
class CacheSettings(
    __pydantic_self__,
    _case_sensitive: 'bool | None' = None,
    _env_prefix: 'str | None' = None,
    _env_file: 'DotenvType | None' = PosixPath('.'),
    _env_file_encoding: 'str | None' = None,
    _env_nested_delimiter: 'str | None' = None,
    _secrets_dir: 'str | Path | None' = None,
    **values: 'Any'
)
```

Cache settings

#### Ancestors (in MRO)

* pydantic_settings.main.BaseSettings
* pydantic.main.BaseModel

#### Class variables

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
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

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
| strict | None | Whether to raise an exception on invalid fields. | None |
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

Usage docs: https://docs.pydantic.dev/2.5/concepts/json/#json-parsing

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

    
#### settings_customise_sources

```python3
def settings_customise_sources(
    settings_cls: 'type[BaseSettings]',
    init_settings: 'PydanticBaseSettingsSource',
    env_settings: 'PydanticBaseSettingsSource',
    dotenv_settings: 'PydanticBaseSettingsSource',
    file_secret_settings: 'PydanticBaseSettingsSource'
) -> 'tuple[PydanticBaseSettingsSource, ...]'
```

Define the sources and their order for loading the settings values.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| settings_cls | None | The Settings class. | None |
| init_settings | None | The `InitSettingsSource` instance. | None |
| env_settings | None | The `EnvSettingsSource` instance. | None |
| dotenv_settings | None | The `DotEnvSettingsSource` instance. | None |
| file_secret_settings | None | The `SecretsSettingsSource` instance. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A tuple containing the sources and their order for loading the settings values. |

    
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
model_computed_fields
```

Get the computed fields of this model instance.

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been explicitly set on this model instance.

#### Methods

    
#### check_enable

```python3
def check_enable(
    self
)
```

Check if cache is disabled.

    
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
| include | None | Optional set or mapping<br>specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping<br>specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values<br>in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep copied. | None |

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

Usage docs: https://docs.pydantic.dev/2.5/concepts/serialization/#model_copy

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
    mode: "Literal[('json', 'python')] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.5/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the dictionary will only contain JSON serializable types.<br>If mode is 'python', the dictionary may contain any Python objects. | None |
| include | None | A list of fields to include in the output. | None |
| exclude | None | A list of fields to exclude from the output. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value from the output. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None` from the output. | None |
| round_trip | None | Whether to enable serialization and deserialization round-trip support. | None |
| warnings | None | Whether to log warnings when invalid fields are encountered. | None |

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
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.5/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. Can take either a string or set of strings. | None |
| exclude | None | Field(s) to exclude from the JSON output. Can take either a string or set of strings. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that have the default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | Whether to use serialization/deserialization between JSON and class instance. | None |
| warnings | None | Whether to show any warnings that occurred during serialization. | None |

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

### PostgresSettings

```python3
class PostgresSettings(
    __pydantic_self__,
    _case_sensitive: 'bool | None' = None,
    _env_prefix: 'str | None' = None,
    _env_file: 'DotenvType | None' = PosixPath('.'),
    _env_file_encoding: 'str | None' = None,
    _env_nested_delimiter: 'str | None' = None,
    _secrets_dir: 'str | Path | None' = None,
    **values: 'Any'
)
```

Postgres-specific API settings.

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| postgres_user | None | postgres username. | None |
| postgres_pass | None | postgres password. | None |
| postgres_host | None | database hostname. | None |
| postgres_port | None | database port. | None |
| postgres_dbname | None | database name. | None |

#### Ancestors (in MRO)

* pydantic_settings.main.BaseSettings
* pydantic.main.BaseModel

#### Class variables

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### assemble_db_connection

```python3
def assemble_db_connection(
    v: Union[str, NoneType],
    info: pydantic_core.core_schema.ValidationInfo
) -> Any
```

Validate database config.

    
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
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

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
| strict | None | Whether to raise an exception on invalid fields. | None |
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

Usage docs: https://docs.pydantic.dev/2.5/concepts/json/#json-parsing

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

    
#### settings_customise_sources

```python3
def settings_customise_sources(
    settings_cls: 'type[BaseSettings]',
    init_settings: 'PydanticBaseSettingsSource',
    env_settings: 'PydanticBaseSettingsSource',
    dotenv_settings: 'PydanticBaseSettingsSource',
    file_secret_settings: 'PydanticBaseSettingsSource'
) -> 'tuple[PydanticBaseSettingsSource, ...]'
```

Define the sources and their order for loading the settings values.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| settings_cls | None | The Settings class. | None |
| init_settings | None | The `InitSettingsSource` instance. | None |
| env_settings | None | The `EnvSettingsSource` instance. | None |
| dotenv_settings | None | The `DotEnvSettingsSource` instance. | None |
| file_secret_settings | None | The `SecretsSettingsSource` instance. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A tuple containing the sources and their order for loading the settings values. |

    
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
model_computed_fields
```

Get the computed fields of this model instance.

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
| include | None | Optional set or mapping<br>specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping<br>specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values<br>in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep copied. | None |

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

Usage docs: https://docs.pydantic.dev/2.5/concepts/serialization/#model_copy

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
    mode: "Literal[('json', 'python')] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'dict[str, Any]'
```

Usage docs: https://docs.pydantic.dev/2.5/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.<br>If mode is 'json', the dictionary will only contain JSON serializable types.<br>If mode is 'python', the dictionary may contain any Python objects. | None |
| include | None | A list of fields to include in the output. | None |
| exclude | None | A list of fields to exclude from the output. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value from the output. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None` from the output. | None |
| round_trip | None | Whether to enable serialization and deserialization round-trip support. | None |
| warnings | None | Whether to log warnings when invalid fields are encountered. | None |

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
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'str'
```

Usage docs: https://docs.pydantic.dev/2.5/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. Can take either a string or set of strings. | None |
| exclude | None | Field(s) to exclude from the JSON output. Can take either a string or set of strings. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that have the default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | Whether to use serialization/deserialization between JSON and class instance. | None |
| warnings | None | Whether to show any warnings that occurred during serialization. | None |

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