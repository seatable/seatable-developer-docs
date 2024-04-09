# SeaTable\Client\BaseInfoApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getBaseInfo()**](BaseInfoApi.md#getBaseInfo) | **GET** /dtable-server/dtables/{base_uuid} | Get Base Info |
| [**getBigDataStatus()**](BaseInfoApi.md#getBigDataStatus) | **GET** /dtable-db/api/v1/base-info/{base_uuid}/ | Get Big Data Status |
| [**getMetadata()**](BaseInfoApi.md#getMetadata) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/metadata/ | Get Metadata |
| [**listCollaborators()**](BaseInfoApi.md#listCollaborators) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/related-users/ | List Collaborators |


## `getBaseInfo()`

```php
getBaseInfo($base_uuid): object
```

Get Base Info

Returns basic information about the specified base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BaseInfoApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->getBaseInfo($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseInfoApi->getBaseInfo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

BaseTokenAuth




## `getBigDataStatus()`

```php
getBigDataStatus($base_uuid): object
```

Get Big Data Status

Returns the total number of rows stored in the big data backend of the specified base as well as rows in the big data backend per table.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BaseInfoApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->getBigDataStatus($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseInfoApi->getBigDataStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

BaseTokenAuth




## `getMetadata()`

```php
getMetadata($base_uuid): object
```

Get Metadata

Returns all metadata of the specified base including tables, columns, views and settings.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BaseInfoApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->getMetadata($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseInfoApi->getMetadata: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

BaseTokenAuth




## `listCollaborators()`

```php
listCollaborators($base_uuid): object
```

List Collaborators

Returns all collaborators in the specified base including name, email address and avatar.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\BaseInfoApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->listCollaborators($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseInfoApi->listCollaborators: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

BaseTokenAuth



