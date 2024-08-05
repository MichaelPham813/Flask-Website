import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
def get_country_data(name):
    API_KEY = os.getenv('COUNTRY_API_KEY')
    PAYLOADS = {'Accept':'application/json','Authorization': f'Bearer {API_KEY}'}
    URL = f'https://restfulcountries.com/api/v1/countries/{name}'
    request = requests.get(URL,headers=PAYLOADS)
    response = json.loads(request.text)
    return response
