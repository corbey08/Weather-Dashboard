import os
import requests
from dotenv import load_dotenv
from argparse import ArgumentParser

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
        }
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"

def main():
    parser = ArgumentParser(description="Get the current weather for a city")
    parser.add_argument("city", type=str, help="City name to fetch weather for")
    args = parser.parse_args()
    weather = get_weather(args.city)
    if isinstance(weather, dict):
        print(f"\nWeather in {weather['city']}:\n")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%\n")
    else:
        print(weather)

if __name__ == "__main__":
    main()
