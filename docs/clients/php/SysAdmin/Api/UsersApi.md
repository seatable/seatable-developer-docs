# SeaTable\Client\UsersApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addNewUser()**](UsersApi.md#addNewUser) | **POST** /api/v2.1/admin/users/ | Add New User |
| [**deleteUser()**](UsersApi.md#deleteUser) | **DELETE** /api/v2.1/admin/users/{user_id}/ | Delete User |
| [**disableTwoFactor()**](UsersApi.md#disableTwoFactor) | **DELETE** /api2/two-factor-auth/{user_id}/ | Disable 2FA |
| [**enforceTwoFactor()**](UsersApi.md#enforceTwoFactor) | **PUT** /api/v2.1/admin/users/{user_id}/two-factor-auth/ | Enforce 2FA |
| [**getUser()**](UsersApi.md#getUser) | **GET** /api/v2.1/admin/users/{user_id}/ | Get User |
| [**importUsers()**](UsersApi.md#importUsers) | **POST** /api/v2.1/admin/import-users/ | Import users |
| [**listAdminUsers()**](UsersApi.md#listAdminUsers) | **GET** /api/v2.1/admin/admin-users/ | List Admin Users |
| [**listBasesSharedToUser()**](UsersApi.md#listBasesSharedToUser) | **GET** /api/v2.1/admin/users/{user_id}/shared-dtables/ | List Bases Shared to User |
| [**listUserStorageObjects()**](UsersApi.md#listUserStorageObjects) | **GET** /api/v2.1/admin/users/{user_id}/storage/ | List User&#39;s Storage Objects |
| [**listUsers()**](UsersApi.md#listUsers) | **GET** /api/v2.1/admin/users/ | List Users |
| [**resetUserPassword()**](UsersApi.md#resetUserPassword) | **PUT** /api/v2.1/admin/users/{user_id}/reset-password/ | Reset User&#39;s Password |
| [**searchUser()**](UsersApi.md#searchUser) | **GET** /api/v2.1/admin/search-user/ | Search User / Users |
| [**searchUserByOrgId()**](UsersApi.md#searchUserByOrgId) | **GET** /api/v2.1/admin/search-user-by-org-id/ | Search User by Org-ID |
| [**updateAdminRole()**](UsersApi.md#updateAdminRole) | **PUT** /api/v2.1/admin/admin-role/ | Update Admin&#39;s Role |
| [**updateUser()**](UsersApi.md#updateUser) | **PUT** /api/v2.1/admin/users/{user_id}/ | Update User |


## `addNewUser()`

```php
addNewUser($add_new_user_request): object
```

Add New User

Add a new user with desired details.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$add_new_user_request = new \SeaTable\Client\SysAdmin/Model\AddNewUserRequest(); // \SeaTable\Client\SysAdmin/Model\AddNewUserRequest

try {
    $result = $apiInstance->addNewUser($add_new_user_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->addNewUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **add_new_user_request** | [**\SeaTable\Client\SysAdmin/Model\AddNewUserRequest**](../Model/AddNewUserRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteUser()`

```php
deleteUser($user_id): object
```

Delete User

Delete a user by their ID.  If the user is in a team, you cannot delete them with this request, but with the request [Delete Team User](/reference/delete-team-user).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.

try {
    $result = $apiInstance->deleteUser($user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->deleteUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `disableTwoFactor()`

```php
disableTwoFactor($user_id): object
```

Disable 2FA

When users activate 2 factor authentication (2FA) in their personal settings, they need to provide a one-time passcode after entering their username and password at login.  However, sometimes bad things happen: lost of the phone or similar, and they cannot retrieve that passcode any more. If they also didn't save their backup codes, login would become impossible for them.  They should contact you, the system administrator then. You can then use this API request to disable their 2FA. After successful operation, they can login with just their username and password, and eventually reactivate their 2FA.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.

try {
    $result = $apiInstance->disableTwoFactor($user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->disableTwoFactor: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `enforceTwoFactor()`

```php
enforceTwoFactor($user_id, $enforce_two_factor_request): object
```

Enforce 2FA

As the system administrator, you can force each user to use 2-factor authentication (2FA).  When the value of `force_2fa` is `1` in this request, the user will be requested to activate 2FA by scanning a QR code next time they log in. To cancel enforcing them to use 2FA, change the value to `0` and send this request again.  This request is to be distinguished from the next request, because cancelling the enforcement doesn't necesssarily [Disable 2FA for A User in System](/reference/disable-2fa), which serves a different purpose.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.
$enforce_two_factor_request = new \SeaTable\Client\SysAdmin/Model\EnforceTwoFactorRequest(); // \SeaTable\Client\SysAdmin/Model\EnforceTwoFactorRequest

try {
    $result = $apiInstance->enforceTwoFactor($user_id, $enforce_two_factor_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->enforceTwoFactor: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |
| **enforce_two_factor_request** | [**\SeaTable\Client\SysAdmin/Model\EnforceTwoFactorRequest**](../Model/EnforceTwoFactorRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `getUser()`

```php
getUser($user_id)
```

Get User

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.

try {
    $apiInstance->getUser($user_id);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->getUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `importUsers()`

```php
importUsers($file): object
```

Import users

As system administrator, you can batch import users with an Excel file, which lists the users'  - `email` as their contact email address, which is also used to login as their username; - `password` as their initial login password; - Optionally, also define their display name, role, and quota.       An example user list Excel file looks like this:  <img src=\"https://seatable.io/wp-content/uploads/2022/12/example.png\">

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$file = "/path/to/file.txt"; // \SplFileObject

try {
    $result = $apiInstance->importUsers($file);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->importUsers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **file** | **\SplFileObject****\SplFileObject**|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listAdminUsers()`

```php
listAdminUsers(): object
```

List Admin Users

List all the system administrators in the current system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listAdminUsers();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->listAdminUsers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listBasesSharedToUser()`

```php
listBasesSharedToUser($user_id, $page, $per_page): object
```

List Bases Shared to User

List all the bases shared to a certain user with the user's ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listBasesSharedToUser($user_id, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->listBasesSharedToUser: ', $e->getMessage(), PHP_EOL;
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



## `listUserStorageObjects()`

```php
listUserStorageObjects($user_id, $parent_dir): object
```

List User's Storage Objects

List objects stored by a certain user by the user's ID. In the returned list, if the `is_file` value is `false`, it means this object is a folder.  In this example, the `obj_name` stands for the base's UUID. By using `/asset/<base_uuid>` as the value of `parent_dir`, you can go into the base's asset folder, where there're probably a `files` and an `images` folder for your further inspections.  However, you as system administrator can only see the names and size of these objects, but cannot access the data saved in them.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.
$parent_dir = /asset/; // string

try {
    $result = $apiInstance->listUserStorageObjects($user_id, $parent_dir);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->listUserStorageObjects: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |
| **parent_dir** | **string**|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listUsers()`

```php
listUsers($page, $per_page): object
```

List Users

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listUsers($page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->listUsers: ', $e->getMessage(), PHP_EOL;
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



## `resetUserPassword()`

```php
resetUserPassword($user_id): object
```

Reset User's Password

Reset a user's password.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.

try {
    $result = $apiInstance->resetUserPassword($user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->resetUserPassword: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `searchUser()`

```php
searchUser($query): object
```

Search User / Users

As system administrator, you can search all the users in your system by using this API request.   For the `query` value, you can give any string from the user's name, `email` (ID) or contact email address. All the users that fit to this search criteria will be listed in the response.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$query = teamuser001@example.com; // string | Enter any query string from the user's name, ID, or contact email.

try {
    $result = $apiInstance->searchUser($query);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->searchUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **query** | **string**| Enter any query string from the user&#39;s name, ID, or contact email. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `searchUserByOrgId()`

```php
searchUserByOrgId($query, $org_id, $limit)
```

Search User by Org-ID

Hier muss noch eine Beschreibung ergänzt werden

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$query = 'query_example'; // string
$org_id = 1; // int
$limit = 10; // int | Limit of search User

try {
    $apiInstance->searchUserByOrgId($query, $org_id, $limit);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->searchUserByOrgId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **query** | **string**|  | [optional] |
| **org_id** | **int**|  | [optional] |
| **limit** | **int**| Limit of search User | [optional] |

### Return type

void (empty response body)

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `updateAdminRole()`

```php
updateAdminRole($update_admins_role): object
```

Update Admin's Role

> Use this request with caution!! > - > Do not change your own role! Once your role has been changed, you **cannot use this API request to change it back**: You'll get a permission error, and lose access to a majority of admin functions. If you already did that, the only solution left for you is to login as another superuser and change your role back with that account. If there's no further superuser available, you can create one. Don't remember how to create a superuser? Read the [Manual](https://manual.seatable.io/).  ### There are 4 types of system administrators: - default admin (can use this request) - system admin (cannot use this request) - daily admin (cannot use this request) - audit admin (cannot use this request)    The default admin has the most permissions, while the other 3 types have limited permissions:  |      Permissions         | Default admin     | Daily admin        | System admin       | Audit admin        | |   -------------: |:--------------------:|:--------------------:|:--------------------:|:--------------------:| |               Info | &check; | &check; | &check; | &check; | |         Statistics | &check; | &check; |                    |                    | |           Settings | &check; |                    | &check; |                    | |              Bases | &check; |                    |                    |                    | |              Forms | &check; |                    |                    |                    | |              Users | &check; | &check; |                    |                    | |             Groups | &check; | &check; |                    |                    | |     External links | &check; |                    |                    |                    | |      Organizations | &check; |                    |                    |                    | |      Notifications | &check; |                    |                    |                    | | Administrator-logs | &check; |                    |                    | &check; | |            Plugins | &check; |                    |                    |                    | |              Rules | &check; |                    |                    |                    | |      Abuse reports | &check; |                    |                    |                    | |            Scripts | &check; |                    |                    |                    | | Email sending logs | &check; |                    |                    |                    |  ### Do not change your own admin role  As seen from the table above - If you change your role from \"default admin\" to \"system admin\" or \"audit admin\", you won't be able to change it back because the \"Users\" page is gone.  ### What to do if you already did that  Add another super user, login as that super user and change your role back. Unfortunately, you cannot do this with the API. Refer to [SeaTable Admin Manual - Starting SeaTable Server](https://manual.seatable.io/docker/Developer-Edition/Deploy%20SeaTable-DE%20with%20Docker/#starting-seatable-server) for details.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$update_admins_role = new \SeaTable\Client\SysAdmin/Model\UpdateAdminsRole(); // \SeaTable\Client\SysAdmin/Model\UpdateAdminsRole

try {
    $result = $apiInstance->updateAdminRole($update_admins_role);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->updateAdminRole: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **update_admins_role** | [**\SeaTable\Client\SysAdmin/Model\UpdateAdminsRole**](../Model/UpdateAdminsRole.md)|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `updateUser()`

```php
updateUser($user_id, $update_user_request): object
```

Update User

Update a user's details. See the parameter list for the detailed description of each entry.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.
$update_user_request = new \SeaTable\Client\SysAdmin/Model\UpdateUserRequest(); // \SeaTable\Client\SysAdmin/Model\UpdateUserRequest

try {
    $result = $apiInstance->updateUser($user_id, $update_user_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->updateUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |
| **update_user_request** | [**\SeaTable\Client\SysAdmin/Model\UpdateUserRequest**](../Model/UpdateUserRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


