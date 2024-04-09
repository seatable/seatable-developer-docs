# SeaTable\Client\APITokenApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createApiToken()**](APITokenApi.md#createApiToken) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/api-tokens/ | Create API-Token |
| [**createTempApiToken()**](APITokenApi.md#createTempApiToken) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/temp-api-token/ | Create API-Token (temporary) |
| [**deleteApiToken()**](APITokenApi.md#deleteApiToken) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/api-tokens/{app_name}/ | Delete API-Token |
| [**listApiTokens()**](APITokenApi.md#listApiTokens) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/api-tokens/ | List API-Tokens |
| [**updateApiToken()**](APITokenApi.md#updateApiToken) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/api-tokens/{app_name}/ | Update API-Token |


## `createApiToken()`

```php
createApiToken($workspace_id, $base_name, $app_name, $permission): \SeaTable\Client\Auth\ApiToken
```

Create API-Token

Create an *API-Token* for a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer (Account-Token) authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Auth\APITokenApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang=auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used.
$base_name = My Projects; // string | The name of your base.
$app_name = 'app_name_example'; // string | The name of your app. Every API-Token has a name to identify the purpose. The name of the app must be unique for every base.
$permission = new \SeaTable\Client\Auth\AuthenticationPermission(); // \SeaTable\Client\Auth\AuthenticationPermission

try {
    $result = $apiInstance->createApiToken($workspace_id, $base_name, $app_name, $permission);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling APITokenApi->createApiToken: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang&#x3D;auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used. | |
| **base_name** | **string**| The name of your base. | |
| **app_name** | **string**| The name of your app. Every API-Token has a name to identify the purpose. The name of the app must be unique for every base. | |
| **permission** | [**\SeaTable\Client\Auth\AuthenticationPermission**](../Model/AuthenticationPermission.md)|  | |

### Return type

[**\SeaTable\Client\Auth\ApiToken**](../Model/ApiToken.md)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `createTempApiToken()`

```php
createTempApiToken($workspace_id, $base_name): \SeaTable\Client\Auth\ApiTokenTemporary
```

Create API-Token (temporary)

Create a *temporary API-Token* for a base that expires after one hour.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer (Account-Token) authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Auth\APITokenApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang=auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used.
$base_name = My Projects; // string | The name of your base.

try {
    $result = $apiInstance->createTempApiToken($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling APITokenApi->createTempApiToken: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang&#x3D;auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used. | |
| **base_name** | **string**| The name of your base. | |

### Return type

[**\SeaTable\Client\Auth\ApiTokenTemporary**](../Model/ApiTokenTemporary.md)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteApiToken()`

```php
deleteApiToken($workspace_id, $base_name, $app_name): object
```

Delete API-Token

Delete one specific API token from a base. The token is identified by his *app_name*.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer (Account-Token) authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Auth\APITokenApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang=auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used.
$base_name = My Projects; // string | The name of your base.
$app_name = My App; // string | The name of your app. Every API-Token has a name to identify the purpose. The name of the app must be unique for every base.

try {
    $result = $apiInstance->deleteApiToken($workspace_id, $base_name, $app_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling APITokenApi->deleteApiToken: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang&#x3D;auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used. | |
| **base_name** | **string**| The name of your base. | |
| **app_name** | **string**| The name of your app. Every API-Token has a name to identify the purpose. The name of the app must be unique for every base. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listApiTokens()`

```php
listApiTokens($workspace_id, $base_name): \SeaTable\Client\Auth\ApiTokenList
```

List API-Tokens

List all *API-Tokens* of a base with additional informations like permission, generation date and last access time.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer (Account-Token) authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Auth\APITokenApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang=auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used.
$base_name = My Projects; // string | The name of your base.

try {
    $result = $apiInstance->listApiTokens($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling APITokenApi->listApiTokens: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang&#x3D;auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used. | |
| **base_name** | **string**| The name of your base. | |

### Return type

[**\SeaTable\Client\Auth\ApiTokenList**](../Model/ApiTokenList.md)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `updateApiToken()`

```php
updateApiToken($workspace_id, $base_name, $app_name, $permission): \SeaTable\Client\Auth\ApiToken
```

Update API-Token

Update the permission of an existing *API-Token*.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer (Account-Token) authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Auth\APITokenApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang=auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used.
$base_name = My Projects; // string | The name of your base.
$app_name = My App; // string | The name of your app. Every API-Token has a name to identify the purpose. The name of the app must be unique for every base.
$permission = new \SeaTable\Client\Auth\AuthenticationPermission(); // \SeaTable\Client\Auth\AuthenticationPermission

try {
    $result = $apiInstance->updateApiToken($workspace_id, $base_name, $app_name, $permission);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling APITokenApi->updateApiToken: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| The id of the workspace. For an explanation how to get the *workspace_id*, check out this [help-article](https://seatable.io/docs/arbeiten-mit-gruppen/workspace-id-einer-gruppe-ermitteln/?lang&#x3D;auto).  Alternatively the API endpoint [get metadata](/reference/get-metadata) can be used. | |
| **base_name** | **string**| The name of your base. | |
| **app_name** | **string**| The name of your app. Every API-Token has a name to identify the purpose. The name of the app must be unique for every base. | |
| **permission** | [**\SeaTable\Client\Auth\AuthenticationPermission**](../Model/AuthenticationPermission.md)|  | |

### Return type

[**\SeaTable\Client\Auth\ApiToken**](../Model/ApiToken.md)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


