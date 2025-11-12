# Send emails

This Python script demonstrates sending emails via SMTP using the [smtplib module](https://docs.python.org/3/library/smtplib.html), constructing MIME objects to compose rich content emails within SeaTable and creating HTML content from a "long text"-type column using the markdown module. It also retrieves configuration parameters from the database. This example uses two tables:

- The `Contacts` table storing the contacts you want to send email to:

| Column name | Name | Email | 
| ----------- |: ------ :|: ------ :|
| **Column type**  |  text   |   email  |

- The `Send email config` table storing the email sending parameters:

| Column name | Subject | Recipient email | Subject source| Email format | Attach file | File |
| ----------- |: ----- :|: ------------- :|: ----------- :|: ---------- :|: --------- :|: -- :|
| **Column type**  | text  | single select | single select | single select | checkbox | file |

- Recipient email can be `hard-coded` (recipients are defined l.48 of the script as a list of email addresses) or `database` (recipients are retrieved from the `Email` column of the `Contacts` table).
- `Subject source` can be `hard-coded` (define manually the subject of the mail l.57 of the script) or `database` (the subject is retrieved from the `Subject` column of the `Send email config` table).
- Email format can be `text` (plain text defined l.71), `html` (HTML-formatted message, defined l.77) or `database` (the email body retrieved from the `Email body` column of the `Send email config` table).
- If `Attach file` is checked, the first file from the `File` column will be enclosed (don't forget to adapt the `_subtype` l.115 of the script if your file is not a pdf).
- You can eventually add a `Send email` column, configured to launch the script. The script itself is written to use either the `context.current_row` data, or the first row of the table if no `context` is defined (script launched from outside SeaTable).

## Process overview

1. **Retrieves email configuration** from the `Send email config` table.
2. Eventually **retrieves recipient email addresses** from a designated SeaTable table column (`Email` column in `Contact` table).
3. Eventually **retrieves email subject**.
3. Eventually **retrieves email body**.
4. **Composes an email** using plain text or HTML content to create a rich-text message body.
5. **Attaches a file** from SeaTable to the email by fetching its download link using the SeaTable API and attaching it to the email.
6. **Sends the email** after authenticating using SMTP parameters.

## Code

```python linenums="1"
import markdown
import smtplib, ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from urllib import parse
import requests
from seatable_api import Base, context
"""
This Python script demonstrates sending emails via SMTP 
using the smtplib module and constructing MIME objects 
to compose rich content emails within SeaTable.
"""

# SeaTable API authentication
base = Base(context.api_token, context.server_url)
base.auth()

CONFIG_TABLE = 'Send email config'
CONTACTS_TABLE = 'Contacts'

# SMTP server configurations for sending emails
SMTP_SERVER = 'my.smtpserver.com'
SMTP_PORT = 465
USERNAME = 'my.em@il.com'
PASSWORD = 'topsecret'
SENDER = 'My name'

# 1. Get email configuration from the 'Send email config' table
current_row = context.current_row or base.list_rows(CONFIG_TABLE)[0]
# Choose RECIPIENT_EMAIL between "hard-coded" (addresses l.48 of this script)
# or "database" (get emails from 'Email' column in the 'Contacts' table)
RECIPIENT_EMAIL = current_row.get('Recipient email')
# Choose SUBJECT between "hard-coded" (subject l.57 of this script)
# or "database" (get subject from 'Subject' column in the 'Send email config' table)
SUBJECT_SOURCE = current_row.get('Subject source')
# Choose EMAIL_FORMAT between "text" (hard-coded plain text, defined l.71),
# "html" (hard-coded HTML, defined l.77)
# and "database" (content of the 'Email body' column in the 'Send email config' table)
EMAIL_FORMAT = current_row.get('Email format')
# If Attach file, the script retrieves the first file from the 'File' column of the 'Sending email config'
ATTACH_FILE = current_row.get('Attach file')

# 2. Set recipient email addresses
if RECIPIENT_EMAIL == "hard-coded" :
  # Option a) Define the recipient email address in this script
  receivers = ['johndoe@email.com']
elif RECIPIENT_EMAIL == "database" :
  # Option b) Retrieve recipient email addresses from the 'Contacts' table in SeaTable
  receiver_rows = base.list_rows(CONTACTS_TABLE)
  receivers = [row['Email'] for row in receiver_rows if row.get('Email')]

# 3. Set email subject
if SUBJECT_SOURCE == "hard-coded" :
  # Option a) Define the subject in this script
  subject = 'SeaTable Send email'
elif SUBJECT_SOURCE == "database" :
  # Option b) Retrieve the subject from the 'Send email config' table
  current_row = context.current_row or base.list_rows(CONFIG_TABLE)[0]
  subject = current_row.get('Subject')

# 4. Construct the email message
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = SENDER + '<' + USERNAME + '>'
msg['To'] = ", ".join(receivers)

if EMAIL_FORMAT == "text" :
  # Option a) plain text message
  text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.seatable.com"
  text_plain = MIMEText(text,'plain', 'utf-8')
  msg.attach(text_plain)

elif EMAIL_FORMAT == "html" :
  # Option b) HTML content for the email body
  html = """
  <html>
    <head></head>
    <body>
      <p>Hi!<br>
         This is a sample message from SeaTable
      </p>
    </body>
  </html>
  """
  text_html = MIMEText(html, 'html', 'utf-8')
  msg.attach(text_html)

elif EMAIL_FORMAT == "database" :
  # Option c) HTML content for the email body from the Email body column
  current_row = context.current_row or base.list_rows(CONFIG_TABLE)[0]
  text_html = MIMEText(markdown.markdown(current_row['Email body']),'html', 'utf-8')
  msg.attach(text_html)

# 5. Attach a file from SeaTable to the email
if ATTACH_FILE :
  # Get the file from the 'send email config' table
  current_row = context.current_row or base.list_rows(CONFIG_TABLE)[0]
  file_name = current_row['File'][0]['name']
  file_url = current_row['File'][0]['url']
  path = file_url[file_url.find('/files/'):]
  download_link = base.get_file_download_link(parse.unquote(path))

  try:
      response = requests.get(download_link)
      if response.status_code != 200:
          print('Failed to download file, status code: ', response.status_code)
          exit(1)
  except Exception as e:
      print(e)
      exit(1)

  # Attach the file to the email (adapt _subtype to the type of your file)
  attached_file = MIMEApplication(response.content, _subtype = "pdf")
  attached_file.add_header('content-disposition', 'attachment', filename = file_name)
  msg.attach(attached_file)

# 6. Send the email

# option a) Sending the email using SMTP
try:
    with smtplib.SMTP() as email_server:
        email_server.connect(SMTP_SERVER)
        email_server.login(USERNAME, PASSWORD)
        email_server.send_message(msg)
        email_server.quit()
except smtplib.SMTPAuthenticationError:
    print("SMTP User authentication error, Email not sent!")
except Exception as e:
    print(f"SMTP exception {e}")

'''
# option b) Sending the email using SMTP / SSL
ssl_context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, 
                          context=ssl_context) as email_server:
        email_server.login(USERNAME, PASSWORD)
        email_server.send_message(msg)
        email_server.quit()
except smtplib.SMTPAuthenticationError:
    print("SMTP User authentication error, Email not sent!")
except Exception as e:
    print(f"SMTP exception {e}")

# option c) Sending the email using SMTP with STARTTLS
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as email_server:
        email_server.starttls()
        email_server.login(USERNAME, PASSWORD)
        email_server.send_message(msg)
        email_server.quit()
except smtplib.SMTPAuthenticationError:
    print("SMTP User authentication error, Email not sent!")
except Exception as e:
    print(f"SMTP exception {e}")
'''
```
