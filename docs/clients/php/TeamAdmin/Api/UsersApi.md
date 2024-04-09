# SeaTable\Client\UsersApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addUser()**](UsersApi.md#addUser) | **POST** /api/v2.1/org/{org_id}/admin/users/ | Add User |
| [**deleteUser()**](UsersApi.md#deleteUser) | **DELETE** /api/v2.1/org/{org_id}/admin/users/{user_id}/ | Delete User |
| [**disableTwoFactor()**](UsersApi.md#disableTwoFactor) | **DELETE** /api/v2.1/org/{org_id}/admin/users/{user_id}/two-factor-auth/ | Disable 2FA |
| [**enforceTwofactor()**](UsersApi.md#enforceTwofactor) | **PUT** /api/v2.1/org/{org_id}/admin/users/{user_id}/two-factor-auth/ | Enforce 2FA |
| [**listTeamUsers()**](UsersApi.md#listTeamUsers) | **GET** /api/v2.1/org/{org_id}/admin/users/ | List Users (Team) |
| [**resetUserPassword()**](UsersApi.md#resetUserPassword) | **PUT** /api/v2.1/org/{org_id}/admin/users/{user_id}/set-password/ | Reset User Password |
| [**updateUser()**](UsersApi.md#updateUser) | **PUT** /api/v2.1/org/{org_id}/admin/users/{user_id}/ | Update User |


## `addUser()`

```php
addUser($org_id, $email, $name, $password, $with_workspace): object
```

Add User

Add a new user in the team (organization).  In the request body, define the new user's `email`, `name` and `password`.   SeaTable does not automatically create a workspace for a newly added user: the `with_workspace` parameter is `false` by default. If you would like your new user to have a workspace when they are added (so that they can start operating workspaces and bases right away with API requests), make sure you set `true` for this parameter.  Otherwise, their workspace will only be created when they login to the SeaTable web interface for the first time.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$email = 'email_example'; // string | User's contact email to login.
$name = 'name_example'; // string | User's full name.
$password = 'password_example'; // string | User's password to login.
$with_workspace = True; // bool | If a workspace should be automatically created for the user. Optional. `false` by default.

try {
    $result = $apiInstance->addUser($org_id, $email, $name, $password, $with_workspace);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->addUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **email** | **string**| User&#39;s contact email to login. | [optional] |
| **name** | **string**| User&#39;s full name. | [optional] |
| **password** | **string**| User&#39;s password to login. | [optional] |
| **with_workspace** | **bool**| If a workspace should be automatically created for the user. Optional. &#x60;false&#x60; by default. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteUser()`

```php
deleteUser($org_id, $user_id): object
```

Delete User

Delete a user by their `user_id` permanently. When you delete a user, their bases are automatically moved into the organization's trash bin.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$user_id = 123456789f1e4c8d8e1c31415867317c@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.

try {
    $result = $apiInstance->deleteUser($org_id, $user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->deleteUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `disableTwoFactor()`

```php
disableTwoFactor($org_id, $user_id): object
```

Disable 2FA

If a user in your team has lost their phone or deleted the authenticator App by accident, they cannot log in to SeaTable anymore if 2FA is enabled for them. In this case, you as the team administrator can disable 2FA for them. Again, this is to be distinguished from the request [Enforce 2FA for A User in Team](/reference/team-admin-users-enforce-2fa) when you use `force_2fa = 0`, which only cancels the enforcement of 2FA but doesn't necessarily disable it for them.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$user_id = 123456789f1e4c8d8e1c31415867317c@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.

try {
    $result = $apiInstance->disableTwoFactor($org_id, $user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->disableTwoFactor: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `enforceTwofactor()`

```php
enforceTwofactor($org_id, $user_id, $enforce_twofactor_request): object
```

Enforce 2FA

As the team administrator, you can force each team member to use 2-factor authentication (2FA).  When the value of `force_2fa` is `1` in this request, the member will be requested to activate 2FA by scanning a QR code next time they log in. To cancel enforcing them to use 2FA, change the value to `0` and send this request again.  This request is to be distinguished from the next request, because cancelling the enforcement doesn't necesssarily [Disable 2FA for A User in Team](/reference/team-admin-users-disable-2fa), which serves a different purpose.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$user_id = 123456789f1e4c8d8e1c31415867317c@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.
$enforce_twofactor_request = new \SeaTable\Client\TeamAdmin\EnforceTwofactorRequest(); // \SeaTable\Client\TeamAdmin\EnforceTwofactorRequest

try {
    $result = $apiInstance->enforceTwofactor($org_id, $user_id, $enforce_twofactor_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->enforceTwofactor: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |
| **enforce_twofactor_request** | [**\SeaTable\Client\TeamAdmin\EnforceTwofactorRequest**](../Model/EnforceTwofactorRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listTeamUsers()`

```php
listTeamUsers($org_id, $page, $per_page): object
```

List Users (Team)

List all the users in the organization, or only the admins/non-admins.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listTeamUsers($org_id, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->listTeamUsers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **page** | **int**| The page number you want to start showing the entries. If no value is provided, 1 will be used. | [optional] |
| **per_page** | **int**| The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `resetUserPassword()`

```php
resetUserPassword($org_id, $user_id): object
```

Reset User Password

Reset the password of a user and get a new password. The new password will be automatically sent to the user per email.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$user_id = 123456789f1e4c8d8e1c31415867317c@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.

try {
    $result = $apiInstance->resetUserPassword($org_id, $user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->resetUserPassword: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateUser()`

```php
updateUser($org_id, $user_id, $name, $contact_email, $is_staff, $is_active, $quota_total, $id_in_org): object
```

Update User

Update a user's details. See the parameter list for the detailed description of each entry.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\UsersApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$user_id = 123456789f1e4c8d8e1c31415867317c@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.
$name = 'name_example'; // string | User's full name.
$contact_email = 'contact_email_example'; // string | User's contact email.
$is_staff = True; // bool | Determines if the user account has access to the system administration area.
$is_active = True; // bool | Determines the current status of this account. An inactive account can not login anymore.
$quota_total = 56; // int | Update their total quota in MB.
$id_in_org = 'id_in_org_example'; // string | The team ID of the user, could be a student's ID or employee ID. String.

try {
    $result = $apiInstance->updateUser($org_id, $user_id, $name, $contact_email, $is_staff, $is_active, $quota_total, $id_in_org);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->updateUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |
| **name** | **string**| User&#39;s full name. | [optional] |
| **contact_email** | **string**| User&#39;s contact email. | [optional] |
| **is_staff** | **bool**| Determines if the user account has access to the system administration area. | [optional] |
| **is_active** | **bool**| Determines the current status of this account. An inactive account can not login anymore. | [optional] |
| **quota_total** | **int**| Update their total quota in MB. | [optional] |
| **id_in_org** | **string**| The team ID of the user, could be a student&#39;s ID or employee ID. String. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



