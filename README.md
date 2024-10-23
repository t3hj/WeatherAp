# Weather Application

A simple command-line weather application that fetches current weather data for multiple cities using the OpenWeatherMap API. Users can choose between metric (Celsius) and imperial (Fahrenheit) units for temperature.

## Features

- Fetch current weather data for multiple cities at once.
- Choose between Celsius and Fahrenheit for temperature units.
- Display temperature, humidity, wind speed, and weather description.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/t3hj/WeatherApp.git
   cd WeatherApp
   ```

2. **Install required libraries:**
   Ensure you have the `requests` library installed:
   ```bash
   pip install requests
   ```

3. **API Key:**
   - Sign up for an account at [OpenWeatherMap](https://openweathermap.org/) and obtain your API key.
   - Replace the placeholder API key in the script with your valid API key:
     ```python
     API_KEY = 'your_api_key_here'  # Ensure this is valid
     ```

### Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Follow the prompts:
   - Choose the temperature unit (`C` for Celsius, `F` for Fahrenheit).
   - Enter city names separated by commas (e.g., `London,Paris,Berlin`).

3. View the weather information displayed for each city.

## Example Output

```
![image](https://github.com/user-attachments/assets/2f46b7dd-6f9e-4c9b-b382-ca8396392cd2)

```

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API.
