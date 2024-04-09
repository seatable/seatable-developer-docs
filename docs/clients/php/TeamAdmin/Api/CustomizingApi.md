# SeaTable\Client\CustomizingApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteTeamLogo()**](CustomizingApi.md#deleteTeamLogo) | **DELETE** /api/v2.1/org/{org_id}/admin/org-logo/ | Delete Team Logo |
| [**getTeamLogo()**](CustomizingApi.md#getTeamLogo) | **GET** /api/v2.1/org/{org_id}/admin/org-logo/ | Get Team Logo |
| [**updateTeamLogo()**](CustomizingApi.md#updateTeamLogo) | **POST** /api/v2.1/org/{org_id}/admin/org-logo/ | Update Team Logo |


## `deleteTeamLogo()`

```php
deleteTeamLogo($org_id)
```

Delete Team Logo

Restore the team logo to SeaTable's original default by removing the current logo.\"

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\CustomizingApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $apiInstance->deleteTeamLogo($org_id);
} catch (Exception $e) {
    echo 'Exception when calling CustomizingApi->deleteTeamLogo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth




## `getTeamLogo()`

```php
getTeamLogo($org_id)
```

Get Team Logo

Get the path to the custom team logo.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\CustomizingApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $apiInstance->getTeamLogo($org_id);
} catch (Exception $e) {
    echo 'Exception when calling CustomizingApi->getTeamLogo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth




## `updateTeamLogo()`

```php
updateTeamLogo($org_id, $file)
```

Update Team Logo

Replace the current team logo by uploading a new one.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\CustomizingApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$file = "/path/to/file.txt"; // \SplFileObject | The image you'd like to upload from your local drive. Only .jpg, .jpeg, .gif or .png are allowed.

try {
    $apiInstance->updateTeamLogo($org_id, $file);
} catch (Exception $e) {
    echo 'Exception when calling CustomizingApi->updateTeamLogo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **file** | **\SplFileObject****\SplFileObject**| The image you&#39;d like to upload from your local drive. Only .jpg, .jpeg, .gif or .png are allowed. | [optional] |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth



