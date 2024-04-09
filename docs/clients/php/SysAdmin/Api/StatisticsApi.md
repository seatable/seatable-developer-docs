# SeaTable\Client\StatisticsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getActiveUsersPerDay()**](StatisticsApi.md#getActiveUsersPerDay) | **GET** /api/v2.1/admin/statistics/active-users/ | Get Active Users (per Day) |
| [**getAutomationRules()**](StatisticsApi.md#getAutomationRules) | **GET** /api/v2.1/admin/statistics/auto-rules/ | Get Automation Rules |
| [**getExternalApps()**](StatisticsApi.md#getExternalApps) | **GET** /api/v2.1/admin/statistics/external-apps/ | Get External Apps |
| [**getScriptRunningCountByUser()**](StatisticsApi.md#getScriptRunningCountByUser) | **GET** /api/v2.1/admin/statistics/scripts-running/ | Get Script Running Count by User |
| [**listActiveUsersByDay()**](StatisticsApi.md#listActiveUsersByDay) | **GET** /api/v2.1/admin/daily-active-users/ | List Active Users (one Day) |
| [**listScriptTasks()**](StatisticsApi.md#listScriptTasks) | **GET** /api/v2.1/admin/scripts-tasks/ | List Scripts Tasks |


## `getActiveUsersPerDay()`

```php
getActiveUsersPerDay($start, $end): object
```

Get Active Users (per Day)

List the number of daily active users in a given period of time.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\StatisticsApi(
    new GuzzleHttp\Client(),
    $config
);
$start = 2021-02-21+00:00:00; // string | Starting time of the statistics in ISO format like in the example. Required.
$end = 2021-02-24+00:00:00; // string | Ending time of the statistics in ISO format like in the example. Required.

try {
    $result = $apiInstance->getActiveUsersPerDay($start, $end);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StatisticsApi->getActiveUsersPerDay: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **start** | **string**| Starting time of the statistics in ISO format like in the example. Required. | [optional] |
| **end** | **string**| Ending time of the statistics in ISO format like in the example. Required. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `getAutomationRules()`

```php
getAutomationRules($is_user, $month): object
```

Get Automation Rules

The system documents automation rules by single users (users who are not in any teams) or by teams. In most cases, especially on cloud.seatable.io, there're no such scenario that a single user could exist, so the usage of the param `is_user` as `true` is seldom. As this API request is developed in SeaTable 2.4.2 which came out in September 2021, automation rules statistics before September 2021 could not be correctly summarized with this call.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\StatisticsApi(
    new GuzzleHttp\Client(),
    $config
);
$is_user = false; // bool | Whether you'd like to list automation rules triggered by single users who are not in any teams (`true`) or by teams (`false`).  The usage of `true` here is seldom meaningful for cloud.seatable.io as all the users in the SeaTable Cloud are team users.
$month = 202109; // int | For which month you'd like to list the statistics in the format of YYYYMM. Statistics of automation rules before 202109 are not correctly summarized.

try {
    $result = $apiInstance->getAutomationRules($is_user, $month);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StatisticsApi->getAutomationRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **is_user** | **bool**| Whether you&#39;d like to list automation rules triggered by single users who are not in any teams (&#x60;true&#x60;) or by teams (&#x60;false&#x60;).  The usage of &#x60;true&#x60; here is seldom meaningful for cloud.seatable.io as all the users in the SeaTable Cloud are team users. | |
| **month** | **int**| For which month you&#39;d like to list the statistics in the format of YYYYMM. Statistics of automation rules before 202109 are not correctly summarized. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `getExternalApps()`

```php
getExternalApps($is_user, $month, $page, $per_page): object
```

Get External Apps

As system admin, you can have an overview of the external apps statistics with this API request. The result can be queried by user or by team.  In the request parameter:  *   `is_user` is `true` by default. If you need to see the results by team, use this param and let it be `false`. *   `month` is the time filter, and it lets you see the result by month. Use e.g. 202207 for July, 2022. *   `page` and `per_page` are your controls of the returned pages and results per page.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\StatisticsApi(
    new GuzzleHttp\Client(),
    $config
);
$is_user = false; // bool | Whether you'd like to list automation rules triggered by single users who are not in any teams (`true`) or by teams (`false`).  The usage of `true` here is seldom meaningful for cloud.seatable.io as all the users in the SeaTable Cloud are team users.
$month = 202109; // int | For which month you'd like to list the statistics in the format of YYYYMM. Statistics of automation rules before 202109 are not correctly summarized.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->getExternalApps($is_user, $month, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StatisticsApi->getExternalApps: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **is_user** | **bool**| Whether you&#39;d like to list automation rules triggered by single users who are not in any teams (&#x60;true&#x60;) or by teams (&#x60;false&#x60;).  The usage of &#x60;true&#x60; here is seldom meaningful for cloud.seatable.io as all the users in the SeaTable Cloud are team users. | |
| **month** | **int**| For which month you&#39;d like to list the statistics in the format of YYYYMM. Statistics of automation rules before 202109 are not correctly summarized. | [optional] |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `getScriptRunningCountByUser()`

```php
getScriptRunningCountByUser($is_user, $owner, $month): object
```

Get Script Running Count by User

Use this request to overview the scripts running statistics of a certain user, or all the users in your system.  In the response:  *   `total_run_count` is the total number of runs; *   `total_run_time` is the total time of runs, in seconds.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\StatisticsApi(
    new GuzzleHttp\Client(),
    $config
);
$is_user = false; // bool | Whether you'd like to list automation rules triggered by single users who are not in any teams (`true`) or by teams (`false`).  The usage of `true` here is seldom meaningful for cloud.seatable.io as all the users in the SeaTable Cloud are team users.
$owner = 123abc456def789ghi123jkl456mno789@auth.local; // string | The ID of the user you are querying. Optional. If you don't define a user, all the users are queried.
$month = 202109; // int | For which month you'd like to list the statistics in the format of YYYYMM. Statistics of automation rules before 202109 are not correctly summarized.

try {
    $result = $apiInstance->getScriptRunningCountByUser($is_user, $owner, $month);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StatisticsApi->getScriptRunningCountByUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **is_user** | **bool**| Whether you&#39;d like to list automation rules triggered by single users who are not in any teams (&#x60;true&#x60;) or by teams (&#x60;false&#x60;).  The usage of &#x60;true&#x60; here is seldom meaningful for cloud.seatable.io as all the users in the SeaTable Cloud are team users. | |
| **owner** | **string**| The ID of the user you are querying. Optional. If you don&#39;t define a user, all the users are queried. | [optional] |
| **month** | **int**| For which month you&#39;d like to list the statistics in the format of YYYYMM. Statistics of automation rules before 202109 are not correctly summarized. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listActiveUsersByDay()`

```php
listActiveUsersByDay($date, $page, $per_page): object
```

List Active Users (one Day)

List the active users' details on a given day.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\StatisticsApi(
    new GuzzleHttp\Client(),
    $config
);
$date = 2020-06-19+00:00:00; // string | The date in ISO format. Required.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listActiveUsersByDay($date, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StatisticsApi->listActiveUsersByDay: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **date** | **string**| The date in ISO format. Required. | [optional] |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listScriptTasks()`

```php
listScriptTasks($page, $per_page): object
```

List Scripts Tasks

List off all the scheduled scripts tasks in the current system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\StatisticsApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listScriptTasks($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StatisticsApi->listScriptTasks: ', $e->getMessage(), PHP_EOL;
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

AccountTokenAuth



