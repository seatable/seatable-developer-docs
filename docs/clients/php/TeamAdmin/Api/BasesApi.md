# SeaTable\Client\BasesApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**clearTeamTrashBin()**](BasesApi.md#clearTeamTrashBin) | **DELETE** /api/v2.1/org/{org_id}/admin/trash-dtables/ | Clear Team Trash Bin |
| [**deleteBase()**](BasesApi.md#deleteBase) | **DELETE** /api/v2.1/org/{org_id}/admin/dtables/{base_id}/ | Delete Base |
| [**listBaseSharings()**](BasesApi.md#listBaseSharings) | **GET** /api/v2.1/org/{org_id}/admin/dtables/{base_uuid}/shares | List Base Sharings |
| [**listBases()**](BasesApi.md#listBases) | **GET** /api/v2.1/org/{org_id}/admin/dtables/ | List Bases (Team) |
| [**listTrashBases()**](BasesApi.md#listTrashBases) | **GET** /api/v2.1/org/{org_id}/admin/trash-dtables/ | List Trash Bases |
| [**restoreBaseFromTrash()**](BasesApi.md#restoreBaseFromTrash) | **PUT** /api/v2.1/org/{org_id}/admin/trash-dtables/{base_id}/ | Restore Base from Trash |
| [**searchBase()**](BasesApi.md#searchBase) | **GET** /api/v2.1/org/{org_id}/admin/search-dtables/ | Search Base |


## `clearTeamTrashBin()`

```php
clearTeamTrashBin($org_id): object
```

Clear Team Trash Bin

Clear the team trash bin. All the bases there will be removed permanently and cannot be restored any more.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $result = $apiInstance->clearTeamTrashBin($org_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->clearTeamTrashBin: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteBase()`

```php
deleteBase($org_id, $base_id): object
```

Delete Base

Delete a base. This base will be put into the organization's trash bin, and permanently deleted automatically after 30 days.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$base_id = 000; // string | The ID of the base. Don't mix this up with the base_uuid!

try {
    $result = $apiInstance->deleteBase($org_id, $base_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->deleteBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **base_id** | **string**| The ID of the base. Don&#39;t mix this up with the base_uuid! | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listBaseSharings()`

```php
listBaseSharings($org_id, $base_uuid)
```

List Base Sharings

Use this request to list all the users and groups that a base is being shared with.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.

try {
    $apiInstance->listBaseSharings($org_id, $base_uuid);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listBaseSharings: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth




## `listBases()`

```php
listBases($org_id, $page, $per_page): object
```

List Bases (Team)

List all the bases in the current organization.  The returned `id` value is the ID of the base, to be distinguished from the base's `base_uuid`. Details see the **SeaTable API Parameter Reference**.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listBases($org_id, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listBases: ', $e->getMessage(), PHP_EOL;
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




## `listTrashBases()`

```php
listTrashBases($org_id, $page, $per_page): object
```

List Trash Bases

List the bases in the organization's trash bin.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$page = 1; // int | The page number you want to start showing the entries. If no value is provided, 1 will be used.
$per_page = 25; // int | The number of results that should be returned. If no value is provided, 25 results will be returned.

try {
    $result = $apiInstance->listTrashBases($org_id, $page, $per_page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listTrashBases: ', $e->getMessage(), PHP_EOL;
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




## `restoreBaseFromTrash()`

```php
restoreBaseFromTrash($org_id, $base_id): object
```

Restore Base from Trash

Restore a base from the trash bin.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$base_id = 000; // string | The ID of the base. Don't mix this up with the base_uuid!

try {
    $result = $apiInstance->restoreBaseFromTrash($org_id, $base_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->restoreBaseFromTrash: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **base_id** | **string**| The ID of the base. Don&#39;t mix this up with the base_uuid! | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `searchBase()`

```php
searchBase($org_id, $query): object
```

Search Base

By giving the exact or fuzzy match of the name of a base, you can find a base or all the bases that fit to that search criteria. The search is case-insensitive.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\BasesApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$query = Example; // string | Exact name or a part of the name of the base, case insensitive.

try {
    $result = $apiInstance->searchBase($org_id, $query);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->searchBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **query** | **string**| Exact name or a part of the name of the base, case insensitive. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



