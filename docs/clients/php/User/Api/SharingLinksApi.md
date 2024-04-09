# SeaTable\Client\SharingLinksApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createBaseExternalLink()**](SharingLinksApi.md#createBaseExternalLink) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/external-links/ | Create Base External Link |
| [**createInviteLink()**](SharingLinksApi.md#createInviteLink) | **POST** /api/v2.1/dtables/invite-links/ | Create Invite Link |
| [**createViewExternalLink()**](SharingLinksApi.md#createViewExternalLink) | **POST** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/view-external-links/ | Create View External Link |
| [**deleteExternalLink()**](SharingLinksApi.md#deleteExternalLink) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/external-links/{external_link_token}/ | Delete External Link |
| [**deleteInviteLink()**](SharingLinksApi.md#deleteInviteLink) | **DELETE** /api/v2.1/dtables/invite-links/{invite_link_token}/ | Delete Invite Link |
| [**deleteViewExternalLink()**](SharingLinksApi.md#deleteViewExternalLink) | **DELETE** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/view-external-links/{view_external_link_token}/ | Delete View External Link |
| [**listBaseExternalLinks()**](SharingLinksApi.md#listBaseExternalLinks) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/external-links/ | List Base External Links |
| [**listViewExternalLinks()**](SharingLinksApi.md#listViewExternalLinks) | **GET** /api/v2.1/workspace/{workspace_id}/dtable/{base_name}/view-external-links/ | List View External Links |


## `createBaseExternalLink()`

```php
createBaseExternalLink($workspace_id, $base_name, $password, $expire_days, $token): object
```

Create Base External Link

Generate a read-only external link for a base.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$password = 'password_example'; // string
$expire_days = 56; // int | Add expiration period in days. Optional.
$token = 'token_example'; // string | An optional custom token of the generated link. For example, it'll appear as \\\"https<span>://cloud.seatable.io/dtable/view-external-links/custom/example/\\\". If not given, SeaTable will give a random token to the link.

try {
    $result = $apiInstance->createBaseExternalLink($workspace_id, $base_name, $password, $expire_days, $token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->createBaseExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **password** | **string**|  | [optional] |
| **expire_days** | **int**| Add expiration period in days. Optional. | [optional] |
| **token** | **string**| An optional custom token of the generated link. For example, it&#39;ll appear as \\\&quot;https&lt;span&gt;://cloud.seatable.io/dtable/view-external-links/custom/example/\\\&quot;. If not given, SeaTable will give a random token to the link. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `createInviteLink()`

```php
createInviteLink($table_name, $workspace_id, $permission, $password, $expire_days): object
```

Create Invite Link

Use this request to generate an invite link for your base. See below for the details for the params.  In the **response:**  *   If you have set a password, it won't be returned in the response. As soon as the response code is 200, your password has been successfully set. *   The `token` returned is the invite link's token. You'd need it in other requests like [Get Base-Token with Invite-Link](/reference/get_api-v2-1-dtable-share-link-access-token-1), or [Delete Invite Link](/reference/delete_api-v2-1-dtables-invite-links-invite-link-token-1).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$table_name = 'table_name_example'; // string | The name of the table.
$workspace_id = 'workspace_id_example'; // string | The workspace ID where your base is.
$permission = 'permission_example'; // string | `r` for read only or `rw` for read and write
$password = 'password_example'; // string
$expire_days = 56; // int | Add expiration period in days. Optional.

try {
    $result = $apiInstance->createInviteLink($table_name, $workspace_id, $permission, $password, $expire_days);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->createInviteLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table_name** | **string**| The name of the table. | [optional] |
| **workspace_id** | **string**| The workspace ID where your base is. | [optional] |
| **permission** | **string**| &#x60;r&#x60; for read only or &#x60;rw&#x60; for read and write | [optional] |
| **password** | **string**|  | [optional] |
| **expire_days** | **int**| Add expiration period in days. Optional. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `createViewExternalLink()`

```php
createViewExternalLink($workspace_id, $base_name, $table_id, $view_id, $token, $password, $expire_days): object
```

Create View External Link

Create a view external link from a view and optionally custom the link's token, password, permission and expiration days.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$table_id = 'table_id_example'; // string
$view_id = 'view_id_example'; // string
$token = 'token_example'; // string | An optional custom token of the generated link. For example, it'll appear as \\\"https<span>://cloud.seatable.io/dtable/view-external-links/custom/example/\\\". If not given, SeaTable will give a random token to the link.
$password = 'password_example'; // string
$expire_days = 56; // int | Add expiration period in days. Optional.

try {
    $result = $apiInstance->createViewExternalLink($workspace_id, $base_name, $table_id, $view_id, $token, $password, $expire_days);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->createViewExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **table_id** | **string**|  | [optional] |
| **view_id** | **string**|  | [optional] |
| **token** | **string**| An optional custom token of the generated link. For example, it&#39;ll appear as \\\&quot;https&lt;span&gt;://cloud.seatable.io/dtable/view-external-links/custom/example/\\\&quot;. If not given, SeaTable will give a random token to the link. | [optional] |
| **password** | **string**|  | [optional] |
| **expire_days** | **int**| Add expiration period in days. Optional. | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteExternalLink()`

```php
deleteExternalLink($workspace_id, $base_name, $external_link_token): object
```

Delete External Link

Delete a base external link by its token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$external_link_token = fleischkaesebroetchen; // string

try {
    $result = $apiInstance->deleteExternalLink($workspace_id, $base_name, $external_link_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->deleteExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **external_link_token** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteInviteLink()`

```php
deleteInviteLink($invite_link_token): object
```

Delete Invite Link

Delete an invite link via its `token`.  Deleting an invite link won't stop sharing the base with the other users. If you want to stop sharing it, you can  *   either use the base sharing dialogue on the web interface to stop sharing the base to certain users, or *   use the API request to [Stop Sharing Base to a user](/reference/delete_api-v2-1-workspace-workspace-id-dtable-base-name-share-1).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$invite_link_token = 65432148a9074901923d; // string

try {
    $result = $apiInstance->deleteInviteLink($invite_link_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->deleteInviteLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **invite_link_token** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteViewExternalLink()`

```php
deleteViewExternalLink($workspace_id, $base_name, $view_external_link_token): object
```

Delete View External Link

Delete a view external link by its token. This token could be a custom token or a random token. Include the token in the URL, in this example, it's `example`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.
$view_external_link_token = f234baec8ce44028978a; // string

try {
    $result = $apiInstance->deleteViewExternalLink($workspace_id, $base_name, $view_external_link_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->deleteViewExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base. | |
| **view_external_link_token** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listBaseExternalLinks()`

```php
listBaseExternalLinks($workspace_id, $base_name): object
```

List Base External Links

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listBaseExternalLinks($workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->listBaseExternalLinks: ', $e->getMessage(), PHP_EOL;
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

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listViewExternalLinks()`

```php
listViewExternalLinks($table_id, $view_id, $workspace_id, $base_name): object
```

List View External Links

List all the external links generated for a specific view with the table's and the view's IDs.    Normally when you open a view in the browser, you can see the `tid` and `vid` in the address line, which are indeed the `table_id` and `view_id` here.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$table_id = 0000; // string | The id of the table. The id of a table is unique inside a base and is often used to identify a table. **Important: the table_id is not the table_name**.
$view_id = Jz4d; // string | id of view, string
$workspace_id = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base.

try {
    $result = $apiInstance->listViewExternalLinks($table_id, $view_id, $workspace_id, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->listViewExternalLinks: ', $e->getMessage(), PHP_EOL;
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

[AccountTokenAuth](../../README.md#AccountTokenAuth)


