import requests
from datetime import datetime
import pandas as pd
from config import API_KEY, CITY, UNITS

def fetch_current_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    return response.json()

def fetch_forecast():
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    return response.json()

def process_forecast(forecast_data):
    forecast_list = []
    for entry in forecast_data['list']:
        forecast_list.append({
            'datetime': datetime.fromtimestamp(entry['dt']),
            'temperature': entry['main']['temp'],
            'humidity': entry['main']['humidity'],
            'wind_speed': entry['wind']['speed'],
            'description': entry['weather'][0]['description']
        })
    return pd.DataFrame(forecast_list)