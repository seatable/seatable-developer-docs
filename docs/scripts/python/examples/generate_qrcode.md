# Generate QR code

This Python script is designed to generate QR codes and associate them with corresponding records in a SeaTable base. In addition to `seatable_api` library, it uses the `qrcode` module to accomplish this task. In comparison to the [Generate barcode example], this example adds an `OVERWRITE` parameter to choose if existing QRcodes should be recreated or not.

Here is the structure of the table named `Generate 1 or 2D barcodes` you need so that this script could run (variables are present at the beginning of the script to easily adapt the names):

| Column name | Message | QRcode image | 
| ----------- |: ------ :|: ------ :|
| **Column type**  |  text   |   image  |

This table can be shared with the [Generate barcode example](./generate_barcode.md) by adding it an extra *Barcode image* image-type column.

## Process Overview

1. **Iterates through rows** in a SeaTable table whose name is specified in the `TABLE_NAME` variable and check if a QRcode already exists for each row (operates either on all rows or only on rows without QRcodes depending on the `OVERWRITE` parameter). Includes exception handling to manage errors encountered during the barcode image generation process.
2. **Generates QR codes** based on the text content in the designated column (`TEXT_COL`).
3. **Saves the QR code images** temporarily.
4. **Uploads the generated images** to SeaTable and associates them with corresponding records (in the `QRCODE_IMAGE_COL` column).
5. **Removes temporary image files** after successful upload.

## Code

```python
import os
import time
import qrcode
from seatable_api import Base, context
"""
The python script shows how to transfer a slice of text into a QR code image and save it into
the image column
"""

api_token = context.api_token or "859ad340d9a2b...8992e14853af5"
server_url = context.server_url or "https://cloud.seatable.io"

TABLE_NAME = "Generate 1 or 2D barcodes"
TEXT_COL = "Message"  # text column which is expected to be transferred into QR code
QRCODE_IMAGE_COL = "QR code image column"

OVERWRITE = True  # set to True to overwrite existing barcode images

base = Base(api_token, server_url)
base.auth()

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=40,
    border=8
)

def get_time_stamp():
    return str(int(time.time() * 100000))

def main():
  # 1. Iterate through rows
  for row in base.list_rows(TABLE_NAME):
    # 1.b Continue if the image is already shown up here 
    # and OVERWRITE parameter is not True
    if not OVERWRITE and row.get(QRCODE_IMAGE_COL):
      print("Skipping row. Image already exists.")
      continue
    # 1.c Error handling
    try:
      row_id = row.get('_id')
      message = row.get(TEXT_COL)

      # Check if message isn't empty before processing
      if not message:
        print("Skipping row. Empty message.")
        continue

      # 2. Clear, add data and make a QRCode object
      qr.clear()
      qr.add_data(str(message))
      qr.make()

      img = qr.make_image(fill_color="black", back_color="white")

      # 3. Temporarily save the image
      save_name = f"{row_id}_{get_time_stamp()}"
      img.save(f"/tmp/{save_name}.png")

      # 4. Upload the QR code image to the base and associate it to the row
      info_dict = base.upload_local_file(f"/tmp/{save_name}.png", name=None, file_type='image', replace=True)
      img_url = info_dict.get('url')
      base.update_row(TABLE_NAME, row_id, {QRCODE_IMAGE_COL: [img_url]})

      # 4. Remove the image file which was saved temporarily
      os.remove(f"/tmp/{save_name}.png")
    except Exception as exception:
      print("Error occurred during Image generation:", exception)
      continue

if __name__ == "__main__":
    main()
```
