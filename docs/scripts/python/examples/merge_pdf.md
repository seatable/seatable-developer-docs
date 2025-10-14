# Merge PDF

!!! warning "Requires Python Runner v4.1.1"

    The library `pdfmerge` was added with the Python Runner version 4.1.1. If you're using SeaTable Cloud, this was added with v5.1.

This Python script demonstrates how to merge several PDF files and save the merged file into a new column in a SeaTable base. It utilizes the `pdfmerge` library to handle the PDF merging process and the `seatable_api` library to interact with SeaTable.

Here is the structure of the table named `Merge PDF` you need so that this script could run (variables are present at the beginning of the script to easily adapt the names):

| Column name | PDF files | Merged file | 
| ----------- |: ------ :|: ------ :|
| **Column type**  |  file   |   file  |

## Script Overview

The script performs the following steps:

1. **Authenticate with SeaTable:** Uses the API token and server URL to authenticate.
2. **Retrieve the files:** For each row, the script gets the name and URL of every file in the `PDF files` column.
3. **Download PDF Files**
4. **Merge PDFs:** Combines the downloaded PDF files using `pdfmerge` into a single PDF named with the pattern `output-{row_id}.pdf`.
5. **Upload Merged PDF:** Uploads the merged PDF back to SeaTable and updates the row with the new file in the `Merged file` column.

## Example Script

```python
import os
import requests
import sys
import shutil
from pdfmerge import pdfmerge
from seatable_api import Base, context
"""
This Python script demonstrates how to merge PDF 
files and save the merged file into a new column.
"""

TABLE_NAME = "Merge PDF"
FILE_COLUMN = "PDF files"
RESULT_COLUMN = "Merged file"

# 1. Authentication
base = Base(context.api_token, context.server_url)
base.auth()

# Get rows
for row in base.list_rows(TABLE_NAME):
    if row.get(FILE_COLUMN) is None:
        continue

    # 2. Retrieve all files from the row
    files = [{'name': file['name'], 'URL': file['url']} for file in row[FILE_COLUMN]]
    file_names = []

    # 3. Download PDFs
    for f in files :
        base.download_file(f['URL'],f['name'])
        file_names.append(f['name'])
    assert len(file_names) == len(files)
    print(f"Downloaded {len(files)} files")

    # 4. Merge
    output_filename = f'output-{row["_id"]}.pdf'
    pdfmerge(file_names, output_filename)
    print('Merged PDF files')

    # 5. Upload file + store URL in the base
    info_dict = base.upload_local_file(output_filename, name=None, file_type='file', replace=True)
    print(info_dict)
    base.update_row(TABLE_NAME, row['_id'], {RESULT_COLUMN: [info_dict]})
    print('Uploaded PDF file')
```
