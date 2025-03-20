import requests
import tkinter as tk
from tkinter import Label, Radiobutton, StringVar, font
from PIL import Image, ImageTk
import io
from geopy.geocoders import Nominatim

IP_GEOLOCATION_API_KEY = "df8704606bc6afa58034ea12c235c818"
WEATHER_API_KEY = "b16147791f2355b1fd91571889f8d393"

def get_location():
    try:
        response = requests.get(f"http://api.ipstack.com/check?access_key={IP_GEOLOCATION_API_KEY}")
        geo_data = response.json()
        lat = geo_data['latitude']
        lon = geo_data['longitude']
        return lat, lon
    except Exception as e:
        print("Error getting location:", e)
        return None, None

def get_weather(lat, lon, units):
    try:
        response = requests.get(f"https://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={lat},{lon}&units={units}")
        weather_data = response.json()
        return weather_data['current']
    except Exception as e:
        print("Error getting weather:", e)
        return None

def get_county(lat, lon):
    try:
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.reverse(f"{lat}, {lon}")
        if location and location.raw.get('address'):
            address = location.raw['address']
            county = address.get('county', address.get('city_district', ''))
            state = address.get('state', '')
            return county, state
        else:
            return None, None
    except Exception as e:
        print("Error getting county:", e)
        return None, None

def get_alerts(state, county):
    try:
        if not state:
            return ["State information not available."]

        response = requests.get(f'https://api.weather.gov/alerts/active?area={state}')
        alerts_data = response.json()

        if not county:
            if 'features' in alerts_data and alerts_data['features']:
                alerts = [f['properties']['headline'] for f in alerts_data['features']]
            else:
                alerts = ["No alerts"]
            return alerts

        alerts = []
        if 'features' in alerts_data and alerts_data['features']:
            for alert in alerts_data['features']:
                properties = alert['properties']
                area_desc = properties['areaDesc']
                headline = properties['headline']
                if county.upper() in area_desc.upper():
                    alerts.append(headline)

        return alerts if alerts else ["No alerts for the specified county."]

    except Exception as e:
        print("Error getting alerts:", e)
        return ["Error retrieving alerts"]

def update_display(weather, alerts, units):
    if weather is None:
        temp_label.config(text="Weather data unavailable")
        return

    try:
        image_url = weather['weather_icons'][0]
        image_response = requests.get(image_url)
        image_data = image_response.content
        image = Image.open(io.BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)
        icon_label.config(image=photo)
        icon_label.image = photo
    except Exception as e:
        print("Error loading image:", e)

    precip = weather['precip'] / 25.4 if units == 'f' else weather['precip']
    unit_symbol = 'F' if units == 'f' else 'C'
    wind_unit = 'mph' if units == 'f' else 'km/h'
    precip_unit = 'in' if units == 'f' else 'mm'

    temp_label.config(text=f"Temperature: {weather['temperature']}°{unit_symbol}")
    labels['feelslike'].config(text=f"Feels Like: {weather['feelslike']}°{unit_symbol}")
    labels['description'].config(text=f"Weather: {weather['weather_descriptions'][0]}")
    labels['wind_speed'].config(text=f"Wind Speed: {weather['wind_speed']} {wind_unit}")
    labels['wind_dir'].config(text=f"Wind Direction: {weather['wind_dir']}")
    labels['pressure'].config(text=f"Pressure: {weather['pressure']} mb")
    labels['humidity'].config(text=f"Humidity: {weather['humidity']}%")
    labels['precip'].config(text=f"Precipitation: {precip:.2f} {precip_unit}")
    alerts_text = "\n".join(alerts)
    alerts_label.config(text=f"Alerts:\n{alerts_text}")

    # Set background based on is_day boolean
    if weather['is_day'] == 'yes':
        background_image = ImageTk.PhotoImage(Image.open("C:\College Work\CIS189 - Python I\Personal projects\Weather\ForecastWithNWSAPI\images\daytime.jpg"))
    else:
        background_image = ImageTk.PhotoImage(Image.open("C:\College Work\CIS189 - Python I\Personal projects\Weather\ForecastWithNWSAPI\images\nighttime.jpg"))

    background_label.config(image=background_image)
    background_label.image = background_image

def update_weather():
    lat, lon = get_location()
    if lat is not None and lon is not None:
        weather = get_weather(lat, lon, unit_var.get())
        county, state = get_county(lat, lon)
        alerts = get_alerts(state, county)
        if weather is not None:
            update_display(weather, alerts, unit_var.get())

root = tk.Tk()
root.title("Weather App")
root.geometry("425x325")

unit_var = StringVar(value='f')
metric_radio = Radiobutton(root, text="Metric (°C, km/h)", variable=unit_var, value='m', command=update_weather)
imperial_radio = Radiobutton(root, text="Imperial (°F, mph)", variable=unit_var, value='f', command=update_weather)

icon_label = Label(root)

label_font = font.Font(family="Helvetica", size=12, weight="bold")
temp_font = font.Font(family="Helvetica", size=24, weight="bold")

label_names = ['feelslike', 'description', 'wind_speed', 'wind_dir', 'pressure', 'humidity', 'precip']
labels = {}
for i, name in enumerate(label_names):
    labels[name] = Label(root, text=f"{name.capitalize()}: ", font=label_font, bg=root.cget('bg'))

alerts_label = Label(root, text="Alerts:", font=label_font, bg=root.cget('bg'))
temp_label = Label(root, text="Temperature: ", font=temp_font, bg=root.cget('bg'))

background_image = ImageTk.PhotoImage(Image.open("C:\College Work\CIS189 - Python I\Personal projects\Weather\ForecastWithNWSAPI\images\daytime.jpg"))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()

temp_label.grid(row=1, column=0)
icon_label.grid(row=1, column=1)

for i, name in enumerate(label_names):
    labels[name].grid(row=i +20, column=0)

alerts_label.grid(row=len(label_names)+20, column=0)

metric_radio.grid(row=99, column=1)
imperial_radio.grid(row=99, column=0)


update_weather()
root.mainloop()