from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather_detailes(city="Mysore city"):
    request_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=imperial"
    weather_data=requests.get(request_url).json()
    return weather_data
if __name__ == "__main__":
    print("\n The current weather detailes")
    city=input("Enter the city name to know the weather condition in that  city : ")\
    
    if not  bool(city.strip()):
        city="Mysore"
    weather_data=get_weather_detailes(city)


    print()
    pprint(weather_data)