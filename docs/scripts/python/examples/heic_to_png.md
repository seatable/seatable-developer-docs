# Convert HEIC to PNG

!!! warning "Requires Python Runner v4.1.1"

    The library `pillow_heif` was added with the Python Runner version 4.1.1. If you're using SeaTable Cloud, this was added with v5.1.

This Python script demonstrates how to convert HEIC image files to PNG format and save the converted file into a new row in a SeaTable base. It uses the `pillow_heif` library to handle HEIC files, `Pillow` for image processing, and the `seatable_api` library to interact with SeaTable. The script processes **one HEIC file per row**; if you need to handle multiple HEIC files per row, you'll need to modify the script accordingly.

Here is the structure of the table named `Convert images` you need so that this script could run (variables are present at the beginning of the script to easily adapt the names):

| Column name | HEIC | PNG | 
| ----------- |: ------ :|: ------ :|
| **Column type**  |  image   |   image  |

## Script Overview

The script performs the following steps:

1. **Authenticate with SeaTable:** Uses the API token and server URL to authenticate.
2. **Download HEIC Files:** Retrieves HEIC files from the `HEIC` column in SeaTable.
3. **Convert HEIC to PNG:** Transforms the downloaded HEIC file to PNG format with 90% quality using `Pillow`.
4. **Upload Converted PNG:** (a) Uploads the PNG file back to SeaTable and (b) updates the row with the new file URL in the `PNG` column.

## Example Script

```python
import requests
from PIL import Image
from pillow_heif import register_heif_opener
from seatable_api import Base, context
"""
This Python script demonstrates how to convert HEIC image files
 to PNG format and save the converted file into a new row in a SeaTable base.
"""

# Activate heif/heic support
register_heif_opener() # (1)!

TABLE_NAME = "Convert images"
FILE_COLUMN = "HEIC"
RESULT_COLUMN = "PNG"

# 1. Authentication
base = Base(context.api_token, context.server_url)
base.auth()

for row in base.list_rows(TABLE_NAME):
    if row.get(FILE_COLUMN) is None:
        continue

    # 2. Download heic image
    url = row.get(FILE_COLUMN)[0]
    filename_heic = url.split('/')[-1]
    base.download_file(url, filename_heic)

    # 3. Transform image to png
    im = Image.open(filename_heic)
    filename_png = f'image-{row["_id"]}.png'
    im.save(filename_png, quality=90)
    print('Saved image')

    # 4.a) Upload
    info_dict = base.upload_local_file(filename_png, name=None, file_type='image', replace=True)
    print('Uploaded file')

    # 4.b) Save back to SeaTable Base
    img_url = info_dict.get('url')
    base.update_row(TABLE_NAME, row['_id'], {RESULT_COLUMN: [img_url]})
    print('Stored image info in base')
```

1. Note the `register_heif_opener()` call to enable HEIC file support.

