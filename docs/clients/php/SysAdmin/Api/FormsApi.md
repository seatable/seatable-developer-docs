# SeaTable\Client\FormsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteDataCollectionForms()**](FormsApi.md#deleteDataCollectionForms) | **DELETE** /api/v2.1/admin/collection-tables/{collection_table_token}/ | Delete Data Collection Forms |
| [**deleteForm()**](FormsApi.md#deleteForm) | **DELETE** /api/v2.1/admin/forms/{form_token}/ | Delete Form |
| [**listDataCollectionForms()**](FormsApi.md#listDataCollectionForms) | **GET** /api/v2.1/admin/collection-tables/ | List Data Collection Forms |
| [**listForms()**](FormsApi.md#listForms) | **GET** /api/v2.1/admin/forms/ | List Forms |


## `deleteDataCollectionForms()`

```php
deleteDataCollectionForms($collection_table_token): object
```

Delete Data Collection Forms

Delete a data collection table with its token. The token can be retrieved with the call [List Data Collection Tables](/reference/list-data-collection-forms), or from the table's URL as its suffix.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\FormsApi(
    new GuzzleHttp\Client(),
    $config
);
$collection_table_token = 12345678-d378-4c12-8d7a-6da0fb48ee83; // string

try {
    $result = $apiInstance->deleteDataCollectionForms($collection_table_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->deleteDataCollectionForms: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **collection_table_token** | **string**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteForm()`

```php
deleteForm($form_token): object
```

Delete Form

Delete a form with its token. Get a form's token with the call [List Forms](/reference/user-forms-list-forms).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\FormsApi(
    new GuzzleHttp\Client(),
    $config
);
$form_token = 12345678-d378-4c12-8d7a-6da0fb48ee83; // string

try {
    $result = $apiInstance->deleteForm($form_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->deleteForm: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **form_token** | **string**|  | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listDataCollectionForms()`

```php
listDataCollectionForms(): object
```

List Data Collection Forms

List all the data collection forms generated in the system.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\FormsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listDataCollectionForms();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->listDataCollectionForms: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `listForms()`

```php
listForms(): object
```

List Forms

List all the forms in the current system. The returned `id` value is the ID of the form, and the `token` is the form's token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\FormsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listForms();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->listForms: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth



