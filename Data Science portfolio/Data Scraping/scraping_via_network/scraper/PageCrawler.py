import requests
import json
import os

import pandas as pd
from time import sleep
import logging

from data import company_size_dict, user_types
from scraper import query_finder

class PageCrawler:
    def __init__(self, base_path, download_pdf = False ,sleep_time = 1):
        assert os.path.isdir(base_path), f"Path Not Exist, {base_path}"
        self.download_pdf = download_pdf
        self.base_path = base_path
        self.sleep_time = sleep_time
        self.country_df = pd.read_csv(".\data\wikipedia-iso-country-codes.csv")
        self.original_data = []
        self.company_size_dict = company_size_dict
        self.user_types =  user_types
        logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)
    def eu_scraper(self,url):
        self.p_id, self.initiative_id = query_finder(url)
        pg_no = 0
        scrapping = True
        logging.info("Scrapping Started..")

        while scrapping:
            url = f"https://ec.europa.eu/info/law/better-regulation/brpapi/allFeedback?publicationId={self.p_id}&page={pg_no}&size=10"

            payload={}
            headers = {}


            response = requests.request("GET", url, headers=headers, data=payload)

            json_data = json.loads(response.text)
            last_pg_no = json_data["page"]["totalPages"] -1 
            self.original_data.extend(json_data["_embedded"]["feedbackV1"])

            if pg_no == last_pg_no:
                scrapping =False
            else:
                pg_no+=1

        logging.info(f"Scrapping Done, Total data found {len(self.original_data)}")
        

        
    def initiative_finder(self,initiative_id):
        url = f'https://ec.europa.eu/info/law/better-regulation/brpapi/shortTitleById?initiativeId={initiative_id}&language=EN'

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        return str(response.text)

    

    def pdf_download(self, attachments, fid):
        sleep(self.sleep_time)
        for attachment in attachments:
            response = requests.get(f"https://ec.europa.eu/info/law/better-regulation/api/download/{attachment.get('documentId')}")
            if not os.path.isdir( os.path.join(self.base_path, fid)):
                os.mkdir(os.path.join(self.base_path, fid))
                
            with open(os.path.join(self.base_path, fid,attachment.get('ersFileName')), "wb") as fp:
                fp.write(response.content)

            
    def save_data(self, filename:str = None):
        initiative = self.initiative_finder(self.initiative_id)
        if filename == None:
            filename = f"{initiative}.csv"

        cleaned_data = []
        for i in self.original_data:
            new_dic = {}
            if 'id' in i.keys() or i.get('id') not  in [None, ""]:
                new_dic["Feedback reference"] = f"F{i.get('id')}"
                
            if "dateFeedback" in i.keys() and i.get("dateFeedback") not in [None, ""]:
                new_dic["Submitted on"] = i.get("dateFeedback")
                
            if "firstName" in i.keys() and "surname":    
                new_dic["Submitted by"] = f"{i.get('firstName')} {i.get('surname')}"
                
            if i.get("userType") is not None and i.get("userType")  not in [None, ""]:
                new_dic["User type"] = self.user_types[i.get("userType")]
                
            if "organization" in i.keys() and i.get("organization") not in [None, ""]:            
                new_dic["Organisation"] = i.get("organization")
                
            if "companySize" in i.keys() and i.get("companySize") not in [None, ""]:
                new_dic["Organisation size"] = f"{i.get('companySize')} {self.company_size_dict[i.get('companySize')]}"
                
            if "scope" in i.keys() and i.get("scope") not in [None, ""]:
                new_dic["Scope"]= i.get("scope")
                
            if "tr_number" in i.keys() and i.get("tr_number") not in [None, ""]:            
                new_dic["Transparency register number"] = i.get("tr_number")
                
            if "country" in i.keys() and i.get("country") not in [None, ""]:
                new_dic["Country of origin"] = self.country_df[self.country_df["Alpha-3 code"] == i.get("country")]["English short name lower case"].to_list()[0]
                    
            new_dic["Initiative"] = initiative
            if "feedback" in i.keys() and i.get("feedback") not in [None, ""]:
                new_dic["Comment"] = i.get("feedback")

            if self.download_pdf:
                if len(i.get('attachments')) > 0:
                    logging.info(f"downloading pdf for {new_dic['Feedback reference']}")
                    self.pdf_download(attachments = i.get('attachments'), fid = new_dic["Feedback reference"])
                else:
                    logging.info(f"No pdf found for {new_dic['Feedback reference']}")
            cleaned_data.append(new_dic)

        df = pd.DataFrame(cleaned_data)

        df.to_csv(os.path.join(self.base_path,filename), index= False, encoding="utf-8")
        logging.info(f"File save at {os.path.join(self.base_path,filename)}")
        
        


