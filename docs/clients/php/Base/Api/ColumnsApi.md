# SeaTable\Client\ColumnsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addSelectOption()**](ColumnsApi.md#addSelectOption) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/column-options/ | Add Single/Multiple Select Options |
| [**appendColumns()**](ColumnsApi.md#appendColumns) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/batch-append-columns/ | Append Columns |
| [**deleteColumn()**](ColumnsApi.md#deleteColumn) | **DELETE** /dtable-server/api/v1/dtables/{base_uuid}/columns/ | Delete Column |
| [**deleteSelectOption()**](ColumnsApi.md#deleteSelectOption) | **DELETE** /dtable-server/api/v1/dtables/{base_uuid}/column-options/ | Delete Single/Multiple Select Options |
| [**insertColumn()**](ColumnsApi.md#insertColumn) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/columns/ | Insert Column |
| [**listColumns()**](ColumnsApi.md#listColumns) | **GET** /dtable-server/api/v1/dtables/{base_uuid}/columns/ | List Columns |
| [**updateColumn()**](ColumnsApi.md#updateColumn) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/columns/ | Update Column |
| [**updateColumnCascade()**](ColumnsApi.md#updateColumnCascade) | **POST** /dtable-server/api/v1/dtables/{base_uuid}/column-cascade-settings/ | Update Column Cascade |
| [**updateSelectOption()**](ColumnsApi.md#updateSelectOption) | **PUT** /dtable-server/api/v1/dtables/{base_uuid}/column-options/ | Update Single/Multiple Select Options |


## `addSelectOption()`

```php
addSelectOption($base_uuid, $add_single_multiple_select_options): object
```

Add Single/Multiple Select Options

Once you have created a single/multiple select column, use this request to add options for it.  In the request body:  `table_name` is the name of the table;  `column` is the name or the `key` of the single/multiple select column;  `options` is an array containing the label (`name`), option color (`color`) and the color of the arrow (`textColor`):  ![Options](https://seatable.io/wp-content/uploads/2021/11/Screenshot-2021-04-28-105719.png)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ColumnsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$add_single_multiple_select_options = new \SeaTable\Client\Base\AddSingleMultipleSelectOptions(); // \SeaTable\Client\Base\AddSingleMultipleSelectOptions

try {
    $result = $apiInstance->addSelectOption($base_uuid, $add_single_multiple_select_options);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ColumnsApi->addSelectOption: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **add_single_multiple_select_options** | [**\SeaTable\Client\Base\AddSingleMultipleSelectOptions**](../Model/AddSingleMultipleSelectOptions.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `appendColumns()`

```php
appendColumns($base_uuid, $append_columns_request): object
```

Append Columns

Use this request to append multiple columns to your table at once. As for the request body, refer to the previous call, [Insert Column](/reference/insert-column), for a detailed list of column formats. These requested and optional params can be used in the request body: `table_name` is the name of your table, required. `columns` is a list of columns you'd like to append, in each object of which: *   `column_name` is the name of your new column, required; *   `column_type` is the type of your new column, required; *   `data` is the format setting of a special column, required in case. For details, refer to the call [Insert Column](/reference/insert-column).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ColumnsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$append_columns_request = new \SeaTable\Client\Base\AppendColumnsRequest(); // \SeaTable\Client\Base\AppendColumnsRequest

try {
    $result = $apiInstance->appendColumns($base_uuid, $append_columns_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ColumnsApi->appendColumns: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **append_columns_request** | [**\SeaTable\Client\Base\AppendColumnsRequest**](../Model/AppendColumnsRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `deleteColumn()`

```php
deleteColumn($base_uuid, $delete_column): object
```

Delete Column

Delete a column with its name or `key`. See the request body for detailed params.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ColumnsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$delete_column = new \SeaTable\Client\Base\DeleteColumn(); // \SeaTable\Client\Base\DeleteColumn

try {
    $result = $apiInstance->deleteColumn($base_uuid, $delete_column);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ColumnsApi->deleteColumn: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **delete_column** | [**\SeaTable\Client\Base\DeleteColumn**](../Model/DeleteColumn.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `deleteSelectOption()`

```php
deleteSelectOption($base_uuid, $delete_select_options): object
```

Delete Single/Multiple Select Options

Use this request to remove single select or multiple select options that you don't need any more. Thes deleted options will be removed from the entries containing them.  In the request body:  `table_name` is the name of the table;  `column` is the name or the `key` of the single/multiple select column;  `option_names` is a list of options you'd like to delete.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ColumnsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$delete_select_options = new \SeaTable\Client\Base\DeleteSelectOptions(); // \SeaTable\Client\Base\DeleteSelectOptions

try {
    $result = $apiInstance->deleteSelectOption($base_uuid, $delete_select_options);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ColumnsApi->deleteSelectOption: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **delete_select_options** | [**\SeaTable\Client\Base\DeleteSelectOptions**](../Model/DeleteSelectOptions.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `insertColumn()`

```php
insertColumn($base_uuid, $insert_column_request): object
```

Insert Column

Create a new column. You can only add one new column at the end of a table.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ColumnsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$insert_column_request = new \SeaTable\Client\Base\InsertColumnRequest(); // \SeaTable\Client\Base\InsertColumnRequest | Choose which column type you want to add. If you want to add multiple columns, use the request [Append Columns](/reference/append-columns).

try {
    $result = $apiInstance->insertColumn($base_uuid, $insert_column_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ColumnsApi->insertColumn: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **insert_column_request** | [**\SeaTable\Client\Base\InsertColumnRequest**](../Model/InsertColumnRequest.md)| Choose which column type you want to add. If you want to add multiple columns, use the request [Append Columns](/reference/append-columns). | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `listColumns()`

```php
listColumns($table_name, $base_uuid, $view_name): object
```

List Columns

List all the visible columns in a certain view in a table.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ColumnsApi(
    new GuzzleHttp\Client(),
    $config
);
$table_name = Table1; // string | The name of the table.
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$view_name = Default View; // string | The name of the view.

try {
    $result = $apiInstance->listColumns($table_name, $base_uuid, $view_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ColumnsApi->listColumns: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table_name** | **string**| The name of the table. | |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **view_name** | **string**| The name of the view. | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `updateColumn()`

```php
updateColumn($base_uuid, $update_column): object
```

Update Column

Allows various changes of the column: name, column_type, freeze/unfreeze, resize, etc... `op_type` is required. The following options are available: - rename_column - modify_column_type - resize_column - move_column - freeze_column (eventuell weglassen) `column` is the name or `key` of the target column. `new_column_type` is the new type of the target column. For a list of column type params refer to the SeaTable API Parameter. Get more information about columns and column types in [Models](https://api.seatable.io/reference/models).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ColumnsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$update_column = new \SeaTable\Client\Base\UpdateColumn(); // \SeaTable\Client\Base\UpdateColumn

try {
    $result = $apiInstance->updateColumn($base_uuid, $update_column);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ColumnsApi->updateColumn: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **update_column** | [**\SeaTable\Client\Base\UpdateColumn**](../Model/UpdateColumn.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `updateColumnCascade()`

```php
updateColumnCascade($base_uuid, $body): object
```

Update Column Cascade

After you have added at least two single select columns and have added relevant options, you can start to set the cascade relationships between these single select columns. ## What are cascade settings? With cascade settings for the single select column, you can set up a \"parent\" single select column and a \"child\" single select column, so that when you select one option in the parent, the child column will only show you the options belonging to that parent.  For example, if the parent column is \"continent\" and you've selected \"Europe\", then the child column will only show you the countries in Europe. Of course, this doesn't happen automatically - you have to set up the cascade relationship with this API request first.  ![](https://seatable.io/wp-content/uploads/2021/11/cascade.png)  ## What are the preconditions? This API request has the following preconditions:  - The table already exists (This API request cannot create a new table); - The parent and child column already exist (same as above); - The parent and child column already have options (same as above).  ## How to set up the cascade relationship? It's so easy: just like demonstrated in the example request, define the following parameters/objects and you'll get `success`:  - `table_name`: The name of the table. - `parent_column`: The 1st level of single select column's name or `key`. - `child_column`: The 2nd level of single select column's name or `key`. - `cascade_settings`: In this object, list all the child options for each parent option, like demonstrated in the example request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ColumnsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$body = array('key' => new \stdClass); // object

try {
    $result = $apiInstance->updateColumnCascade($base_uuid, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ColumnsApi->updateColumnCascade: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **body** | **object**|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)



## `updateSelectOption()`

```php
updateSelectOption($base_uuid, $update_single_multiple_select_options): object
```

Update Single/Multiple Select Options

Use this request to update existing single/multiple select options by changing their name and/or color.  In the request body:  `table_name` is the name of your table, required;   `column` is the name of the column, required;   `options` is a list of option objects that you would like to update, in which:  *   `id` is the ID of that option, which you can retrive with the call \"List Columns in A View in A Table\", required; *   `color` is the label's new color, optional; *   `name` is the label's new name, optional.       `return_options` gives you the possibility to get an overview of all the options you just updated, optional, `false` by default.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: BaseTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\Base\ColumnsApi(
    new GuzzleHttp\Client(),
    $config
);
$base_uuid = 5c264e76-0e5a-448a-9f34-580b551364ca; // string | The unique identifier of a base. Sometimes also called dtable_uuid.
$update_single_multiple_select_options = new \SeaTable\Client\Base\UpdateSingleMultipleSelectOptions(); // \SeaTable\Client\Base\UpdateSingleMultipleSelectOptions

try {
    $result = $apiInstance->updateSelectOption($base_uuid, $update_single_multiple_select_options);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ColumnsApi->updateSelectOption: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_uuid** | **string**| The unique identifier of a base. Sometimes also called dtable_uuid. | |
| **update_single_multiple_select_options** | [**\SeaTable\Client\Base\UpdateSingleMultipleSelectOptions**](../Model/UpdateSingleMultipleSelectOptions.md)|  | [optional] |

### Return type

**object**

### Authorization

[BaseTokenAuth](../../README.md#BaseTokenAuth)


