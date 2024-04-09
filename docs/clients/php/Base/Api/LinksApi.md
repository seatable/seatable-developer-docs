# SeaTable\Client\LinksApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createRowLink()**](LinksApi.md#createRowLink) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/links/ | Create Row Link |
| [**createRowLinks()**](LinksApi.md#createRowLinks) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/links/ | Create Row Links |
| [**deleteRowLink()**](LinksApi.md#deleteRowLink) | **DELETE** /dtable-server/api/v1/dtables/{base_uuid}/links/ | Delete Row Link |
| [**listRowLinks()**](LinksApi.md#listRowLinks) | **POST** /dtable-db/api/v1/linked-records/{base_uuid} | List Row Links |
| [**updateRowLinks()**](LinksApi.md#updateRowLinks) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/batch-update-links/ | Update Row Links (Batch) |


## `createRowLink()`

```php
createRowLink($base_uuid, $create_row_link): object
```

Create Row Link

You can link a row to another row in the same table, or in another table in the same base. **Before you use this request**, you should create a link column first, and retrieve its `link_id`. This value is an attribute of a link column, and can also be retrieved from the call [Get Metadata](/reference/get-metadata).  Check out the [Models](/reference/models#a-link) page to get more information about the structure of a link.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\LinksApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$create_row_link = new \SeaTable\Client\Base\CreateRowLink(); // \SeaTable\Client\Base\CreateRowLink

try {
    $result = $apiInstance->createRowLink($base_uuid, $create_row_link);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LinksApi->createRowLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **create_row_link** | [**\SeaTable\Client\Base\CreateRowLink**](../Model/CreateRowLink.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `createRowLinks()`

```php
createRowLinks($base_uuid, $create_row_links): object
```

Create Row Links

Creates multiple links between one column and many others (1:n relation).  > 🚧 No support for Big Data > > This request does not support to add links in big data rows. There is another call [supporting big data](/reference/post_dtable-db-api-v1-base-base-uuid-links).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\LinksApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$create_row_links = new \SeaTable\Client\Base\CreateRowLinks(); // \SeaTable\Client\Base\CreateRowLinks

try {
    $result = $apiInstance->createRowLinks($base_uuid, $create_row_links);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LinksApi->createRowLinks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **create_row_links** | [**\SeaTable\Client\Base\CreateRowLinks**](../Model/CreateRowLinks.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `deleteRowLink()`

```php
deleteRowLink($base_uuid, $delete_row_link): object
```

Delete Row Link

Delete an existing link between two rows.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\LinksApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$delete_row_link = new \SeaTable\Client\Base\DeleteRowLink(); // \SeaTable\Client\Base\DeleteRowLink

try {
    $result = $apiInstance->deleteRowLink($base_uuid, $delete_row_link);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LinksApi->deleteRowLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **delete_row_link** | [**\SeaTable\Client\Base\DeleteRowLink**](../Model/DeleteRowLink.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `listRowLinks()`

```php
listRowLinks($base_uuid, $list_row_links): object
```

List Row Links

When you have a \"Link to other records\" column in your table and you have created some links to the current or another table, you can use this request to query each row's linked records' IDs and display values. In the request body (see example request for demonstration): - `table_id` is the ID of the table you are querying; - `link_column` is the `key` of the \"Link to other records\" column. **Attention**: do not use the `link_id` of the link column here. - `rows` is an array. Include the following details of each row you are querying in every object:     - `row_id` is the ID of the row you are querying;     - `offset` is the beginning number of your query. If your record is linked to multiple records, use e.g. `0` to start quering from the 1st element or e.g. `5` to start querying from the 6th element, etc. **Attention**: The returned list of linked rows is not ordered by its original order on the web interface, but rather by created time (`ctime`).     - `limit` lets you to set a limit to the number of records returned. Use e.g. `10` to return no more than 10 records.  In the response: - `row_id` is the ID of each linked record; - `display_value` is how this record is displayed on the web interface.      To get more information about each linked record, retrieve their `row_id` and use the **Query with SQL** request, for example: ``` SELECT * FROM Table2 WHERE _id IN (row_id1, row_id2, ...); ```

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\LinksApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$list_row_links = new \SeaTable\Client\Base\ListRowLinks(); // \SeaTable\Client\Base\ListRowLinks

try {
    $result = $apiInstance->listRowLinks($base_uuid, $list_row_links);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LinksApi->listRowLinks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **list_row_links** | [**\SeaTable\Client\Base\ListRowLinks**](../Model/ListRowLinks.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth




## `updateRowLinks()`

```php
updateRowLinks($base_uuid, $update_links): object
```

Update Row Links (Batch)

Update multiple links in batch in one table for one link column. It is possible to create multiple links with a n:m relation. Here is an example how the body with `row_id_list` and `other_rows_ids_map` should look like:  ``` \"row_id_list\": [         \"Qtf7xPmoRaiFyQPO1aENTjb\",         \"Qtf7xPmoRaiFyQPO1aENTjc\"     ],     \"other_rows_ids_map\": {         \"Qtf7xPmoRaiFyQPO1aENTjb\": [\"Qtf7xPmoRaiFyQPO1aENTjc\", \"{{row3_id}}\"],         \"Qtf7xPmoRaiFyQPO1aENTjc\": [\"Qtf7xPmoRaiFyQPO1aENTjb\", \"{{row3_id}}\"]     } ```

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\LinksApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$update_links = new \SeaTable\Client\Base\UpdateLinks(); // \SeaTable\Client\Base\UpdateLinks

try {
    $result = $apiInstance->updateRowLinks($base_uuid, $update_links);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LinksApi->updateRowLinks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **update_links** | [**\SeaTable\Client\Base\UpdateLinks**](../Model/UpdateLinks.md)|  | [optional] |

### Return type

**object**

### Authorization

BaseTokenAuth



