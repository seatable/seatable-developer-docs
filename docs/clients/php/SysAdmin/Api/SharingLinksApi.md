# SeaTable\Client\SharingLinksApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteBaseExternalLink()**](SharingLinksApi.md#deleteBaseExternalLink) | **DELETE** /api/v2.1/admin/external-links/{external_link_token}/ | Delete Base External Link |
| [**deleteViewExternalLink()**](SharingLinksApi.md#deleteViewExternalLink) | **DELETE** /api/v2.1/admin/view-external-links/{view_external_link_token}/ | Delete View External Link |
| [**listBaseExternalLinks()**](SharingLinksApi.md#listBaseExternalLinks) | **GET** /api/v2.1/admin/dtable/{base_id}/external-links/ | List Base External Links |
| [**listExternalLinks()**](SharingLinksApi.md#listExternalLinks) | **GET** /api/v2.1/admin/external-links/ | List External Links |
| [**listViewExternalLinks()**](SharingLinksApi.md#listViewExternalLinks) | **GET** /api/v2.1/admin/view-external-links/ | List View External Links |


## `deleteBaseExternalLink()`

```php
deleteBaseExternalLink($external_link_token): object
```

Delete Base External Link

A base external link can be deleted by its token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$external_link_token = fleischkaesebroetchen; // string

try {
    $result = $apiInstance->deleteBaseExternalLink($external_link_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->deleteBaseExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **external_link_token** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteViewExternalLink()`

```php
deleteViewExternalLink($view_external_link_token): object
```

Delete View External Link

Delete a view external link with its token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$view_external_link_token = 1f0447eab4df4343ab6d; // string

try {
    $result = $apiInstance->deleteViewExternalLink($view_external_link_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->deleteViewExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **view_external_link_token** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listBaseExternalLinks()`

```php
listBaseExternalLinks($base_id): object
```

List Base External Links

List all the external links and view external links of a base. For this request, you'll need the base's `base_id`, which is to be distinguished from the base's `base_uuid`. You can retrieve a base's `base_id` with the API request e.g. [List User's Bases](/reference/list-users-bases).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$base_id = base_id; // string | The id of the base. This is not the base_uuid.

try {
    $result = $apiInstance->listBaseExternalLinks($base_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->listBaseExternalLinks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_id** | **string**| The id of the base. This is not the base_uuid. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listExternalLinks()`

```php
listExternalLinks($page, $per_page): object
```

List External Links

List all the base external links generated in the system.  In the returned objects, you can see the creator of the links, and how many times these links have been viewed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listExternalLinks($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->listExternalLinks: ', $e->getMessage(), PHP_EOL;
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

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listViewExternalLinks()`

```php
listViewExternalLinks(): object
```

List View External Links

Use this request to list all the view external links generated in the current system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listViewExternalLinks();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->listViewExternalLinks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


