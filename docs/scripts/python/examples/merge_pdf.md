# Merge PDF

!!! warning "Requires Python Runner v4.1.1"

    The library `pdfmerge` was added with the Python Runner version 4.1.1. If you're using SeaTable Cloud, this was added with v5.1.

This Python script demonstrates how to merge two PDF files and save the merged file into a new row in a SeaTable base. It utilizes the `pdfmerge` library to handle the PDF merging process and the `seatable_api` library to interact with SeaTable.

## Script Overview

The script performs the following steps:

- **Authenticate with SeaTable:** Uses the API token and server URL to authenticate.
- **Download PDF Files:** Retrieves two PDF files from a specified column in SeaTable.
- **Merge PDFs:** Combines the downloaded PDF files into a single PDF using pdfmerge.
- **Upload Merged PDF:** Uploads the merged PDF back to SeaTable and updates the row with the new file.

## Example Script

```python
import os
import pdfmerge
import requests
import sys
import shutil
from pdfmerge import pdfmerge
from seatable_api import Base, context

# >>> UPDATE THESE VALUES ACCORDING TO YOUR NEEDS
TABLE_NAME = "Table1"
FILE_COLUMN = "PDF Files"
RESULT_COLUMN = "Merged Files"
FILENAMES = ['file-1.pdf', 'file-2.pdf']

# Authentication
base = Base(context.api_token, context.server_url)
base.auth()

# Get rows
for row in base.list_rows(TABLE_NAME):
    if row.get(FILE_COLUMN) is None:
        continue

    files = [file['url'] for file in row[FILE_COLUMN]]
    assert len(files) == 2

    # Download pdfs
    base.download_file(files[0], FILENAMES[0])
    base.download_file(files[1], FILENAMES[1])
    print('Downloaded 2 files')

    # Merge
    output_filename = f'output-{row["_id"]}.pdf'
    pdfmerge(FILENAMES, output_filename)
    print('Merged PDF files')

    # Upload file + store URL in base
    info_dict = base.upload_local_file(output_filename, name=None, file_type='file', replace=True)
    base.update_row(TABLE_NAME, row['_id'], {RESULT_COLUMN: [info_dict]})
    print('Uploaded PDF file')
```

## Detailed Steps

- **Authentication:** The script uses Base from seatable_api to authenticate using the API token and server URL.
- **File Handling:** It downloads two PDFs specified in the `PDF Files` column for each row. The files are saved locally as `file-1.pdf` and `file-2.pdf`.
- **Merging Process:** The pdfmerge function is used to merge these two PDFs into a single file named with the pattern output-{row_id}.pdf.
- **Uploading and Updating:** The merged file is uploaded back to SeaTable, and its URL is stored in the `Merged Files` column of the same row.

## Usage Notes

Ensure that each row in `Table1` contains exactly two PDFs in the `PDF Files` column for successful execution.
Adjust table and column names as necessary to fit your specific SeaTable configuration.
