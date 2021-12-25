import logging
import requests
import json

logger = logging.getLogger(__name__)

def _get_header():
    with open("creds.json") as fp:
        headers = json.load(fp)
        logger.info("successfully loaded creds")
    return headers

def get_random_quote():
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = _get_header()

    response = requests.request("GET", url, headers=headers)
    logger.info(f"response status: {response.status_code}")
    output = response.json()
    
    return output 


if __name__ == "__main__":
   print(get_random_quote())