# SeaTable\Client\DepartmentsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addDepartment()**](DepartmentsApi.md#addDepartment) | **POST** /api/v2.1/admin/address-book/groups/ | Add Department |
| [**deleteDepartment()**](DepartmentsApi.md#deleteDepartment) | **DELETE** /api/v2.1/admin/address-book/groups/{department_id}/ | Delete Department |
| [**getDepartments()**](DepartmentsApi.md#getDepartments) | **GET** /api/v2.1/admin/address-book/groups/{department_id}/ | Get Department |
| [**listDepartments()**](DepartmentsApi.md#listDepartments) | **GET** /api/v2.1/admin/address-book/groups/{parent_department_id}/ | List Departments |


## `addDepartment()`

```php
addDepartment($add_department_request): object
```

Add Department

Add a new department with a desired name and, by optional, in a parent department.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\DepartmentsApi(
    new GuzzleHttp\Client(),
    $config
);
$add_department_request = new \SeaTable\Client\SysAdmin/Model\AddDepartmentRequest(); // \SeaTable\Client\SysAdmin/Model\AddDepartmentRequest

try {
    $result = $apiInstance->addDepartment($add_department_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DepartmentsApi->addDepartment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **add_department_request** | [**\SeaTable\Client\SysAdmin/Model\AddDepartmentRequest**](../Model/AddDepartmentRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `deleteDepartment()`

```php
deleteDepartment($department_id): object
```

Delete Department

Delete a department by its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\DepartmentsApi(
    new GuzzleHttp\Client(),
    $config
);
$department_id = 1; // string

try {
    $result = $apiInstance->deleteDepartment($department_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DepartmentsApi->deleteDepartment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **department_id** | **string**|  | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `getDepartments()`

```php
getDepartments($department_id, $return_ancestors): object
```

Get Department

Get the information of a certain department by its ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\DepartmentsApi(
    new GuzzleHttp\Client(),
    $config
);
$department_id = 1; // string
$return_ancestors = true; // bool

try {
    $result = $apiInstance->getDepartments($department_id, $return_ancestors);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DepartmentsApi->getDepartments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **department_id** | **string**|  | |
| **return_ancestors** | **bool**|  | [optional] |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listDepartments()`

```php
listDepartments($parent_department_id): object
```

List Departments

List all the departments in the current level. The parameter `parent_department_id` in the URL is optional. If not given, the default of `-1` is taken. In this example, the parent department has the ID of `1`, and there are two departments with the IDs of `2` and `3` in it.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\DepartmentsApi(
    new GuzzleHttp\Client(),
    $config
);
$parent_department_id = 1; // int | Optional. -1 by default.

try {
    $result = $apiInstance->listDepartments($parent_department_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DepartmentsApi->listDepartments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **parent_department_id** | **int**| Optional. -1 by default. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


