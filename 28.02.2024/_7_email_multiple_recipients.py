"""write a python program to send an email with multiple recipients using the smtplib library."""


import smtplib
from email.mime.text import MIMEText
import mailtrap_credentials as credentials # Create a file named as mailtrap_credentials and add all credentials related to Mailtrap


def send_email():
    try:
        sender_email = input("Enter sender's email address: ")
        recipient_emails = input("Enter recipient's email addresses separated by commas: ").split(',')
        subject = input("Enter email subject: ")
        body = input("Enter email body: ")

        message = MIMEText(body)
        message['From'] = sender_email
        message['To'] = ', '.join(recipient_emails)
        message['Subject'] = subject

        server = smtplib.SMTP(credentials.smtp_server, credentials.smtp_port)
        server.starttls()
        text = message.as_string()
        server.login(credentials.smtp_username, credentials.smtp_password)
        server.sendmail(sender_email, recipient_emails, text)
        print('Email sent successfully!')

    except Exception as e:
        print(f'Failed to send email. Error: {e}')
    finally:
        server.quit()


send_email()
