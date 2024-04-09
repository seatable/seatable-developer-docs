# SeaTable\Client\WebhooksApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createWebhook()**](WebhooksApi.md#createWebhook) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/webhooks/ | Create Webhook |
| [**deleteWebhook()**](WebhooksApi.md#deleteWebhook) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/webhooks/{webhook_id}/ | Delete Webhook |
| [**listWebhooks()**](WebhooksApi.md#listWebhooks) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/webhooks/ | List Webhooks |
| [**updateWebhook()**](WebhooksApi.md#updateWebhook) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/webhooks/{webhook_id}/ | Update Webhook |


## `createWebhook()`

```php
createWebhook($workspace_id, $base_name, $url, $secret): object
```

Create Webhook

Create a new webhook for a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\WebhooksApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$url = 'url_example'; // string | The URL of the webhook. It should start with `http(s)`. Required.
$secret = 56; // int | When you set a secret, you'll receive the X-SeaTable-Signature header, whose value is the result of SHA1 encryption of the secret key, in the webhook POST request. Optional.

try {
    $result = $apiInstance->createWebhook($workspace_id, $base_name, $url, $secret);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->createWebhook: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **url** | **string**| The URL of the webhook. It should start with &#x60;http(s)&#x60;. Required. | [optional] |
| **secret** | **int**| When you set a secret, you&#39;ll receive the X-SeaTable-Signature header, whose value is the result of SHA1 encryption of the secret key, in the webhook POST request. Optional. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteWebhook()`

```php
deleteWebhook($workspace_id, $base_name, $webhook_id): object
```

Delete Webhook

Remove a webhook from a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\WebhooksApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$webhook_id = 1; // int

try {
    $result = $apiInstance->deleteWebhook($workspace_id, $base_name, $webhook_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->deleteWebhook: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **webhook_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listWebhooks()`

```php
listWebhooks($workspace_id, $base_name): object
```

List Webhooks

List all the webhooks created in a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\WebhooksApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listWebhooks($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->listWebhooks: ', $e->getMessage(), PHP_EOL;
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




## `updateWebhook()`

```php
updateWebhook($workspace_id, $base_name, $webhook_id, $url, $secret): object
```

Update Webhook

Update the URL and/or secret of a webhook.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\WebhooksApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$webhook_id = 1; // int
$url = 'url_example'; // string | The URL of the webhook. It should start with `http(s)`. Required.
$secret = 56; // int | When you set a secret, you'll receive the X-SeaTable-Signature header, whose value is the result of SHA1 encryption of the secret key, in the webhook POST request. Optional.

try {
    $result = $apiInstance->updateWebhook($workspace_id, $base_name, $webhook_id, $url, $secret);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->updateWebhook: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **webhook_id** | **int**|  | |
| **url** | **string**| The URL of the webhook. It should start with &#x60;http(s)&#x60;. Required. | [optional] |
| **secret** | **int**| When you set a secret, you&#39;ll receive the X-SeaTable-Signature header, whose value is the result of SHA1 encryption of the secret key, in the webhook POST request. Optional. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



