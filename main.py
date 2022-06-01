import os
import requests
import json

api_key = os.environ['API_KEY']
lat = os.environ['LAT']
lon = os.environ['LONG']

url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)