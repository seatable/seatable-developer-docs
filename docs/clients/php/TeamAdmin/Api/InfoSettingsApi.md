# SeaTable\Client\InfoSettingsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getTeamInfo()**](InfoSettingsApi.md#getTeamInfo) | **GET** /api/v2.1/org/admin/info/ | Get Team Info |
| [**getTeamSettings()**](InfoSettingsApi.md#getTeamSettings) | **GET** /api/v2.1/org/admin/settings/ | Get Team Settings |
| [**updateTeam()**](InfoSettingsApi.md#updateTeam) | **PUT** /api/v2.1/org/admin/info/ | Update Team |
| [**updateTeamSettings()**](InfoSettingsApi.md#updateTeamSettings) | **PUT** /api/v2.1/org/admin/settings/ | Update Team Settings |


## `getTeamInfo()`

```php
getTeamInfo(): object
```

Get Team Info

Get the basic information (e.g. ID, name, storage quota etc. see example response for details) of your team (organization).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\InfoSettingsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getTeamInfo();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InfoSettingsApi->getTeamInfo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `getTeamSettings()`

```php
getTeamSettings(): object
```

Get Team Settings

List the current organization settings.  **Return Values**  `enable_force_2fa`: if the 2-factor-authentication is forced (`true` or `false`).  `enable_new_user_email`: if newly added users will get a system email (`true` or `false`).  `enable_external_user_access_invite_link`: if external users can access bases via invite links (`true` or `false`).  `enable_member_modify_name`: if members are allowed to change their names (`true` or `false`).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\InfoSettingsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getTeamSettings();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InfoSettingsApi->getTeamSettings: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateTeam()`

```php
updateTeam($new_org_name): object
```

Update Team

Update the infos (e.g. name) of the organization

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\InfoSettingsApi(
    new GuzzleHttp\Client(),
    $config
);
$new_org_name = 'new_org_name_example'; // string | The new name of your team.

try {
    $result = $apiInstance->updateTeam($new_org_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InfoSettingsApi->updateTeam: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **new_org_name** | **string**| The new name of your team. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateTeamSettings()`

```php
updateTeamSettings($enable_force_2fa, $enable_new_user_email, $enable_external_user_access_invite_link, $enable_member_modify_name): object
```

Update Team Settings

Update the settings of the organization.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\InfoSettingsApi(
    new GuzzleHttp\Client(),
    $config
);
$enable_force_2fa = True; // bool | if the 2-factor-authentication is forced (`true` or `false`).
$enable_new_user_email = True; // bool | if newly added users will get a system email (`true` or `false`).
$enable_external_user_access_invite_link = True; // bool | if external users can access bases via invite links (`true` or `false`).
$enable_member_modify_name = True; // bool | if members are allowed to change their names (`true` or `false`).

try {
    $result = $apiInstance->updateTeamSettings($enable_force_2fa, $enable_new_user_email, $enable_external_user_access_invite_link, $enable_member_modify_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InfoSettingsApi->updateTeamSettings: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **enable_force_2fa** | **bool**| if the 2-factor-authentication is forced (&#x60;true&#x60; or &#x60;false&#x60;). | [optional] |
| **enable_new_user_email** | **bool**| if newly added users will get a system email (&#x60;true&#x60; or &#x60;false&#x60;). | [optional] |
| **enable_external_user_access_invite_link** | **bool**| if external users can access bases via invite links (&#x60;true&#x60; or &#x60;false&#x60;). | [optional] |
| **enable_member_modify_name** | **bool**| if members are allowed to change their names (&#x60;true&#x60; or &#x60;false&#x60;). | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



