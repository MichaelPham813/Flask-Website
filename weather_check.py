import urllib
import json
from dotenv import load_dotenv
import os
load_dotenv()

def get_weather(lat,lon):
    API_KEY = os.getenv('WEATHER_API_KEY')
    WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    
    request = urllib.request.urlopen(WEATHER_URL,timeout = 15)
    response = json.loads(request.read())
    
    return response