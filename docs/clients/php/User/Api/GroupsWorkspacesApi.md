# SeaTable\Client\GroupsWorkspacesApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addGroupMember()**](GroupsWorkspacesApi.md#addGroupMember) | **POST** /api/v2.1/groups/{group_id}/members/ | Add Group Member |
| [**copyBaseFromExternalLink()**](GroupsWorkspacesApi.md#copyBaseFromExternalLink) | **POST** /api/v2.1/dtable-external-link/dtable-copy/ | Copy Base from External Link |
| [**copyBaseFromWorkspace()**](GroupsWorkspacesApi.md#copyBaseFromWorkspace) | **POST** /api/v2.1/dtable-copy/ | Copy Base from Workspace |
| [**createGroup()**](GroupsWorkspacesApi.md#createGroup) | **POST** /api/v2.1/groups/ | Create Group |
| [**deleteGroup()**](GroupsWorkspacesApi.md#deleteGroup) | **DELETE** /api/v2.1/groups/{group_id}/ | Delete Group |
| [**getGroup()**](GroupsWorkspacesApi.md#getGroup) | **GET** /api/v2.1/groups/{group_id}/ | Get Group |
| [**getGroupMembers()**](GroupsWorkspacesApi.md#getGroupMembers) | **GET** /api/v2.1/groups/{group_id}/members/ | Get Group Members |
| [**listGroups()**](GroupsWorkspacesApi.md#listGroups) | **GET** /api/v2.1/groups/ | List Groups |
| [**listWorkspaces()**](GroupsWorkspacesApi.md#listWorkspaces) | **GET** /api/v2.1/workspaces/ | List Workspaces |
| [**removeGroupMember()**](GroupsWorkspacesApi.md#removeGroupMember) | **DELETE** /api/v2.1/groups/{group_id}/members/{group_member}/ | Remove Group Member |
| [**searchGroup()**](GroupsWorkspacesApi.md#searchGroup) | **GET** /api/v2.1/search-group/ | Search Group |
| [**searchGroupMembers()**](GroupsWorkspacesApi.md#searchGroupMembers) | **GET** /api/v2.1/groups/{group_id}/search-member/ | Search Group Members |
| [**updateGroup()**](GroupsWorkspacesApi.md#updateGroup) | **PUT** /api/v2.1/groups/{group_id}/ | Update Group |
| [**updateGroupRole()**](GroupsWorkspacesApi.md#updateGroupRole) | **PUT** /api/v2.1/groups/{group_id}/members/{group_member}/ | Update Group Role |


## `addGroupMember()`

```php
addGroupMember($group_id, $add_group_member_request): object
```

Add Group Member

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int
$add_group_member_request = new \SeaTable\Client\User\AddGroupMemberRequest(); // \SeaTable\Client\User\AddGroupMemberRequest

try {
    $result = $apiInstance->addGroupMember($group_id, $add_group_member_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->addGroupMember: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **int**|  | |
| **add_group_member_request** | [**\SeaTable\Client\User\AddGroupMemberRequest**](../Model/AddGroupMemberRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `copyBaseFromExternalLink()`

```php
copyBaseFromExternalLink($link, $dst_workspace_id)
```

Copy Base from External Link

Copy a base from an external link to a workspace.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$link = 'link_example'; // string | Source external link.
$dst_workspace_id = 56; // int | Destination workspace's ID.

try {
    $apiInstance->copyBaseFromExternalLink($link, $dst_workspace_id);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->copyBaseFromExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **link** | **string**| Source external link. | [optional] |
| **dst_workspace_id** | **int**| Destination workspace&#39;s ID. | [optional] |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth




## `copyBaseFromWorkspace()`

```php
copyBaseFromWorkspace($src_workspace_id, $name, $dst_workspace_id): object
```

Copy Base from Workspace

Copy a base from a workspace to the destination workspace.  A workspace could be your own \"My library\", or a group's workspace. Therefore you need to define the `src_workspace_id` and `dst_workspace_id` in the call.   For the source workspace, you at least have to have the read permission of the base; for the source workspace, you must have write permission.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$src_workspace_id = 56; // int | Source workspace's ID.
$name = 'name_example'; // string | Name of the base.
$dst_workspace_id = 56; // int | Destination workspace's ID.

try {
    $result = $apiInstance->copyBaseFromWorkspace($src_workspace_id, $name, $dst_workspace_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->copyBaseFromWorkspace: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **src_workspace_id** | **int**| Source workspace&#39;s ID. | |
| **name** | **string**| Name of the base. | |
| **dst_workspace_id** | **int**| Destination workspace&#39;s ID. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `createGroup()`

```php
createGroup($create_group_request): object
```

Create Group

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$create_group_request = new \SeaTable\Client\User\CreateGroupRequest(); // \SeaTable\Client\User\CreateGroupRequest

try {
    $result = $apiInstance->createGroup($create_group_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->createGroup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_group_request** | [**\SeaTable\Client\User\CreateGroupRequest**](../Model/CreateGroupRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteGroup()`

```php
deleteGroup($group_id): object
```

Delete Group

Delete a group with its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int

try {
    $result = $apiInstance->deleteGroup($group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->deleteGroup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `getGroup()`

```php
getGroup($group_id): object
```

Get Group

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int

try {
    $result = $apiInstance->getGroup($group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->getGroup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `getGroupMembers()`

```php
getGroupMembers($group_id): object
```

Get Group Members

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int

try {
    $result = $apiInstance->getGroupMembers($group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->getGroupMembers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **int**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listGroups()`

```php
listGroups(): object
```

List Groups

Show a list of all groups of the user.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listGroups();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->listGroups: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listWorkspaces()`

```php
listWorkspaces($detail): object
```

List Workspaces

List all the workspaces/bases you have access to.  With the param `detail`, you can define if the returned list is with details (`true` or leave it by default) or without details (`false`). See the examples \"with detail=false\" and \"with detail=true\" for more information.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$detail = false; // bool | `true` or `false`, optional, `true` by default. When `false`, only the ID, name and type of each workspace is listed.

try {
    $result = $apiInstance->listWorkspaces($detail);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->listWorkspaces: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **detail** | **bool**| &#x60;true&#x60; or &#x60;false&#x60;, optional, &#x60;true&#x60; by default. When &#x60;false&#x60;, only the ID, name and type of each workspace is listed. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `removeGroupMember()`

```php
removeGroupMember($group_id, $group_member): object
```

Remove Group Member

Group admins can remove other group members or a group member can leave the group.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int
$group_member = 12345678-d378-4c12-8d7a-6da0fb48ee83; // string

try {
    $result = $apiInstance->removeGroupMember($group_id, $group_member);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->removeGroupMember: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **int**|  | |
| **group_member** | **string**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `searchGroup()`

```php
searchGroup($q): object
```

Search Group

Just give a search keyword in the `q` param.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$q = Micha; // string

try {
    $result = $apiInstance->searchGroup($q);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->searchGroup: ', $e->getMessage(), PHP_EOL;
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




## `searchGroupMembers()`

```php
searchGroupMembers($group_id, $q): object
```

Search Group Members

As a group's administrator, you can use this API call to search for members in this group.  Just give a search keyword in the `q` param. Attention: Although a fussy search is allowed, unlike the web interface, the search via API is still case sensitive! A successful search will return each member's details that fit to your search criteria. See example.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int
$q = Micha; // string

try {
    $result = $apiInstance->searchGroupMembers($group_id, $q);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->searchGroupMembers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **int**|  | |
| **q** | **string**|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateGroup()`

```php
updateGroup($group_id, $update_group_request): object
```

Update Group

Use this request to rename, and/or change owner of a group. In the request body, both parameters are optional. Only use the ones that you need to update: *   `owner` is the new owner of the group, include the user's ID here. If you don't want to change the owner, remove this parameter because if you enter the current owner's ID here, you'll get an error \"User xxx is already group owner\". *   `name` is the new name of your group. If you don't want to change the name, remove shi parameter because if you enter the current group name here you'll get an error \"There is already a group with that name\".

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int
$update_group_request = new \SeaTable\Client\User\UpdateGroupRequest(); // \SeaTable\Client\User\UpdateGroupRequest

try {
    $result = $apiInstance->updateGroup($group_id, $update_group_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->updateGroup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **int**|  | |
| **update_group_request** | [**\SeaTable\Client\User\UpdateGroupRequest**](../Model/UpdateGroupRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateGroupRole()`

```php
updateGroupRole($group_id, $group_member, $update_group_role_request): object
```

Update Group Role

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\GroupsWorkspacesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int
$group_member = 12345678-d378-4c12-8d7a-6da0fb48ee83; // string
$update_group_role_request = new \SeaTable\Client\User\UpdateGroupRoleRequest(); // \SeaTable\Client\User\UpdateGroupRoleRequest

try {
    $result = $apiInstance->updateGroupRole($group_id, $group_member, $update_group_role_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsWorkspacesApi->updateGroupRole: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **int**|  | |
| **group_member** | **string**|  | |
| **update_group_role_request** | [**\SeaTable\Client\User\UpdateGroupRoleRequest**](../Model/UpdateGroupRoleRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



