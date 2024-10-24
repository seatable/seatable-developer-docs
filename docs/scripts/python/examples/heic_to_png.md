# Convert HEIC to PNG

!!! warning "Requires Python Runner v4.1.1"

    The library `pillow_heif` was added with the Python Runner version 4.1.1. If you're using SeaTable Cloud, this was added with v5.1.

This Python script demonstrates how to convert HEIC image files to PNG format and save the converted file into a new row in a SeaTable base. It utilizes the `pillow_heif` library to handle HEIC files, `Pillow` for image processing, and the `seatable_api` library to interact with SeaTable.

## Script Overview

The script performs the following steps:

- **Authenticate with SeaTable:** Uses the API token and server URL to authenticate.
- **Download HEIC Files:** Retrieves HEIC files from a specified column in SeaTable.
- **Convert HEIC to PNG:** Transforms the downloaded HEIC file to PNG format.
- **Upload Converted PNG:** Uploads the PNG file back to SeaTable and updates the row with the new file URL.

## Example Script

```python
import requests
from PIL import Image
from pillow_heif import register_heif_opener
from seatable_api import Base, context

# Activate heif/heic support
register_heif_opener()

# >>> UPDATE THESE VALUES ACCORDING TO YOUR NEEDS
TABLE_NAME = "Table1"
FILE_COLUMN = "HEIC"
RESULT_COLUMN = "PNG"

# Authentication
base = Base(context.api_token, context.server_url)
base.auth()

for row in base.list_rows(TABLE_NAME):
    if row.get(FILE_COLUMN) is None:
        continue

    # input must be image.heic, output is image-xxx.png
    filename_heic = 'image.heic'
    filename_png = f'image-{row["_id"]}.png'

    # Download heic image
    url = row.get(FILE_COLUMN)[0]
    base.download_file(url, filename_heic)

    # transform image to png
    im = Image.open(filename_heic)
    im.save(filename_png, quality=90)
    print('Saved image')

    # Upload
    info_dict = base.upload_local_file(filename_png, name=None, file_type='image', replace=True)
    print('Uploaded file')

    # Save back to SeaTable Base
    img_url = info_dict.get('url')
    base.update_row(TABLE_NAME, row['_id'], {RESULT_COLUMN: [img_url]})
    print('Stored image info in base')
```

## Detailed Steps

- **HEIC Support Activation:** The script uses register_heif_opener() to enable HEIC file support.
- **Authentication:** The script uses Base from seatable_api to authenticate using the API token and server URL.
- **File Handling:** It downloads HEIC files specified in the HEIC column for each row. The files are saved locally as image.heic.
- **Conversion Process:** The script uses Pillow to open the HEIC file and save it as a PNG with 90% quality.
- **Uploading and Updating:** The converted PNG file is uploaded back to SeaTable, and its URL is stored in the PNG column of the same row.

## Usage Notes

Ensure that each row in `Table1` contains a HEIC-file in the `HEIC` column for successful execution.
Adjust table and column names as necessary to fit your specific SeaTable configuration.
The script processes one HEIC file per row. If you need to handle multiple HEIC files per row, you'll need to modify the script accordingly.
