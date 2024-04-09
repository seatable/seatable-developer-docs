# SeaTable\Client\AttachmentApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**checkIfAssetExists()**](AttachmentApi.md#checkIfAssetExists) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/asset-exists/ | Check If Asset Exists |
| [**deleteBaseAsset()**](AttachmentApi.md#deleteBaseAsset) | **DELETE** /api/v2.1/dtable-asset/{base_uuid}/ | Delete Base Asset |
| [**deleteBaseAssets()**](AttachmentApi.md#deleteBaseAssets) | **DELETE** /api/v2.1/dtable-asset/{base_uuid}/batch-delete-assets/ | Delete Base Assets |
| [**getBaseAttachmentUploadLink()**](AttachmentApi.md#getBaseAttachmentUploadLink) | **GET** /api/v2.1/workspace/{workspace_id}/dtable-asset-upload-link/ | Get Base Attachment Upload Link |
| [**listBaseAssets()**](AttachmentApi.md#listBaseAssets) | **GET** /api/v2.1/dtable-asset/{base_uuid}/ | List Base Asset Directories And Files |
| [**listRecentlyUploadedFiles()**](AttachmentApi.md#listRecentlyUploadedFiles) | **GET** /api/v2.1/dtable-recent-asset/{base_uuid}/ | List Recently Uploaded Files |
| [**renameBaseAsset()**](AttachmentApi.md#renameBaseAsset) | **POST** /api/v2.1/dtable-asset/{base_uuid}/rename/ | Rename Base Asset |


## `checkIfAssetExists()`

```php
checkIfAssetExists($workspace_id, $base_name, $path): object
```

Check If Asset Exists

Check if a certain asset exists. The returned `is_exist` value confirms the existence (`true`).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AttachmentApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$path = /files/2021-01/abc.jpg; // string

try {
    $result = $apiInstance->checkIfAssetExists($workspace_id, $base_name, $path);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttachmentApi->checkIfAssetExists: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **path** | **string**|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteBaseAsset()`

```php
deleteBaseAsset($base_uuid, $path): object
```

Delete Base Asset

Delete a directory, a file or an image from a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AttachmentApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$path = /files/2021-01/abc.jpg; // string

try {
    $result = $apiInstance->deleteBaseAsset($base_uuid, $path);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttachmentApi->deleteBaseAsset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **path** | **string**|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteBaseAssets()`

```php
deleteBaseAssets($base_uuid): object
```

Delete Base Assets

Delete base assets/attachments by batch. In the request body: - `parent_path` is the parent path in which the objects are in, that you would like to delete. They could be files, or folders. - `asset_names` is an array of objects you'd like to delete in this path. You can list folders or file names here.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AttachmentApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->deleteBaseAssets($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttachmentApi->deleteBaseAssets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `getBaseAttachmentUploadLink()`

```php
getBaseAttachmentUploadLink($workspace_id, $base_name): object
```

Get Base Attachment Upload Link

Get the attachment upload link to a base. Images should be uploaded to the `img_relative_path`, all other files should be uploaded to the `file_relative_path`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AttachmentApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base

try {
    $result = $apiInstance->getBaseAttachmentUploadLink($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttachmentApi->getBaseAttachmentUploadLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listBaseAssets()`

```php
listBaseAssets($base_uuid, $parent_dir): object
```

List Base Asset Directories And Files

List all the directories, files and images in the given path in a base.  The returned `is_file` value indicates if this object is a file (`true`) or a folder (`false`).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AttachmentApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$parent_dir = /; // string

try {
    $result = $apiInstance->listBaseAssets($base_uuid, $parent_dir);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttachmentApi->listBaseAssets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **parent_dir** | **string**|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listRecentlyUploadedFiles()`

```php
listRecentlyUploadedFiles($base_uuid, $months): object
```

List Recently Uploaded Files

Use this request to list off the files uploaded to the current base in the past months.  If there is no upload in a certain month, an empty list is returned for that month. See example for details.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AttachmentApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$months = 3; // int | Number of months to list file upload history. Optional. 2 by default.

try {
    $result = $apiInstance->listRecentlyUploadedFiles($base_uuid, $months);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttachmentApi->listRecentlyUploadedFiles: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **months** | **int**| Number of months to list file upload history. Optional. 2 by default. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `renameBaseAsset()`

```php
renameBaseAsset($base_uuid, $path, $new_name): object
```

Rename Base Asset

Once you have the exact path and filename of an asset, you can use this request to rename it. In the request body:    `path` is the exact path and filename of your asset;  `new_name` is the new filename of your asset without path.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AttachmentApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$path = 'path_example'; // string
$new_name = 'new_name_example'; // string

try {
    $result = $apiInstance->renameBaseAsset($base_uuid, $path, $new_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttachmentApi->renameBaseAsset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **path** | **string**|  | [optional] |
| **new_name** | **string**|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


