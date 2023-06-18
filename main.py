import requests #pip3 install requests
import os
from datetime import datetime

user_api = os.getenv('WEATHERAPP_KEY', default=None)

def get_weather(city):
    #use the get method of the requests module to get the data from openweathermap
    complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={user_api}"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        print(f"Invalid City: {city}, Please check your City name")
    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_description = api_data['weather'][0]['description']
        humidity = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print("------------------------------------------------------------")
        print(f"Weather Stats for {city} || {date_time}")
        print("------------------------------------------------------------")

        print(f"Current temperature is: {temp_city:.2f} deg C")
        print(f"Current weather desc: {weather_description}")
        print(f"Current Humidity: {humidity}%")
        print(f"Current wind speed: {wind_speed}kmph")

#Main Program Loop
while True:
    city = input("Enter the city name (or 'quit' to exit): ")
    if city.lower() == "quit":
        break

    get_weather(city)