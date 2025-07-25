import re
import requests
import json

# Mock weather data (for demonstration, based on X posts and web info)
MOCK_WEATHER_DATA = {
    "karachi": {"temp_c": 29, "condition": "partly cloudy", "humidity": 83, "wind_kmh": 16, "pressure_mb": 998},
    "london": {"temp_c": 15, "condition": "cloudy", "humidity": 70, "wind_kmh": 10, "pressure_mb": 1012},
    "new york": {"temp_c": 22, "condition": "sunny", "humidity": 65, "wind_kmh": 12, "pressure_mb": 1010}
}

# Weather function tool
def get_weather(city):
    """
    Fetches weather data for a given city using WeatherAPI.com or mock data.
    Args:
        city (str): Name of the city
    Returns:
        dict: Weather data or error message
    """
    # For real API usage (uncomment and add your API key):
    """
    api_key = "YOUR_WEATHERAPI_KEY"  # Replace with actual API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "temp_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "humidity": data["current"]["humidity"],
            "wind_kmh": data["current"]["wind_kph"],
            "pressure_mb": data["current"]["pressure_mb"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather data for {city}: {str(e)}"}
    """
    
    # Mock implementation
    city = city.lower().strip()
    if city in MOCK_WEATHER_DATA:
        return MOCK_WEATHER_DATA[city]
    else:
        return {"error": f"No weather data available for {city}"}

# Weather Agent class
class WeatherAgent:
    def __init__(self):
        self.tools = {
            "get_weather": get_weather
        }
    
    def process_query(self, query):
        # Check if the query is about weather (e.g., "What's the weather in Karachi?")
        weather_pattern = r"what\'?s\s+the\s+weather\s+(?:in\s+)?([\w\s]+)\??"
        match = re.match(weather_pattern, query.lower().strip())
        
        if match:
            city = match.group(1).strip()
            weather_data = self.tools["get_weather"](city)
            if "error" in weather_data:
                return weather_data["error"]
            return (f"Weather in {city.title()}: {weather_data['condition'].title()}, "
                    f"Temperature: {weather_data['temp_c']}°C, "
                    f"Humidity: {weather_data['humidity']}%, "
                    f"Wind: {weather_data['wind_kmh']} km/h, "
                    f"Pressure: {weather_data['pressure_mb']} mb")
        else:
            return "Sorry, I can only handle weather queries in the format 'What's the weather in [city]?'"

# Test the agent
def test_weather_agent():
    agent = WeatherAgent()
    test_queries = [
        "What's the weather in Karachi?",
        "What's the weather in London?",
        "What's the weather in New York?",
        "What's the weather in Tokyo?",
        "What is the time in Paris?"
    ]
    
    for query in test_queries:
        print(f"Query: {query}")
        print(f"Response: {agent.process_query(query)}")
        print("-" * 50)

if __name__ == "__main__":
    test_weather_agent()