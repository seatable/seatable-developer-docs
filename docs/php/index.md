# PHP

The SeaTable PHP Client encapsulates the SeaTable REST API. It enables you to call every available API endpoint from your PHP application -- interact with user accounts, bases, rows, or files.

!!! info "Auto-generated from OpenAPI specification"

    Since April 2024, the PHP client is auto-generated from the public OpenAPI specification. This ensures all API endpoints are covered automatically. The trade-off: the new version is not compatible with v0.2 and earlier.

## Installation

The SeaTable PHP Client is available on [Packagist](https://packagist.org/packages/seatable/seatable-api-php) and can be installed with [Composer](https://getcomposer.org/):

```
composer require seatable/seatable-api-php
```

The source code is available on [GitHub](https://github.com/seatable/seatable-api-php).

## Authentication

SeaTable uses two types of tokens:

- **Account Token**: Identifies a user. Gives access to all bases the user can see. Obtained by logging in with username and password ([see API docs](https://api.seatable.com/reference/getaccounttokenfromusername)).
- **API Token**: Identifies a specific base. Grants read or read/write access to one base. Generated in the [SeaTable web interface](https://seatable.com/help/erzeugen-eines-api-tokens/).

Most operations on base data require a **Base Token**, which you obtain by exchanging an API Token:

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

For account-level operations (list bases, get user info), use the Account Token directly.

### Connecting to a self-hosted server

By default, the client connects to SeaTable Cloud. For self-hosted installations, set the host:

```php
$config = SeaTable\Client\Configuration::getDefaultConfiguration();
$config->setAccessToken('YOUR_TOKEN');
$config->setHost('https://seatable.example.com');
```
