# Weather App README

This is a simple weather application built using Python and the Tkinter GUI library. It retrieves weather data based on the user's IP address and displays it in a user-friendly window. It also shows weather alerts for the user's county.

## Features

* **Automatic Location Detection:** Uses the IP address to determine the user's latitude and longitude.
* **Current Weather Display:** Shows temperature, "feels like" temperature, weather description, wind speed, wind direction, pressure, humidity, and precipitation.
* **Weather Alerts:** Fetches and displays weather alerts for the user's county and state.
* **Unit Selection:** Allows the user to switch between metric (°C, km/h) and imperial (°F, mph) units.
* **Dynamic Background:** changes the background of the application based on if it is day or night.
* **Weather Icon Display:** Displays the current weather condition icon.

## Prerequisites

Before running the application, ensure you have the following installed:

* **Python 3.x:** Download and install Python from [python.org](https://www.python.org/).
* **Required Python Libraries:** Install the following libraries using pip:

    ```bash
    pip install requests tkinter pillow geopy
    ```

* **API Keys:** You will need API keys from the following services:
    * **ipstack:** Get a free API key from [ipstack.com](https://ipstack.com/).
    * **Weatherstack:** Get a free API key from [weatherstack.com](https://weatherstack.com/).
    * **Note:** The weather alerts are retrieved from the National Weather Service, which does not require an API key, but only works for locations within the United States.

## Setup

1.  **Clone or download the repository:** Obtain the application files.
2.  **Replace API Keys:** Open the Python script (`your_script_name.py`) and replace the placeholder API keys with your actual keys:

    ```python
    IP_GEOLOCATION_API_KEY = "YOUR_IPSTACK_API_KEY"
    WEATHER_API_KEY = "YOUR_WEATHERSTACK_API_KEY"
    ```
3.  **Image Paths:** Make sure the image paths in the `update_display` function are correct. Change:

    ```python
    background_image = ImageTk.PhotoImage(Image.open("C:\College Work\CIS189 - Python I\Personal projects\Weather\images\daytime.jpg"))
    ```

    and

    ```python
    background_image = ImageTk.PhotoImage(Image.open("C:\College Work\CIS189 - Python I\Personal projects\Weather\images\nighttime.jpg"))
    ```

    to the correct paths for your `daytime.jpg` and `nighttime.jpg` images.

## Running the Application

1.  **Open a terminal or command prompt.**
2.  **Navigate to the directory containing the Python script.**
3.  **Run the script:**

    ```bash
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the actual name of your Python file.

## Usage

* The application will automatically fetch and display the weather data and alerts.
* Use the radio buttons to switch between metric and imperial units.
* The background will change automatically based on the time of day.

## Notes

* The weather alerts are specific to the United States.
* Make sure you have a stable internet connection for the application to function correctly.
* You must have the images `daytime.jpg` and `nighttime.jpg` in the correct directory, or change the file path in the python file.
* Error handling is included, but further improvements can be made.