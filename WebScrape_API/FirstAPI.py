# lets you send HTTP requests in Python (needed for calling the API)
import requests
# use to organize and display the API results in df later
import pandas as pd

# 5 sample cities in Virginia with lat/lon
cities_va = {
    "Williamsburg": (37.2707, -76.7075),
    "Richmond": (37.5407, -77.4360),
    "Virginia Beach": (36.8529, -75.9780),
    "Roanoke": (37.27097, -79.94143),
    "Charlottesville": (38.0293, -78.4767)
}

url = "https://api.open-meteo.com/v1/forecast"

results = []

for city, (lat, lon) in cities_va.items():
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True # tells open-meteo API to return the latest weather data
    }
    response = requests.get(url, params=params) # makes an HTTP GET request to the url with these parameters
    data = response.json() # converts JSON text into python dictionary called data
    # this will let you access fields like data["current_weather"] directly
    
    if "current_weather" in data: # checks if "current_weather" exists
        weather = data["current_weather"] # saves current_weather dict to weather
        results.append({
            "City": city,
            "Temperature (°C)": weather["temperature"],
            "Wind Speed (m/s)": weather["windspeed"],
            "Time": weather["time"]
        })
    else: # if "current_weather" does not exist, store None so the final table is consistent -- error check
        results.append({"City": city, "Temperature (°C)": None, 
                        "Wind Speed (m/s)": None, "Time": None})

# Display as table
df = pd.DataFrame(results)
print(df)
