from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# Load environment variables from .env file
load_dotenv()

def get_current_weather(city="Kansas City"):
    """
    Fetch current weather data for a given city from OpenWeatherMap API
    
    Args:
        city (str): Name of the city to get weather for (default: "Kansas City")
    
    Returns:
        dict: Weather data as JSON, or None if error occurs
    """
    try:
        # Get API key from environment variables
        api_key = os.getenv("API_KEY")
        
        if not api_key:
            print("Error: API_KEY not found in environment variables!")
            print("Please make sure you have a .env file with: API_KEY=your_api_key_here")
            return None
        
        # Construct the API request URL
        request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial'
        
        # Make the API request
        response = requests.get(request_url)
        
        # Check if request was successful
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        elif response.status_code == 401:
            print("Error: Invalid API key. Please check your API key in the .env file.")
            return None
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found. Please check the spelling.")
            return None
        else:
            print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API. Please check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def display_weather_info(weather_data):
    """
    Display formatted weather information
    
    Args:
        weather_data (dict): Weather data from API
    """
    if not weather_data:
        return
    
    try:
        # Extract relevant information
        city_name = weather_data.get('name', 'Unknown')
        country = weather_data.get('sys', {}).get('country', 'Unknown')
        temperature = weather_data.get('main', {}).get('temp', 'N/A')
        feels_like = weather_data.get('main', {}).get('feels_like', 'N/A')
        humidity = weather_data.get('main', {}).get('humidity', 'N/A')
        description = weather_data.get('weather', [{}])[0].get('description', 'N/A').capitalize()
        wind_speed = weather_data.get('wind', {}).get('speed', 'N/A')
        
        # Print formatted weather information
        print("\n" + "="*50)
        print(f"📍 Weather in {city_name}, {country}")
        print("="*50)
        print(f"🌡️  Temperature: {temperature}°F")
        print(f"🤔 Feels like: {feels_like}°F")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️  Wind Speed: {wind_speed} mph")
        print(f"☁️  Conditions: {description}")
        print("="*50 + "\n")
        
    except Exception as e:
        print("Error displaying weather information.")
        print("Raw data:")
        pprint(weather_data)

def main():
    """
    Main function to run the weather app
    """
    print("\n" + "="*50)
    print("🌤️  WEATHER FORECAST APP 🌤️")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Get weather for a city")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == '1':
            city = input("\nPlease enter a city name: ").strip()
            
            if not city:
                print("No city entered. Using default: Kansas City")
                city = "Kansas City"
            
            print(f"\nFetching weather data for {city}...")
            
            # Get weather data
            weather_data = get_current_weather(city)
            
            # Display weather information
            if weather_data:
                display_weather_info(weather_data)
            else:
                print("\n❌ Failed to retrieve weather data. Please try again.")
                
        elif choice == '2':
            print("\n👋 Thank you for using the Weather App! Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")