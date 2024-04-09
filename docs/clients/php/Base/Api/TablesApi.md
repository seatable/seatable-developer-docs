# SeaTable\Client\TablesApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createTable()**](TablesApi.md#createTable) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/tables/ | Create Table |
| [**deleteTable()**](TablesApi.md#deleteTable) | **DELETE** /dtable-server/api/v1/dtables/{base_uuid}/tables/ | Delete Table |
| [**duplicateTable()**](TablesApi.md#duplicateTable) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/tables/duplicate-table/ | Duplicate Table |
| [**renameTable()**](TablesApi.md#renameTable) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/tables/ | Rename Table |


## `createTable()`

```php
createTable($base_uuid, $create_table_request): \SeaTable\Client\Base\Base
```

Create Table

Creates a new table in a base. Optionally, you can already add some columns to the base.  > 📘 The first column is special > > Please be aware, that the first column can only be the column type `text`, `number`, `date`, `single select`, `formula` and `autonumber`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\TablesApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$create_table_request = new \SeaTable\Client\Base\CreateTableRequest(); // \SeaTable\Client\Base\CreateTableRequest

try {
    $result = $apiInstance->createTable($base_uuid, $create_table_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TablesApi->createTable: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **create_table_request** | [**\SeaTable\Client\Base\CreateTableRequest**](../Model/CreateTableRequest.md)|  | [optional] |

### Return type

[**\SeaTable\Client\Base\Base**](../Model/Base.md)

### Authorization

BaseTokenAuth




## `deleteTable()`

```php
deleteTable($base_uuid, $delete_table): object
```

Delete Table

Delete an existing table identified by its name.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\TablesApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$delete_table = new \SeaTable\Client\Base\DeleteTable(); // \SeaTable\Client\Base\DeleteTable

try {
    $result = $apiInstance->deleteTable($base_uuid, $delete_table);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TablesApi->deleteTable: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **delete_table** | [**\SeaTable\Client\Base\DeleteTable**](../Model/DeleteTable.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `duplicateTable()`

```php
duplicateTable($base_uuid, $duplicate_table): object
```

Duplicate Table

Duplicate an existing table in your base with or without the existing data in it.  > 🚧 Rename the table in a second step > > If you duplicate one table, the name of this new table will always be the same like the original one plus the appendix **(copy)**. To rename the table, you will need another call.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\TablesApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$duplicate_table = new \SeaTable\Client\Base\DuplicateTable(); // \SeaTable\Client\Base\DuplicateTable

try {
    $result = $apiInstance->duplicateTable($base_uuid, $duplicate_table);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TablesApi->duplicateTable: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **duplicate_table** | [**\SeaTable\Client\Base\DuplicateTable**](../Model/DuplicateTable.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `renameTable()`

```php
renameTable($base_uuid, $rename_table): object
```

Rename Table

Rename a table by providing it's original `table_name` and the desired `new_table_name`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\TablesApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$rename_table = new \SeaTable\Client\Base\RenameTable(); // \SeaTable\Client\Base\RenameTable

try {
    $result = $apiInstance->renameTable($base_uuid, $rename_table);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TablesApi->renameTable: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **rename_table** | [**\SeaTable\Client\Base\RenameTable**](../Model/RenameTable.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth



