import requests

def get_weather_alerts():
    """
    Fetches and displays weather alerts from the National Weather Service API.

    Prompts the user to enter a state abbreviation and an optional county.
    Displays alerts for the specified state, optionally filtered by county.
    """
    # Prompt the user to enter a state and county
    print('\n')
    state = input('Enter a state abbreviation example Alabama = AL: ')
    county = input('Enter a county to get all alerts fort state press enter: ')

    # Fetch weather alerts for the specified state
    response = requests.get(f'https://api.weather.gov/alerts/active?area={state}').json()

    # Check if no county is entered
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
            
            print('******')
            print(f"Area: {area_upper}")
            print('\n')
            print(f"Headline: {headline_upper}")
            print('\n')
            print(f"Severity: {severity}")
            print(f"Event: {event}")
            print('\n')
            print("Description:")
            print(f"{description}")
            print('\n')
            print(f"Instruction: {instruction}")
            print('\n******\n')
    else:
        # Iterate through the features in the response and filter by county
        for alert in response.get('features', []):
            properties = alert.get('properties', {})
            area_desc = properties.get('areaDesc', 'N/A')
            
            # Check if the county is mentioned in the area description
            if county.title() in area_desc.title():
                headline = properties.get('headline', 'N/A')
                description = properties.get('description', 'N/A')
                instruction = properties.get('instruction', 'N/A')
                severity = properties.get('severity', 'N/A')
                event = properties.get('event', 'N/A')
                
                # Convert the area and headline to uppercase
                headline_upper = headline.upper()
                area_upper = area_desc.upper()

                # Print the refined and formatted data
                print('******')
                print(f"Area: {area_upper}")
                print('\n')
                print(f"Headline: {headline_upper}")
                print('\n')
                print(f"Severity: {severity}")
                print(f"Event: {event}")
                print('\n')
                print("Description:")
                print(f"{description}")
                print('\n')
                print(f"Instruction: {instruction}")
                print('\n******\n')

if __name__ == "__main__":
    get_weather_alerts()