# SeaTable\Client\AccountTokenApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAccountTokenfromUsername()**](AccountTokenApi.md#getAccountTokenfromUsername) | **POST** /api2/auth-token/ | Get Account-Token with Username and Password |


## `getAccountTokenfromUsername()`

```php
getAccountTokenfromUsername($username, $password, $x_seafile_otp): \SeaTable\Client\Auth\AccountToken
```

Get Account-Token with Username and Password

Generate an *Account-Token* with your username and password. This Account-Token is necessary for all the following account operations. Use the optional paramater if two-factor-authentication (2FA) is activated for your account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new SeaTable\Client\Auth\AccountTokenApi(
    new GuzzleHttp\Client()
);
$username = 'username_example'; // string | Your email address
$password = 'password_example'; // string | Your password
$x_seafile_otp = 'x_seafile_otp_example'; // string | Two-factor token (usually generated with a mobile app like the google authenticator), optional, only needed if 2FA is activated for your account.

try {
    $result = $apiInstance->getAccountTokenfromUsername($username, $password, $x_seafile_otp);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountTokenApi->getAccountTokenfromUsername: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **username** | **string**| Your email address | |
| **password** | **string**| Your password | |
| **x_seafile_otp** | **string**| Two-factor token (usually generated with a mobile app like the google authenticator), optional, only needed if 2FA is activated for your account. | [optional] |

### Return type

[**\SeaTable\Client\Auth\AccountToken**](../Model/AccountToken.md)

### Authorization

No authorization required


