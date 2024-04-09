# SeaTable\Client\NotificationsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addNotificationRule()**](NotificationsApi.md#addNotificationRule) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/notification-rules/ | Add Notification Rule |
| [**deleteNotificationRule()**](NotificationsApi.md#deleteNotificationRule) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/notification-rules/{notification_rule_id}/ | Delete Notification Rule |
| [**listNotificationRules()**](NotificationsApi.md#listNotificationRules) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/notification-rules/ | List Notification Rules |
| [**markNotificationAsSeen()**](NotificationsApi.md#markNotificationAsSeen) | **DELETE** /api/v2.1/notifications/ | Mark Notifications As Seen |
| [**updateNotificationRule()**](NotificationsApi.md#updateNotificationRule) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/notification-rules/{notification_rule_id}/ | Update Notification Rule |


## `addNotificationRule()`

```php
addNotificationRule($workspace_id, $base_name, $body): object
```

Add Notification Rule

Use this request to add a new notification rule for a base.  **Input Parameters**  **workspace_id** _\\[int, required\\]_  > The ID of the workspace where the base is stored.  **base_name** _\\[string, required\\]_  > The name of the base.  **RuleData** _\\[JSON object, required\\]_  > In this JSON object, use the following params to define this notification rule: >  > **run_condition** _\\[enum(__`per_day`__,_ _`per_update`__), required\\]_ >  > > Define whether the action should be triggered by date or table update. For **Records near deadline**, use `per_day` and for **Records modified** and **Records meet specific conditions after modification**, use `per_update`. Details see below. >  > **trigger** _\\[JSON object, required\\]_ >  > > In this JSON object, define the trigger of the rule with the following params: > >  > > > **rule_name** _\\[string, required\\]_ > > >  > > > > The name of the rule. > > >  > > > **table_id** _\\[string, required\\]_ > > >  > > > > The ID of the table. > > >  > > > **view_id** _\\[string, required\\]_ > > >  > > > > The ID of the view. > > >  > > > **condition** _\\[enum(__`rows_modified`__,_ _`near_deadline`__,_ _`filters_satisfy`__), required\\]_ > > >  > > > > - For 'Records near deadline', use `per_day` in the **run_condition** param and `near_deadline` here. > > > > - For 'Records modified', use `per_update` in the **run_condition** param and `rows_modified` here. > > > > - For 'Records meet specific conditions after modification', use `per_update` in the **run_condition** param and `filters_satisfy` here. > >  > > For the case **Records near deadline**, when `run_condition` is `per_day` and `condition` is `near_deadline`, you'll define which date column to use as deadline dates, and optionally define how many days before and to which time of the day should the notification be sent: > >  > > > **date_column_name** _\\[string, required\\]_ > > >  > > > > For 'Records near deadline', give the name of the date column that contains the deadline dates. If left blank, the first date column in the table will be taken as deadline. > > >  > > > **alarm_days** _\\[int, optional\\]_ > > >  > > > > Use a number to define how many days before the deadline should the notification be triggered. > > >  > > > **notify_hour** _\\[int(0-23), optional\\]_ > > >  > > > > Specify to which hour of the day should the notification be sent. > >  > > For the case **Records modified**, when `run_condition` is `per_update` and `condition` is `rows_modified`, a notification is sent right away inside the base editor. If this notification is not read within two hours, it'll be sent via email, if the receiver has enabled email notification in their personal settings: > >  > > > There is no further trigger conditions necessary. > >  > > For the case **Records meet specific conditions after modification**, when `run_condition` is `per_update` and `condition` is `filters_satisfy`, you can define which fields to watch and set filters: > >  > > > **watch_all_columns** _\\[enum(`true`, `false`, optional, `true` by default)\\] > > >  > > > > Use `true` or leave this param blank, if you want all columns to be watched. > > >  > > > **column_keys** _\\[list, optional\\] > > >  > > > > When certain columns should be watched, use this list to include their keys, so only when there's modification in these columns, this notification rule will be triggered. > > >  > > > **filters** and **filter_conjunction** refer to the API Request **Base Operations > Rows >** **List Filtered Rows**. You can define filters for all the fields in the table as a combination to the watched fields. So that only when the filtered records in the watched fields are modified, will this notification rule be triggered. >  > **action** _\\[JSON object, required\\]_ >  > > In this JSON object, define the users to be notified with the following params: > >  > > > **type** _\\[enum(__`notify`__), optional\\]_ > > >  > > > > For the moment, there's only one option to notify the user. The `notify` value means a notification will be sent inside the base editor, and when this isn't read within 2 hours, it'll be sent via email to the user, if the user's email setting is activated. In the near future, SeaTable will provide the option to send emails directly to users even outside your organization by configuring an email sending service. > > >  > > > **users** _\\[list, optional\\]_ > > >  > > > > In this list, provide the users' IDs to be notified. Alternatively, use the `users_column_key` to automatically select users from a collaborator column. > > >  > > > **users_column_key** _\\[string, optional\\]_ > > >  > > > > Select users to be notified from a collaborator column by providing its key. > > >  > > > **default_msg** _\\[string, optional\\]_ > > >  > > > > Here you can write a short message to remind notified users why this notification is sent, for example \"The battery has to be changed in 2 days!\".

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$body = array('key' => new \stdClass); // object

try {
    $result = $apiInstance->addNotificationRule($workspace_id, $base_name, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->addNotificationRule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **body** | **object**|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteNotificationRule()`

```php
deleteNotificationRule($workspace_id, $base_name, $notification_rule_id): object
```

Delete Notification Rule

Delete an existing notification rule.  The `notification_rule_id` is the ID of the notification to be deleted. This can be retrieved by [List Notification Rules](/reference/get_api-v2-1-workspace-workspace-id-dtable-base-name-notification-rules-1) or can be seen when you [Add Base Notification Rule](/reference/post_api-v2-1-workspace-workspace-id-dtable-base-name-notification-rules-1).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$notification_rule_id = 1; // string

try {
    $result = $apiInstance->deleteNotificationRule($workspace_id, $base_name, $notification_rule_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->deleteNotificationRule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **notification_rule_id** | **string**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listNotificationRules()`

```php
listNotificationRules($workspace_id, $base_name): object
```

List Notification Rules

Use this request to list all the existing notification rules in the current base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listNotificationRules($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->listNotificationRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `markNotificationAsSeen()`

```php
markNotificationAsSeen(): object
```

Mark Notifications As Seen

Delete all notifications sent to the current user.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->markNotificationAsSeen();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->markNotificationAsSeen: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateNotificationRule()`

```php
updateNotificationRule($workspace_id, $base_name, $notification_rule_id, $update_notification_rule_request): object
```

Update Notification Rule

Update the params of an existing notification rule.  The `notification_rule_id` is the ID of the notification to be updated. This can be retrieved by [List Notification Rules](/reference/get_api-v2-1-workspace-workspace-id-dtable-base-name-notification-rules-1) or can be seen when you [Add Base Notification Rule](/reference/post_api-v2-1-workspace-workspace-id-dtable-base-name-notification-rules-1).  For the exact params that you can update, refer to the params list in the call [Add Base Notification Rule](/reference/post_api-v2-1-workspace-workspace-id-dtable-base-name-notification-rules-1).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\NotificationsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$notification_rule_id = 1; // string
$update_notification_rule_request = new \SeaTable\Client\User\UpdateNotificationRuleRequest(); // \SeaTable\Client\User\UpdateNotificationRuleRequest

try {
    $result = $apiInstance->updateNotificationRule($workspace_id, $base_name, $notification_rule_id, $update_notification_rule_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NotificationsApi->updateNotificationRule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **notification_rule_id** | **string**|  | |
| **update_notification_rule_request** | [**\SeaTable\Client\User\UpdateNotificationRuleRequest**](../Model/UpdateNotificationRuleRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



