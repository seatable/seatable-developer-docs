# SeaTable\Client\ImportExportApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**appendToTableFromFile()**](ImportExportApi.md#appendToTableFromFile) | **POST** /api/v2.1/workspace/{workspace_id}/synchronous-import/append-excel-csv-to-table/ | Append Excel CSV |
| [**exportBase()**](ImportExportApi.md#exportBase) | **GET** /api/v2.1/workspace/{workspace_id}/synchronous-export/export-dtable/ | Export Base |
| [**exportBaseFromExternalLink()**](ImportExportApi.md#exportBaseFromExternalLink) | **GET** /dtable/external-links/{external_link_token}/download-zip/ | Export Base from External Link |
| [**exportBigDataView()**](ImportExportApi.md#exportBigDataView) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/convert-big-data-view-to-excel/ | Export Big Data View to Excel |
| [**exportTable()**](ImportExportApi.md#exportTable) | **GET** /api/v2.1/workspace/{workspace_id}/synchronous-export/export-table-to-excel/ | Export Table |
| [**exportView()**](ImportExportApi.md#exportView) | **GET** /api/v2.1/workspace/{workspace_id}/synchronous-export/export-view-to-excel/ | Export View |
| [**importBasefromFile()**](ImportExportApi.md#importBasefromFile) | **POST** /api/v2.1/workspace/{workspace_id}/synchronous-import/import-excel-csv-to-base/ | Import Base from xlsx or csv |
| [**importTableFromFile()**](ImportExportApi.md#importTableFromFile) | **POST** /api/v2.1/workspace/{workspace_id}/synchronous-import/import-excel-csv-to-table/ | Import Table from xlsx or csv |
| [**updateFromFile()**](ImportExportApi.md#updateFromFile) | **POST** /api/v2.1/workspace/{workspace_id}/synchronous-import/update-table-via-excel-csv/ | Update from xlsx or csv |


## `appendToTableFromFile()`

```php
appendToTableFromFile($workspace_id, $file, $dtable_uuid, $table_name): object
```

Append Excel CSV

Hier muss noch eine Beschreibung ergänzt werden.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\ImportExportApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$file = "/path/to/file.txt"; // \SplFileObject
$dtable_uuid = 'dtable_uuid_example'; // string | The UUID of the base.
$table_name = 'table_name_example'; // string | The name of the table.

try {
    $result = $apiInstance->appendToTableFromFile($workspace_id, $file, $dtable_uuid, $table_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ImportExportApi->appendToTableFromFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **file** | **\SplFileObject****\SplFileObject**|  | [optional] |
| **dtable_uuid** | **string**| The UUID of the base. | [optional] |
| **table_name** | **string**| The name of the table. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `exportBase()`

```php
exportBase($dtable_name, $workspace_id, $password, $ignore_asset)
```

Export Base

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\ImportExportApi(
    new GuzzleHttp\Client(),
    $config
);
$dtable_name = Example; // string
$workspace_id = 127; // int | id of your workspace.
$password = 'password_example'; // string | The password of your Base.
$ignore_asset = false; // bool | Set this to `true` to export the base without assets. Default is `false`.

try {
    $apiInstance->exportBase($dtable_name, $workspace_id, $password, $ignore_asset);
} catch (Exception $e) {
    echo 'Exception when calling ImportExportApi->exportBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dtable_name** | **string**|  | |
| **workspace_id** | **int**| id of your workspace. | |
| **password** | **string**| The password of your Base. | [optional] |
| **ignore_asset** | **bool**| Set this to &#x60;true&#x60; to export the base without assets. Default is &#x60;false&#x60;. | [optional] |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `exportBaseFromExternalLink()`

```php
exportBaseFromExternalLink($external_link_token)
```

Export Base from External Link

Download a base with its external link as a .dtable zip file. **Password protected external links are not supported yet**.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new SeaTable\Client\User\ImportExportApi(
    new GuzzleHttp\Client()
);
$external_link_token = fleischkaesebroetchen; // string

try {
    $apiInstance->exportBaseFromExternalLink($external_link_token);
} catch (Exception $e) {
    echo 'Exception when calling ImportExportApi->exportBaseFromExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **external_link_token** | **string**|  | |

### Return type

void (empty response body)

### Authorization

No authorization required



## `exportBigDataView()`

```php
exportBigDataView($workspace_id, $base_name, $table_id, $view_id)
```

Export Big Data View to Excel

Hier muss noch eine Beschreibung ergänzt werden

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\ImportExportApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$table_id = 0000; // string | The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**.
$view_id = Jz4d; // string | id of view, string

try {
    $apiInstance->exportBigDataView($workspace_id, $base_name, $table_id, $view_id);
} catch (Exception $e) {
    echo 'Exception when calling ImportExportApi->exportBigDataView: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **table_id** | **string**| The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**. | |
| **view_id** | **string**| id of view, string | |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `exportTable()`

```php
exportTable($table_id, $table_name, $dtable_name, $workspace_id)
```

Export Table

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\ImportExportApi(
    new GuzzleHttp\Client(),
    $config
);
$table_id = 0000; // string | The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**.
$table_name = Table1; // string | The name of the table.
$dtable_name = Example; // string
$workspace_id = 127; // int | id of your workspace.

try {
    $apiInstance->exportTable($table_id, $table_name, $dtable_name, $workspace_id);
} catch (Exception $e) {
    echo 'Exception when calling ImportExportApi->exportTable: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table_id** | **string**| The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**. | |
| **table_name** | **string**| The name of the table. | |
| **dtable_name** | **string**|  | |
| **workspace_id** | **int**| id of your workspace. | |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `exportView()`

```php
exportView($table_id, $table_name, $dtable_name, $view_id, $view_name, $workspace_id)
```

Export View

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\ImportExportApi(
    new GuzzleHttp\Client(),
    $config
);
$table_id = 0000; // string | The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**.
$table_name = Table1; // string | The name of the table.
$dtable_name = Example; // string
$view_id = Jz4d; // string | id of view, string
$view_name = Default View; // string | name of view, required, string
$workspace_id = 127; // int | id of your workspace.

try {
    $apiInstance->exportView($table_id, $table_name, $dtable_name, $view_id, $view_name, $workspace_id);
} catch (Exception $e) {
    echo 'Exception when calling ImportExportApi->exportView: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table_id** | **string**| The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**. | |
| **table_name** | **string**| The name of the table. | |
| **dtable_name** | **string**|  | |
| **view_id** | **string**| id of view, string | |
| **view_name** | **string**| name of view, required, string | |
| **workspace_id** | **int**| id of your workspace. | |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `importBasefromFile()`

```php
importBasefromFile($workspace_id, $dtable, $folder): object
```

Import Base from xlsx or csv

With this request, you can create a base by uploading a .xlsx or a .csv file.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\ImportExportApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$dtable = "/path/to/file.txt"; // \SplFileObject
$folder = 'folder_example'; // string | If you would like to create the base into a folder, give its `folder_id` here. A base is created in the root folder by default. Optional.

try {
    $result = $apiInstance->importBasefromFile($workspace_id, $dtable, $folder);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ImportExportApi->importBasefromFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **dtable** | **\SplFileObject****\SplFileObject**|  | [optional] |
| **folder** | **string**| If you would like to create the base into a folder, give its &#x60;folder_id&#x60; here. A base is created in the root folder by default. Optional. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `importTableFromFile()`

```php
importTableFromFile($workspace_id, $file, $dtable_uuid): object
```

Import Table from xlsx or csv

An XLSX or CSV file can also be imported as a new table in your base. Just select the `file` and tell SeaTable your base's UUID and the file will be added to that base as a new table. The new table's name will be the filename by default.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\ImportExportApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$file = "/path/to/file.txt"; // \SplFileObject
$dtable_uuid = 'dtable_uuid_example'; // string | The UUID of the base.

try {
    $result = $apiInstance->importTableFromFile($workspace_id, $file, $dtable_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ImportExportApi->importTableFromFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **file** | **\SplFileObject****\SplFileObject**|  | [optional] |
| **dtable_uuid** | **string**| The UUID of the base. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `updateFromFile()`

```php
updateFromFile($workspace_id, $file, $dtable_uuid, $table_name, $selected_columns): object
```

Update from xlsx or csv

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\ImportExportApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$file = "/path/to/file.txt"; // \SplFileObject
$dtable_uuid = 'dtable_uuid_example'; // string | The UUID of the base.
$table_name = 'table_name_example'; // string | The name of the table.
$selected_columns = 'selected_columns_example'; // string | The columns to update. Use comma (,) to separate column names. Required.

try {
    $result = $apiInstance->updateFromFile($workspace_id, $file, $dtable_uuid, $table_name, $selected_columns);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ImportExportApi->updateFromFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **file** | **\SplFileObject****\SplFileObject**|  | [optional] |
| **dtable_uuid** | **string**| The UUID of the base. | [optional] |
| **table_name** | **string**| The name of the table. | [optional] |
| **selected_columns** | **string**| The columns to update. Use comma (,) to separate column names. Required. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


