# SeaTable\Client\RowsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addRow()**](RowsApi.md#addRow) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/rows/ | Add Row |
| [**appendRows()**](RowsApi.md#appendRows) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/batch-append-rows/ | Append Rows |
| [**deleteRow()**](RowsApi.md#deleteRow) | **DELETE** /dtable-server/api/v1/dtables/{base_uuid}/rows/ | Delete Row |
| [**deleteRows()**](RowsApi.md#deleteRows) | **DELETE** /dtable-server/api/v1/dtables/{base_uuid}/batch-delete-rows/ | Delete Rows |
| [**getRow()**](RowsApi.md#getRow) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/rows/{row_id}/ | Get Row |
| [**listFilteredRows()**](RowsApi.md#listFilteredRows) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/filtered-rows/ | List Filtered Rows |
| [**listRows()**](RowsApi.md#listRows) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/rows/ | List Rows |
| [**lockRows()**](RowsApi.md#lockRows) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/lock-rows/ | Lock Rows |
| [**querySQL()**](RowsApi.md#querySQL) | **POST** /dtable-db/api/v1/query/{base_uuid}/ | List Rows (with SQL) |
| [**unlockRows()**](RowsApi.md#unlockRows) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/unlock-rows/ | Unlock Rows |
| [**updateRow()**](RowsApi.md#updateRow) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/rows/ | Update Row |
| [**updateRows()**](RowsApi.md#updateRows) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/batch-update-rows/ | Update Rows |


## `addRow()`

```php
addRow($base_uuid, $add_row_request): object
```

Add Row

Appends or inserts a single row.  > 📘 How to define the row object >  > The row object contains key:value pairs with the column name as key and the desired values. Check the page [Models](/reference/models) to get a better understanding of the row object.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$add_row_request = new \SeaTable\Client\Base\AddRowRequest(); // \SeaTable\Client\Base\AddRowRequest

try {
    $result = $apiInstance->addRow($base_uuid, $add_row_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->addRow: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **add_row_request** | [**\SeaTable\Client\Base\AddRowRequest**](../Model/AddRowRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `appendRows()`

```php
appendRows($base_uuid, $append_rows): object
```

Append Rows

Appends multiple rows.  > 🚧 Appends at most 1 000 rows > > A maximum of 1 000 rows can be appended with a single request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$append_rows = new \SeaTable\Client\Base\AppendRows(); // \SeaTable\Client\Base\AppendRows

try {
    $result = $apiInstance->appendRows($base_uuid, $append_rows);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->appendRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **append_rows** | [**\SeaTable\Client\Base\AppendRows**](../Model/AppendRows.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `deleteRow()`

```php
deleteRow($base_uuid, $delete_row): object
```

Delete Row

Deletes a single row.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$delete_row = new \SeaTable\Client\Base\DeleteRow(); // \SeaTable\Client\Base\DeleteRow

try {
    $result = $apiInstance->deleteRow($base_uuid, $delete_row);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->deleteRow: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **delete_row** | [**\SeaTable\Client\Base\DeleteRow**](../Model/DeleteRow.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `deleteRows()`

```php
deleteRows($base_uuid, $delete_rows): object
```

Delete Rows

Deletes multiple rows. > 🚧 Deletes at most 10 000 rows > > A maximum of 10 000 rows can be deleted with a single request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$delete_rows = new \SeaTable\Client\Base\DeleteRows(); // \SeaTable\Client\Base\DeleteRows

try {
    $result = $apiInstance->deleteRows($base_uuid, $delete_rows);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->deleteRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **delete_rows** | [**\SeaTable\Client\Base\DeleteRows**](../Model/DeleteRows.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `getRow()`

```php
getRow($base_uuid, $row_id, $table_name, $convert): object
```

Get Row

Retrieves a single row.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$row_id = Qtf7xPmoRaiFyQPO1aENTjb; // string | The id of the row.
$table_name = Table1; // string | The name of the table.
$convert = true; // bool | If 'true', the column's id will be converted to column names.

try {
    $result = $apiInstance->getRow($base_uuid, $row_id, $table_name, $convert);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->getRow: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **row_id** | **string**| The id of the row. | |
| **table_name** | **string**| The name of the table. | |
| **convert** | **bool**| If &#39;true&#39;, the column&#39;s id will be converted to column names. | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `listFilteredRows()`

```php
listFilteredRows($base_uuid, $table_name, $filtered_rows_filter)
```

List Filtered Rows

List rows by filter conditions. This is especially useful when you want to filter out records and only see those records. > 🚧 Deprecated since version 2.3 >  > This request has been depricated since SeaTable 2.3. This means you can probably still use it, but it will not be maintained and will probably be removed/deactivated any time without further notice in the future. > Please use [List rows (with SQL)](/reference/list-rows-with-sql) or [List rows](/reference/list-rows) instead.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$table_name = Table1; // string | The name of the table.
$filtered_rows_filter = new \SeaTable\Client\Base\FilteredRowsFilter(); // \SeaTable\Client\Base\FilteredRowsFilter

try {
    $apiInstance->listFilteredRows($base_uuid, $table_name, $filtered_rows_filter);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->listFilteredRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **table_name** | **string**| The name of the table. | |
| **filtered_rows_filter** | [**\SeaTable\Client\Base\FilteredRowsFilter**](../Model/FilteredRowsFilter.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `listRows()`

```php
listRows($base_uuid, $table_name, $view_name, $convert_link_id, $order_by, $direction, $start, $limit): object
```

List Rows

Lists rows in a table (or in a view if provided), ordered according to the filter conditions and sort criteria provided in the request.   > 📘 Returns no data from the big data backend >  > This request does not return rows stored in the big data backend. To query the big data backend, use the request [List Rows (with SQL)](/reference/list-rows-with-sql) instead.  > 🚧 Returns at most 1 000 rows > > The request returns a maximum of 1 000 rows regardless of the limit specified in the SQL-statement.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$table_name = Table1; // string | The name of the table.
$view_name = Default View; // string | The name of the view.
$convert_link_id = false; // bool | Whether the link column in the returned row is the ID (false) of the linked row or the name (true) of the linked row. If no value is provided, false is the default.
$order_by = Likes; // string | The name or id of a column that is used to sort the results.
$direction = desc; // string | The direction of the sort, ascending `asc` or descending `desc`. asc by default. Works only if start and limit are set, too.
$start = 0; // int | Starting position (number) of the returned rows. 0 by default.
$limit = 100; // int | Number of rows that should be returned. 1000 by default.

try {
    $result = $apiInstance->listRows($base_uuid, $table_name, $view_name, $convert_link_id, $order_by, $direction, $start, $limit);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->listRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **table_name** | **string**| The name of the table. | |
| **view_name** | **string**| The name of the view. | [optional] |
| **convert_link_id** | **bool**| Whether the link column in the returned row is the ID (false) of the linked row or the name (true) of the linked row. If no value is provided, false is the default. | [optional] |
| **order_by** | **string**| The name or id of a column that is used to sort the results. | [optional] |
| **direction** | **string**| The direction of the sort, ascending &#x60;asc&#x60; or descending &#x60;desc&#x60;. asc by default. Works only if start and limit are set, too. | [optional] [default to &#39;&#39;] |
| **start** | **int**| Starting position (number) of the returned rows. 0 by default. | [optional] |
| **limit** | **int**| Number of rows that should be returned. 1000 by default. | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `lockRows()`

```php
lockRows($base_uuid, $table_with_row_ids): object
```

Lock Rows

Locks a single or multiple rows.   The request ensures that all specified rows are locked. Locked rows are ignored.  > 📘 Advanced feature >  > Row locking is only available in [SeaTable Cloud Plus and Enterprise](https://seatable.io/preise/?lang=auto) as well as SeaTable Server Enterprise Edition.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$table_with_row_ids = new \SeaTable\Client\Base\TableWithRowIds(); // \SeaTable\Client\Base\TableWithRowIds

try {
    $result = $apiInstance->lockRows($base_uuid, $table_with_row_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->lockRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **table_with_row_ids** | [**\SeaTable\Client\Base\TableWithRowIds**](../Model/TableWithRowIds.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `querySQL()`

```php
querySQL($base_uuid, $sql_query): \SeaTable\Client\Base\SqlQueryResponse
```

List Rows (with SQL)

Lists rows in a table based on an SQL-query provided in the request. Also returns the metadata of the table.  Typical SQL-statements are supported. Below some basic examples: `SELECT name, age, birthday, gender FROM Participants`<br/> `SELECT name, surname FROM Participants ORDER BY name`<br/> `SELECT * FROM Participants LIMIT 25` For more details, check the [SQL-syntax supported by SeaTable](https://developer.seatable.io/scripts/sql/reference/).  > 📘 Returns also data from the big data backend >  > This request is the only available endpoint that returns rows stored in the big data backend.   > 🚧 Returns at most 10 000 rows > > The request returns a maximum of 10 000 rows regardless of the limit specified in the SQL-statement.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$sql_query = new \SeaTable\Client\Base\SqlQuery(); // \SeaTable\Client\Base\SqlQuery | description des requestBody

try {
    $result = $apiInstance->querySQL($base_uuid, $sql_query);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->querySQL: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **sql_query** | [**\SeaTable\Client\Base\SqlQuery**](../Model/SqlQuery.md)| description des requestBody | [optional] |

### Return type

[**\SeaTable\Client\Base\SqlQueryResponse**](../Model/SqlQueryResponse.md)

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `unlockRows()`

```php
unlockRows($base_uuid, $table_with_row_ids): object
```

Unlock Rows

Unlocks a single or multiple rows.  The request ensures that all specified rows are unlocked. Unlocked rows are ignored.  > 📘 Advanced feature >  > Row locking is only available in [SeaTable Cloud Plus and Enterprise](https://seatable.io/preise/?lang=auto) as well as SeaTable Server Enterprise Edition.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$table_with_row_ids = new \SeaTable\Client\Base\TableWithRowIds(); // \SeaTable\Client\Base\TableWithRowIds

try {
    $result = $apiInstance->unlockRows($base_uuid, $table_with_row_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->unlockRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **table_with_row_ids** | [**\SeaTable\Client\Base\TableWithRowIds**](../Model/TableWithRowIds.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `updateRow()`

```php
updateRow($base_uuid, $update_row): object
```

Update Row

Updates a single row.  > 📘 Structure of the row object >  > The row object contains key:value pairs with the column name as key and the desired values. Check the page [Models](/reference/models) to get a better understanding of the row object.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$update_row = new \SeaTable\Client\Base\UpdateRow(); // \SeaTable\Client\Base\UpdateRow

try {
    $result = $apiInstance->updateRow($base_uuid, $update_row);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->updateRow: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **update_row** | [**\SeaTable\Client\Base\UpdateRow**](../Model/UpdateRow.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `updateRows()`

```php
updateRows($base_uuid, $update_rows): object
```

Update Rows

Updates multiple rows. > 🚧 Updates at most 1 000 rows > > A maximum of 1 000 rows can be updated with a single request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$update_rows = new \SeaTable\Client\Base\UpdateRows(); // \SeaTable\Client\Base\UpdateRows

try {
    $result = $apiInstance->updateRows($base_uuid, $update_rows);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->updateRows: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **update_rows** | [**\SeaTable\Client\Base\UpdateRows**](../Model/UpdateRows.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)


