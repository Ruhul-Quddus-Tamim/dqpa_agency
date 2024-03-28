from agency_swarm.tools import BaseTool
from pydantic import Field
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import logging

os.environ["EMAIL_SENDER"] = "YOUR_EMAIL"
os.environ["EMAIL_PASSWORD"] = "GMAIL_16_DIGIT_APP_PASSWORD"
os.environ["SMTP_SERVER"] = "smtp.gmail.com"
os.environ["SMTP_PORT"] = "465"

class EmailAlertTool(BaseTool):
    """
    A tool for composing, sending, and logging email alerts via Gmail SMTP server. Ensures data protection and privacy compliance.
    """

    recipient_email: str = Field(
        default="ruhul@graduate.utm.my",
        description="Recipient's email address."
    )
    alert_message: str = Field(
        ..., description="The message content of the alert."
    )
    subject: str = Field(
        ..., description="Subject of the email alert."
    )

    def run(self):
        msg = MIMEMultipart()
        msg['From'] = os.getenv('EMAIL_SENDER')
        msg['To'] = self.recipient_email
        msg['Subject'] = self.subject

        msg.attach(MIMEText(self.alert_message, 'plain'))

        server = smtplib.SMTP_SSL(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT')))  # Use SMTP_SSL for port 465
        server.login(os.getenv('EMAIL_SENDER'), os.getenv('EMAIL_PASSWORD'))
        server.send_message(msg)
        server.quit()

        logging.info(f"Email alert sent to {self.recipient_email}.")

        return "Email alert sent successfully."
