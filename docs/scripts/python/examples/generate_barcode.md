# Generate Barcode

This Python script demonstrates the process of converting text slices into barcode images and storing them in an image column within SeaTable.

## Functionality

- Setup and Authentication: Utilizes SeaTable API credentials for authentication.
- Barcode Generation: Processes rows in a specified SeaTable table, extracting text from a designated column (TEXT_COL) to generate barcode images.
- Association with Records: Associates generated barcode images with the respective records by updating an image column (BARCODE_IMAGE_COL) in the SeaTable table.
- Handling Existing Images: Skips rows if a barcode image already exists for efficient processing.
- Customization Options: Provides customizable parameters such as module width, height, padding, font size, and text-barcode distance for barcode image generation.
- Error Handling: Includes exception handling to manage errors encountered during the barcode image generation process.

## Process Overview

1. Iterates through rows in a specified SeaTable table.
1. Converts text data from a designated column into barcode images using the specified barcode type (BARCODE_TYPE).
1. Saves the generated barcode images temporarily.
1. Uploads the generated barcode images to SeaTable and associates them with corresponding records.
1. Removes temporary barcode image files after successful upload.
1. This script offers an automated way to generate barcode images from text data in a SeaTable table, enhancing data visualization and association within the SeaTable platform.

## Code

```python
import os
import time
import barcode
from barcode.writer import ImageWriter
from seatable_api import Base, context
"""
The python script shows how to transfer a slice of text into a barcode image and save it into
the image column
"""

api_token = context.api_token or "859ad340d9a2b11b067c11f43078992e14853af5"
server_url = context.server_url or "https://cloud.seatable.io"

TEXT_COL = "Message"  # column which is expected to be transferred into barcode
BARCODE_IMAGE_COL = "BarcodeImage"
TABLE_NAME = 'Table1'
BARCODE_TYPE = 'code128'

CUSTOM_OPTIONS = {
    "module_width": 0.2,       # width of single stripe of barcode, mm
    "module_height": 15.0,     # height of barcode, mm
    "quiet_zone": 6.5,         # padding size of first and last stripe to the image, mm
    "font_size": 10,           # font size of the text below the barcode,pt
    "text_distance": 5.0,      # distance between the text and the barcode, mm
}


CODE = barcode.get_barcode_class(BARCODE_TYPE)
base = Base(api_token, server_url)
base.auth()

def get_time_stamp():
    return str(int(time.time()*100000))

for row in base.list_rows(TABLE_NAME):
    # continue if the image is already shown up here
    if row.get(BARCODE_IMAGE_COL):
        continue

    try:
        row_id = row.get('_id')
        msg = str(row.get(TEXT_COL))

        # create a barcode object
        code_img = CODE(msg, writer=ImageWriter())
        save_name = "%s_%s" % (row_id, get_time_stamp())

        # temporarily saved as an image
        file_name = code_img.save("/tmp/%s" % save_name, options=CUSTOM_OPTIONS)

        # upload the barcode image to the base
        info_dict = base.upload_local_file(file_name, name=None, file_type='image', replace=True)
        img_url = info_dict.get('url')
        row[BARCODE_IMAGE_COL] = [img_url]
        base.update_row('Table1', row_id, row)

        # remove the image file which is saved temporarily
        os.remove(file_name)
    except Exception as error:
        print("error occured during barcode generate", error)
        continue
```
