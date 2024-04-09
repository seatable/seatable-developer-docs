# SeaTable\Client\AutomationsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteAutomation()**](AutomationsApi.md#deleteAutomation) | **DELETE** /api/v2.1/admin/automation-rules/{automation_rule_id}/ | Delete Automation |
| [**deleteInvalidAutomations()**](AutomationsApi.md#deleteInvalidAutomations) | **DELETE** /api/v2.1/admin/invalid-automation-rules/ | Delete Invalid Automations |
| [**listAutomations()**](AutomationsApi.md#listAutomations) | **GET** /api/v2.1/admin/automation-rules/ | List Automations |
| [**listInvalidAutomations()**](AutomationsApi.md#listInvalidAutomations) | **GET** /api/v2.1/admin/invalid-automation-rules/ | List Invalid Automations |


## `deleteAutomation()`

```php
deleteAutomation($automation_rule_id): object
```

Delete Automation

As system administrator, you can delete any automation rule existing in the current system. Attention - This operation cannot be undone!

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\AutomationsApi(
    new GuzzleHttp\Client(),
    $config
);
$automation_rule_id = 10; // int

try {
    $result = $apiInstance->deleteAutomation($automation_rule_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AutomationsApi->deleteAutomation: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **automation_rule_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteInvalidAutomations()`

```php
deleteInvalidAutomations(): object
```

Delete Invalid Automations

If you don't want to delete the invalid automation rules one by one, you can use this request to delete them all at once.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\AutomationsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->deleteInvalidAutomations();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AutomationsApi->deleteInvalidAutomations: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listAutomations()`

```php
listAutomations($page, $per_page): object
```

List Automations

List all the existing base automation rules in the current system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\AutomationsApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listAutomations($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AutomationsApi->listAutomations: ', $e->getMessage(), PHP_EOL;
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




## `listInvalidAutomations()`

```php
listInvalidAutomations($page, $per_page): object
```

List Invalid Automations

When an automation rule's dependent base, row or column doesn't exist any more, it may become invalid. In this case, the system administrator can list all the invalid automation rules and eventually delete them.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\AutomationsApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listInvalidAutomations($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AutomationsApi->listInvalidAutomations: ', $e->getMessage(), PHP_EOL;
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



