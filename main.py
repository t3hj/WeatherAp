import requests

API_KEY = 'aa3351d11a51f7862f15a76fd5f4a190'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

# Ask the user for the preferred unit
unit_choice = input("Choose temperature unit (C for Celsius, F for Fahrenheit): ").strip().upper()

# Validate the unit choice
if unit_choice not in ['C', 'F']:
    print("Invalid choice! Please select 'C' for Celsius or 'F' for Fahrenheit.")
else:
    cities = input("Enter city names separated by commas (e.g., London,New York,Paris): ").strip()

    if not cities:
        print("Please enter at least one valid city name.")
    else:
        # Set the units based on user choice
        units = 'metric' if unit_choice == 'C' else 'imperial'
        city_list = [city.strip() for city in cities.split(',')]  # Split the input into a list and strip whitespace

        for city in city_list:
            request_url = f"{BASE_URL}q={city}&appid={API_KEY}&units={units}"
            response = requests.get(request_url)

            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temperature = main['temp']
                humidity = main['humidity']
                wind_speed = data['wind']['speed']
                weather_description = data['weather'][0]['description']

                # Adjust the temperature unit in the output
                temp_unit = '°C' if unit_choice == 'C' else '°F'
                print(f"\nWeather in {city.capitalize()}:")
                print(f"Temperature: {temperature}{temp_unit}")
                print(f"Humidity: {humidity}%")
                print(f"Wind Speed: {wind_speed} m/s")
                print(f"Weather: {weather_description.capitalize()}")
            else:
                print(f"\nCity '{city}' not found. Error: {response.status_code} - {response.text}")
