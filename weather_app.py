import requests
import json
import sys

def get_api_key():
    """Get the API key from user or use a demo approach"""
    print("Note: You need a free API key from OpenWeatherMap.org")
    print("Visit: https://openweathermap.org/api")
    
    api_key = input("Enter your API key (or press Enter for demo mode): ").strip()
    
    if not api_key:
        print("\nUsing demo mode - showing sample data for London")
        return "demo"
    
    return api_key

def validate_location(location):
    """Validate the location input"""
    location = location.strip()
    if not location:
        print("Please enter a location.")
        return False, None
    return True, location

def fetch_weather_data(api_key, location):
    """Fetch weather data from OpenWeatherMap API"""
    if api_key == "demo":
        # Return sample data for demo purposes
        return {
            "name": "London",
            "main": {"temp": 15.5, "humidity": 65},
            "weather": [{"description": "clear sky", "main": "Clear"}],
            "wind": {"speed": 3.6}
        }
    
    try:
        # Try to get weather by city name
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        else:
            # Try by ZIP code if city name fails
            url = f"http://api.openweathermap.org/data/2.5/weather?zip={location}&appid={api_key}&units=metric"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: Could not find location '{location}'")
                print("Please check the spelling or try a different location.")
                return None
                
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid response from weather service")
        return None

def display_weather_data(weather_data):
    """Display the weather information in a user-friendly format"""
    if not weather_data:
        return
    
    print("\n" + "="*50)
    print("WEATHER INFORMATION")
    print("="*50)
    
    city = weather_data.get('name', 'Unknown location')
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    weather_desc = weather_data['weather'][0]['description'].title()
    weather_main = weather_data['weather'][0]['main']
    wind_speed = weather_data['wind']['speed']
    
    print(f"Location: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather_desc} ({weather_main})")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print("="*50)

def get_weather_icon(weather_main):
    """Return a simple text icon based on weather condition"""
    icons = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Fog": "🌫️",
        "Haze": "🌫️"
    }
    return icons.get(weather_main, "🌡️")

def display_weather_with_icons(weather_data):
    """Display weather with emoji icons"""
    if not weather_data:
        return
    
    weather_main = weather_data['weather'][0]['main']
    icon = get_weather_icon(weather_main)
    
    print("\n" + "="*50)
    print(f"{icon}  WEATHER INFORMATION  {icon}")
    print("="*50)
    
    city = weather_data.get('name', 'Unknown location')
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    weather_desc = weather_data['weather'][0]['description'].title()
    wind_speed = weather_data['wind']['speed']
    
    print(f"📍 Location: {city}")
    print(f"🌡️  Temperature: {temp}°C")
    print(f"🌈 Condition: {weather_desc}")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} m/s")
    print("="*50)

# Main program execution
print("="*60)
print("🌤️  COMMAND-LINE WEATHER APP")
print("="*60)

# Get API key
api_key = get_api_key()

while True:
    print("\nEnter a location (city name or ZIP code):")
    print("Examples: 'London', 'New York', '10001', 'Tokyo'")
    print("Type 'quit' to exit")
    
    location_input = input("\nLocation: ").strip()
    
    if location_input.lower() in ['quit', 'exit', 'q']:
        print("Thank you for using the Weather App!")
        break
    
    # Validate input
    is_valid, location = validate_location(location_input)
    if not is_valid:
        continue
    
    # Fetch weather data
    print(f"\nFetching weather data for {location}...")
    weather_data = fetch_weather_data(api_key, location)
    
    # Display results
    if weather_data:
        display_weather_with_icons(weather_data)
    else:
        print("Failed to retrieve weather data. Please try again.")
    
    # Ask if user wants to check another location
    while True:
        another = input("\nCheck another location? (y/n): ").strip().lower()
        if another in ['y', 'yes']:
            print("\n" + "-"*40)
            break
        elif another in ['n', 'no']:
            print("Thank you for using the Weather App!")
            sys.exit(0)
        else:
            print("Please enter 'y' or 'n'.")