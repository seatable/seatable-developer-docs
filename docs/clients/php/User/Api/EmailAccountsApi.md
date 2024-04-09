# SeaTable\Client\EmailAccountsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addEmailAccount()**](EmailAccountsApi.md#addEmailAccount) | **POST** /api/v2.1/third-party-accounts/{base_uuid}/ | Add Email Account |
| [**deleteEmailAccount()**](EmailAccountsApi.md#deleteEmailAccount) | **DELETE** /api/v2.1/third-party-accounts/{base_uuid}/{3rd_party_account_id}/ | Delete Email Account |
| [**getEmailAccount()**](EmailAccountsApi.md#getEmailAccount) | **GET** /api/v2.1/third-party-accounts/{base_uuid}/detail/ | Get Email Account |
| [**getEmailSendingStatus()**](EmailAccountsApi.md#getEmailSendingStatus) | **GET** /api/v2.1/dtable-message-status/ | Get Email Sending Status |
| [**listEmailAccounts()**](EmailAccountsApi.md#listEmailAccounts) | **GET** /api/v2.1/third-party-accounts/{base_uuid}/ | List Email Accounts |
| [**updateEmailAccount()**](EmailAccountsApi.md#updateEmailAccount) | **PUT** /api/v2.1/third-party-accounts/{base_uuid}/{3rd_party_account_id}/ | Update Email Account |


## `addEmailAccount()`

```php
addEmailAccount($base_uuid, $add_email_account_request): object
```

Add Email Account

Bound a third party email account in a base by using the params in the sample request body. The returned `id` value is the ID of this account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\EmailAccountsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$add_email_account_request = new \SeaTable\Client\User\AddEmailAccountRequest(); // \SeaTable\Client\User\AddEmailAccountRequest

try {
    $result = $apiInstance->addEmailAccount($base_uuid, $add_email_account_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling EmailAccountsApi->addEmailAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **add_email_account_request** | [**\SeaTable\Client\User\AddEmailAccountRequest**](../Model/AddEmailAccountRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteEmailAccount()`

```php
deleteEmailAccount($base_uuid, $_3rd_party_account_id): object
```

Delete Email Account

Delete a third party account using its ID in the request URL.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\EmailAccountsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$_3rd_party_account_id = 5; // string

try {
    $result = $apiInstance->deleteEmailAccount($base_uuid, $_3rd_party_account_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling EmailAccountsApi->deleteEmailAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **_3rd_party_account_id** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `getEmailAccount()`

```php
getEmailAccount($base_uuid, $account_name)
```

Get Email Account

Get the details of a 3rd party email account's information by its `account_name` in the URL.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\EmailAccountsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$account_name = Email Server2; // string

try {
    $apiInstance->getEmailAccount($base_uuid, $account_name);
} catch (Exception $e) {
    echo 'Exception when calling EmailAccountsApi->getEmailAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **account_name** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `getEmailSendingStatus()`

```php
getEmailSendingStatus($task_id): object
```

Get Email Sending Status

Query the task status with the returned `task_id` when you **Send An Email via 3rd Party Account**. If you get an error message: ```json {     \"error_msg\": \"task_id invalid.\" } ``` it means that the task has failed. This is most probably due to wrong account information.  Attention: After the task has been finished, you can only query it for once. A second query will also return the above error.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\EmailAccountsApi(
    new GuzzleHttp\Client(),
    $config
);
$task_id = 1616585864320; // int | The ID of the task, returned when you **Send An Email via 3rd Party Email Account**.

try {
    $result = $apiInstance->getEmailSendingStatus($task_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling EmailAccountsApi->getEmailSendingStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **task_id** | **int**| The ID of the task, returned when you **Send An Email via 3rd Party Email Account**. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listEmailAccounts()`

```php
listEmailAccounts($base_uuid): object
```

List Email Accounts

List all email accounts available in a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\EmailAccountsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->listEmailAccounts($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling EmailAccountsApi->listEmailAccounts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `updateEmailAccount()`

```php
updateEmailAccount($base_uuid, $_3rd_party_account_id, $add_email_account_request): object
```

Update Email Account

Change the account name, type, or detail (host, port, username or password) of a third party account using the account's ID in the URL. This ID can be retrieved by the call [List 3rd Party Email Accounts](/reference/get_api-v2-1-third-party-accounts-base-uuid-1), or by [Add 3rd Party Email Account](/reference/post_api-v2-1-third-party-accounts-base-uuid-1).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\EmailAccountsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$_3rd_party_account_id = 5; // string
$add_email_account_request = new \SeaTable\Client\User\AddEmailAccountRequest(); // \SeaTable\Client\User\AddEmailAccountRequest

try {
    $result = $apiInstance->updateEmailAccount($base_uuid, $_3rd_party_account_id, $add_email_account_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling EmailAccountsApi->updateEmailAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **_3rd_party_account_id** | **string**|  | |
| **add_email_account_request** | [**\SeaTable\Client\User\AddEmailAccountRequest**](../Model/AddEmailAccountRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


