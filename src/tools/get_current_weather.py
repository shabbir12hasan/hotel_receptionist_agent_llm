import requests
from langchain_core.tools import tool

OPENWEATHERMAP_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your actual OpenWeatherMap API key

@tool
def get_current_weather(city: str) -> str:
    """
    Fetches the current weather for a specified city from the OpenWeatherMap API.
    Use this tool for queries that ask about the weather in a specific location.

    Args:
        city: The name of the city (e.g., 'London', 'New York').

    Returns:
        A string containing the weather description and temperature, or an error message.
    """
    if not OPENWEATHERMAP_API_KEY:
        return "OpenWeatherMap API key not found."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric"
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()

        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']

        return f"The current weather in {city} is {description} with a temperature of {temperature}°C."
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching weather data: {e}"
