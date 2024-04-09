# SeaTable\Client\TeamsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method                                                         | HTTP request                                                         | Description            |
| -------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------------- |
| [**addTeam()**](TeamsApi.md#addTeam)                           | **POST** /api/v2.1/admin/organizations/                              | Add Team               |
| [**addTeamUser()**](TeamsApi.md#addTeamUser)                   | **POST** /api/v2.1/admin/organizations/{org_id}/users/               | Add Team User          |
| [**deleteTeam()**](TeamsApi.md#deleteTeam)                     | **DELETE** /api/v2.1/admin/organizations/{org_id}/                   | Delete Team            |
| [**deleteTeamGroup()**](TeamsApi.md#deleteTeamGroup)           | **DELETE** /api/v2.1/admin/organizations/{org_id}/groups/{group_id}/ | Delete Group           |
| [**deleteTeamUser()**](TeamsApi.md#deleteTeamUser)             | **DELETE** /api/v2.1/admin/organizations/{org_id}/users/{user_id}/   | Delete Team User       |
| [**getOrganizationNames()**](TeamsApi.md#getOrganizationNames) | **GET** /api/v2.1/admin/organizations-basic-info/                    | Get Organization Names |
| [**listTeamBases()**](TeamsApi.md#listTeamBases)               | **GET** /api/v2.1/admin/organizations/{org_id}/dtables/              | List Team Bases        |
| [**listTeamGroups()**](TeamsApi.md#listTeamGroups)             | **GET** /api/v2.1/admin/organizations/{org_id}/groups/               | List Team Groups       |
| [**listTeamUsers()**](TeamsApi.md#listTeamUsers)               | **GET** /api/v2.1/admin/organizations/{org_id}/users/                | List Team Users        |
| [**listTeams()**](TeamsApi.md#listTeams)                       | **GET** /api/v2.1/admin/organizations/                               | List Teams             |
| [**searchTeam()**](TeamsApi.md#searchTeam)                     | **GET** /api/v2.1/admin/organizations/{org_id}/                      | Search Team            |
| [**updateTeam()**](TeamsApi.md#updateTeam)                     | **PUT** /api/v2.1/admin/organizations/{org_id}/                      | Update Team            |
| [**updateTeamUser()**](TeamsApi.md#updateTeamUser)             | **PUT** /api/v2.1/admin/organizations/{org_id}/users/{user_id}/      | Update Team User       |

## `addTeam()`

```php
addTeam($add_team_request): object
```

Add Team

Add a team (organization) with its name and admin credentials. In the request body, define the new team admin's `admin_email`, `admin_name` and `password`. SeaTable does not automatically create a workspace for a newly added user: the `with_workspace` parameter is `false` by default. If you would like your new user to have a workspace when they are added (so that they can start operating workspaces and bases right away with API requests), make sure you set `true` for this parameter. Otherwise, their workspace will only be created when they login to the SeaTable web interface for the first time.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$add_team_request = new \SeaTable\Client\SysAdmin/Model\AddTeamRequest(); // \SeaTable\Client\SysAdmin/Model\AddTeamRequest

try {
    $result = $apiInstance->addTeam($add_team_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->addTeam: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name                 | Type                                                                             | Description | Notes      |
| -------------------- | -------------------------------------------------------------------------------- | ----------- | ---------- |
| **add_team_request** | [**\SeaTable\Client\SysAdmin/Model\AddTeamRequest**](../Model/AddTeamRequest.md) |             | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth

## `addTeamUser()`

```php
addTeamUser($org_id, $add_team_user_request): object
```

Add Team User

Add a new team user with desired details. In the request body: \\_ `email` is the contact email address of your new user; \\_ `password` could be an initial login password you asign to them; \\_ `name` is the display name of your new user; \\_ `with_workspace` should be set to `true` if you want your new user to acquire a `workspace_id` immediately after adding them. The default value is `false`, which means they won't have a `workspace_id` until they login for the first time.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$add_team_user_request = new \SeaTable\Client\SysAdmin/Model\AddTeamUserRequest(); // \SeaTable\Client\SysAdmin/Model\AddTeamUserRequest

try {
    $result = $apiInstance->addTeamUser($org_id, $add_team_user_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->addTeamUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name                      | Type                                                                                     | Description                                                                                                                            | Notes      |
| ------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **org_id**                | **int**                                                                                  | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |            |
| **add_team_user_request** | [**\SeaTable\Client\SysAdmin/Model\AddTeamUserRequest**](../Model/AddTeamUserRequest.md) |                                                                                                                                        | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth

## `deleteTeam()`

```php
deleteTeam($org_id): object
```

Delete Team

Delete a team (organization) with its ID. This will eliminate the team! However, this won't delete the team users - but all its members will become team-less users in the system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $result = $apiInstance->deleteTeam($org_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->deleteTeam: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name       | Type    | Description                                                                                                                            | Notes |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **org_id** | **int** | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |       |

### Return type

**object**

### Authorization

AccountTokenAuth

## `deleteTeamGroup()`

```php
deleteTeamGroup($org_id, $group_id): object
```

Delete Group

Delete a group with its group_id. As system administrator, you can delete any group in the system by their ID, no matter in which team they are.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$group_id = 48; // int

try {
    $result = $apiInstance->deleteTeamGroup($org_id, $group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->deleteTeamGroup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name         | Type    | Description                                                                                                                            | Notes |
| ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **org_id**   | **int** | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |       |
| **group_id** | **int** |                                                                                                                                        |       |

### Return type

**object**

### Authorization

AccountTokenAuth

## `deleteTeamUser()`

```php
deleteTeamUser($org_id, $user_id): object
```

Delete Team User

Delete a team user with this request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.

try {
    $result = $apiInstance->deleteTeamUser($org_id, $user_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->deleteTeamUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name        | Type       | Description                                                                                                                            | Notes |
| ----------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **org_id**  | **int**    | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |       |
| **user_id** | **string** | The unique user id in the form ...@auth.local. This is not the email address of the user.                                              |       |

### Return type

**object**

### Authorization

AccountTokenAuth

## `getOrganizationNames()`

```php
getOrganizationNames($org_ids)
```

Get Organization Names

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_ids = 2; // string[]

try {
    $apiInstance->getOrganizationNames($org_ids);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->getOrganizationNames: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name        | Type         | Description | Notes      |
| ----------- | ------------ | ----------- | ---------- |
| **org_ids** | **string[]** |             | [optional] |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth

## `listTeamBases()`

```php
listTeamBases($org_id, $page, $per_page): object
```

List Team Bases

List all the bases of a team. As system administrator, you can see the information of these bases, but you do not have access to the data inside of them.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listTeamBases($org_id, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->listTeamBases: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name         | Type    | Description                                                                                                                            | Notes      |
| ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **org_id**   | **int** | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |            |
| **page**     | **int** | The page number you want to start showing the entries. If no value is provided, 1 will be used.                                        | [optional] |
| **per_page** | **int** | The number of results that should be returned. If no value is provided, 25 results will be returned.                                   | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth

## `listTeamGroups()`

```php
listTeamGroups($org_id): object
```

List Team Groups

List all the groups in a team with its `org_id`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $result = $apiInstance->listTeamGroups($org_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->listTeamGroups: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name       | Type    | Description                                                                                                                            | Notes |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **org_id** | **int** | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |       |

### Return type

**object**

### Authorization

AccountTokenAuth

## `listTeamUsers()`

```php
listTeamUsers($org_id): object
```

List Team Users

List a team's members with their detailed information. The `is_org_admin` value in the response indicates if this member is the administrator of the team.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $result = $apiInstance->listTeamUsers($org_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->listTeamUsers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name       | Type    | Description                                                                                                                            | Notes |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **org_id** | **int** | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |       |

### Return type

**object**

### Authorization

AccountTokenAuth

## `listTeams()`

```php
listTeams($page, $per_page, $role): object
```

List Teams

List all the current teams (organizations) in the system. Use the `role` filter to only return a type of teams. The exact roles depend on your configuration.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.
$role = default; // string | Optional. When left blank, all role types are returned.

try {
    $result = $apiInstance->listTeams($page, $per_page, $role);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->listTeams: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name         | Type       | Description                                                                                          | Notes      |
| ------------ | ---------- | ---------------------------------------------------------------------------------------------------- | ---------- |
| **page**     | **int**    | The page number you want to start showing the entries. If no value is provided, 1 will be used.      | [optional] |
| **per_page** | **int**    | The number of results that should be returned. If no value is provided, 25 results will be returned. | [optional] |
| **role**     | **string** | Optional. When left blank, all role types are returned.                                              | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth

## `searchTeam()`

```php
searchTeam($org_id): object
```

Search Team

As system administrator, you can query a team by its `org_id` with this API request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $result = $apiInstance->searchTeam($org_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->searchTeam: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name       | Type    | Description                                                                                                                            | Notes |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **org_id** | **int** | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |       |

### Return type

**object**

### Authorization

AccountTokenAuth

## `updateTeam()`

```php
updateTeam($org_id, $update_team_request): object
```

Update Team

Change an organization's attributes.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$update_team_request = new \SeaTable\Client\SysAdmin/Model\UpdateTeamRequest(); // \SeaTable\Client\SysAdmin/Model\UpdateTeamRequest

try {
    $result = $apiInstance->updateTeam($org_id, $update_team_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->updateTeam: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name                    | Type                                                                                   | Description                                                                                                                            | Notes      |
| ----------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **org_id**              | **int**                                                                                | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |            |
| **update_team_request** | [**\SeaTable\Client\SysAdmin/Model\UpdateTeamRequest**](../Model/UpdateTeamRequest.md) |                                                                                                                                        | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth

## `updateTeamUser()`

```php
updateTeamUser($org_id, $user_id, $update_team_user_request): object
```

Update Team User

The system admin can authorize a regular team member to have team admin rights.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\TeamsApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$user_id = 23abc456def789ghi123jkl456mno789@auth.local; // string | The unique user id in the form ...@auth.local. This is not the email address of the user.
$update_team_user_request = new \SeaTable\Client\SysAdmin/Model\UpdateTeamUserRequest(); // \SeaTable\Client\SysAdmin/Model\UpdateTeamUserRequest

try {
    $result = $apiInstance->updateTeamUser($org_id, $user_id, $update_team_user_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TeamsApi->updateTeamUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name                         | Type                                                                                           | Description                                                                                                                            | Notes      |
| ---------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **org_id**                   | **int**                                                                                        | The id of your team/organization. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. |            |
| **user_id**                  | **string**                                                                                     | The unique user id in the form ...@auth.local. This is not the email address of the user.                                              |            |
| **update_team_user_request** | [**\SeaTable\Client\SysAdmin/Model\UpdateTeamUserRequest**](../Model/UpdateTeamUserRequest.md) |                                                                                                                                        | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth
