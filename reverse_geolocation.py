import urllib.request
import json
from dotenv import load_dotenv
import os
load_dotenv()

def get_country(lat,lon):
    API_KEY = os.getenv('BIG_DATA_CLOUD_API_KEY')
    URL = f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={API_KEY}'
    
    request = urllib.request.urlopen(URL,timeout = 15)
    response = json.loads(request.read())
    
    return response

