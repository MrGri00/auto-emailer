from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enum import Enum
import smtplib
from dotenv import load_dotenv
import os
import csv

# Custom variables (change these)
file_path = 'docs/contacts.csv'
name_col = 0
recipient_col = 1
language_col = 3
email_subject = 'Test email'

# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Definitions
class Language(Enum):
    CATALAN = 'CA'
    SPANISH = 'ES'

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        return list(csv.reader(file))

def read_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def send_email(subject, body, recipient, attachments=[]):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    for attachment in attachments:
        try:
            with open(attachment, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment)}')
                msg.attach(part)
        except Exception as e:
            print(f'Failed to attach file {attachment}: {e}')
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f'Email sent to {recipient}')
    except Exception as e:
        print(f'Failed to send email to {recipient}: {e}')

def format_email(body, name):
    return body.replace('[NAME]', name)

def get_attachments(directory):
    return [os.path.join(directory, filename) for filename in os.listdir(directory) if not filename.startswith('.')]

# Main
contacts = read_csv(file_path)
email_templates = {
    'CA': read_txt('docs/email_CA.txt'),
    'ES': read_txt('docs/email_ES.txt')
}
all_attachments = get_attachments('attachments')

for contact in contacts:
    if '@' not in contact[recipient_col]:
        print(f'Invalid email address for {contact[name_col]}: {contact[recipient_col]}')
        continue
    locale_body = email_templates.get(contact[language_col], email_templates['CA'])
    send_email(
        subject=email_subject,
        body=format_email(locale_body, contact[name_col]),
        recipient=contact[recipient_col],
        attachments=all_attachments
    )
