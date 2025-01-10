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

# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Definitions
class Language(Enum):
    CATALAN = 'CA'
    SPANISH = 'ES'
    
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def read_txt(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def send_email(subject, body, recipient, attachments=[]):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
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

# Main
contacts = read_csv(file_path)
email_CA = read_txt('docs/email_CA.txt')
email_ES = read_txt('docs/email_ES.txt')

for contact in contacts:
    try:
        locale_body = globals()[f'email_{contact[language_col]}']
    except KeyError:
        locale_body = email_CA
    send_email(
        subject='Test email',
        body=format_email(locale_body, contact[name_col]),
        #recipient=contact[recipient_col]
        recipient=EMAIL_ADDRESS
    )
