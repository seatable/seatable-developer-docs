# SeaTable\Client\PluginsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addPlugin()**](PluginsApi.md#addPlugin) | **POST** /api/v2.1/admin/dtable-system-plugins/ | Add Plugin |
| [**deletePlugin()**](PluginsApi.md#deletePlugin) | **DELETE** /api/v2.1/admin/dtable-system-plugins/{plugin_id}/ | Delete Plugin |
| [**listPlugins()**](PluginsApi.md#listPlugins) | **GET** /api/v2.1/admin/dtable-system-plugins/ | List Plugins |
| [**listPluginsInstallCount()**](PluginsApi.md#listPluginsInstallCount) | **GET** /api/v2.1/admin/plugins-install-count/ | List Plugins Install Count |
| [**updatePlugin()**](PluginsApi.md#updatePlugin) | **PUT** /api/v2.1/admin/dtable-system-plugins/{plugin_id}/ | Update Plugin |


## `addPlugin()`

```php
addPlugin($content_type, $plugin): object
```

Add Plugin

Add a plugin with a .zip file. This file could be retrieved from the internet, for example, from the [SeaTable Plugins Market](https://cloud.seatable.io/dtable/view-external-links/custom/plugins/).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\PluginsApi(
    new GuzzleHttp\Client(),
    $config
);
$content_type = multipart/form-data;; // string
$plugin = "/path/to/file.txt"; // \SplFileObject | Path and file name to the plugin file.

try {
    $result = $apiInstance->addPlugin($content_type, $plugin);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PluginsApi->addPlugin: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **content_type** | **string**|  | [optional] |
| **plugin** | **\SplFileObject****\SplFileObject**| Path and file name to the plugin file. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deletePlugin()`

```php
deletePlugin($plugin_id): object
```

Delete Plugin

Delete a plugin via its ID (retrieved from the call [List Plugins](/reference/list-plugins)).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\PluginsApi(
    new GuzzleHttp\Client(),
    $config
);
$plugin_id = 5; // int

try {
    $result = $apiInstance->deletePlugin($plugin_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PluginsApi->deletePlugin: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listPlugins()`

```php
listPlugins(): object
```

List Plugins

List all the plugins currently available in the system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\PluginsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listPlugins();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PluginsApi->listPlugins: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listPluginsInstallCount()`

```php
listPluginsInstallCount()
```

List Plugins Install Count

List plugins install count logs

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\PluginsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $apiInstance->listPluginsInstallCount();
} catch (Exception $e) {
    echo 'Exception when calling PluginsApi->listPluginsInstallCount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

AccountTokenAuth




## `updatePlugin()`

```php
updatePlugin($plugin_id, $content_type, $plugin): object
```

Update Plugin

Update a plugin via its ID (retrieved from the call [List Plugins](/reference/list-plugins)) with a .zip file.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\PluginsApi(
    new GuzzleHttp\Client(),
    $config
);
$plugin_id = 5; // int
$content_type = multipart/form-data; boundary; // string
$plugin = "/path/to/file.txt"; // \SplFileObject | Path and file name to the plugin file.

try {
    $result = $apiInstance->updatePlugin($plugin_id, $content_type, $plugin);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PluginsApi->updatePlugin: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_id** | **int**|  | |
| **content_type** | **string**|  | [optional] |
| **plugin** | **\SplFileObject****\SplFileObject**| Path and file name to the plugin file. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



