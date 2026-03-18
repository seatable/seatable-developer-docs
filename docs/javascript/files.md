# Files

The `seatable-api` npm package does not currently support file or image uploads. To upload files, you need to use the SeaTable REST API directly via `fetch()`.

## Upload workflow

Uploading a file to SeaTable requires three steps:

1. **Get an upload link** from SeaTable
2. **Upload the file** to that link
3. **Attach the file** to a row by updating the file/image column

## Complete example: Upload an image

This Node.js script uploads an image from the local filesystem and attaches it to an image column in a new row. No external dependencies required.

### Prerequisites

- A valid API token ([how to generate one](https://seatable.com/help/create-api-tokens/))
- Node.js installed on your machine

### Code

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
 * Step 1: Get upload link
 * Docs: https://api.seatable.com/reference/getuploadlink
 */
let url = `${SERVER_URL}/api/v2.1/dtable/app-upload-link/`;

let response = await fetch(url, {
  method: "GET",
  headers: { Authorization: `Token ${API_TOKEN}` },
});

const uploadLink = await response.json();

/**
 * Step 2: Upload file
 * Docs: https://api.seatable.com/reference/uploadfile
 */
const file = readFileSync(FILE_PATH);

const formData = new FormData();
formData.append("parent_dir", uploadLink.parent_path);
formData.append("file", new Blob([file.buffer]), FILE_NAME);
formData.append('relative_path', uploadLink.img_relative_path);

response = await fetch(uploadLink.upload_link + "?ret-json=1", {
  method: "POST",
  body: formData,
});

const files = await response.json();

/**
 * Step 3: Attach file to a row
 * Docs: https://api.seatable.com/reference/appendrows
 */
url = `${SERVER_URL}/api/v2.1/dtable/app-access-token/`;

response = await fetch(url, {
    headers: { Authorization: `Token ${API_TOKEN}` }
});

const baseToken = await response.json();

const workspaceId = baseToken.workspace_id;
const baseUuid = baseToken.dtable_uuid;
const relativeImageURL = `/workspace/${workspaceId}${uploadLink.parent_path}/${uploadLink.img_relative_path}/${files[0].name}`;

const body = {
    table_name: TABLE_NAME,
    rows: [
        {
            [IMAGE_COLUMN_NAME]: [relativeImageURL],
        },
    ],
};

url = `${SERVER_URL}/api-gateway/api/v2/dtables/${baseUuid}/rows/`;

response = await fetch(url, {
    method: 'POST',
    headers: {
        accept: 'application/json',
        authorization: `Bearer ${baseToken.access_token}`,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
});

console.log(await response.json());
```

### Run

```bash
node upload-file.js
```

## Further reading

The complete file and image API is documented at [api.seatable.com](https://api.seatable.com/reference/uploadfile).
