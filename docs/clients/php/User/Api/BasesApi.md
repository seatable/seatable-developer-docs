# SeaTable\Client\BasesApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**basePassword()**](BasesApi.md#basePassword) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/password/ | Base Password |
| [**clearTrash()**](BasesApi.md#clearTrash) | **DELETE** /api/v2.1/trash-dtables/ | Clear Trash |
| [**createBase()**](BasesApi.md#createBase) | **POST** /api/v2.1/dtables/ | Create Base |
| [**createFolder()**](BasesApi.md#createFolder) | **POST** /api/v2.1/workspace/{workspace_id}/folders/ | Create Folder |
| [**deleteBase()**](BasesApi.md#deleteBase) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/ | Delete Base |
| [**deleteFolder()**](BasesApi.md#deleteFolder) | **DELETE** /api/v2.1/workspace/{workspace_id}/folders/{folder_id}/ | Delete Folder |
| [**favoriteBase()**](BasesApi.md#favoriteBase) | **POST** /api/v2.1/starred-dtables/ | Favorite Base |
| [**listBases()**](BasesApi.md#listBases) | **GET** /api/v2.1/user-admin-dtables/ | List Bases |
| [**listFavorites()**](BasesApi.md#listFavorites) | **GET** /api/v2.1/starred-dtables/ | List Favorites |
| [**listGroupTrashedBases()**](BasesApi.md#listGroupTrashedBases) | **GET** /api/v2.1/groups/{group_id}/trash-dtables/ | List Group Trashed Bases |
| [**listTrashedBases()**](BasesApi.md#listTrashedBases) | **GET** /api/v2.1/trash-dtables/ | List Trashed Bases |
| [**moveBaseIntoFolder()**](BasesApi.md#moveBaseIntoFolder) | **POST** /api/v2.1/workspace/{workspace_id}/folder-item-moving/ | Move Base into Folder |
| [**restoreGroupTrashedBase()**](BasesApi.md#restoreGroupTrashedBase) | **PUT** /api/v2.1/groups/{group_id}/trash-dtables/{base_uuid}/ | Restore Group Trashed Base |
| [**restoreTrashedBase()**](BasesApi.md#restoreTrashedBase) | **PUT** /api/v2.1/trash-dtables/{trashed_base_id}/ | Restore Trashed Base |
| [**searchBaseOrApps()**](BasesApi.md#searchBaseOrApps) | **GET** /api/v2.1/dtable/items-search/ | Search base or apps |
| [**unfavoriteBase()**](BasesApi.md#unfavoriteBase) | **DELETE** /api/v2.1/starred-dtables/ | Unfavorite Base |
| [**updateBase()**](BasesApi.md#updateBase) | **PUT** /api/v2.1/workspace/{workspace_id}/dtable/ | Update Base |
| [**updateFolder()**](BasesApi.md#updateFolder) | **PUT** /api/v2.1/workspace/{workspace_id}/folders/{folder_id}/ | Update Folder |


## `basePassword()`

```php
basePassword($workspace_id, $base_name, $base_password_request): object
```

Base Password

Use this request to unset a base password. You'll need to enter the current password `password` to be able to unset it. After unsetting a password, the base is not protected by a password anymore (the `is_encrypted` is not `false`).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$base_password_request = new \SeaTable\Client\User\BasePasswordRequest(); // \SeaTable\Client\User\BasePasswordRequest

try {
    $result = $apiInstance->basePassword($workspace_id, $base_name, $base_password_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->basePassword: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **base_password_request** | [**\SeaTable\Client\User\BasePasswordRequest**](../Model/BasePasswordRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `clearTrash()`

```php
clearTrash(): object
```

Clear Trash

By cleaning the trash bin, all the bases there will be removed permanently and cannot be restored any more.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->clearTrash();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->clearTrash: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `createBase()`

```php
createBase($name, $workspace_id, $icon, $color): object
```

Create Base

Create a new base.   When you create a new base with this API request or on the web UI, SeaTable automatically adds the following content into the new base:  - A new table \"Table1\" (with the `table_id` of `0000`), and - A \"Default View\" (with the `view_id` of `0000`), and - A new text column \"Name\" (with the column's `key` of `0000`); - Three empty rows (The row's IDs are randomly generated. Use the call [List Rows](/reference/get_dtable-server-api-v1-dtables-base-uuid-rows-1) to see their IDs).       Optionally, you can select icons and colors from the following list to customize your base's icon in the web UI:  **SeaTable base icon list**  ``` DTABLE_ICON_LIST = [   'icon-worksheet',   'icon-task-management',   'icon-software-test-management',   'icon-design-assignment',   'icon-video-production',   'icon-market-analysis',   'icon-data-analysis',   'icon-product-knowledge-base',   'icon-asset-management',   'icon-financial-information-record',   'icon-dollar',   'icon-company-inventory',   'icon-customer-inquiry',   'icon-customer-list',   'icon-product-list',   'icon-store-address',   'icon-leave-record',   'icon-administrative-matters-calendar',   'icon-customer-relationship',   'icon-teachers-list',   'icon-book-library',   'icon-server-management',   'icon-time-management',   'icon-work-log',   'icon-online-promotion',   'icon-research',   'icon-user-interview',   'icon-client-review',   'icon-club-members', ]  ```  **SeaTable base icon color list**  ``` DTABLE_ICON_COLORS = [   '#FF8000',   '#FFB600',   '#E91E63',   '#EB00B1',   '#7626FD',   '#972CB0',   '#1DDD1D',   '#4CAF50',   '#02C0FF',   '#00C9C7',   '#1688FC',   '#656463' ]  ```  You can create a base in your personal workspace (\"My bases\"), or in a group you have write permission to. Just specify the optional `workspace_id` parameter in the request.  The returned `id` value is the ID of your base, this numeric ID is to be distinguished from the base's UUID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$name = 'name_example'; // string
$workspace_id = 'workspace_id_example'; // string | The workspace ID where your base is.
$icon = 'icon_example'; // string | The icon of the base. Optional. Refer to [\\\"Create A Base\\\"](/reference/post_api-v2-1-dtables) for the list of available icons.
$color = 'color_example'; // string | The icon color of the base. Optional. Refer to [\\\"Create A Base\\\"](/reference/post_api-v2-1-dtables) for the list of available icon colors.

try {
    $result = $apiInstance->createBase($name, $workspace_id, $icon, $color);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->createBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**|  | [optional] |
| **workspace_id** | **string**| The workspace ID where your base is. | [optional] |
| **icon** | **string**| The icon of the base. Optional. Refer to [\\\&quot;Create A Base\\\&quot;](/reference/post_api-v2-1-dtables) for the list of available icons. | [optional] |
| **color** | **string**| The icon color of the base. Optional. Refer to [\\\&quot;Create A Base\\\&quot;](/reference/post_api-v2-1-dtables) for the list of available icon colors. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `createFolder()`

```php
createFolder($workspace_id, $name): object
```

Create Folder

With this request, you can create a base folder easily with the desired `name` of your folder. In the response body, the `id` will be the ID of your folder. You'll need this specific ID to move bases into this folder or update, or delete this folder.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$name = 'name_example'; // string | Name of your folder. If the name already exists in the workspace, the system will add a \\\"(1)\\\" to it.

try {
    $result = $apiInstance->createFolder($workspace_id, $name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->createFolder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **name** | **string**| Name of your folder. If the name already exists in the workspace, the system will add a \\\&quot;(1)\\\&quot; to it. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteBase()`

```php
deleteBase($workspace_id): object
```

Delete Base

Delete an existing base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.

try {
    $result = $apiInstance->deleteBase($workspace_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->deleteBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteFolder()`

```php
deleteFolder($workspace_id, $folder_id): object
```

Delete Folder

You can only delete a folder when it's empty. To do so, first move your bases out of it and then delete it with its `folder_id` in this request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$folder_id = 'folder_id_example'; // string

try {
    $result = $apiInstance->deleteFolder($workspace_id, $folder_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->deleteFolder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **folder_id** | **string**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `favoriteBase()`

```php
favoriteBase($dtable_uuid): object
```

Favorite Base

Add a star to a base to make it a \"favorite\" base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$dtable_uuid = 'dtable_uuid_example'; // string | The UUID of the base.

try {
    $result = $apiInstance->favoriteBase($dtable_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->favoriteBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dtable_uuid** | **string**| The UUID of the base. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listBases()`

```php
listBases(): object
```

List Bases

List all the bases that the current user can administer. These include: - All the bases in the user's personal workspace; - All the bases in the groups where the current user is an owner or an admin. Each base's details are included in an object in the returned `dtables` array.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listBases();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listBases: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listFavorites()`

```php
listFavorites(): object
```

List Favorites

List all the starred (favorite) bases in my library.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listFavorites();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listFavorites: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listGroupTrashedBases()`

```php
listGroupTrashedBases($group_id): object
```

List Group Trashed Bases

When a group base is deleted, it's sent to the group's trash bin. If you are the owner or administrator of this group, you have access to the group's trash bin.  Use this API request to take a look into your group's trash bin. You'll get a permission error if you are not the owner or admin of this group.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int

try {
    $result = $apiInstance->listGroupTrashedBases($group_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listGroupTrashedBases: ', $e->getMessage(), PHP_EOL;
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




## `listTrashedBases()`

```php
listTrashedBases($page, $per_page): object
```

List Trashed Bases

List all the bases in the trash bin.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$page = 1; // int
$per_page = 2; // int

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
| **page** | **int**|  | [optional] |
| **per_page** | **int**|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `moveBaseIntoFolder()`

```php
moveBaseIntoFolder($workspace_id, $item_type, $item_id, $from, $to): object
```

Move Base into Folder

Move your base from one folder to another by giving the `folder_id` of your source and target folders. Exception: the root folder doesn't have an ID, but can be identified with '/'. See example.  All the parameters in this request are required, as we might allow you to move folders into folders in the future, by then, you will be able to use another parameter in the `item_type`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$item_type = 'item_type_example'; // string | Required.
$item_id = 'item_id_example'; // string | When moving a base, use its `UUID`. Required.
$from = 'from_example'; // string | From which folder are you moving the base out of? If from the root, use '/'. Otherwise use a `folder_id`. Required.
$to = 'to_example'; // string | The ID of the target folder. Required.

try {
    $result = $apiInstance->moveBaseIntoFolder($workspace_id, $item_type, $item_id, $from, $to);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->moveBaseIntoFolder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **item_type** | **string**| Required. | [optional] |
| **item_id** | **string**| When moving a base, use its &#x60;UUID&#x60;. Required. | [optional] |
| **from** | **string**| From which folder are you moving the base out of? If from the root, use &#39;/&#39;. Otherwise use a &#x60;folder_id&#x60;. Required. | [optional] |
| **to** | **string**| The ID of the target folder. Required. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `restoreGroupTrashedBase()`

```php
restoreGroupTrashedBase($group_id, $base_uuid): object
```

Restore Group Trashed Base

With the UUID (retrievable with the previous call) of the trashed base, you can restore it with this request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$group_id = 1; // int
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->restoreGroupTrashedBase($group_id, $base_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->restoreGroupTrashedBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **int**|  | |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `restoreTrashedBase()`

```php
restoreTrashedBase($trashed_base_id): object
```

Restore Trashed Base

Restore a trashed base from the trash bin. The base's ID can be retrieved from the call [List Trashed Bases](/reference/get_api-v2-1-trash-dtables-1). The base's ID is written directly in the URL, like in this example, `497`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$trashed_base_id = 497; // int | The ID of the trashed base.

try {
    $result = $apiInstance->restoreTrashedBase($trashed_base_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->restoreTrashedBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **trashed_base_id** | **int**| The ID of the trashed base. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `searchBaseOrApps()`

```php
searchBaseOrApps($query_str, $query_type): object
```

Search base or apps

Search the base or apps of a user. Capitalization is irrelevant for the search and substrings are also allowed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$query_str = test; // string | Search string. Substrings are allowed and capitalization does not matter.
$query_type = 'query_type_example'; // string

try {
    $result = $apiInstance->searchBaseOrApps($query_str, $query_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->searchBaseOrApps: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **query_str** | **string**| Search string. Substrings are allowed and capitalization does not matter. | [optional] |
| **query_type** | **string**|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `unfavoriteBase()`

```php
unfavoriteBase($dtable_uuid): object
```

Unfavorite Base

Remove the star of a base and therefore removing it from \"Favorites\".

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$dtable_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $result = $apiInstance->unfavoriteBase($dtable_uuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->unfavoriteBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dtable_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateBase()`

```php
updateBase($workspace_id, $name, $new_name, $icon, $color): object
```

Update Base

Update a base's name, icon, and icon color.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$name = 'name_example'; // string | The old name of the base. Required.
$new_name = 'new_name_example'; // string | The new name of the base. Optional.
$icon = 'icon_example'; // string | The icon of the base. Optional. Refer to [\\\"Create A Base\\\"](/reference/post_api-v2-1-dtables) for the list of available icons.
$color = 'color_example'; // string | The icon color of the base. Optional. Refer to [\\\"Create A Base\\\"](/reference/post_api-v2-1-dtables) for the list of available icon colors.

try {
    $result = $apiInstance->updateBase($workspace_id, $name, $new_name, $icon, $color);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->updateBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **name** | **string**| The old name of the base. Required. | [optional] |
| **new_name** | **string**| The new name of the base. Optional. | [optional] |
| **icon** | **string**| The icon of the base. Optional. Refer to [\\\&quot;Create A Base\\\&quot;](/reference/post_api-v2-1-dtables) for the list of available icons. | [optional] |
| **color** | **string**| The icon color of the base. Optional. Refer to [\\\&quot;Create A Base\\\&quot;](/reference/post_api-v2-1-dtables) for the list of available icon colors. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateFolder()`

```php
updateFolder($workspace_id, $folder_id, $name): object
```

Update Folder

Use this request to rename an existing folder with its `folder_id`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$folder_id = 'folder_id_example'; // string
$name = 'name_example'; // string | Name of your folder. If the name already exists in the workspace, the system will add a \\\"(1)\\\" to it.

try {
    $result = $apiInstance->updateFolder($workspace_id, $folder_id, $name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->updateFolder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **folder_id** | **string**|  | |
| **name** | **string**| Name of your folder. If the name already exists in the workspace, the system will add a \\\&quot;(1)\\\&quot; to it. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



