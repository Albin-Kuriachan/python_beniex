
"""write a python program to handle exceptions when sending emails using Python's smtplib library."""

import smtplib
from email.mime.text import MIMEText
import mailtrap_credentials as credentials # Create a file named as mailtrap_credentials and add all credentials related to Mailtrap

def send_email():
    try:


        sender_email = input("Enter sender's email address: ")
        recipient_email = input("Enter recipient's email address: ")
        subject = input("Enter email subject: ")
        body = input("Enter email body: ")

        message = MIMEText(body)
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        server = smtplib.SMTP(credentials.smtp_server, credentials.smtp_port)
        server.starttls()
        text = message.as_string()
        server.login(credentials.smtp_username, credentials.smtp_password)
        server.sendmail(sender_email, recipient_email, text)
        print('Email sent successfully!')

    except Exception as e:
            print(f'Failed to send email. Error: {e}')
    finally:
        server.quit()


send_email()
