import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from quote_gen import get_random_quote
from html_template import html_template
class EmailAutomation:
    def __init__(self, host_address, host_port):
        self.server = smtplib.SMTP(host=host_address, port=host_port)
        self.server.starttls()
        self.logger = logging.getLogger(__name__)

    def login(self, email_address, password):
        self.email_address = email_address
        self.server.login(email_address, password)
        self.logger.info("successfully login.")
        
    def send_mail(self, recipient, subject = "Quote Of Day"):
        message = MIMEMultipart()
        message = MIMEMultipart("alternative")

        message['From'] = self.email_address
        message['To'] = recipient
        message['Subject'] = subject
        htmlPart = MIMEText(html_template(get_random_quote()["content"]), 'html')
        message.attach(htmlPart)
        
        self.server.send_message(message)
        self.logger.info("mail sent.")
        
    def close_connection(self):
        self.server.quit()
        self.logger.info("connection closed")


