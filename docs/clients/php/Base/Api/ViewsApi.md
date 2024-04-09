# SeaTable\Client\ViewsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createView()**](ViewsApi.md#createView) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/views/ | Create View |
| [**deleteView()**](ViewsApi.md#deleteView) | **DELETE** /dtable-server/api/v1/dtables/{base_uuid}/views/{view_name}/ | Delete View |
| [**getView()**](ViewsApi.md#getView) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/views/{view_name}/ | Get View |
| [**listViews()**](ViewsApi.md#listViews) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/views/ | List Views |
| [**updateView()**](ViewsApi.md#updateView) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/views/{view_name}/ | Update View |


## `createView()`

```php
createView($base_uuid, $table_name, $new_view): object
```

Create View

Create a new view in the current table. In the **request body**, use `name` for the name of the new view. After creating the new view, use the request [Update View](/reference/update-view) to further define your view.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ViewsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$table_name = Table1; // string | The name of the table.
$new_view = new \SeaTable\Client\Base\NewView(); // \SeaTable\Client\Base\NewView

try {
    $result = $apiInstance->createView($base_uuid, $table_name, $new_view);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ViewsApi->createView: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **table_name** | **string**| The name of the table. | |
| **new_view** | [**\SeaTable\Client\Base\NewView**](../Model/NewView.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `deleteView()`

```php
deleteView($base_uuid, $view_name, $table_name): object
```

Delete View

Delete a view by its name.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ViewsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$view_name = Default View; // string | The name of the view.
$table_name = Table1; // string | The name of the table.

try {
    $result = $apiInstance->deleteView($base_uuid, $view_name, $table_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ViewsApi->deleteView: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **view_name** | **string**| The name of the view. | |
| **table_name** | **string**| The name of the table. | |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `getView()`

```php
getView($base_uuid, $view_name, $table_name): object
```

Get View

Get the detailed settings of a view by its name.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ViewsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$view_name = Default View; // string | The name of the view.
$table_name = Table1; // string | The name of the table.

try {
    $result = $apiInstance->getView($base_uuid, $view_name, $table_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ViewsApi->getView: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **view_name** | **string**| The name of the view. | |
| **table_name** | **string**| The name of the table. | |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `listViews()`

```php
listViews($base_uuid, $table_name): object
```

List Views

List all the views and their settings in a table.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ViewsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$table_name = Table1; // string | The name of the table.

try {
    $result = $apiInstance->listViews($base_uuid, $table_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ViewsApi->listViews: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **table_name** | **string**| The name of the table. | |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `updateView()`

```php
updateView($base_uuid, $view_name, $table_name, $update_view): object
```

Update View

Change the settings of a current view by its name. All parameters are optional.   If you don't define a parameter, existing settings for this parameter will not be changed.  To remove existing filters, sortings or groups you have to send an empty object like this: `\"sorts\": [{}]`

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ViewsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$view_name = Default View; // string | The name of the view.
$table_name = Table1; // string | The name of the table.
$update_view = new \SeaTable\Client\Base\UpdateView(); // \SeaTable\Client\Base\UpdateView

try {
    $result = $apiInstance->updateView($base_uuid, $view_name, $table_name, $update_view);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ViewsApi->updateView: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **view_name** | **string**| The name of the view. | |
| **table_name** | **string**| The name of the table. | |
| **update_view** | [**\SeaTable\Client\Base\UpdateView**](../Model/UpdateView.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)


