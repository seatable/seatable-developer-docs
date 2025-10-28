# File Upload

The following script uploads an image from the local filesystem and attaches it to an image column.

!!! note "seatable-api NPM Package"

    The script does **not** use the `seatable-api` NPM package since the package does not currently support file/image uploads.
    Instead, `fetch()` is used. The script does not require any external dependencies.

## Prerequisites

You need a valid API token in order to execute the script.
Set the `API_TOKEN` variable inside the script to the value of your token.
You can generate an API token inside the [SeaTable UI](https://seatable.com/help/create-api-tokens/) or by using your [account token](https://api.seatable.com/reference/createapitoken).

## Code

```js
import { readFileSync } from 'fs';
import { basename } from 'path';

const SERVER_URL = 'https://cloud.seatable.io';
const API_TOKEN = '';
const TABLE_NAME = 'Table1';
const IMAGE_COLUMN_NAME = 'Images';

// Absolute path to the file on the local filesystem
const FILE_PATH = 'Test.svg';
const FILE_NAME = basename(FILE_PATH);

/**
 * Get file upload link
 * Docs: https://api.seatable.com/reference/getuploadlink
 */
let url = `${SERVER_URL}/api/v2.1/dtable/app-upload-link/`;

console.log("Generating upload link...\n");

let response = await fetch(url, {
  method: "GET",
  headers: { Authorization: `Token ${API_TOKEN}` },
});

const uploadLink = await response.json();

console.log(uploadLink, '\n');

/**
 * Upload file from the local filesystem
 * Docs: https://api.seatable.com/reference/uploadfile
 */
const file = readFileSync(FILE_PATH);

const formData = new FormData();
formData.append("parent_dir", uploadLink.parent_path);
formData.append("file", new Blob([file.buffer]), FILE_NAME);
formData.append('relative_path', uploadLink.img_relative_path);

console.log('Uploading file...\n')

response = await fetch(uploadLink.upload_link + "?ret-json=1", {
  method: "POST",
  body: formData,
});

const files = await response.json();

console.log(files, '\n');

/**
 * Generate base token by using an API token
 * Base operations such as inserting or updating rows require a base token
 * Docs: https://api.seatable.com/reference/getbasetokenwithapitoken
 */
url = `${SERVER_URL}/api/v2.1/dtable/app-access-token/`;

console.log('Generating base token...\n');

response = await fetch(url, {
    headers: { Authorization: `Token ${API_TOKEN}` }
});

const baseToken = await response.json();

console.log(baseToken, '\n');

/**
 * Append row to base
 * This attaches the image to an image column
 * This API call requires a valid base token
 * Docs: https://api.seatable.com/reference/appendrows
 */
const workspaceId = baseToken.workspace_id;
const baseUuid = baseToken.dtable_uuid;
const relativeImageURL = `/workspace/${workspaceId}${uploadLink.parent_path}/${uploadLink.img_relative_path}/${files[0].name}`;

const body = {
    table_name: TABLE_NAME,
    rows: [
        {
            // The values of image/file columns are arrays
            [IMAGE_COLUMN_NAME]: [relativeImageURL],
        },
    ],
};

url = `${SERVER_URL}/api-gateway/api/v2/dtables/${baseUuid}/rows/`;

console.log('Appending row...\n')

response = await fetch(url, {
    method: 'POST',
    headers: {
        accept: 'application/json',
        authorization: `Bearer ${baseToken.access_token}`,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
});

console.log(await response.json())
```

## Executing the Script

You can use the following command to execute the script on the commandline using Node.js:

```bash
node upload-file.js
```
