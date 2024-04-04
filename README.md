## Weather App

This is a simple weather application built using Python's Tkinter library and the OpenWeatherMap API. It allows users to enter the name of a city and retrieves current weather information for that city.

### Requirements

- Python 3.x
- Tkinter library
- Requests library
- OpenWeatherMap API key

### Installation

1. Clone or download the repository to your local machine.
2. Install the required libraries if you haven't already:
   ```bash
   pip install requests
   ```
3. Sign up for an OpenWeatherMap API key [here](https://openweathermap.org/api) if you don't have one.
4. Replace `'YOUR_API_KEY'` with your actual API key in the `api_key` variable inside the `get_weather()` function in the code.

### Usage

1. Run the `weather_app.py` script.
   ```bash
   python weather_app.py
   ```
2. Enter the name of the city you want to get weather information for in the provided input field.
3. Click the "Get Weather" button.
4. The weather information for the entered city will be displayed below the button.
