import json
import logging
logger = logging.getLogger(__name__)

def get_mail_id():
    with open("mail_id.json") as fp:
        mail_ids = json.load(fp)
    return mail_ids