# SeaTable\Client\SharingApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createGroupShare()**](SharingApi.md#createGroupShare) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/group-shares/ | Create Group Share |
| [**createGroupViewShare()**](SharingApi.md#createGroupViewShare) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/group-view-shares/ | Create Group View Share |
| [**createUserShare()**](SharingApi.md#createUserShare) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/share/ | Create User Share |
| [**createUserViewShare()**](SharingApi.md#createUserViewShare) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/user-view-shares/ | Create User View Share |
| [**deleteGroupAllViewShare()**](SharingApi.md#deleteGroupAllViewShare) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/group-view-shares/ | Delete Group View Share |
| [**deleteGroupShare()**](SharingApi.md#deleteGroupShare) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/group-shares/{group_id}/ | Delete Group Share |
| [**deleteGroupViewShare()**](SharingApi.md#deleteGroupViewShare) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/group-view-shares/{group_view_share_id}/ | Delete Group View Share |
| [**deleteUserAllViewShare()**](SharingApi.md#deleteUserAllViewShare) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/user-view-shares/ | Delete User View Share |
| [**deleteUserShare()**](SharingApi.md#deleteUserShare) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/share/ | Delete User Share |
| [**deleteUserViewShare()**](SharingApi.md#deleteUserViewShare) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/user-view-shares/{user_view_share_id}/ | Delete User View Share |
| [**leaveSharedView()**](SharingApi.md#leaveSharedView) | **DELETE** /api/v2.1/dtables/view-shares-user-shared/{user_view_share_id}/ | Leave Shared View |
| [**listCollaborators()**](SharingApi.md#listCollaborators) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/related-users/ | List Collaborators |
| [**listGroupShares()**](SharingApi.md#listGroupShares) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/group-shares/ | List Group Shares |
| [**listGroupViewShares()**](SharingApi.md#listGroupViewShares) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/group-view-shares/ | List Group View Shares |
| [**listMyGroupShares()**](SharingApi.md#listMyGroupShares) | **GET** /api/v2.1/dtables/group-shared/ | List My Group Shares |
| [**listMyGroupViewShares()**](SharingApi.md#listMyGroupViewShares) | **GET** /api/v2.1/dtables/view-shares-group-shared/ | My Group View Shares |
| [**listMyShares()**](SharingApi.md#listMyShares) | **GET** /api/v2.1/dtables/shared/ | List My Shares |
| [**listMyUserViewShares()**](SharingApi.md#listMyUserViewShares) | **GET** /api/v2.1/dtables/view-shares-user-shared/ | List My User View Shares |
| [**listUserShares()**](SharingApi.md#listUserShares) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/share/ | List User Shares |
| [**listUserViewShares()**](SharingApi.md#listUserViewShares) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/user-view-shares/ | List User View Shares |
| [**updateGroupShare()**](SharingApi.md#updateGroupShare) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/group-shares/{group_id}/ | Update Group Share |
| [**updateGroupViewShare()**](SharingApi.md#updateGroupViewShare) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/group-view-shares/{group_view_share_id}/ | Update Group View Share |
| [**updateUserShare()**](SharingApi.md#updateUserShare) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/share/ | Update User Share |
| [**updateUserViewShare()**](SharingApi.md#updateUserViewShare) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/user-view-shares/{user_view_share_id}/ | Update User View Share |


## `createGroupShare()`

```php
createGroupShare($workspace_id, $base_name, $group_id, $permission): object
```

Create Group Share

Share a base from My Bases to a group with read-only or read and write permissions.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$group_id = 'group_id_example'; // string | The ID of the group.
$permission = 'permission_example'; // string | `r` for read only or `rw` for read and write

try {
    $result = $apiInstance->createGroupShare($workspace_id, $base_name, $group_id, $permission);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->createGroupShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **group_id** | **string**| The ID of the group. | [optional] |
| **permission** | **string**| &#x60;r&#x60; for read only or &#x60;rw&#x60; for read and write | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `createGroupViewShare()`

```php
createGroupViewShare($workspace_id, $base_name, $table_id, $view_id, $permission, $to_group_id): object
```

Create Group View Share

Share a view to a group, thus you are the `FromUser` here.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$table_id = 'table_id_example'; // string
$view_id = 'view_id_example'; // string
$permission = 'permission_example'; // string | `r` for read only or `rw` for read and write
$to_group_id = 'to_group_id_example'; // string | The ID of the group.

try {
    $result = $apiInstance->createGroupViewShare($workspace_id, $base_name, $table_id, $view_id, $permission, $to_group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->createGroupViewShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **table_id** | **string**|  | [optional] |
| **view_id** | **string**|  | [optional] |
| **permission** | **string**| &#x60;r&#x60; for read only or &#x60;rw&#x60; for read and write | [optional] |
| **to_group_id** | **string**| The ID of the group. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `createUserShare()`

```php
createUserShare($workspace_id, $base_name, $permission, $email): object
```

Create User Share

Share a base to a certain user with certain permission.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$permission = 'permission_example'; // string | `r` for read only or `rw` for read and write
$email = 'email_example'; // string | The user ID ending with @auth.local

try {
    $result = $apiInstance->createUserShare($workspace_id, $base_name, $permission, $email);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->createUserShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **permission** | **string**| &#x60;r&#x60; for read only or &#x60;rw&#x60; for read and write | [optional] |
| **email** | **string**| The user ID ending with @auth.local | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `createUserViewShare()`

```php
createUserViewShare($workspace_id, $base_name, $permission, $to_user, $table_id, $view_id): object
```

Create User View Share

Start sharing a view to another user, which is the `ToUser` in this case.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$permission = 'permission_example'; // string | `r` for read only or `rw` for read and write
$to_user = 'to_user_example'; // string | The user ID ending with @auth.local
$table_id = 'table_id_example'; // string
$view_id = 'view_id_example'; // string

try {
    $result = $apiInstance->createUserViewShare($workspace_id, $base_name, $permission, $to_user, $table_id, $view_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->createUserViewShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **permission** | **string**| &#x60;r&#x60; for read only or &#x60;rw&#x60; for read and write | [optional] |
| **to_user** | **string**| The user ID ending with @auth.local | [optional] |
| **table_id** | **string**|  | [optional] |
| **view_id** | **string**|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteGroupAllViewShare()`

```php
deleteGroupAllViewShare($table_id, $view_id, $workspace_id, $base_name): object
```

Delete Group View Share

Stop sharing the view to all the groups.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$table_id = 0000; // string | The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**.
$view_id = Jz4d; // string | id of view, string
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->deleteGroupAllViewShare($table_id, $view_id, $workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->deleteGroupAllViewShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table_id** | **string**| The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**. | |
| **view_id** | **string**| id of view, string | |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteGroupShare()`

```php
deleteGroupShare($workspace_id, $base_name, $group_id): object
```

Delete Group Share

Stop sharing a base to a certain group.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$group_id = 1; // int

try {
    $result = $apiInstance->deleteGroupShare($workspace_id, $base_name, $group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->deleteGroupShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **group_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteGroupViewShare()`

```php
deleteGroupViewShare($workspace_id, $base_name, $group_view_share_id): object
```

Delete Group View Share

Use this request to stop sharing a view to a certain group as `FromUser`. If you would like to stop sharing it with all of the groups you are in, use the next request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$group_view_share_id = 6; // int

try {
    $result = $apiInstance->deleteGroupViewShare($workspace_id, $base_name, $group_view_share_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->deleteGroupViewShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **group_view_share_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteUserAllViewShare()`

```php
deleteUserAllViewShare($table_id, $view_id, $workspace_id, $base_name): object
```

Delete User View Share

Stop sharing a view to all users.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$table_id = 0000; // string | The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**.
$view_id = Jz4d; // string | id of view, string
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->deleteUserAllViewShare($table_id, $view_id, $workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->deleteUserAllViewShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table_id** | **string**| The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**. | |
| **view_id** | **string**| id of view, string | |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteUserShare()`

```php
deleteUserShare($workspace_id, $base_name): object
```

Delete User Share

Stop sharing a base to a user.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->deleteUserShare($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->deleteUserShare: ', $e->getMessage(), PHP_EOL;
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




## `deleteUserViewShare()`

```php
deleteUserViewShare($workspace_id, $base_name, $user_view_share_id): object
```

Delete User View Share

Stop sharing a view to a certain user. The `user_view_share_id` here is the value you can retrieve from the above requests when you list, add or update a sharing permission.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$user_view_share_id = 15; // int

try {
    $result = $apiInstance->deleteUserViewShare($workspace_id, $base_name, $user_view_share_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->deleteUserViewShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **user_view_share_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `leaveSharedView()`

```php
leaveSharedView($user_view_share_id): object
```

Leave Shared View

Delete your access to a view shared to you. After executing this request, you won't be able to see that view as a `ToUser`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$user_view_share_id = 15; // int

try {
    $result = $apiInstance->leaveSharedView($user_view_share_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->leaveSharedView: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_view_share_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listCollaborators()`

```php
listCollaborators($workspace_id, $base_name): object
```

List Collaborators

List all the collaborators (related users who have read&write permission) to a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listCollaborators($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->listCollaborators: ', $e->getMessage(), PHP_EOL;
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




## `listGroupShares()`

```php
listGroupShares($workspace_id, $base_name): object
```

List Group Shares

List all the groups a particular base is being shared to.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listGroupShares($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->listGroupShares: ', $e->getMessage(), PHP_EOL;
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




## `listGroupViewShares()`

```php
listGroupViewShares($workspace_id, $base_name): object
```

List Group View Shares

This request lets you, as `FromUser`, see which views you are sharing to the groups you are in.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listGroupViewShares($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->listGroupViewShares: ', $e->getMessage(), PHP_EOL;
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




## `listMyGroupShares()`

```php
listMyGroupShares(): object
```

List My Group Shares

List all the bases shared to the groups I am in. These bases may include:  * Bases you or others created in the group; * Bases you or others shared or copied to the group.  In the returned object, each group's ID and the details of each base are listed in the form of ``` \"group_id\":[bases] ``` Judging by the `workspace_id` you can determine if a base is in the group or shared to the group.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listMyGroupShares();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->listMyGroupShares: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listMyGroupViewShares()`

```php
listMyGroupViewShares(): object
```

My Group View Shares

As `ToUser`, you can use this request to list all the views shared to you via your groups.  In the response you can see which views you are being shared to via which groups.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listMyGroupViewShares();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->listMyGroupViewShares: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listMyShares()`

```php
listMyShares(): object
```

List My Shares

List all the bases currently shared to you. This request only lists off all the bases shared explicit to YOU, not your groups. To see all the bases shared to your groups, use the request **List Bases Shared to My Groups**.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listMyShares();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->listMyShares: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listMyUserViewShares()`

```php
listMyUserViewShares(): object
```

List My User View Shares

List all the views shared to you.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listMyUserViewShares();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->listMyUserViewShares: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listUserShares()`

```php
listUserShares($workspace_id, $base_name): object
```

List User Shares

List all the users sharing a base (except the current user). This request only lists off all the individual users sharing the base, which does not includ groups and group members sharing this base.  To see which groups are sharing this base, use the request [List Groups Base is Shared To](/reference/get_api-v2-1-workspace-workspace-id-dtable-base-name-group-shares-1).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listUserShares($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->listUserShares: ', $e->getMessage(), PHP_EOL;
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




## `listUserViewShares()`

```php
listUserViewShares($workspace_id, $base_name): object
```

List User View Shares

Use this request to list all the views you are currently sharing to other users.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listUserViewShares($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->listUserViewShares: ', $e->getMessage(), PHP_EOL;
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




## `updateGroupShare()`

```php
updateGroupShare($workspace_id, $base_name, $group_id, $permission): object
```

Update Group Share

Change the sharing permission (read-only/read and write) to a group.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$group_id = 1; // int
$permission = 'permission_example'; // string | `r` for read only or `rw` for read and write

try {
    $result = $apiInstance->updateGroupShare($workspace_id, $base_name, $group_id, $permission);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->updateGroupShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **group_id** | **int**|  | |
| **permission** | **string**| &#x60;r&#x60; for read only or &#x60;rw&#x60; for read and write | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateGroupViewShare()`

```php
updateGroupViewShare($workspace_id, $base_name, $group_view_share_id, $permission): object
```

Update Group View Share

Update the permission of a view sharing as a `FromUser`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$group_view_share_id = 6; // int
$permission = 'permission_example'; // string | `r` for read only or `rw` for read and write

try {
    $result = $apiInstance->updateGroupViewShare($workspace_id, $base_name, $group_view_share_id, $permission);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->updateGroupViewShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **group_view_share_id** | **int**|  | |
| **permission** | **string**| &#x60;r&#x60; for read only or &#x60;rw&#x60; for read and write | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateUserShare()`

```php
updateUserShare($workspace_id, $base_name, $permission, $email): object
```

Update User Share

Change the sharing permission (read-only or read and write) of a base to a user.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$permission = 'permission_example'; // string | `r` for read only or `rw` for read and write
$email = 'email_example'; // string | The user ID ending with @auth.local

try {
    $result = $apiInstance->updateUserShare($workspace_id, $base_name, $permission, $email);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->updateUserShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **permission** | **string**| &#x60;r&#x60; for read only or &#x60;rw&#x60; for read and write | [optional] |
| **email** | **string**| The user ID ending with @auth.local | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateUserViewShare()`

```php
updateUserViewShare($workspace_id, $base_name, $user_view_share_id, $permission): object
```

Update User View Share

As `FromUser`, you can use this request to update the sharing permission to a certain user.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$user_view_share_id = 15; // int
$permission = 'permission_example'; // string | `r` for read only or `rw` for read and write

try {
    $result = $apiInstance->updateUserViewShare($workspace_id, $base_name, $user_view_share_id, $permission);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingApi->updateUserViewShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **user_view_share_id** | **int**|  | |
| **permission** | **string**| &#x60;r&#x60; for read only or &#x60;rw&#x60; for read and write | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



