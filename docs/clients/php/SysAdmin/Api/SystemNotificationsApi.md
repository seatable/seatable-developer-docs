# SeaTable\Client\SystemNotificationsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addNotificationToUser()**](SystemNotificationsApi.md#addNotificationToUser) | **POST** /api/v2.1/admin/sys-user-notifications/ | Add Notification to User |
| [**deleteNotification()**](SystemNotificationsApi.md#deleteNotification) | **DELETE** /api/v2.1/admin/sys-user-notifications/{sys_notification_id}/ | Delete Notification |
| [**listNotifications()**](SystemNotificationsApi.md#listNotifications) | **GET** /api/v2.1/admin/sys-user-notifications/ | List Notifications |


## `addNotificationToUser()`

```php
addNotificationToUser($add_notification_to_user_request): object
```

Add Notification to User

Add a system notification to a specific user with their ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SystemNotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$add_notification_to_user_request = new \SeaTable\Client\SysAdmin/Model\AddNotificationToUserRequest(); // \SeaTable\Client\SysAdmin/Model\AddNotificationToUserRequest

try {
    $result = $apiInstance->addNotificationToUser($add_notification_to_user_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemNotificationsApi->addNotificationToUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **add_notification_to_user_request** | [**\SeaTable\Client\SysAdmin/Model\AddNotificationToUserRequest**](../Model/AddNotificationToUserRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteNotification()`

```php
deleteNotification($sys_notification_id): object
```

Delete Notification

Delete a system notification with its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SystemNotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$sys_notification_id = 1; // int

try {
    $result = $apiInstance->deleteNotification($sys_notification_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemNotificationsApi->deleteNotification: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sys_notification_id** | **int**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listNotifications()`

```php
listNotifications($page, $per_page): object
```

List Notifications

List all the system notifications sent to the users.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SystemNotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listNotifications($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemNotificationsApi->listNotifications: ', $e->getMessage(), PHP_EOL;
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


