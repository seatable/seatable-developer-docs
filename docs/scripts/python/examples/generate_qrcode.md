# Generate QR-Code

This Python script is designed to generate QR codes and associate them with corresponding records in a SeaTable base. It uses the `seatable_api` library and `qrcode` module to accomplish this task.

## Functionality

- Setup and Authentication: Utilizes SeaTable API credentials for authentication.
- QR Code Generation: Processes rows in a specified SeaTable table, extracting text from a designated column (STRING_COLUMN) to generate QR codes.
- Association with Records: Associates generated QR code images with the respective records by updating an image column (IMAGE_COLUMN) in the SeaTable table.
- Handling Existing Images: Allows the option to skip rows if an image already exists or overwrite existing barcode images based on the OVERWRITE flag.
- Error Handling: Provides error handling to manage exceptions during the QR code generation process.

## Process Overview

1. Iterates through rows in a specified SeaTable table.
1. Generates QR codes based on the text content in the designated column.
1. Saves the QR code images temporarily.
1. Uploads the generated images to SeaTable and associates them with corresponding records.
1. Removes temporary image files after successful upload.

This script offers an automated way to generate QR codes from text data in a SeaTable table, enhancing data visualization and association within the SeaTable platform.

## Code

```python
import os
import time
import qrcode
from seatable_api import Base, context

api_token = context.api_token or "..."
server_url = context.server_url or "https://cloud.seatable.io"

STRING_COLUMN = "String"  # text column which is expected to be transferred into qrcode
IMAGE_COLUMN = "Image"
TABLE_NAME = "Table1"
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
  for row in base.list_rows(TABLE_NAME):
    if not OVERWRITE and row.get(IMAGE_COLUMN):
      print("Skipping row. Image already exists.")
      continue

    try:
      row_id = row.get('_id')
      message = row.get(STRING_COLUMN)

      if not message:
        print("Skipping row. Empty message.")
        continue

      # clear, add data and make an qrcode object
      qr.clear()
      qr.add_data(str(message))
      qr.make()

      img = qr.make_image(fill_color="black", back_color="white")

      save_name = f"{row_id}_{get_time_stamp()}"
      img.save(f"/tmp/{save_name}.png")

      # temporarily saved as an image
      info_dict = base.upload_local_file(f"/tmp/{save_name}.png", name=None, file_type='image', replace=True)
      img_url = info_dict.get('url')
      row[IMAGE_COLUMN] = [img_url]
      base.update_row(TABLE_NAME, row_id, row)

      # remove the image file which is saved temporarily
      os.remove(f"/tmp/{save_name}.png")
    except Exception as exception:
      print("Error occurred during Image generation:", exception)
      continue

if __name__ == "__main__":
    main()
```
