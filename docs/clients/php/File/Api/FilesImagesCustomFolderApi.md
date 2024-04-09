# SeaTable\Client\FilesImagesCustomFolderApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getCustomDownloadLink()**](FilesImagesCustomFolderApi.md#getCustomDownloadLink) | **GET** /api/v2.1/dtable/custom/app-download-link | Get Download Link |
| [**getCustomFileMetadata()**](FilesImagesCustomFolderApi.md#getCustomFileMetadata) | **GET** /api/v2.1/dtable/custom/app-asset-file/ | Get File Metadata |
| [**getCustomFiles()**](FilesImagesCustomFolderApi.md#getCustomFiles) | **GET** /api/v2.1/dtable/custom/app-asset-dir/ | Get Files from Folder |
| [**getCustomUploadLink()**](FilesImagesCustomFolderApi.md#getCustomUploadLink) | **GET** /api/v2.1/dtable/custom/app-upload-link/ | Get Upload Link |


## `getCustomDownloadLink()`

```php
getCustomDownloadLink($path): object
```

Get Download Link

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: ApiTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\File\FilesImagesCustomFolderApi(
    new GuzzleHttp\Client(),
    $config
);
$path = /supplierOne/b374.pdf; // string | Path and name of the file in the custom folder

try {
    $result = $apiInstance->getCustomDownloadLink($path);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilesImagesCustomFolderApi->getCustomDownloadLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **path** | **string**| Path and name of the file in the custom folder | |

### Return type

**object**

### Authorization

[ApiTokenAuth](../../README.md#ApiTokenAuth)



## `getCustomFileMetadata()`

```php
getCustomFileMetadata($path, $name): object
```

Get File Metadata

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: ApiTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\File\FilesImagesCustomFolderApi(
    new GuzzleHttp\Client(),
    $config
);
$path = /; // string | Path of the custom folder
$name = b374.pdf; // string | Name of the file in the custom folder

try {
    $result = $apiInstance->getCustomFileMetadata($path, $name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilesImagesCustomFolderApi->getCustomFileMetadata: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **path** | **string**| Path of the custom folder | |
| **name** | **string**| Name of the file in the custom folder | |

### Return type

**object**

### Authorization

[ApiTokenAuth](../../README.md#ApiTokenAuth)



## `getCustomFiles()`

```php
getCustomFiles($path): object
```

Get Files from Folder

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: ApiTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\File\FilesImagesCustomFolderApi(
    new GuzzleHttp\Client(),
    $config
);
$path = /; // string | Path of the custom folder

try {
    $result = $apiInstance->getCustomFiles($path);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilesImagesCustomFolderApi->getCustomFiles: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **path** | **string**| Path of the custom folder | |

### Return type

**object**

### Authorization

[ApiTokenAuth](../../README.md#ApiTokenAuth)



## `getCustomUploadLink()`

```php
getCustomUploadLink($path): object
```

Get Upload Link

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: ApiTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\File\FilesImagesCustomFolderApi(
    new GuzzleHttp\Client(),
    $config
);
$path = /; // string | Path of the custom folder

try {
    $result = $apiInstance->getCustomUploadLink($path);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilesImagesCustomFolderApi->getCustomUploadLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **path** | **string**| Path of the custom folder | |

### Return type

**object**

### Authorization

[ApiTokenAuth](../../README.md#ApiTokenAuth)


