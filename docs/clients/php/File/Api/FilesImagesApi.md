# SeaTable\Client\FilesImagesApi

All URIs are relative to https://cloud.seatable.io, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getFileDownloadLink()**](FilesImagesApi.md#getFileDownloadLink) | **GET** /api/v2.1/dtable/app-download-link/ | Get File Download Link |
| [**getUploadLink()**](FilesImagesApi.md#getUploadLink) | **GET** /api/v2.1/dtable/app-upload-link/ | Get Upload Link |
| [**uploadFile()**](FilesImagesApi.md#uploadFile) | **POST** /seafhttp/upload-api/{upload_link}?ret-json&#x3D;1 | Upload File (or Image) |


## `getFileDownloadLink()`

```php
getFileDownloadLink($path): object
```

Get File Download Link

Get the file download link of a base's attachment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: ApiTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\File\FilesImagesApi(
    new GuzzleHttp\Client(),
    $config
);
$path = /images/2021-03/test.png; // string | Path to the file

try {
    $result = $apiInstance->getFileDownloadLink($path);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilesImagesApi->getFileDownloadLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **path** | **string**| Path to the file | |

### Return type

**object**

### Authorization

[ApiTokenAuth](../../README.md#ApiTokenAuth)



## `getUploadLink()`

```php
getUploadLink(): object
```

Get Upload Link

With the **API token** (not the Base Token), you can generate an upload link, the parent- and the relative path. These information are needed to upload a file / an image to a bases. Then this file/image can be attached to a file/image column.   > 📘 The upload link is only valid for a short time >  > The upload link is only valid for some minutes. After that the upload link must be created again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: ApiTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\File\FilesImagesApi(
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getUploadLink();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilesImagesApi->getUploadLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiTokenAuth](../../README.md#ApiTokenAuth)



## `uploadFile()`

```php
uploadFile($upload_link, $file, $parent_dir, $relative_path, $replace): object
```

Upload File (or Image)

Upload a file or an image as an attachment to a base. To execute this request you need to generate an upload link first.   > 📘 Three steps to add a file/an image to a base >  > To add an image or a file to a base, three steps are necessary:  > 1. [Generate an upload link](/reference/getUploadLink). > 2. Upload the file to the base as an attachment. (this article) > 3. [Update a row](/reference/updateRow) and attach the file/the image to a file or image column.   > 📘 Different variable names >  > Pay attention that the return values of upload link have slightly different names, so `parent_path` is `parent_dir` in this call.  ## Attach the file/image to a file or image column  After uploading the file/image to a base, SeaTable saves the uploaded file at non-public URL in the form: `/workspace/{workspace_id}`+`parent_dir`+`relative_path`+`name`.   Here is an example how this might look like: `https://cloud.seatable.io/workspace/24/asset/55f2f056-5da1-4095-b5f8-791bb51b991e/images/2023-07/party.png` If you are logged in with your browser, you can access this file. Otherwise you will see the login screen.  Knowing this URL, you can add a new row or update an existing row and use the URL to add this attachment to your file/image column. ``` # Example how to add an already uploaded image to a row: \"row\": {   \"My Image Column\": [\"/workspace/24/asset/55f2f056-5da1-4095-b5f8-791bb51b991e/images/2023-07/party.png`\"] }  # Example how to add an already uploaded file to a row: \"row\": {   \"File Column\": [{     \"name\": \"invoice.pdf\",      \"size\": 101454,      \"type\": \"file\",      \"url\": \"/workspace/24/asset/55f2f056-5da1-4095-b5f8-791bb51b991e/images/2023-07/invoice.pdf\"   }] } ``` > 🚧 File requires the input variables size, type and url >  > As you can see, in the case of an image the URL is sufficient to attach the image to an image column. In case of a file, you have to provide all four input values.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure Bearer authorization: ApiTokenAuth (use the right token for your request)
$config = SeaTable\Client\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');

$apiInstance = new SeaTable\Client\File\FilesImagesApi(
    new GuzzleHttp\Client(),
    $config
);
$upload_link = 5e666848-4152-45e5-990e-d686960f2a05; // string | This is the value you got from the call Get File/Image Upload Link via API Token.
$file = "/path/to/file.txt"; // \SplFileObject | The file or image you'd like to upload from your local drive.
$parent_dir = 'parent_dir_example'; // string | This is the value of the `parent_path` you got from the call **Get File/Image Upload Link via API Token**.
$relative_path = 'relative_path_example'; // string | If you are uploading a file, use the value of the `file_relative_path` returned in the call **Get File/Image Upload Link via API Token**; or the `img_relative_path` for image.
$replace = 'replace_example'; // string | Do you want to overwrite a file/image with the same name? `0` - No, `1` - Yes. Optional. `0` by default. If existing file is not overwritten, the uploaded file will be renamed as `filename(1).xxx`.

try {
    $result = $apiInstance->uploadFile($upload_link, $file, $parent_dir, $relative_path, $replace);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilesImagesApi->uploadFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **upload_link** | **string**| This is the value you got from the call Get File/Image Upload Link via API Token. | |
| **file** | **\SplFileObject****\SplFileObject**| The file or image you&#39;d like to upload from your local drive. | |
| **parent_dir** | **string**| This is the value of the &#x60;parent_path&#x60; you got from the call **Get File/Image Upload Link via API Token**. | |
| **relative_path** | **string**| If you are uploading a file, use the value of the &#x60;file_relative_path&#x60; returned in the call **Get File/Image Upload Link via API Token**; or the &#x60;img_relative_path&#x60; for image. | |
| **replace** | **string**| Do you want to overwrite a file/image with the same name? &#x60;0&#x60; - No, &#x60;1&#x60; - Yes. Optional. &#x60;0&#x60; by default. If existing file is not overwritten, the uploaded file will be renamed as &#x60;filename(1).xxx&#x60;. | [optional] |

### Return type

**object**

### Authorization

[ApiTokenAuth](../../README.md#ApiTokenAuth)


