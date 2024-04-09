# SeaTable\Client\SharingLinksApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteExternalLink()**](SharingLinksApi.md#deleteExternalLink) | **DELETE** /api/v2.1/org/{org_id}/admin/external-links/{external_link_token}/ | Delete External Link |
| [**deleteInviteLink()**](SharingLinksApi.md#deleteInviteLink) | **DELETE** /api/v2.1/org/{org_id}/admin/invite-links/{invite_link_token}/ | Delete Invite Link |
| [**deleteViewExternalLink()**](SharingLinksApi.md#deleteViewExternalLink) | **DELETE** /api/v2.1/org/{org_id}/admin/view-external-links/{view_external_link_token}/ | Delete View External Link |
| [**listBaseExternalLinks()**](SharingLinksApi.md#listBaseExternalLinks) | **GET** /api/v2.1/org/{org_id}/admin/external-links/ | List Base External Links |
| [**listInviteLinks()**](SharingLinksApi.md#listInviteLinks) | **GET** /api/v2.1/org/{org_id}/admin/invite-links/ | List Invite Links |
| [**listViewExternalLinks()**](SharingLinksApi.md#listViewExternalLinks) | **GET** /api/v2.1/org/{org_id}/admin/view-external-links/ | List View External Links |
| [**updateInviteLink()**](SharingLinksApi.md#updateInviteLink) | **PUT** /api/v2.1/org/{org_id}/admin/invite-links/{invite_link_token}/ | Update Invite Link |


## `deleteExternalLink()`

```php
deleteExternalLink($org_id, $external_link_token): object
```

Delete External Link

Delete an external link with its token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$external_link_token = d6d006b319ca4d2aa060; // string

try {
    $result = $apiInstance->deleteExternalLink($org_id, $external_link_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->deleteExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **external_link_token** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteInviteLink()`

```php
deleteInviteLink($org_id, $invite_link_token): object
```

Delete Invite Link

Delete an invite link with this request. The `invite_link_token` can be retrieved from the previous calls, or simply from the URL of the invite link, which is the last part of the URL.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$invite_link_token = 0366b8995d7f47d8eu3t; // string

try {
    $result = $apiInstance->deleteInviteLink($org_id, $invite_link_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->deleteInviteLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **invite_link_token** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteViewExternalLink()`

```php
deleteViewExternalLink($org_id, $view_external_link_token): object
```

Delete View External Link

Use this request to delete an existing view external link with its token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$view_external_link_token = d6d006b319ca4d2aa060; // string

try {
    $result = $apiInstance->deleteViewExternalLink($org_id, $view_external_link_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->deleteViewExternalLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **view_external_link_token** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listBaseExternalLinks()`

```php
listBaseExternalLinks($org_id): object
```

List Base External Links

Use this request to list all the external links generated in the current team (organization).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $result = $apiInstance->listBaseExternalLinks($org_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->listBaseExternalLinks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listInviteLinks()`

```php
listInviteLinks($org_id, $page, $per_page): object
```

List Invite Links

As administrator of your team, you can use this request to gain a overview of all the invite links currently generated in your team, regardless which user or group.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listInviteLinks($org_id, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->listInviteLinks: ', $e->getMessage(), PHP_EOL;
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

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listViewExternalLinks()`

```php
listViewExternalLinks($org_id): object
```

List View External Links

Use this request to list all the view external links generated in the current team (organization).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $result = $apiInstance->listViewExternalLinks($org_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->listViewExternalLinks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `updateInviteLink()`

```php
updateInviteLink($org_id, $invite_link_token, $update_invite_link_request): object
```

Update Invite Link

You as team admin can also update an invite link. In the request body:    - `permission` is the read/write permission of the new invite link, with `r` as read-only and `rw` as read-and-write;  - `password` is the new password of your invite link;  - `expire_days` is the number of days after which the invite link will expire.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SharingLinksApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$invite_link_token = 0366b8995d7f47d8eu3t; // string
$update_invite_link_request = new \SeaTable\Client\TeamAdmin\UpdateInviteLinkRequest(); // \SeaTable\Client\TeamAdmin\UpdateInviteLinkRequest

try {
    $result = $apiInstance->updateInviteLink($org_id, $invite_link_token, $update_invite_link_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SharingLinksApi->updateInviteLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **invite_link_token** | **string**|  | |
| **update_invite_link_request** | [**\SeaTable\Client\TeamAdmin\UpdateInviteLinkRequest**](../Model/UpdateInviteLinkRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


