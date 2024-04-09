# SeaTable\Client\SystemInfoCustomizingApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getSystemInformation()**](SystemInfoCustomizingApi.md#getSystemInformation) | **GET** /api/v2.1/admin/sysinfo/ | Get system information |
| [**updateFavicon()**](SystemInfoCustomizingApi.md#updateFavicon) | **POST** /api/v2.1/admin/favicon/ | Update Favicon |
| [**updateGeneralSettings()**](SystemInfoCustomizingApi.md#updateGeneralSettings) | **PUT** /api/v2.1/admin/web-settings/ | Update General Settings |
| [**updateLoginBackgroundImage()**](SystemInfoCustomizingApi.md#updateLoginBackgroundImage) | **POST** /api/v2.1/admin/login-background-image/ | Update Login Background Image |
| [**updateLogo()**](SystemInfoCustomizingApi.md#updateLogo) | **POST** /api/v2.1/admin/logo/ | Update Logo |


## `getSystemInformation()`

```php
getSystemInformation(): object
```

Get system information

Get the general system information with this request as system administrator.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SystemInfoCustomizingApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getSystemInformation();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemInfoCustomizingApi->getSystemInformation: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateFavicon()`

```php
updateFavicon($favicon, $with_notify): object
```

Update Favicon

Upload an image (.png with a transparent background is recommended) as the favicon of your SeaTable installation. As per the `with_notify` param in the request body: you can use this API request twice to upload two favicons: - one is the \"normal\" favicon（leave `with_nofity` blank). - the other one is the \"notifying\" favicon which should have something like a \"notifying\" red dot on it (set `with_notify` to `true`). ![Image](https://seatable.io/wp-content/uploads/2021/11/favicon.png)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SystemInfoCustomizingApi(
    new GuzzleHttp\Client(),
    $config
);
$favicon = "/path/to/file.txt"; // \SplFileObject | The path and filename of the image file of your favicon.
$with_notify = True; // bool | Leave this param as its default (`false`) to upload your favicon, and use this param as `true` to upload a favicon with a notification sign.

try {
    $result = $apiInstance->updateFavicon($favicon, $with_notify);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemInfoCustomizingApi->updateFavicon: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **favicon** | **\SplFileObject****\SplFileObject**| The path and filename of the image file of your favicon. | [optional] |
| **with_notify** | **bool**| Leave this param as its default (&#x60;false&#x60;) to upload your favicon, and use this param as &#x60;true&#x60; to upload a favicon with a notification sign. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateGeneralSettings()`

```php
updateGeneralSettings($update_general_settings_request): object
```

Update General Settings

Change the general settings of your system. For details, see the description for each parameter in the request body. Just like the settings via web interface, these settings via API request are also saved in the database table (dtable-db/constance_config). They have a higher priority over the settings in the config files. However, in the `dtable_web_settings` you'll find more setting options. For details, visit the [SeaTable Admin Manual](https://manual.seatable.io/config/dtable_web_settings/#user-management-options).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SystemInfoCustomizingApi(
    new GuzzleHttp\Client(),
    $config
);
$update_general_settings_request = new \SeaTable\Client\SysAdmin/Model\UpdateGeneralSettingsRequest(); // \SeaTable\Client\SysAdmin/Model\UpdateGeneralSettingsRequest

try {
    $result = $apiInstance->updateGeneralSettings($update_general_settings_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemInfoCustomizingApi->updateGeneralSettings: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **update_general_settings_request** | [**\SeaTable\Client\SysAdmin/Model\UpdateGeneralSettingsRequest**](../Model/UpdateGeneralSettingsRequest.md)|  | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateLoginBackgroundImage()`

```php
updateLoginBackgroundImage($login_bg_image): object
```

Update Login Background Image

Change the background image shown on the login mask.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SystemInfoCustomizingApi(
    new GuzzleHttp\Client(),
    $config
);
$login_bg_image = "/path/to/file.txt"; // \SplFileObject | The path and filename of the background image.

try {
    $result = $apiInstance->updateLoginBackgroundImage($login_bg_image);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemInfoCustomizingApi->updateLoginBackgroundImage: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **login_bg_image** | **\SplFileObject****\SplFileObject**| The path and filename of the background image. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth




## `updateLogo()`

```php
updateLogo($logo): object
```

Update Logo

Upload an image (.png with a transparent background is recommended) as the logo of your SeaTable installation.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\SysAdmin\SystemInfoCustomizingApi(
    new GuzzleHttp\Client(),
    $config
);
$logo = "/path/to/file.txt"; // \SplFileObject | The path and filename of the image file of your logo.

try {
    $result = $apiInstance->updateLogo($logo);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SystemInfoCustomizingApi->updateLogo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **logo** | **\SplFileObject****\SplFileObject**| The path and filename of the image file of your logo. | [optional] |

### Return type

**object**

### Authorization

AccountTokenAuth



