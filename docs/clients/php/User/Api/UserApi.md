# SeaTable\Client\UserApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addUserAvatar()**](UserApi.md#addUserAvatar) | **POST** /api/v2.1/user-avatar/ | Upload/Update User Avatar |
| [**getAccountInfo()**](UserApi.md#getAccountInfo) | **GET** /api2/account/info/ | Get Account Info |
| [**getPublicUserInfo()**](UserApi.md#getPublicUserInfo) | **GET** /api/v2.1/user-common-info/{user_id}/ | Get Public User Info |
| [**listPublicUserInfos()**](UserApi.md#listPublicUserInfos) | **POST** /api/v2.1/user-list/ | List Public User Infos |
| [**searchUser()**](UserApi.md#searchUser) | **GET** /api2/search-user/ | Search User |
| [**updateEmailAddress()**](UserApi.md#updateEmailAddress) | **PUT** /api/v2.1/user/contact-email/ | Update Email Address |


## `addUserAvatar()`

```php
addUserAvatar($avatar, $avatar_size): object
```

Upload/Update User Avatar

Upload an image to make it your current avatar. After successful uploading/updating your avatar, the file will be renamed and converted to .png. The URL of your new avatar is returned in the response.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\UserApi(
    new GuzzleHttp\Client(),
    $config
);
$avatar = "/path/to/file.txt"; // \SplFileObject | Upload an image file. Authorized extensions are : .jpg, .png, .jpeg, .gif. Accepted max. size is 1.0 MB.
$avatar_size = 'avatar_size_example'; // string

try {
    $result = $apiInstance->addUserAvatar($avatar, $avatar_size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->addUserAvatar: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **avatar** | **\SplFileObject****\SplFileObject**| Upload an image file. Authorized extensions are : .jpg, .png, .jpeg, .gif. Accepted max. size is 1.0 MB. | [optional] |
| **avatar_size** | **string**|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `getAccountInfo()`

```php
getAccountInfo(): object
```

Get Account Info

Get the detailed account information with the user's Account Token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\UserApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getAccountInfo();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->getAccountInfo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `getPublicUserInfo()`

```php
getPublicUserInfo($user_id): object
```

Get Public User Info

Get the common info from a user by his email address.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\UserApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 123456789f1e4c8d8e1c31415867317c@auth.local; // string

try {
    $result = $apiInstance->getPublicUserInfo($user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->getPublicUserInfo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listPublicUserInfos()`

```php
listPublicUserInfos($list_public_user_infos_request): object
```

List Public User Infos

List the details of other users identified by their email addresses.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\UserApi(
    new GuzzleHttp\Client(),
    $config
);
$list_public_user_infos_request = new \SeaTable\Client\User\ListPublicUserInfosRequest(); // \SeaTable\Client\User\ListPublicUserInfosRequest

try {
    $result = $apiInstance->listPublicUserInfos($list_public_user_infos_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->listPublicUserInfos: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **list_public_user_infos_request** | [**\SeaTable\Client\User\ListPublicUserInfosRequest**](../Model/ListPublicUserInfosRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `searchUser()`

```php
searchUser($q): object
```

Search User

Just search for a user with the string or substring in the `q` param. You can search by `email` (case sensitive), `name` (case insensitive) or `contact_email` (case insensitive).  Substrings are allowed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\UserApi(
    new GuzzleHttp\Client(),
    $config
);
$q = Micha; // string

try {
    $result = $apiInstance->searchUser($q);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->searchUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **q** | **string**|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateEmailAddress()`

```php
updateEmailAddress($new_contact_email): object
```

Update Email Address

Update the user's email address. This feature is disabled on cloud.seatable.io. If you would like to change your email address in a self-hosted instance, contact your system administrator to check if this feature is activated.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\UserApi(
    new GuzzleHttp\Client(),
    $config
);
$new_contact_email = 'new_contact_email_example'; // string | The new email address of the user.

try {
    $result = $apiInstance->updateEmailAddress($new_contact_email);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->updateEmailAddress: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **new_contact_email** | **string**| The new email address of the user. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



