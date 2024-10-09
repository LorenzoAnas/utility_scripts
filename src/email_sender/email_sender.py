import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

class EmailSender:
    def __init__(self, config_path='src/email_sender/email_config.env'):
        # Load environment variables from the config file
        load_dotenv(config_path)
        self.from_email = os.getenv('FROM_EMAIL_USER')
        self.password = os.getenv('EMAIL_PASSWORD')
        self.server = None

    def connect(self):
        """Connect to the email server."""
        if not self.from_email or not self.password:
            raise ValueError("Email credentials are not set.")

        self.server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
        self.server.login(self.from_email, self.password)

    def disconnect(self):
        """Disconnect from the email server."""
        if self.server:
            self.server.quit()

    def send_email(self, subject, body, to_emails):
        """Send an email to multiple recipients."""
        if not self.server:
            self.connect()

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.from_email

        for to_email in to_emails:
            msg['To'] = to_email
            print(f"Sending email to {to_email}")
            self.server.sendmail(self.from_email, to_email, msg.as_string())

    def __enter__(self):
        """Enable usage of the class in a context manager."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure disconnection from the server when exiting."""
        self.disconnect()

# Example usage
if __name__ == "__main__":
    subject = input("Enter subject: ")
    body = input("Enter body: ")
    to_emails = input("Enter recipient emails (comma-separated): ").split(',')

    # Using the EmailSender class
    with EmailSender() as email_sender:
        email_sender.send_email(subject, body, to_emails)
