import tkinter as tk
from tkinter import messagebox
import requests
from dotenv import load_dotenv
import os

# Load the API key
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract weather data
        weather_desc = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        result_label.config(text=f"Weather in {city}:\n"
                                 f"Temperature: {temp}°C\n"
                                 f"Description: {weather_desc}\n"
                                 f"Humidity: {humidity}%")
    except requests.exceptions.HTTPError as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")

# Tkinter setup
root = tk.Tk()
root.title("Weather Dashboard")

# Create GUI elements
tk.Label(root, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)
tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
result_label = tk.Label(root, text="", font=("Aptos", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()