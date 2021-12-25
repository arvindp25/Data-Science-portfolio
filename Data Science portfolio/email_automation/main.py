from multiprocessing import Pool
import json
import logging
from tools import get_mail_id
from email_automation import EmailAutomation

if __name__ == "__main__":
    logging.basicConfig()
    mail_ids = get_mail_id()["mail_id"]

    MY_ADDRESS = ""         # Replace with yours
    MY_PASSWORD = ""      # Replace with yours

    HOST_ADDRESS = 'smtp-mail.outlook.com'   # Replace with yours
    HOST_PORT = 587                          # Replace with yours

    mail = EmailAutomation(HOST_ADDRESS, HOST_PORT)
    mail.login(MY_ADDRESS,MY_PASSWORD )
    for mail_id in mail_ids:
        mail.send_mail(mail_id)

    mail.close_connection()
