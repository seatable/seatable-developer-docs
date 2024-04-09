# SeaTable\Client\ActivitiesLogsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listTeamLogins()**](ActivitiesLogsApi.md#listTeamLogins) | **GET** /api/v2.1/org/{org_id}/admin/login-logs/ | List Team Logins |
| [**listTeamOperationLog()**](ActivitiesLogsApi.md#listTeamOperationLog) | **GET** /api/v2.1/org/{org_id}/admin/admin-logs/ | List Team Operations |
| [**listUserLogins()**](ActivitiesLogsApi.md#listUserLogins) | **GET** /api/v2.1/org/{org_id}/admin/login-logs/{user_id} | List User Logins |


## `listTeamLogins()`

```php
listTeamLogins($org_id, $page, $per_page)
```

List Team Logins

Retrieves the login activities of all team members.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\ActivitiesLogsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $apiInstance->listTeamLogins($org_id, $page, $per_page);
} catch (Exception $e) {
    echo 'Exception when calling ActivitiesLogsApi->listTeamLogins: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listTeamOperationLog()`

```php
listTeamOperationLog($org_id, $page, $per_page)
```

List Team Operations

Retrieves the operation log of all team members.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\ActivitiesLogsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $apiInstance->listTeamOperationLog($org_id, $page, $per_page);
} catch (Exception $e) {
    echo 'Exception when calling ActivitiesLogsApi->listTeamOperationLog: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listUserLogins()`

```php
listUserLogins($org_id, $user_id, $page, $per_page)
```

List User Logins

Returns the login activities of one specific team member.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\ActivitiesLogsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$user_id = 123456789f1e4c8d8e1c31415867317c@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $apiInstance->listUserLogins($org_id, $user_id, $page, $per_page);
} catch (Exception $e) {
    echo 'Exception when calling ActivitiesLogsApi->listUserLogins: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


