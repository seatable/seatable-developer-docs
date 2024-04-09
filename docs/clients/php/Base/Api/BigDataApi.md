# SeaTable\Client\BigDataApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createBigDataRowsLink()**](BigDataApi.md#createBigDataRowsLink) | **POST** /dtable-db/api/v1/base/{base_uuid}/links/ | Create Row Links in Big Data |
| [**deleteBigDataRowLinks()**](BigDataApi.md#deleteBigDataRowLinks) | **DELETE** /dtable-db/api/v1/base/{base_uuid}/links/ | Delete Row Links in Big Data |
| [**deleteBigDataRows()**](BigDataApi.md#deleteBigDataRows) | **DELETE** /dtable-db/api/v1/delete-rows/{base_uuid}/ | Delete Rows in Big Data |
| [**insertBigDataRows()**](BigDataApi.md#insertBigDataRows) | **POST** /dtable-db/api/v1/insert-rows/{base_uuid}/ | Insert Rows into Big Data |
| [**moveRowsToBigData()**](BigDataApi.md#moveRowsToBigData) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/archive-view/ | Move Rows to Big Data |
| [**updateBigDataRows()**](BigDataApi.md#updateBigDataRows) | **PUT** /dtable-db/api/v1/update-rows/{base_uuid}/ | Update Rows in Big Data |


## `createBigDataRowsLink()`

```php
createBigDataRowsLink($base_uuid, $archived_row_links): object
```

Create Row Links in Big Data

This API can handle both archived and unarchived rows.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BigDataApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$archived_row_links = new \SeaTable\Client\Base\ArchivedRowLinks(); // \SeaTable\Client\Base\ArchivedRowLinks

try {
    $result = $apiInstance->createBigDataRowsLink($base_uuid, $archived_row_links);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BigDataApi->createBigDataRowsLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **archived_row_links** | [**\SeaTable\Client\Base\ArchivedRowLinks**](../Model/ArchivedRowLinks.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `deleteBigDataRowLinks()`

```php
deleteBigDataRowLinks($base_uuid, $archived_row_links): object
```

Delete Row Links in Big Data

This API can handle both archived and unarchived rows.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BigDataApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$archived_row_links = new \SeaTable\Client\Base\ArchivedRowLinks(); // \SeaTable\Client\Base\ArchivedRowLinks

try {
    $result = $apiInstance->deleteBigDataRowLinks($base_uuid, $archived_row_links);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BigDataApi->deleteBigDataRowLinks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **archived_row_links** | [**\SeaTable\Client\Base\ArchivedRowLinks**](../Model/ArchivedRowLinks.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `deleteBigDataRows()`

```php
deleteBigDataRows($base_uuid, $delete_rows): object
```

Delete Rows in Big Data

Delete rows that are currently stored the big data backend identified by their row id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BigDataApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$delete_rows = new \SeaTable\Client\Base\DeleteRows(); // \SeaTable\Client\Base\DeleteRows

try {
    $result = $apiInstance->deleteBigDataRows($base_uuid, $delete_rows);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BigDataApi->deleteBigDataRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **delete_rows** | [**\SeaTable\Client\Base\DeleteRows**](../Model/DeleteRows.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `insertBigDataRows()`

```php
insertBigDataRows($base_uuid, $insert_rows_into_big_data): object
```

Insert Rows into Big Data

Insert rows into the big data backend.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BigDataApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$insert_rows_into_big_data = new \SeaTable\Client\Base\InsertRowsIntoBigData(); // \SeaTable\Client\Base\InsertRowsIntoBigData

try {
    $result = $apiInstance->insertBigDataRows($base_uuid, $insert_rows_into_big_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BigDataApi->insertBigDataRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **insert_rows_into_big_data** | [**\SeaTable\Client\Base\InsertRowsIntoBigData**](../Model/InsertRowsIntoBigData.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `moveRowsToBigData()`

```php
moveRowsToBigData($base_uuid, $archive_view): object
```

Move Rows to Big Data

Use an sql-like where clause to select the rows that should be moved into the big data backend.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BigDataApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$archive_view = new \SeaTable\Client\Base\ArchiveView(); // \SeaTable\Client\Base\ArchiveView

try {
    $result = $apiInstance->moveRowsToBigData($base_uuid, $archive_view);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BigDataApi->moveRowsToBigData: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **archive_view** | [**\SeaTable\Client\Base\ArchiveView**](../Model/ArchiveView.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `updateBigDataRows()`

```php
updateBigDataRows($base_uuid, $update_rows): object
```

Update Rows in Big Data

Update multipe rows in the big data backend identified by their row id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BigDataApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$update_rows = new \SeaTable\Client\Base\UpdateRows(); // \SeaTable\Client\Base\UpdateRows

try {
    $result = $apiInstance->updateBigDataRows($base_uuid, $update_rows);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BigDataApi->updateBigDataRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **update_rows** | [**\SeaTable\Client\Base\UpdateRows**](../Model/UpdateRows.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth



