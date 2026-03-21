---
description: PHP code examples for SeaTable — get account info, list bases, retrieve metadata, run SQL queries, and add rows.
---

# Examples

## Get account information

Connect to SeaTable Cloud and retrieve your account details.

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$config = SeaTable\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCOUNT_TOKEN');

$apiInstance = new SeaTable\Client\User\UserApi(
    new GuzzleHttp\Client(), $config
);

try {
    $result = $apiInstance->getAccountInfo();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception: ', $e->getMessage(), PHP_EOL;
}
```

## List your bases

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$config = SeaTable\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCOUNT_TOKEN');

$apiInstance = new SeaTable\Client\User\BasesApi(
    new GuzzleHttp\Client(), $config
);

try {
    $result = $apiInstance->listBases();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception: ', $e->getMessage(), PHP_EOL;
}
```

## Get base metadata

First obtain a Base Token from your API Token, then retrieve the metadata.

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Step 1: Get Base Token
$config = SeaTable\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_API_TOKEN');

$apiInstance = new SeaTable\Client\Auth\BaseTokenApi(
    new GuzzleHttp\Client(), $config
);

$result = $apiInstance->getBaseTokenWithApiToken();

// Step 2: Get Metadata
$config = SeaTable\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken($result['access_token']);

$apiInstance = new SeaTable\Client\Base\BaseInfoApi(
    new GuzzleHttp\Client(), $config
);

try {
    $result = $apiInstance->getMetadata($result['dtable_uuid']);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception: ', $e->getMessage(), PHP_EOL;
}
```

## Execute an SQL query

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Step 1: Get Base Token
$config = SeaTable\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_API_TOKEN');

$authApi = new SeaTable\Client\Auth\BaseTokenApi(
    new GuzzleHttp\Client(), $config
);
$auth = $authApi->getBaseTokenWithApiToken();

// Step 2: Query
$config = SeaTable\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken($auth['access_token']);

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(), $config
);

$sqlQuery = new SeaTable\Client\Base\SqlQuery([
    "sql" => "SELECT * FROM Table1",
    "convert_keys" => false
]);

try {
    $result = $apiInstance->querySQL($auth['dtable_uuid'], $sqlQuery);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception: ', $e->getMessage(), PHP_EOL;
}
```

## Add a row

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Step 1: Get Base Token
$config = SeaTable\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_API_TOKEN');

$authApi = new SeaTable\Client\Auth\BaseTokenApi(
    new GuzzleHttp\Client(), $config
);
$auth = $authApi->getBaseTokenWithApiToken();

// Step 2: Append row
$config = SeaTable\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken($auth['access_token']);

$apiInstance = new SeaTable\Client\Base\RowsApi(
    new GuzzleHttp\Client(), $config
);

$request = new SeaTable\Client\Base\AppendRows([
    'table_name' => 'Table1',
    'rows' => [
        ['Name' => 'Inserted via API'],
    ],
    'apply_default' => false,
]);

try {
    $result = $apiInstance->appendRows($auth['dtable_uuid'], $request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception: ', $e->getMessage(), PHP_EOL;
}
```
