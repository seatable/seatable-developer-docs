# SeaTable\Client\GroupsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addGroup()**](GroupsApi.md#addGroup) | **POST** /api/v2.1/org/{org_id}/admin/groups/ | Add Group |
| [**addGroupMembers()**](GroupsApi.md#addGroupMembers) | **POST** /api/v2.1/org/{org_id}/admin/groups/{group_id}/members/ | Add Group Members |
| [**deleteGroup()**](GroupsApi.md#deleteGroup) | **DELETE** /api/v2.1/org/{org_id}/admin/groups/{group_id}/ | Delete Group |
| [**getGroup()**](GroupsApi.md#getGroup) | **GET** /api/v2.1/org/{org_id}/admin/groups/{group_id}/ | Get Group |
| [**listGroupBases()**](GroupsApi.md#listGroupBases) | **GET** /api/v2.1/org/{org_id}/admin/groups/{group_id}/dtables/ | List Group Bases |
| [**listGroupMembers()**](GroupsApi.md#listGroupMembers) | **GET** /api/v2.1/org/{org_id}/admin/groups/{group_id}/members/ | List Group Members |
| [**listGroups()**](GroupsApi.md#listGroups) | **GET** /api/v2.1/org/{org_id}/admin/groups/ | List Groups (Team) |
| [**orderGroups()**](GroupsApi.md#orderGroups) | **PUT** /api/v2.1/groups/move-group/ | Re-order Your Groups |
| [**removeGroupMembers()**](GroupsApi.md#removeGroupMembers) | **DELETE** /api/v2.1/org/{org_id}/admin/groups/{group_id}/members/{user_id}/ | Remove Group Members |
| [**updateGroup()**](GroupsApi.md#updateGroup) | **PUT** /api/v2.1/org/{org_id}/admin/groups/{group_id}/ | Update Group |


## `addGroup()`

```php
addGroup($org_id, $group_name, $group_owner): object
```

Add Group

Add a group in the current organization and assign a group name, and a group owner.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$group_name = 'group_name_example'; // string | The name of the group.
$group_owner = 'group_owner_example'; // string | The `user_id` of the owner of the group. Optional. If left blank, the newly added group will not be visible to anyone but still operatable.

try {
    $result = $apiInstance->addGroup($org_id, $group_name, $group_owner);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->addGroup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **group_name** | **string**| The name of the group. | [optional] |
| **group_owner** | **string**| The &#x60;user_id&#x60; of the owner of the group. Optional. If left blank, the newly added group will not be visible to anyone but still operatable. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `addGroupMembers()`

```php
addGroupMembers($org_id, $group_id, $user_id): object
```

Add Group Members

Add multiple members to a group in one call.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$group_id = 1; // int | The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team).
$user_id = 'user_id_example'; // string | The `user_id`

try {
    $result = $apiInstance->addGroupMembers($org_id, $group_id, $user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->addGroupMembers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **group_id** | **int**| The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team). | |
| **user_id** | **string**| The &#x60;user_id&#x60; | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteGroup()`

```php
deleteGroup($org_id, $group_id): object
```

Delete Group

Delete a group with its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$group_id = 1; // int | The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team).

try {
    $result = $apiInstance->deleteGroup($org_id, $group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->deleteGroup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **group_id** | **int**| The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team). | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `getGroup()`

```php
getGroup($org_id, $group_id): object
```

Get Group

Get the specific information of one group by its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$group_id = 1; // int | The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team).

try {
    $result = $apiInstance->getGroup($org_id, $group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->getGroup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **group_id** | **int**| The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team). | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listGroupBases()`

```php
listGroupBases($org_id, $group_id): object
```

List Group Bases

List all the bases in a specific group in your team.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$group_id = 1; // int | The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team).

try {
    $result = $apiInstance->listGroupBases($org_id, $group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->listGroupBases: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **group_id** | **int**| The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team). | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listGroupMembers()`

```php
listGroupMembers($org_id, $group_id): object
```

List Group Members

List the members of a group in the current team (organization).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$group_id = 1; // int | The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team).

try {
    $result = $apiInstance->listGroupMembers($org_id, $group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->listGroupMembers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **group_id** | **int**| The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team). | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listGroups()`

```php
listGroups($org_id, $page, $per_page): object
```

List Groups (Team)

List all the groups existing in your team (organization). In the response, each group's ID, name, created time, name,creator etc. are returned. The `page_next` value indicates if there is a next page or not.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listGroups($org_id, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->listGroups: ', $e->getMessage(), PHP_EOL;
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




## `orderGroups()`

```php
orderGroups($group_id, $anchor_group_id, $to_last): object
```

Re-order Your Groups

On the **web user interface**, you can have an overview of all the groups you are currently in on the left-hand side navigation when you click on \"Bases\". Perhaps you'd like to re-order these groups. Besides moving them manually with your mouse on the interface, you can also use this API request to do the same job. Here's how it works: In the request form, give the `group_id` of the group you'd like to move and tell the system where to move it to: under which group ( `anchor_group_id` ). If you are just moving it to the bottom of the list, let `to_last` be `true` .

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 'group_id_example'; // string | The ID of the group you'd like to move.
$anchor_group_id = 'anchor_group_id_example'; // string | The ID of the group where you'd like your group to be moved under.
$to_last = True; // bool | Whether you'd like to move your group to the bottom of the list (`true`). `false` by default.

try {
    $result = $apiInstance->orderGroups($group_id, $anchor_group_id, $to_last);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->orderGroups: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **string**| The ID of the group you&#39;d like to move. | [optional] |
| **anchor_group_id** | **string**| The ID of the group where you&#39;d like your group to be moved under. | [optional] |
| **to_last** | **bool**| Whether you&#39;d like to move your group to the bottom of the list (&#x60;true&#x60;). &#x60;false&#x60; by default. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `removeGroupMembers()`

```php
removeGroupMembers($org_id, $group_id, $user_id): object
```

Remove Group Members

Move a member out of a group. The group's owner cannot be removed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$group_id = 1; // int | The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team).
$user_id = 123456789f1e4c8d8e1c31415867317c@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.

try {
    $result = $apiInstance->removeGroupMembers($org_id, $group_id, $user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->removeGroupMembers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **group_id** | **int**| The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team). | |
| **user_id** | **string**| The unique user id in the form ...@auth.local. This is not the email address of the user. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateGroup()`

```php
updateGroup($org_id, $group_id, $update_group_request): object
```

Update Group

Use this request to rename, and/or change owner of a group. In the request body, both parameters are optional. Only use the ones that you need to update: *   `new_owner` is the new owner of the group, include the user's ID here. If you don't want to change the owner, remove this parameter because if you enter the current owner's ID here, you'll get an error \"User xxx is already group owner\". *   `new_group_name` is the new name of your group. If you don't want to change the name, remove shi parameter because if you enter the current group name here you'll get an error \"There is already a group with that name\".

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\GroupsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$group_id = 1; // int | The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team).
$update_group_request = new \SeaTable\Client\TeamAdmin\UpdateGroupRequest(); // \SeaTable\Client\TeamAdmin\UpdateGroupRequest

try {
    $result = $apiInstance->updateGroup($org_id, $group_id, $update_group_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->updateGroup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **group_id** | **int**| The ID of the group to query. Can be retrieved from the call [List Groups in Your Team](/reference/list-groups-team). | |
| **update_group_request** | [**\SeaTable\Client\TeamAdmin\UpdateGroupRequest**](../Model/UpdateGroupRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



