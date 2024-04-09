# SeaTable\Client\BasesApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteBase()**](BasesApi.md#deleteBase) | **DELETE** /api/v2.1/admin/dtable/{base_uuid}/ | Delete Base |
| [**deleteBasePassword()**](BasesApi.md#deleteBasePassword) | **PUT** /api/v2.1/admin/dtable/{base_uuid}/unset-password/ | Delete Base Password |
| [**listAllBases()**](BasesApi.md#listAllBases) | **GET** /api/v2.1/admin/dtables/ | List All Bases |
| [**listBaseNotifications()**](BasesApi.md#listBaseNotifications) | **GET** /api/v2.1/admin/dtable-notifications/ | List Notifications |
| [**listTrashedBases()**](BasesApi.md#listTrashedBases) | **GET** /api/v2.1/admin/trash-dtables/ | List Trashed Bases |
| [**listUsersBases()**](BasesApi.md#listUsersBases) | **GET** /api/v2.1/admin/users/{user_id}/dtables/ | List User&#39;s Bases |
| [**restoreTrashedBase()**](BasesApi.md#restoreTrashedBase) | **PUT** /api/v2.1/admin/trash-dtables/{base_id}/ | Restore Trashed Base |


## `deleteBase()`

```php
deleteBase($base_uuid): object
```

Delete Base

Delete a base. This will move this base to its team's trash.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->deleteBase($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->deleteBase: ', $e->getMessage(), PHP_EOL;
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



## `deleteBasePassword()`

```php
deleteBasePassword($base_uuid): object
```

Delete Base Password

In the case that a user has forgotten their base password, the system admin can unset the base password with this API request. The returned value of `is_encrypted` indicates that the base's password has been unset.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->deleteBasePassword($base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->deleteBasePassword: ', $e->getMessage(), PHP_EOL;
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



## `listAllBases()`

```php
listAllBases($per_page, $page)
```

List All Bases

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.

try {
    $apiInstance->listAllBases($per_page, $page);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listAllBases: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listBaseNotifications()`

```php
listBaseNotifications($dtable_uuid, $username, $contact_email, $seen, $page, $per_page): object
```

List Notifications

As the system administrator, you can inspect a certain user's notifications inside of a certain base. To enquire these notifications, you'll need the base's UUID and the user's contact email or their username. You can also filter the result by read or unread status.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$dtable_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$username = 'username_example'; // string | Who you want to get the notifications of, optional
$contact_email = test013@fun-mail.net; // string | The contact email of the user you're querying. Optional if `username` is defined.
$seen = 56; // int | Seen status, whether seen or not, 0/1, optional
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listBaseNotifications($dtable_uuid, $username, $contact_email, $seen, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listBaseNotifications: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dtable_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **username** | **string**| Who you want to get the notifications of, optional | [optional] |
| **contact_email** | **string**| The contact email of the user you&#39;re querying. Optional if &#x60;username&#x60; is defined. | [optional] |
| **seen** | **int**| Seen status, whether seen or not, 0/1, optional | [optional] |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listTrashedBases()`

```php
listTrashedBases($page, $per_page): object
```

List Trashed Bases

List all the trashed bases of all teams in the system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listTrashedBases($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listTrashedBases: ', $e->getMessage(), PHP_EOL;
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



## `listUsersBases()`

```php
listUsersBases($user_id, $page, $per_page): object
```

List User's Bases

List all the bases of a certain user by the user's ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listUsersBases($user_id, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listUsersBases: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `restoreTrashedBase()`

```php
restoreTrashedBase($base_id): object
```

Restore Trashed Base

Restore a deleted base from the trash bin and put it back where it was. If a base already exists there with the same name, the operation will fail and return an error.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$base_id = base_id; // string | The id of the base. This is not the base_uuid.

try {
    $result = $apiInstance->restoreTrashedBase($base_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->restoreTrashedBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_id** | **string**| The id of the base. This is not the base_uuid. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


