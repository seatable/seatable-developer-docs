# SeaTable\Client\CommonDatasetApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteCommonDataset()**](CommonDatasetApi.md#deleteCommonDataset) | **DELETE** /api/v2.1/dtable/common-datasets/{dataset_id}/ | Delete Common Dataset |
| [**getCommonDataset()**](CommonDatasetApi.md#getCommonDataset) | **GET** /api/v2.1/dtable/common-datasets/{dataset_id}/ | Get Common Dataset |
| [**getCommonDatasetInfo()**](CommonDatasetApi.md#getCommonDatasetInfo) | **GET** /api/v2.1/dtable/common-datasets/{dataset_id}/info/ | Get Common Dataset Info |
| [**importCommonDataset()**](CommonDatasetApi.md#importCommonDataset) | **POST** /api/v2.1/dtable/common-datasets/{dataset_id}/import/ | Import Common Dataset |
| [**listCommonDataset()**](CommonDatasetApi.md#listCommonDataset) | **GET** /api/v2.1/dtable/common-datasets/ | List Common Datasets |
| [**listSyncHistory()**](CommonDatasetApi.md#listSyncHistory) | **GET** /api/v2.1/dtable/common-datasets/syncs/ | List Sync History |
| [**publishCommonDataset()**](CommonDatasetApi.md#publishCommonDataset) | **POST** /api/v2.1/dtable/common-datasets/ | Publish Common Dataset |
| [**renameCommonDataset()**](CommonDatasetApi.md#renameCommonDataset) | **PUT** /api/v2.1/dtable/common-datasets/{dataset_id}/ | Rename Common Dataset |
| [**syncCommonDataset()**](CommonDatasetApi.md#syncCommonDataset) | **POST** /api/v2.1/dtable/common-datasets/{dataset_id}/sync/ | Sync Common Dataset |
| [**updateCommonDatasetSync()**](CommonDatasetApi.md#updateCommonDatasetSync) | **PUT** /api/v2.1/dtable/common-datasets/{dataset_id}/sync/ | Update Common Dataset Sync |


## `deleteCommonDataset()`

```php
deleteCommonDataset($dataset_id): object
```

Delete Common Dataset

Delete a common dataset by its ID. This ID could be retrieved by the call e.g. [List Common Datasets A Base Can Access](/reference/get_api-v2-1-dtable-common-datasets-1).  This request doesn't delete anything in real. It just stops sharing that view from the original base. The data in the original base is intact.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dataset_id = 5; // int | The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned `id` is what you need here.

try {
    $result = $apiInstance->deleteCommonDataset($dataset_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->deleteCommonDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **int**| The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned &#x60;id&#x60; is what you need here. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `getCommonDataset()`

```php
getCommonDataset($dataset_id): object
```

Get Common Dataset

List the content of the common dataset by rows, columns and related users. The `dataset_id` used here is the ID you have retrieved from the response when you publish a common dataset.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dataset_id = 5; // int | The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned `id` is what you need here.

try {
    $result = $apiInstance->getCommonDataset($dataset_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->getCommonDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **int**| The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned &#x60;id&#x60; is what you need here. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `getCommonDatasetInfo()`

```php
getCommonDatasetInfo($dataset_id): object
```

Get Common Dataset Info

List the basic information of the common dataset by the source table name and view name. The `dataset_id` used here is the ID you have retrieved from the response when you publish a common dataset.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dataset_id = 5; // int | The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned `id` is what you need here.

try {
    $result = $apiInstance->getCommonDatasetInfo($dataset_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->getCommonDatasetInfo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **int**| The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned &#x60;id&#x60; is what you need here. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `importCommonDataset()`

```php
importCommonDataset($dataset_id, $dst_dtable_uuid): object
```

Import Common Dataset

Import a common dataset into your destination base. This will create a new table labeled as a common dataset table.    To import a common dataset into a base, the following conditions have to be met:    - The destination base is in a group, and  - You are the admin or owner of this group, and  - This group has access to the common dataset.    The ID of the common dataset can be retrieved via the request e.g. [List Common Datasets A Base Can Access](/reference/get_api-v2-1-dtable-common-datasets-1).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dataset_id = 5; // int | The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned `id` is what you need here.
$dst_dtable_uuid = 'dst_dtable_uuid_example'; // string | The name of the base.

try {
    $result = $apiInstance->importCommonDataset($dataset_id, $dst_dtable_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->importCommonDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **int**| The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned &#x60;id&#x60; is what you need here. | |
| **dst_dtable_uuid** | **string**| The name of the base. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listCommonDataset()`

```php
listCommonDataset($dtable_uuid, $by_group): object
```

List Common Datasets

List all the common datasets a particular base can access by its `base_uuid`.  Basically, when a common dataset is shared to a group and this base is in the group, it has access to the common dataset.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dtable_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$by_group = True; // bool | Whether return the list of datasets by groups when dtable_uuid is not given, default false, optional

try {
    $result = $apiInstance->listCommonDataset($dtable_uuid, $by_group);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->listCommonDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dtable_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **by_group** | **bool**| Whether return the list of datasets by groups when dtable_uuid is not given, default false, optional | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listSyncHistory()`

```php
listSyncHistory($dtable_uuid): object
```

List Sync History

Use this call to list off the common datasets synchronization history of the current base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dtable_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->listSyncHistory($dtable_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->listSyncHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dtable_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `publishCommonDataset()`

```php
publishCommonDataset($dataset_name, $workspace_id, $dtable_name, $table_name, $view_name): object
```

Publish Common Dataset

You can publish a common dataset from a view, if the following conditions are met: - This base is in a group, and - You are the owner or admin of this group. After successful publishing, the returned `id` value is the ID of the common dataset.  All the request params are required.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dataset_name = 'dataset_name_example'; // string | The name of the common dataset.
$workspace_id = 'workspace_id_example'; // string | The workspace ID where your base is.
$dtable_name = 'dtable_name_example'; // string | The name of the base.
$table_name = 'table_name_example'; // string | The name of the table.
$view_name = 'view_name_example'; // string | The name of the view

try {
    $result = $apiInstance->publishCommonDataset($dataset_name, $workspace_id, $dtable_name, $table_name, $view_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->publishCommonDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_name** | **string**| The name of the common dataset. | [optional] |
| **workspace_id** | **string**| The workspace ID where your base is. | [optional] |
| **dtable_name** | **string**| The name of the base. | [optional] |
| **table_name** | **string**| The name of the table. | [optional] |
| **view_name** | **string**| The name of the view | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `renameCommonDataset()`

```php
renameCommonDataset($dataset_id, $dataset_name): object
```

Rename Common Dataset

Use this request to rename a common dataset.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dataset_id = 5; // int | The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned `id` is what you need here.
$dataset_name = 'dataset_name_example'; // string | The name of the common dataset.

try {
    $result = $apiInstance->renameCommonDataset($dataset_id, $dataset_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->renameCommonDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **int**| The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned &#x60;id&#x60; is what you need here. | |
| **dataset_name** | **string**| The name of the common dataset. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `syncCommonDataset()`

```php
syncCommonDataset($dataset_id, $dst_dtable_uuid, $is_sync, $dst_table_id, $dst_view_id)
```

Sync Common Dataset

Common datasets do not automatically synchronize with the original view. Use this request regularly to keep your data up-to-date.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dataset_id = 5; // int | The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned `id` is what you need here.
$dst_dtable_uuid = 'dst_dtable_uuid_example'; // string | The UUID of the destination base.
$is_sync = True; // bool
$dst_table_id = 'dst_table_id_example'; // string
$dst_view_id = 'dst_view_id_example'; // string

try {
    $apiInstance->syncCommonDataset($dataset_id, $dst_dtable_uuid, $is_sync, $dst_table_id, $dst_view_id);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->syncCommonDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **int**| The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned &#x60;id&#x60; is what you need here. | |
| **dst_dtable_uuid** | **string**| The UUID of the destination base. | [optional] |
| **is_sync** | **bool**|  | [optional] |
| **dst_table_id** | **string**|  | [optional] |
| **dst_view_id** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth




## `updateCommonDatasetSync()`

```php
updateCommonDatasetSync($dataset_id, $update_common_dataset_sync_request): object
```

Update Common Dataset Sync

You can change the configuration of your common dataset's syncing with these params:    `is_sync_periodically`: Whether syncing should be carried out daily (`true` or `false`, required);  `dst_dtable_uuid`: The UUID of the base where you'd like this common dataset to sync to;  `dst_table_id`: The ID of the destination table.    Attention: This configuration update doesn't establish a new common dataset synchronization, but only can update existing common dataset connections.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\CommonDatasetApi(
    new GuzzleHttp\Client(),
    $config
);
$dataset_id = 5; // int | The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned `id` is what you need here.
$update_common_dataset_sync_request = new \SeaTable\Client\User\UpdateCommonDatasetSyncRequest(); // \SeaTable\Client\User\UpdateCommonDatasetSyncRequest

try {
    $result = $apiInstance->updateCommonDatasetSync($dataset_id, $update_common_dataset_sync_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonDatasetApi->updateCommonDatasetSync: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **int**| The ID of the common dataset. When you e.g. publish a common dataset from a view, the returned &#x60;id&#x60; is what you need here. | |
| **update_common_dataset_sync_request** | [**\SeaTable\Client\User\UpdateCommonDatasetSyncRequest**](../Model/UpdateCommonDatasetSyncRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



