import json
import requests
import tkinter as tk
from tkinter import messagebox


def get_weather():
    api_key = '9bfe52920d89fabc6001e7fdeda7c9a8'
    city = str(city_entry.get())
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")

    if weather_data.status_code == 404:
        messagebox.showerror("Error", "City not found!")
    else:
        data = weather_data.json()
        weather = data['weather'][0]['main']
        temp = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        temp_min = round(data['main']['temp_min'])
        temp_max = round(data['main']['temp_max'])
        humidity = round(data['main']['humidity'])
        visibility = data['visibility']
        wind_speed = data['wind']['speed']

        result_text = f"Weather: {weather}\nTemperature: {temp}°C\nFeels like: {feels_like}°C\nMin Temperature: {temp_min}°C\nMax Temperature: {temp_max}°C\nHumidity: {humidity}%\nVisibility: {visibility} meters\nWind Speed: {wind_speed} m/s"
        result_label.config(text=result_text)


# GUI
root = tk.Tk()
root.title("Weather App")

root.geometry("300x250")

city_label = tk.Label(root, text="Enter city: ")
city_label.grid(row=0, column=0, padx=10, pady=5)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.grid(row=1, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()
