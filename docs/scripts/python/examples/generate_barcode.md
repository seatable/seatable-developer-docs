# Generate Barcode

This Python script demonstrates the process of converting text slices into barcode images using the `barcode` module and storing them in an image column within SeaTable. It offers an automated way to generate barcode images from text data in a SeaTable table, enhancing data visualization and association within the SeaTable platform.

Here is the structure of the table named `Generate 1 or 2D barcodes` you need so that this script could run (variables are present at the beginning of the script to easily adapt the names):

| Column name | Message | Barcode image | 
| ----------- |: ------ :|: ------ :|
| **Column type**  |  text   |   image  |

This table can be shared with the [Generate QR code example](./generate_qrcode.md) by adding it an extra *QRcode image* image-type column.

## Process Overview

1. **Iterates through rows** in a SeaTable table whose name is specified in the `TABLE_NAME` variable and check if a barcode already exists for each row (operates only on rows without barcode). Includes exception handling to manage errors encountered during the barcode image generation process.
2. **Converts text data** from a designated column (`TEXT_COL`) into barcode images using the specified barcode type (`BARCODE_TYPE`).
3. **Saves the generated barcode images** temporarily.
4. **Uploads the generated barcode images** to SeaTable and associates them with corresponding records (in the `BARCODE_IMAGE_COL` column).
5. **Removes temporary barcode image files** after successful upload.

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

api_token = context.api_token or "859ad340d9a2b...8992e14853af5"
server_url = context.server_url or "https://cloud.seatable.io"

TABLE_NAME = 'Generate 1 or 2D barcodes'
TEXT_COL = "Message"  # column which is expected to be transferred into barcode
BARCODE_IMAGE_COL = "Barcode image"
BARCODE_TYPE = 'code128'

CUSTOM_OPTIONS = {
    "module_width": 0.2,       # width of single stripe of barcode, mm
    "module_height": 30.0,     # height of barcode, mm
    "quiet_zone": 6.5,         # padding size of first and last stripe to the image, mm
    "font_size": 10,           # font size of the text below the barcode,pt
    "text_distance": 5.0,      # distance between the text and the barcode, mm
}


CODE = barcode.get_barcode_class(BARCODE_TYPE)
base = Base(api_token, server_url)
base.auth()

def get_time_stamp():
    return str(int(time.time()*100000))

updated_rows = 0
# 1. Iterate through rows
for row in base.list_rows(TABLE_NAME):
    # 1.b Continue if the image is already shown up here
    if row.get(BARCODE_IMAGE_COL):
        continue
    # 1.c Error handling
    try:
        row_id = row.get('_id')
        msg = str(row.get(TEXT_COL))

        # 2. Create a barcode object
        code_img = CODE(msg, writer=ImageWriter())

        # 3. Temporarily save the image
        save_name = "%s_%s" % (row_id, get_time_stamp())
        file_name = code_img.save("/tmp/%s" % save_name, options=CUSTOM_OPTIONS)

        # 4. Upload the barcode image to the base and associate it to the row
        info_dict = base.upload_local_file(file_name, name=None, file_type='image', replace=True)
        img_url = info_dict.get('url')
        base.update_row(TABLE_NAME, row_id, {BARCODE_IMAGE_COL: [img_url]})

        # 5. Remove the image file which was saved temporarily
        os.remove(file_name)
        updated_rows += 1
    except Exception as error:
        print("error occured during barcode generate", error)
        continue

# Summary
print("I created %s barcodes" % updated_rows)
```
