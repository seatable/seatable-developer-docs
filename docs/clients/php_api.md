# PHP Client

SeaTable's API exposes the entire SeaTable features via a standardized programmatic interface. The _SeaTable PHP Client_ encapsulates SeaTable Server Restful API. If you are familiar this client enables you to call every available API endpoint of SeaTable. You can interact with the user accounts, bases or files.

!!! success "Auto generated from openapi specification"

    Since April 2024, we auto generate this SeaTable php client from our public available openapi specification. The advantage is that, the php client automatically contains all available API endpoints and we save a lot of programming capacity. Also we could generate more api clients for other programming languages in no time with the same feature set. The disadvantage is, that with this new client we removed some convenitent functions for authentication and the new version is not compatible at all with the version v0.2 and earlier.

## Installation

The SeaTable API installs as part of your project dependencies. It is available from [Packagist](https://packagist.org/packages/seatable/seatable-api-php) and can be installed with [Composer](https://getcomposer.org/):

```
composer require seatable/seatable-api-php
```

The source code of the PHP Client API is available at [GitHub](https://github.com/seatable/seatable-api-php).

## Getting Started

After installation you can easily connect to your SeaTable system and execute API calls.

### Get information about your account

The following code connects to SeaTable Cloud. You have to provide your `Account Token`.
Please refer to [api.seatable.io](https://api.seatable.io/reference/getaccounttokenfromusername) for guidance on how to obtain an `Account Token`.

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCOUNT_TOKEN');

$apiInstance = new SeaTable\Client\User\UserApi(new GuzzleHttp\Client(), $config);

try {
    $result = $apiInstance->getAccountInfo();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling UserApi->getAccountInfo: ', $e->getMessage(), PHP_EOL;
}
```

### List your bases

This time, we connect to a self-hosted SeaTable Server.

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth
$config = SeaTable\Client\Configuration::getDefaultConfiguration();
$config->setAccessToken('YOUR_ACCOUNT_TOKEN');
$config->setHost('https://seatable.example.com');

$apiInstance = new SeaTable\Client\User\BasesApi(new GuzzleHttp\Client(), $config);

try {
    $result = $apiInstance->listBases();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BasesApi->listBases: ', $e->getMessage(), PHP_EOL;
}
```

### Get Metadata from your Base

First we have to get the `Base-Token` and the `base_uuid` and then we can execute the `getMetadata` call.

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Prerequisite: API Token for your base
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_API_TOKEN');

$apiInstance = new SeaTable\Client\Auth\BaseTokenApi(new GuzzleHttp\Client(), $config);

try {
    $result = $apiInstance->getBaseTokenWithApiToken();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseTokenApi->getBaseTokenWithApiToken: ', $e->getMessage(), PHP_EOL;
}

// Metadata
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken($result['access_token']);
$apiInstance = new SeaTable\Client\Base\BaseInfoApi(new GuzzleHttp\Client(), $config);

try {
    $result = $apiInstance->getMetadata($result['dtable_uuid']);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseInfoApi->getMetadata: ', $e->getMessage(), PHP_EOL;
}
```

### Execute SQL-Query against your base

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Prerequisite: API Token for your base
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_API_TOKEN');

$apiInstance = new SeaTable\Client\Auth\BaseTokenApi(new GuzzleHttp\Client(), $config);

try {
    $result = $apiInstance->getBaseTokenWithApiToken();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseTokenApi->getBaseTokenWithApiToken: ', $e->getMessage(), PHP_EOL;
}

// Base query
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken($result['access_token']);

$apiInstance = new SeaTable\Client\Base\RowsApi(new GuzzleHttp\Client(), $config);

$base_uuid = $result['dtable_uuid'];
$sql_query = new SeaTable\Client\Base\SqlQuery(["sql" => "Select * from Table1", "convert_keys" => false]);

try {
    $result = $apiInstance->querySQL($base_uuid, $sql_query);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->querySQL: ', $e->getMessage(), PHP_EOL;
}
```

### Add a row to your base

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Prerequisite: API Token for your base
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_API_TOKEN');

$apiInstance = new SeaTable\Client\Auth\BaseTokenApi(new GuzzleHttp\Client(), $config);

try {
    $result = $apiInstance->getBaseTokenWithApiToken();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BaseTokenApi->getBaseTokenWithApiToken: ', $e->getMessage(), PHP_EOL;
}

// Base query
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken($result['access_token']);

$apiInstance = new SeaTable\Client\Base\RowsApi(new GuzzleHttp\Client(), $config);

$base_uuid = $result['dtable_uuid'];
$request = new SeaTable\Client\Base\AppendRows([
    'table_name' => 'Table1',
    'rows' => [
        [
            'Name' => 'Inserted via API',
        ],
    ],
    // Whether to apply default values
    'apply_default' => false,
]);

try {
    $result = $apiInstance->appendRows($base_uuid, $request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RowsApi->appendRows: ', $e->getMessage(), PHP_EOL;
}
```

## API Endpoints

You can find detailed documentation for all endpoints including auto-generated examples on [GitHub](https://github.com/seatable/seatable-api-php):

 - [Auth](https://github.com/seatable/seatable-api-php/blob/main/README_Auth.md)
 - [Base](https://github.com/seatable/seatable-api-php/blob/main/README_Base.md)
 - [File](https://github.com/seatable/seatable-api-php/blob/main/README_File.md)
 - [SysAdmin](https://github.com/seatable/seatable-api-php/blob/main/README_SysAdmin.md)
 - [TeamAdmin](https://github.com/seatable/seatable-api-php/blob/main/README_TeamAmin.md)
 - [User](https://github.com/seatable/seatable-api-php/blob/main/README_User.md)
