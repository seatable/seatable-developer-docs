# SeaTable\Client\SystemNotificationsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listSystemNotifications()**](SystemNotificationsApi.md#listSystemNotifications) | **GET** /api/v2.1/sys-user-notifications/unseen/ | List System Notifications |
| [**markSystemNotificationsAsSeen()**](SystemNotificationsApi.md#markSystemNotificationsAsSeen) | **PUT** /api/v2.1/sys-user-notifications/{sys_notification_id}/seen/ | Mark System Notification As Seen |


## `listSystemNotifications()`

```php
listSystemNotifications(): object
```

List System Notifications

List all the notifications that are unseen by the users. A user can only mark a system notification as seen by clicking on the \"x\" to close it.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SystemNotificationsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listSystemNotifications();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemNotificationsApi->listSystemNotifications: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `markSystemNotificationsAsSeen()`

```php
markSystemNotificationsAsSeen($sys_notification_id): object
```

Mark System Notification As Seen

Mark a system notification as seen with its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SystemNotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$sys_notification_id = 1; // string | The id of the notification.

try {
    $result = $apiInstance->markSystemNotificationsAsSeen($sys_notification_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemNotificationsApi->markSystemNotificationsAsSeen: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sys_notification_id** | **string**| The id of the notification. | |

### Return type

**object**

### Authorization

AccountTokenAuth



