# SeaTable\Client\NotificationsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteInvalidNotifications()**](NotificationsApi.md#deleteInvalidNotifications) | **DELETE** /api/v2.1/admin/invalid-notification-rules/ | Delete Invalid Notifications |
| [**deleteNotificationRule()**](NotificationsApi.md#deleteNotificationRule) | **DELETE** /api/v2.1/admin/notification-rules/{notification_rule_id}/ | Delete Notification |
| [**listInvalidNotifications()**](NotificationsApi.md#listInvalidNotifications) | **GET** /api/v2.1/admin/invalid-notification-rules/ | List Invalid Notifications |
| [**listNotificationRules()**](NotificationsApi.md#listNotificationRules) | **GET** /api/v2.1/admin/notification-rules/ | List Notification Rules |


## `deleteInvalidNotifications()`

```php
deleteInvalidNotifications(): object
```

Delete Invalid Notifications

Delete all the notification rules that are invalid.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->deleteInvalidNotifications();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->deleteInvalidNotifications: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteNotificationRule()`

```php
deleteNotificationRule($notification_rule_id): object
```

Delete Notification

Delete a notification rule by its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$notification_rule_id = 2; // int

try {
    $result = $apiInstance->deleteNotificationRule($notification_rule_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->deleteNotificationRule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **notification_rule_id** | **int**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listInvalidNotifications()`

```php
listInvalidNotifications($page, $per_page): object
```

List Invalid Notifications

The system can detect notification rules that are invalid. You can list all the invalid notification rules here.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listInvalidNotifications($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->listInvalidNotifications: ', $e->getMessage(), PHP_EOL;
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



## `listNotificationRules()`

```php
listNotificationRules($page, $per_page): object
```

List Notification Rules

List all the existing notification rules in the system. The returned `id` values are the IDs of each notification rule.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listNotificationRules($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->listNotificationRules: ', $e->getMessage(), PHP_EOL;
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


