import csv

# VARIABLES
file_path = 'docs/contacts.csv'

# MAIN
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def send_email(title, body, recipient, attachments=[]):
    print(f'Sending email to {recipient} with title: {title} and body: {body}')

contacts = read_csv(file_path)

for contact in contacts:
    print(contact)
