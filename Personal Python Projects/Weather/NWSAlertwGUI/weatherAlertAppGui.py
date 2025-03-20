import requests
import tkinter as tk
from tkinter import scrolledtext

def fetch_weather_alerts():
    """
    Fetches and displays weather alerts from the National Weather Service API.

    Retrieves alerts based on the provided state and optional county.
    Displays the alerts in a scrolled text widget.
    """
    state = state_entry.get()
    county = county_entry.get()

    response = requests.get(f'https://api.weather.gov/alerts/active?area={state}').json()
    alerts_text.delete(1.0, tk.END)

    if not county:
        for alert in response.get('features', []):
            properties = alert.get('properties', {})
            area_desc = properties.get('areaDesc', 'N/A')
            headline = properties.get('headline', 'N/A')
            description = properties.get('description', 'N/A')
            instruction = properties.get('instruction', 'N/A')
            severity = properties.get('severity', 'N/A')
            event = properties.get('event', 'N/A')

            area_upper = area_desc.upper()
            headline_upper = headline.upper()

            alerts_text.insert(tk.END, '******\n')
            alerts_text.insert(tk.END, f"Area: {area_upper}\n\n")
            alerts_text.insert(tk.END, f"Headline: {headline_upper}\n\n")
            alerts_text.insert(tk.END, f"Severity: {severity}\n")
            alerts_text.insert(tk.END, f"Event: {event}\n\n")
            alerts_text.insert(tk.END, "Description:\n")
            alerts_text.insert(tk.END, f"{description}\n\n")
            alerts_text.insert(tk.END, f"Instruction: {instruction}\n")
            alerts_text.insert(tk.END, '******\n\n')
    else:
        for alert in response.get('features', []):
            properties = alert.get('properties', {})
            area_desc = properties.get('areaDesc', 'N/A')

            if county.title() in area_desc.title():
                headline = properties.get('headline', 'N/A')
                description = properties.get('description', 'N/A')
                instruction = properties.get('instruction', 'N/A')
                severity = properties.get('severity', 'N/A')
                event = properties.get('event', 'N/A')

                headline_upper = headline.upper()
                area_upper = area_desc.upper()

                alerts_text.insert(tk.END, '******\n')
                alerts_text.insert(tk.END, f"Area: {area_upper}\n\n")
                alerts_text.insert(tk.END, f"Headline: {headline_upper}\n\n")
                alerts_text.insert(tk.END, f"Severity: {severity}\n")
                alerts_text.insert(tk.END, f"Event: {event}\n\n")
                alerts_text.insert(tk.END, "Description:\n")
                alerts_text.insert(tk.END, f"{description}\n\n")
                alerts_text.insert(tk.END, f"Instruction: {instruction}\n")
                alerts_text.insert(tk.END, '******\n\n')

def reset_fields():
    """
    Resets the state and county entry fields and adds a reset message to the alert display.
    """
    state_entry.delete(0, tk.END)
    county_entry.delete(0, tk.END)
    county = county_entry.get()
    alerts_text.insert(tk.END, f"End of Alerts for {county}\n")
    alerts_text.insert(tk.END, "\n" * 5)

# Create the main window
window = tk.Tk()
window.title("Weather Alerts")

# Create and place the state entry
tk.Label(window, text="Enter a state abbreviation (e.g., AL for Alabama):").grid(row=0, column=0, padx=10, pady=5)
state_entry = tk.Entry(window)
state_entry.grid(row=0, column=1, padx=10, pady=5)

# Create and place the county entry
tk.Label(window, text="Enter a county (or leave blank for all alerts):").grid(row=1, column=0, padx=10, pady=5)
county_entry = tk.Entry(window)
county_entry.grid(row=1, column=1, padx=10, pady=5)

# Create and place the fetch button
fetch_button = tk.Button(window, text="Get My Alerts", command=fetch_weather_alerts)
fetch_button.grid(row=2, column=0, pady=10)

# Create and place the reset button
reset_button = tk.Button(window, text="Reset To Run Again", command=reset_fields)
reset_button.grid(row=2, column=1, pady=10)

# Create and place the scrolled text widget to display alerts
alerts_text = scrolledtext.ScrolledText(window, width=80, height=20)
alerts_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
window.mainloop()