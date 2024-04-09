# SeaTable\Client\BaseTokenApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getBaseTokenWithAccountToken()**](BaseTokenApi.md#getBaseTokenWithAccountToken) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/access-token/ | Get Base-Token with Account-Token |
| [**getBaseTokenWithApiToken()**](BaseTokenApi.md#getBaseTokenWithApiToken) | **GET** /api/v2.1/dtable/app-access-token/ | Get Base-Token with API-Token |
| [**getBaseTokenWithExternLink()**](BaseTokenApi.md#getBaseTokenWithExternLink) | **GET** /api/v2.1/external-link-tokens/{external_link_token}/access-token/ | Get Base-Token with External-Link |


## `getBaseTokenWithAccountToken()`

```php
getBaseTokenWithAccountToken($workspace_id, $base_name): \SeaTable\Client\Auth\AccessToken
```

Get Base-Token with Account-Token

Generate a Base-Token using the user's Account-Token. The read/write permission depends on the user's access permissions to the base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer (Account-Token) authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Auth\BaseTokenApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang=auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used.
$base_name = My Projects; // string | The name of your base.

try {
    $result = $apiInstance->getBaseTokenWithAccountToken($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseTokenApi->getBaseTokenWithAccountToken: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang&#x3D;auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used. | |
| **base_name** | **string**| The name of your base. | |

### Return type

[**\SeaTable\Client\Auth\AccessToken**](../Model/AccessToken.md)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `getBaseTokenWithApiToken()`

```php
getBaseTokenWithApiToken(): object
```

Get Base-Token with API-Token

Generate a Base-Token with an API-Token. The API-Token grants either read or write permission to this base, depending of the permission of the API-Token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer (API-Token) authorization: ApiTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Auth\BaseTokenApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getBaseTokenWithApiToken();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseTokenApi->getBaseTokenWithApiToken: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiTokenAuth](../../README.md#ApiTokenAuth)



## `getBaseTokenWithExternLink()`

```php
getBaseTokenWithExternLink($external_link_token): \SeaTable\Client\Auth\AccessToken
```

Get Base-Token with External-Link

Generate a Base-Token from an external link to this base. Because external links always grant read-only permissions, the Base-Token generated from a external link will only grant read permissions to the base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new SeaTable\Client\Auth\BaseTokenApi(
    new GuzzleHttp\Client()
);
$external_link_token = c41cef71f5094827a786; // string | The random string from the external link. Eg:  - If the external link is https://cloud.seatable.io/dtable/external-links/c41cef71f5094827a786, the link token is *c41cef71f5094827a786*. - If the external link is a custom link like https://cloud.seatable.io/dtable/external-links/custom/my-personal-link, the link token is only *my-personal-link*.

try {
    $result = $apiInstance->getBaseTokenWithExternLink($external_link_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseTokenApi->getBaseTokenWithExternLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **external_link_token** | **string**| The random string from the external link. Eg:  - If the external link is https://cloud.seatable.io/dtable/external-links/c41cef71f5094827a786, the link token is *c41cef71f5094827a786*. - If the external link is a custom link like https://cloud.seatable.io/dtable/external-links/custom/my-personal-link, the link token is only *my-personal-link*. | |

### Return type

[**\SeaTable\Client\Auth\AccessToken**](../Model/AccessToken.md)

### Authorization

No authorization required


