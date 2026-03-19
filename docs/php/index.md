# PHP

The SeaTable PHP Client encapsulates the SeaTable REST API. It is auto-generated from the public [OpenAPI specification](https://api.seatable.com), which ensures all API endpoints are covered automatically.

- Source code on [GitHub](https://github.com/seatable/seatable-api-php)
- Package on [Packagist](https://packagist.org/packages/seatable/seatable-api-php)
- Complete endpoint documentation in the [API Reference](api-reference.md)

## Installation

```
composer require seatable/seatable-api-php
```

## Authentication

Most operations on base data require a **Base Token**. You obtain it by exchanging an **API Token**, which can be [generated in the SeaTable web interface](https://seatable.com/help/create-api-tokens/):

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$config = SeaTable\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_API_TOKEN');

$apiInstance = new SeaTable\Client\Auth\BaseTokenApi(
    new GuzzleHttp\Client(), $config
);

$result = $apiInstance->getBaseTokenWithApiToken();
$baseToken = $result['access_token'];
$baseUuid = $result['dtable_uuid'];
```

??? question "Account-level operations"

    For operations like listing bases or getting user info, authenticate with an **Account Token** instead of an API Token. An Account Token identifies a user and gives access to all their bases. See the [API docs](https://api.seatable.com/reference/getaccounttokenfromusername) for how to obtain one.

??? question "Connecting to a self-hosted server"

    By default, the client connects to SeaTable Cloud. For self-hosted installations, set the host:

    ```php
    $config = SeaTable\Client\Configuration::getDefaultConfiguration();
    $config->setAccessToken('YOUR_TOKEN');
    $config->setHost('https://seatable.example.com');
    ```
