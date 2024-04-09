# SeaTable\Client\SnapshotsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listSnapshots()**](SnapshotsApi.md#listSnapshots) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/snapshots/ | List Snapshots |
| [**restoreSnapshot()**](SnapshotsApi.md#restoreSnapshot) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/snapshots/{commit_id}/restore/ | Restore Snapshot |


## `listSnapshots()`

```php
listSnapshots($workspace_id, $base_name, $page, $per_page): object
```

List Snapshots

List all the snapshots currently available in a base. The snapshots are saved as `.dtable` files, and therefore returned as a base name with this suffix. The `commit_id` is the ID of the snapshot, and the `ctime` is the time of creation.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SnapshotsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$page = 1; // int
$per_page = 2; // int

try {
    $result = $apiInstance->listSnapshots($workspace_id, $base_name, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SnapshotsApi->listSnapshots: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **page** | **int**|  | [optional] |
| **per_page** | **int**|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `restoreSnapshot()`

```php
restoreSnapshot($workspace_id, $base_name, $commit_id, $snapshot_name): object
```

Restore Snapshot

Restore a snapshot and save it as a new base besides the existing base.   The `commit_id` is the ID of the snapshot to be restored. This can be retrieved with the call [List Snapshots](/reference/get_api-v2-1-workspace-workspace-id-dtable-base-name-snapshots).  You can give the restored base a new name by defining the value of the `snapshot_name` param. If left blank, SeaTable gives the restored base a default name which is a combination of the original base name and \"(restored)\" or similar.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SnapshotsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$commit_id = 7ee107a4eadb9561e8ce7699494939015f0d101b; // string
$snapshot_name = 'snapshot_name_example'; // string | The name of the restored base. Optional. If left blank, a default name will be given.

try {
    $result = $apiInstance->restoreSnapshot($workspace_id, $base_name, $commit_id, $snapshot_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SnapshotsApi->restoreSnapshot: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **commit_id** | **string**|  | |
| **snapshot_name** | **string**| The name of the restored base. Optional. If left blank, a default name will be given. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



