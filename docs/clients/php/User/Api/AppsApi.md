# SeaTable\Client\AppsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**changeAppStatus()**](AppsApi.md#changeAppStatus) | **PUT** /api/v2.1/external-apps/{app_token}/status/ | Change App Status |
| [**importUsersToApp()**](AppsApi.md#importUsersToApp) | **POST** /api/v2.1/universal-apps/{app_token}/app-users/batch/ | Import Users to App |
| [**listAppInviteLinks()**](AppsApi.md#listAppInviteLinks) | **GET** /api/v2.1/universal-apps/{app_token}/invite-links/ | List App Invite Links |
| [**listApps()**](AppsApi.md#listApps) | **GET** /api/v2.1/universal-apps/ | List Apps |
| [**listUniversalAppUsers()**](AppsApi.md#listUniversalAppUsers) | **GET** /api/v2.1/universal-apps/{app_token}/app-users/ | List Universal App Users |


## `changeAppStatus()`

```php
changeAppStatus($app_token, $is_inactive)
```

Change App Status

Activate or deactivate a universal app. Pay attention that `true` means the app is inactive. `false` means the app is active.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AppsApi(
    new GuzzleHttp\Client(),
    $config
);
$app_token = 8254d58e-6a67-45ab-be37-87939d80e99f; // string
$is_inactive = new \SeaTable\Client\User\IsInactive(); // \SeaTable\Client\User\IsInactive

try {
    $apiInstance->changeAppStatus($app_token, $is_inactive);
} catch (Exception $e) {
    echo 'Exception when calling AppsApi->changeAppStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **app_token** | **string**|  | |
| **is_inactive** | [**\SeaTable\Client\User\IsInactive**](../Model/IsInactive.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `importUsersToApp()`

```php
importUsersToApp($app_token, $import_users_to_app_request)
```

Import Users to App

Hier muss noch eine Beschreibung ergänzt werden

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AppsApi(
    new GuzzleHttp\Client(),
    $config
);
$app_token = 8254d58e-6a67-45ab-be37-87939d80e99f; // string
$import_users_to_app_request = new \SeaTable\Client\User\ImportUsersToAppRequest(); // \SeaTable\Client\User\ImportUsersToAppRequest

try {
    $apiInstance->importUsersToApp($app_token, $import_users_to_app_request);
} catch (Exception $e) {
    echo 'Exception when calling AppsApi->importUsersToApp: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **app_token** | **string**|  | |
| **import_users_to_app_request** | [**\SeaTable\Client\User\ImportUsersToAppRequest**](../Model/ImportUsersToAppRequest.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listAppInviteLinks()`

```php
listAppInviteLinks($app_token)
```

List App Invite Links

Hier muss noch eine Beschreibung ergänzt werden

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AppsApi(
    new GuzzleHttp\Client(),
    $config
);
$app_token = 8254d58e-6a67-45ab-be37-87939d80e99f; // string

try {
    $apiInstance->listAppInviteLinks($app_token);
} catch (Exception $e) {
    echo 'Exception when calling AppsApi->listAppInviteLinks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **app_token** | **string**|  | |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listApps()`

```php
listApps()
```

List Apps

Hier muss noch eine Beschreibung ergänzt werden

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AppsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $apiInstance->listApps();
} catch (Exception $e) {
    echo 'Exception when calling AppsApi->listApps: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listUniversalAppUsers()`

```php
listUniversalAppUsers($app_token)
```

List Universal App Users

Hier muss noch eine Beschreibung ergänzt werden

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\AppsApi(
    new GuzzleHttp\Client(),
    $config
);
$app_token = 8254d58e-6a67-45ab-be37-87939d80e99f; // string

try {
    $apiInstance->listUniversalAppUsers($app_token);
} catch (Exception $e) {
    echo 'Exception when calling AppsApi->listUniversalAppUsers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **app_token** | **string**|  | |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


