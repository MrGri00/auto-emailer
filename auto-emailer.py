from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os
import csv

# Custom variables (change these)
file_path = 'docs/contacts.csv'

# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Functions
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def send_email(subject, body, recipient, attachments=[]):
    print(f'Sending email to {recipient} with subject: {subject} and body: {body}')
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

# Main
contacts = read_csv(file_path)

for contact in contacts:
    print(contact)
