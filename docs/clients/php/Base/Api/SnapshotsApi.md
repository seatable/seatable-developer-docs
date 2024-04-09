# SeaTable\Client\SnapshotsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createSnapshot()**](SnapshotsApi.md#createSnapshot) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/snapshot/ | Create Snapshot |


## `createSnapshot()`

```php
createSnapshot($base_uuid, $generate_snapshot): object
```

Create Snapshot

Creates a snapshot for the current base. The pre-conditions are, that there's at least one change since the last snapshot and at least 10 minutes have passed.  To get a list of already existing snapshots, use the the request [List Snapshots](/reference/list-snapshots).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\SnapshotsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$generate_snapshot = new \SeaTable\Client\Base\GenerateSnapshot(); // \SeaTable\Client\Base\GenerateSnapshot

try {
    $result = $apiInstance->createSnapshot($base_uuid, $generate_snapshot);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SnapshotsApi->createSnapshot: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **generate_snapshot** | [**\SeaTable\Client\Base\GenerateSnapshot**](../Model/GenerateSnapshot.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth



