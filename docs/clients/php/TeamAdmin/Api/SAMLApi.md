# SeaTable\Client\SAMLApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getSamlConfig()**](SAMLApi.md#getSamlConfig) | **GET** /api/v2.1/org/{org_id}/admin/saml-config/ | Get SAML Config |
| [**updateSamlConfig()**](SAMLApi.md#updateSamlConfig) | **PUT** /api/v2.1/org/{org_id}/admin/saml-config/ | Update SAML Config |
| [**verifySamlDomain()**](SAMLApi.md#verifySamlDomain) | **PUT** /api/v2.1/org/{org_id}/admin/verify-domain/ | Verify SAML domain |


## `getSamlConfig()`

```php
getSamlConfig($org_id)
```

Get SAML Config

Retrieve the current configuration details of the team's SAML (Single Sign-On) account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SAMLApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.

try {
    $apiInstance->getSamlConfig($org_id);
} catch (Exception $e) {
    echo 'Exception when calling SAMLApi->getSamlConfig: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth




## `updateSamlConfig()`

```php
updateSamlConfig($org_id, $metadata_url, $domain, $idp_certificate)
```

Update SAML Config

Update the current team's SAML (Single Sign-On) account. You have to provide at least one of the parameter `metadata_url`, `domain` or `idp_certificate`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SAMLApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$metadata_url = 'metadata_url_example'; // string | URL pointing to the metadata of your Identity Provider (IdP).
$domain = 'domain_example'; // string | Domain that should be connected to your SeaTable Team. Only email addresses with this domain will be redirected to your Identity Provider (IdP).
$idp_certificate = 'idp_certificate_example'; // string | Provide the certificate from your IdP for this service.

try {
    $apiInstance->updateSamlConfig($org_id, $metadata_url, $domain, $idp_certificate);
} catch (Exception $e) {
    echo 'Exception when calling SAMLApi->updateSamlConfig: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **metadata_url** | **string**| URL pointing to the metadata of your Identity Provider (IdP). | [optional] |
| **domain** | **string**| Domain that should be connected to your SeaTable Team. Only email addresses with this domain will be redirected to your Identity Provider (IdP). | [optional] |
| **idp_certificate** | **string**| Provide the certificate from your IdP for this service. | [optional] |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth




## `verifySamlDomain()`

```php
verifySamlDomain($org_id, $domain)
```

Verify SAML domain

Check for the \"seatable-site-verification\" value in the DNS entries of the selected domain.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: AccountTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\TeamAdmin\SAMLApi(
    new GuzzleHttp\Client(),
    $config
);
$org_id = 1; // int | The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin.
$domain = 'domain_example'; // string | Domain that should be connected to your SeaTable Team. Only email addresses with this domain will be redirected to your Identity Provider (IdP).

try {
    $apiInstance->verifySamlDomain($org_id, $domain);
} catch (Exception $e) {
    echo 'Exception when calling SAMLApi->verifySamlDomain: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **org_id** | **int**| The ID of your team/organization. Numeric. Get it from [Get Team](/reference/get-team-info). Contact your team admin, if you are not the admin. | |
| **domain** | **string**| Domain that should be connected to your SeaTable Team. Only email addresses with this domain will be redirected to your Identity Provider (IdP). | [optional] |

### Return type

void (empty response body)

### Authorization

AccountTokenAuth



