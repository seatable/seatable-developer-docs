# SeaTable\Client\RowCommentsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteComment()**](RowCommentsApi.md#deleteComment) | **DELETE** /dtable-server/api/v1/dtables/{base_uuid}/comments/{comment_id}/ | Delete Comment |
| [**getComment()**](RowCommentsApi.md#getComment) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/comments/{comment_id}/ | Get Comment |
| [**getRowCommentsCount()**](RowCommentsApi.md#getRowCommentsCount) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/comments-count/ | Get Row Comments Count |
| [**listCommentsWithinDays()**](RowCommentsApi.md#listCommentsWithinDays) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/comments-within-days/ | List Comments within Days |
| [**listRowComments()**](RowCommentsApi.md#listRowComments) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/comments/ | List Row Comments |


## `deleteComment()`

```php
deleteComment($base_uuid, $comment_id): object
```

Delete Comment

Delete a certain comment by its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowCommentsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$comment_id = 1; // int | The id of the comment.

try {
    $result = $apiInstance->deleteComment($base_uuid, $comment_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowCommentsApi->deleteComment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **comment_id** | **int**| The id of the comment. | |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `getComment()`

```php
getComment($base_uuid, $comment_id): object
```

Get Comment

Get the details of a certain comment with its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowCommentsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$comment_id = 1; // int | The id of the comment.

try {
    $result = $apiInstance->getComment($base_uuid, $comment_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowCommentsApi->getComment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **comment_id** | **int**| The id of the comment. | |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `getRowCommentsCount()`

```php
getRowCommentsCount($base_uuid, $row_id): object
```

Get Row Comments Count

Get the number of comments in a certain row. This could be a useful request to check if there's new comments there.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowCommentsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$row_id = YMIviMeERQCUiQhPPqo6Gw; // string | Unique id of a row.

try {
    $result = $apiInstance->getRowCommentsCount($base_uuid, $row_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowCommentsApi->getRowCommentsCount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **row_id** | **string**| Unique id of a row. | |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `listCommentsWithinDays()`

```php
listCommentsWithinDays($base_uuid, $days): object
```

List Comments within Days

List all the comments in a base within a given number of days before today.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowCommentsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$days = 7; // int

try {
    $result = $apiInstance->listCommentsWithinDays($base_uuid, $days);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowCommentsApi->listCommentsWithinDays: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **days** | **int**|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `listRowComments()`

```php
listRowComments($base_uuid, $row_id): object
```

List Row Comments

List all the comments in a certain row. The returned `id` value is the ID of each comment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowCommentsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$row_id = YMIviMeERQCUiQhPPqo6Gw; // string | Unique id of a row.

try {
    $result = $apiInstance->listRowComments($base_uuid, $row_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowCommentsApi->listRowComments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **row_id** | **string**| Unique id of a row. | |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)


