# SeaTable\Client\CommonDatasetApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteInvalidSync()**](CommonDatasetApi.md#deleteInvalidSync) | **DELETE** /api/v2.1/admin/common-dataset/sync/{sync_id}/ | Delete Invalid Sync |
| [**deleteInvalidSyncs()**](CommonDatasetApi.md#deleteInvalidSyncs) | **DELETE** /api/v2.1/admin/common-dataset/invalid-syncs/ | Delete Invalid Syncs |
| [**listCommonDataset()**](CommonDatasetApi.md#listCommonDataset) | **GET** /api/v2.1/admin/common-datasets/ | List Common Dataset |
| [**listCommonDatasetSyncs()**](CommonDatasetApi.md#listCommonDatasetSyncs) | **GET** /api/v2.1/admin/common-dataset/periodical-syncs/ | List Common Dataset Syncs |
| [**listInvalidSyncs()**](CommonDatasetApi.md#listInvalidSyncs) | **GET** /api/v2.1/admin/common-dataset/invalid-syncs/ | List invalid Syncs |


## `deleteInvalidSync()`

```php
deleteInvalidSync($sync_id): object
```

Delete Invalid Sync

Delete an invalid common dataset synchronization configuration with its ID retrieved from the previous request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$sync_id = 2; // int | The ID of the invalid synchronization, retrievable from the previous call.

try {
    $result = $apiInstance->deleteInvalidSync($sync_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->deleteInvalidSync: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sync_id** | **int**| The ID of the invalid synchronization, retrievable from the previous call. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteInvalidSyncs()`

```php
deleteInvalidSyncs(): object
```

Delete Invalid Syncs

Use this request to delete all invalid common dataset synchronization configurations at once.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->deleteInvalidSyncs();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->deleteInvalidSyncs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listCommonDataset()`

```php
listCommonDataset($page, $per_page): object
```

List Common Dataset

List all the common datasets in the current system. In the response, you can see *   The name of the common datasets, *   The source base's name, *   The creator's name, and *   The time of the creation.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listCommonDataset($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->listCommonDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listCommonDatasetSyncs()`

```php
listCommonDatasetSyncs($page, $per_page): object
```

List Common Dataset Syncs

Use this request to explicitly list off the periodically synchronized common datasets in the system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listCommonDatasetSyncs($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->listCommonDatasetSyncs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listInvalidSyncs()`

```php
listInvalidSyncs($page, $per_page): object
```

List invalid Syncs

In some cases, a common dataset synchronization configuration becomes invalid. Such cases happen when, for example, the source or destination tables are deleted. Use this request to list off all the invalid common dataset synchronization configurations in the system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listInvalidSyncs($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->listInvalidSyncs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



