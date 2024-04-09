# SeaTable\Client\FormsApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createForm()**](FormsApi.md#createForm) | **POST** /api/v2.1/forms/ | Create Form |
| [**deleteForm()**](FormsApi.md#deleteForm) | **DELETE** /api/v2.1/forms/{form_token}/ | Delete Form |
| [**duplicateForm()**](FormsApi.md#duplicateForm) | **POST** /api/v2.1/forms/{form_token}/duplicate/ | Duplicate Form |
| [**listForms()**](FormsApi.md#listForms) | **GET** /api/v2.1/forms/ | List Forms |
| [**listSharedForms()**](FormsApi.md#listSharedForms) | **GET** /api/v2.1/forms/shared/ | List Shared Forms |
| [**updateForm()**](FormsApi.md#updateForm) | **PUT** /api/v2.1/forms/{form_token}/ | Update Form |
| [**uploadFormLogo()**](FormsApi.md#uploadFormLogo) | **POST** /api/v2.1/forms/{form_token}/logos/ | Upload Form Logo |


## `createForm()`

```php
createForm($workspace_id, $name, $form_config): object
```

Create Form

Create a form in the base.  To customize this form, you can use the following request body in the `form_config` parameter and:  * Define the name of the form; * Choose which columns to include in it; * Set required fields; * Add descriptions; * Add remarks; * Send notifications; * Add a notice on the top of the form; * Add a notice on the bottom of the form; * Show a notice after submission; * Add a redirect link after submission; * Set a submission deadline.  ```     {         \"form_name\":\"Customer Survey\",              // The name of your form         \"columns\":[                                 // Choose the columns to include             {                 \"key\":\"0000\",                       // The column ID                 \"is_required\":false,                // Set obligation                 \"description\":\"\",                   // Add a description if needed                 \"filters\":[],                       // Conditional question (details follow)                 \"filter_conjunction\":\"And\"          // Filter behavior (details follow)             },             {                 \"key\":\"zJSb\",                 \"is_required\":false,                 \"description\":\"\",                 \"filters\":[],                 \"filter_conjunction\":\"And\"             },             {                 \"key\":\"xIy2\",                 \"is_required\":false,                 \"description\":\"\",                 \"filters\":[],                 \"filter_conjunction\":\"And\"             }         ],         \"table_id\":\"0000\",                          // ID of the table         \"remarkOption\":{                            // A notice at the bottom             \"isRemarkContentShow\":false,                           \"remarkContent\":\"\"             },         \"notification_config\":{                     // If notification will be sent               \"is_send_notification\":false,             \"notification_selected_users\":[]             },         \"top_remark_option\":{                       // A notice at the top               \"is_top_remark_content_show\":false,             \"top_remark_content\":\"\"             },         \"success_message_option\":{                  // A message after submission             \"is_success_message_show\":true,             \"success_message\":\"Thanks!\"             },         \"success_redirect_option\":{                 // A redirect URL after submission               \"is_success_redirect_show\":true,             \"success_redirect\":\"www.google.com\"             },         \"\"submit_deadline_option\":{                 // An optional submission deadline             \"is_submit_deadline_show\":true,             \"submit_deadline\":\"2021-10-28 00:00:00\"             }     } ```

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\FormsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id = 'workspace_id_example'; // string | The workspace ID where your base is.
$name = 'name_example'; // string
$form_config = 'form_config_example'; // string | Define the form's name (required) and other details (optional). For a full list of available options, refer to the instruction above.

try {
    $result = $apiInstance->createForm($workspace_id, $name, $form_config);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->createForm: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id** | **string**| The workspace ID where your base is. | [optional] |
| **name** | **string**|  | [optional] |
| **form_config** | **string**| Define the form&#39;s name (required) and other details (optional). For a full list of available options, refer to the instruction above. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `deleteForm()`

```php
deleteForm($form_token): object
```

Delete Form

Delete a form with its token.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\FormsApi(
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




## `duplicateForm()`

```php
duplicateForm($form_token): object
```

Duplicate Form

With a form's `form_token` (or `token` as returned by the call to list a user's or a base's forms), you can duplicate a form with this request.  In the response, the details of the newly created duplication are listed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\FormsApi(
    new GuzzleHttp\Client(),
    $config
);
$form_token = 12345678-d378-4c12-8d7a-6da0fb48ee83; // string

try {
    $result = $apiInstance->duplicateForm($form_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->duplicateForm: ', $e->getMessage(), PHP_EOL;
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




## `listForms()`

```php
listForms($workspace_id_query, $base_name): object
```

List Forms

List all the forms of a base with full details of these forms. The returned `form_link` value is the URL of the form page, ready to be sent to survey participants.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\FormsApi(
    new GuzzleHttp\Client(),
    $config
);
$workspace_id_query = 127; // int | id of your workspace.
$base_name = My Projects; // string | name of your base

try {
    $result = $apiInstance->listForms($workspace_id_query, $base_name);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->listForms: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **workspace_id_query** | **int**| id of your workspace. | |
| **base_name** | **string**| name of your base | |

### Return type

**object**

### Authorization

AccountTokenAuth




## `listSharedForms()`

```php
listSharedForms(): object
```

List Shared Forms

List all the shared forms the user has access to.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\FormsApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->listSharedForms();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->listSharedForms: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateForm()`

```php
updateForm($form_token, $form_config): object
```

Update Form

Update your form's configuration.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\FormsApi(
    new GuzzleHttp\Client(),
    $config
);
$form_token = 12345678-d378-4c12-8d7a-6da0fb48ee83; // string
$form_config = 'form_config_example'; // string | Define the form's name (required) and other details (optional). For a full list of available options, refer to the instruction above.

try {
    $result = $apiInstance->updateForm($form_token, $form_config);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->updateForm: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **form_token** | **string**|  | |
| **form_config** | **string**| Define the form&#39;s name (required) and other details (optional). For a full list of available options, refer to the instruction above. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `uploadFormLogo()`

```php
uploadFormLogo($form_token, $form_logo): object
```

Upload Form Logo

Use this request to upload a custom logo for your form using your form's `form_token`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\User\FormsApi(
    new GuzzleHttp\Client(),
    $config
);
$form_token = 12345678-d378-4c12-8d7a-6da0fb48ee83; // string
$form_logo = "/path/to/file.txt"; // \SplFileObject | Path and file name to your logo image.

try {
    $result = $apiInstance->uploadFormLogo($form_token, $form_logo);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FormsApi->uploadFormLogo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **form_token** | **string**|  | |
| **form_logo** | **\SplFileObject****\SplFileObject**| Path and file name to your logo image. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



