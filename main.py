import requests

def get_weather(api_key, date_time, latitude, longitude, variable):
    base_url = "https://api.meteomatics.com"
    endpoint = f"/{date_time}/{variable}/{latitude},{longitude}/html"
    url = base_url + endpoint

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        weather_data = response.text
        return weather_data
    else:
        print("Failed to retrieve weather information.")
        return None

# Usage example
api_key = "https://api.meteomatics.com/2023-07-15T00:00:00Z/t_2m:C/52.520551,13.461804/html"
date_time = "2023-07-15T00:00:00Z"
latitude = "52.520551"
longitude = "13.461804"  
variable = "t_2m:C"

weather_info = get_weather(api_key, date_time, latitude, longitude, variable)

if weather_info is not None:
    print(weather_info)
