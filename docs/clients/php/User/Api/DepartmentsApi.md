# SeaTable\Client\DepartmentsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listDeparmentMembers()**](DepartmentsApi.md#listDeparmentMembers) | **GET** /api/v2.1/address-book/departments/{department_id}/members/ | List Deparment Members |
| [**listDepartments()**](DepartmentsApi.md#listDepartments) | **GET** /api/v2.1/address-book/departments/ | List Departments |


## `listDeparmentMembers()`

```php
listDeparmentMembers($department_id): object
```

List Deparment Members

List the members of a department in your team (organization).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\DepartmentsApi(
    new GuzzleHttp\Client(),
    $config
);
$department_id = 10; // int | ID of the department. Required.

try {
    $result = $apiInstance->listDeparmentMembers($department_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DepartmentsApi->listDeparmentMembers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **department_id** | **int**| ID of the department. Required. | |

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)



## `listDepartments()`

```php
listDepartments(): object
```

List Departments

As a team (organization) user, you can use this API request to list all the departments in your team (organization).  The returned `id` values are the IDs of each department. If the `parent_group_id` is `-1`, it means this department is in the root level.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\DepartmentsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listDepartments();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DepartmentsApi->listDepartments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[AccountTokenAuth](../../README.md#AccountTokenAuth)


