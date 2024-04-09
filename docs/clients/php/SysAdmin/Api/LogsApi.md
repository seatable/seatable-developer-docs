# SeaTable\Client\LogsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listAbuseReports()**](LogsApi.md#listAbuseReports) | **GET** /api/v2.1/admin/abuse-reports/ | List Abuse Reports |
| [**listEmailLogs()**](LogsApi.md#listEmailLogs) | **GET** /api/v2.1/admin/email-sending-logs/ | List Email Logs |
| [**listLoginLogs()**](LogsApi.md#listLoginLogs) | **GET** /api/v2.1/admin/logs/login-logs/ | List Login Logs |
| [**listRegistrationLogs()**](LogsApi.md#listRegistrationLogs) | **GET** /api/v2.1/admin/registration-logs/ | List Registration Logs |
| [**updateAbuseReport()**](LogsApi.md#updateAbuseReport) | **PUT** /api/v2.1/admin/abuse-reports/{abuse_report_id}/ | Update Abuse Report |


## `listAbuseReports()`

```php
listAbuseReports(): object
```

List Abuse Reports

As system administrator, use this API request to list current abuse reports in the system.  The returned `id` param is the ID of each abuse report.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\LogsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listAbuseReports();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LogsApi->listAbuseReports: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listEmailLogs()`

```php
listEmailLogs($page, $per_page): object
```

List Email Logs

List the email sending logs in the system. The emails sent via 3rd party email accounts are listed here.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\LogsApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listEmailLogs($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LogsApi->listEmailLogs: ', $e->getMessage(), PHP_EOL;
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




## `listLoginLogs()`

```php
listLoginLogs($page, $per_page): object
```

List Login Logs

List the logins of all users in the system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\LogsApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listLoginLogs($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LogsApi->listLoginLogs: ', $e->getMessage(), PHP_EOL;
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




## `listRegistrationLogs()`

```php
listRegistrationLogs()
```

List Registration Logs

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\LogsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $apiInstance->listRegistrationLogs();
} catch (Exception $e) {
    echo 'Exception when calling LogsApi->listRegistrationLogs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

AccountTokenAuth




## `updateAbuseReport()`

```php
updateAbuseReport($abuse_report_id, $update_abuse_report_request): object
```

Update Abuse Report

As system administrator, use this API request to list current abuse reports in the system. In the request URL, type in the `abuse_report_id` that you got from the call to list abuse reports.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\LogsApi(
    new GuzzleHttp\Client(),
    $config
);
$abuse_report_id = 1; // int
$update_abuse_report_request = new \SeaTable\Client\SysAdmin/Model\UpdateAbuseReportRequest(); // \SeaTable\Client\SysAdmin/Model\UpdateAbuseReportRequest

try {
    $result = $apiInstance->updateAbuseReport($abuse_report_id, $update_abuse_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LogsApi->updateAbuseReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **abuse_report_id** | **int**|  | |
| **update_abuse_report_request** | [**\SeaTable\Client\SysAdmin/Model\UpdateAbuseReportRequest**](../Model/UpdateAbuseReportRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



