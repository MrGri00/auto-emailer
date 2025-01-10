# Auto Emailer

**Auto Emailer** is a Python-based script designed to automate sending personalized emails with optional attachments. This tool reads contact information from a CSV file, dynamically customizes email templates, and sends emails using an SMTP server (e.g., Gmail).

⚠️ **Use this tool responsibly.** This script is intended for legitimate purposes such as reaching out to clients, sending newsletters, or other lawful communication. Do not use it to send unsolicited emails or spam recipients.

---

## Features
- Read contact details from a CSV file.
- Dynamically customize email templates based on recipient information.
- Add multiple attachments.
- Supports multilingual email templates.
- Handles invalid email addresses gracefully.

---

## Setup

### 1. Set Up Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Required Libraries
```bash
pip install python-dotenv
```

### 3. Configure Email Authentication
- Create an [App Password](https://myaccount.google.com/apppasswords) for your email account.
- This is more secure than using your account password.

### 4. Customize Environment Variables
Configure the .env file in the project directory with your credentials:
```ini
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### 5. Prepare Your Files
1. Contact List:
- Create a CSV file with contact information (e.g., name, email, preferred language).
- Save this file in the `docs/` folder.
2. Attachments:
- Add any files you want to send as email attachments to the `attachments/` folder.
- The `.gitkeep` file will be ignored.
3. Email Templates:
- Create text files for each language you plan to support (e.g., email_CA.txt, email_ES.txt).
- Save these files in the `docs/` folder.

### 6. Run the Script
```bash
python auto-emailer.py
```

---

## Folder Structure
```bash
auto-emailer/
├── attachments/      # Folder for all email attachments
├── docs/             # Folder for email templates and contact CSV
├── auto-emailer.py   # Main script
├── .env              # Environment variables
├── README.md         # Documentation
```

---

## Responsibilities and Guidelines
- **Use responsibly:** Ensure you have the consent of your recipients before sending emails.
- **Respect privacy:** Avoid sharing or misusing recipient information.
- **Avoid spamming:** This script is not intended for sending unsolicited emails.

Misuse of this tool may violate laws such as the CAN-SPAM Act, GDPR, or other regulations in your jurisdiction.

---

## License
This project is licensed under the [MIT License]().