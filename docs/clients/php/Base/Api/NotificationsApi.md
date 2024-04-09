# SeaTable\Client\NotificationsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteBaseNotifications()**](NotificationsApi.md#deleteBaseNotifications) | **DELETE** /dtable-server/api/v1/dtables/{base_uuid}/notifications/ | Delete Base Notifications |
| [**listBaseNotifications()**](NotificationsApi.md#listBaseNotifications) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/notifications/ | List Base Notifications |
| [**markBaseNotificationAsSeen()**](NotificationsApi.md#markBaseNotificationAsSeen) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/notifications/{notification_id}/ | Mark Notification Read/Unread |
| [**markBaseNotificationsAsSeen()**](NotificationsApi.md#markBaseNotificationsAsSeen) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/notifications/ | Mark Base Notifications as seen |


## `deleteBaseNotifications()`

```php
deleteBaseNotifications($base_uuid): object
```

Delete Base Notifications

Delete all the notifications in the current base irrevocably.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->deleteBaseNotifications($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->deleteBaseNotifications: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

BaseTokenAuth




## `listBaseNotifications()`

```php
listBaseNotifications($base_uuid): object
```

List Base Notifications

List all the notifications, read or unread, in a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->listBaseNotifications($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->listBaseNotifications: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

BaseTokenAuth




## `markBaseNotificationAsSeen()`

```php
markBaseNotificationAsSeen($base_uuid, $notification_id, $seen): object
```

Mark Notification Read/Unread

Mark a specific notification as read or unread.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$notification_id = 1; // int | The id of the notification.
$seen = True; // bool | `true` to mark as \\\"seen\\\" and `false` as \\\"unseen\\\".

try {
    $result = $apiInstance->markBaseNotificationAsSeen($base_uuid, $notification_id, $seen);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->markBaseNotificationAsSeen: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **notification_id** | **int**| The id of the notification. | |
| **seen** | **bool**| &#x60;true&#x60; to mark as \\\&quot;seen\\\&quot; and &#x60;false&#x60; as \\\&quot;unseen\\\&quot;. | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `markBaseNotificationsAsSeen()`

```php
markBaseNotificationsAsSeen($base_uuid, $seen): object
```

Mark Base Notifications as seen

Use this request to mark all the notifications as read.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$seen = True; // bool | true or false for read or unread. Otherwise invalid.

try {
    $result = $apiInstance->markBaseNotificationsAsSeen($base_uuid, $seen);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->markBaseNotificationsAsSeen: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **seen** | **bool**| true or false for read or unread. Otherwise invalid. | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth



