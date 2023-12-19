import requests
from twilio.rest import Client

#API for Twilio
account_sid = 'Get from Twilio Account'
auth_token = 'Get from Twilio Account'

#API for openweather
base_url_weather = 'https://api.openweathermap.org/data/2.5/weather'
base_url_forecast = 'https://api.openweathermap.org/data/2.5/forecast'
payload = {
    "lat" : '43.654260', 
    "lon": '-79.354160',
    "appid": 'Get from openweather',
    "cnt": 4
}


r = requests.get(url=base_url_forecast, params=payload)
r.raise_for_status()
weather_data = r.json()['list']

weather_codes = [int(code['weather'][0]['id']) < 800 for code in weather_data]
if True in weather_codes:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
         body='It is raining outside. Be sure to bring an umbrella',
         from_='+12053182852',
         to='+16476690292'
     )
    print(message.status)

