# Examples

This section contains some examples of Python Scripts. The **first three scripts** are the same than in the JavaScript section. 

Even if Python scripts are capable of checking if the base structure (tables and columns) needed exist and of creating it if necessary, we didn't implement this feature in the scripts so you can focus on the actual goal of each script. 

For each example, you'll then need a special base structure so that you can just copy&paste the scripts into SeaTable and run them.

# Add rows

This script demonstrates how to add rows to record monthly repetitive expenses in a ledger.

[read more :material-arrow-right-thin:](/scripts/javascript/examples/auto-add-rows/)

## Calculate accumulated value

This script computes an accumulated value (adds the value of the current row and the previous rows), similar to the *Calculate accumulated value* operation from the data processing menu.

[read more :material-arrow-right-thin:](/scripts/javascript/examples/calculate-accumulated-value/)

## Statistics

This script computes, from a list of clocking times, daily clock in (earliest clocking) and clock out (latest clocking) times for each day and staff member.

[read more :material-arrow-right-thin:](/scripts/javascript/examples/compute-attendance-statistics/)

## Email sender

This Python script demonstrates sending emails via SMTP using the smtplib module and constructing MIME objects to compose rich content emails within SeaTable.

[read more :material-arrow-right-thin:](/scripts/python/examples/send_email/)

## Barcode generator

This Python script demonstrates the process of converting text slices into barcode images and storing them in an image column within SeaTable.

[read more :material-arrow-right-thin:](/scripts/python/examples/generate_barcode/)

## QR code generator

This Python script is designed to generate QR codes and associate them with corresponding records in a SeaTable base. It uses the seatable_api library and qrcode library to accomplish this task.

[read more :material-arrow-right-thin:](/scripts/python/examples/generate_qrcode/)

## MySQL synchronization

This Python script facilitates the synchronization of data from a MySQL database to a SeaTable table.

[read more :material-arrow-right-thin:](/scripts/python/examples/sync_mysql/)

## Watch stock price

Integrating data from the Twelve Data API with SeaTable facilitates the updating and maintenance of current stock prices within a designated table in the SeaTable environment.

[read more :material-arrow-right-thin:](/scripts/python/examples/update_stock_price/)

## Merge PDF

Merge PDF files and save the merged file into a new row in a SeaTable base.

[read more: :material-arrow-right-thin:](/scripts/python/examples/merge_pdf/)

## Convert HEIC to PNG

Convert HEIC image files to PNG format and save the converted file into a new row in a SeaTable base.

[read more: :material-arrow-right-thin:](/scripts/python/examples/heic_to_png/)
