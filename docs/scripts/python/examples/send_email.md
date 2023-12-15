# Send E-mails

This Python script demonstrates sending emails via SMTP using the smtplib library and constructing MIME objects to compose rich content emails within SeaTable.

## Functionality

- Setup and Authentication: Uses SMTP parameters and SeaTable API credentials for authentication and sending emails.
- Recipient Selection: Retrieves email addresses from a SeaTable table's column (Contacts -> Email) to serve as multiple recipients.
- Email Composition:

      - Constructs an email with a specified subject, sender, and HTML content body for the email.
      - Allows for attaching files stored in SeaTable records to the email.

## Process Overview

1. Retrieves recipient email addresses from a designated SeaTable table column (Contacts -> Email).
1. Composes an email using HTML content to create a rich-text message body.
1. Attaches a file from SeaTable to the email by fetching its download link using the SeaTable API and attaching it to the email.

This script offers an automated way to send emails with rich content and attachments using data stored within SeaTable, enabling streamlined communication and file sharing within the SeaTable environment.

## Code

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from urllib import parse
import requests
from seatable_api import Base, context

# SeaTable API authentication
base = Base(context.api_token, context.server_url)
base.auth()

# SMTP server configurations for sending emails
smtpserver = 'smtp.163.com'
username = '13069744444@163.com'
password = 'topsecret'
sender = '13069744444@163.com'

# Option a) define the recipient email address in this script
receivers = ['1223408888@qq.com']

# Option b) Retrieving recipient email addresses from the 'Contacts' table in SeaTable
receiver_rows = base.list_rows('Contacts')
receivers = [row['Email'] for row in receiver_rows if row.get('Email')]

# Email subject
subject = 'SeaTable Send email'

# Constructing the email message
msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = '13069744444@163.com <13069744444@163.com>'
msg['To'] = ";".join(receivers)

# Option a) plain text message
# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.google.com"
# text_plain = MIMEText(text,'plain', 'utf-8')
# msg.attach(text_plain)

# Option b) HTML content for the email body
html = """
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       This is a sample of messages
       from SeaTable
    </p>
  </body>
</html>
"""
text_html = MIMEText(html,'html', 'utf-8')
msg.attach(text_html)

# Attaching a file from SeaTable to the email
rows = base.list_rows('Table3')
filename = rows[0]['File'][0]['name']
file_url = rows[0]['File'][0]['url']
path = file_url[file_url.find('/files/'):]
download_link = base.get_file_download_link(parse.unquote(path))

try:
    response = requests.get(download_link)
    if response.status_code != 200:
        print('Failed to download image, status code: ', response.status_code)
        exit(1)
except Exception as e:
    print(e)
    exit(1)

# Attaching the file to the email
text_att = MIMEText(response.content, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
text_att["Content-Disposition"] = 'attachment;filename*=UTF-8\'\'' + parse.quote(filename)

msg.attach(text_att)

# Sending the email using SMTP
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receivers, msg.as_string())
smtp.quit()
```
