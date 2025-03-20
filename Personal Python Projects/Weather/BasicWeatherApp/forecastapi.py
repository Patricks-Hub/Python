import requests
import tkinter as tk
from tkinter import Label, Radiobutton, StringVar
from PIL import Image, ImageTk
import io

IP_GEOLOCATION_API_KEY = "df8704606bc6afa58034ea12c235c818"
WEATHER_API_KEY = "b16147791f2355b1fd91571889f8d393"

def get_location():
    """
    Retrieves the latitude and longitude of the user's location based on their IP address.

    Uses the ipstack API to fetch geolocation data.

    Returns:
        tuple: A tuple containing the latitude and longitude (float, float).
    """
    ip_geolocation_url = f"http://api.ipstack.com/check?access_key={IP_GEOLOCATION_API_KEY}"
    geo_response = requests.get(ip_geolocation_url)
    geo_data = geo_response.json()
    return geo_data['latitude'], geo_data['longitude']

def get_weather(latitude, longitude, units):
    """
    Retrieves current weather data for a given latitude and longitude.

    Uses the Weatherstack API to fetch weather information.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
        units (str): 'm' for metric units or 'f' for imperial units.

    Returns:
        dict: A dictionary containing the weather data in JSON format.
    """
    weather_url = f"https://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={latitude},{longitude}&units={units}"
    weather_response = requests.get(weather_url)
    return weather_response.json()

def load_weather_icon(icon_url):
    """
    Loads a weather icon from a given URL and converts it to a Tkinter PhotoImage.

    Args:
        icon_url (str): The URL of the weather icon.

    Returns:
        ImageTk.PhotoImage: A Tkinter PhotoImage of the weather icon.
    """
    icon_response = requests.get(icon_url)
    image_data = Image.open(io.BytesIO(icon_response.content))
    weather_icon = image_data.resize((100, 100), Image.BICUBIC)
    return ImageTk.PhotoImage(weather_icon)

def convert_precipitation(precip_mm, units):
    """
    Converts precipitation from millimeters to inches if using imperial units.

    Args:
        precip_mm (float): Precipitation in millimeters.
        units (str): 'm' for metric units or 'f' for imperial units.

    Returns:
        float: Precipitation in the specified units.
    """
    if units == 'f':
        return precip_mm / 25.4  # Convert mm to inches
    return precip_mm

def format_temperature(temp, units):
    """
    Formats temperature with the appropriate unit symbol.

    Args:
        temp (float): Temperature value.
        units (str): 'm' for metric units or 'f' for imperial units.

    Returns:
        str: Formatted temperature string.
    """
    return f"{temp}°{'F' if units == 'f' else 'C'}"

def format_wind_speed(wind_speed, units):
    """
    Formats wind speed with the appropriate unit.

    Args:
        wind_speed (float): Wind speed value.
        units (str): 'm' for metric units or 'f' for imperial units.

    Returns:
        str: Formatted wind speed string.
    """
    return f"{wind_speed} {'mph' if units == 'f' else 'km/h'}"

def update_display(weather_data, units):
    """
    Updates the Tkinter GUI with the provided weather data.

    Args:
        weather_data (dict): A dictionary containing weather data.
        units (str): 'm' for metric units or 'f' for imperial units.
    """
    icon_url = weather_data['current']['weather_icons'][0]
    weather_icon_tk = load_weather_icon(icon_url)
    icon_label.config(image=weather_icon_tk)
    icon_label.image = weather_icon_tk

    temperature = weather_data['current']['temperature']
    feelslike = weather_data['current']['feelslike']
    weather_descriptions = weather_data['current']['weather_descriptions'][0]
    wind_speed = weather_data['current']['wind_speed']
    wind_dir = weather_data['current']['wind_dir']
    pressure = weather_data['current']['pressure']
    humidity = weather_data['current']['humidity']
    precip_mm = weather_data['current']['precip']

    precip = convert_precipitation(precip_mm, units)

    labels['temperature'].config(text=f"Temperature: {format_temperature(temperature, units)}")
    labels['feelslike'].config(text=f"Feels Like: {format_temperature(feelslike, units)}")
    labels['description'].config(text=f"Weather: {weather_descriptions}")
    labels['wind_speed'].config(text=f"Wind Speed: {format_wind_speed(wind_speed, units)}")
    labels['wind_dir'].config(text=f"Wind Direction: {wind_dir}")
    labels['pressure'].config(text=f"Pressure: {pressure} mb")
    labels['humidity'].config(text=f"Humidity: {humidity}%")
    labels['precip'].config(text=f"Precipitation: {precip:.2f} {'in' if units == 'f' else 'mm'}")

def update_weather():
    """
    Updates the weather display with current weather data based on user's location and selected units.
    """
    units = unit_var.get()
    latitude, longitude = get_location()
    weather_data = get_weather(latitude, longitude, units)
    update_display(weather_data, units)

# Tkinter setup
root = tk.Tk()
root.title("Weather App")

unit_var = StringVar(value='f')
metric_radio = Radiobutton(root, text="Metric (°C, km/h)", variable=unit_var, value='m', command=update_weather)
imperial_radio = Radiobutton(root, text="Imperial (°F, mph)", variable=unit_var, value='f', command=update_weather)
metric_radio.pack()
imperial_radio.pack()

icon_label = Label(root)
icon_label.pack()

label_names = ['temperature', 'feelslike', 'description', 'wind_speed', 'wind_dir', 'pressure', 'humidity', 'precip']
labels = {name: Label(root, text=f"{name.capitalize()}: ") for name in label_names}
for label in labels.values():
    label.pack()

update_weather()
root.mainloop()