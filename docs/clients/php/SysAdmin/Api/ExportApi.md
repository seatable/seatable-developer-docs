# SeaTable\Client\ExportApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**exportBase()**](ExportApi.md#exportBase) | **GET** /api/v2.1/admin/dtables/{base_uuid}/synchronous-export/export-dtable/ | Export base |


## `exportBase()`

```php
exportBase($base_uuid, $ignore_asset)
```

Export base

Use this request to export a base as System Admin.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\ExportApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$ignore_asset = false; // bool | Set this to `true` to export the base without assets. Default is `false`.

try {
    $apiInstance->exportBase($base_uuid, $ignore_asset);
} catch (Exception $e) {
    echo 'Exception when calling ExportApi->exportBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **ignore_asset** | **bool**| Set this to &#x60;true&#x60; to export the base without assets. Default is &#x60;false&#x60;. | [optional] |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth



