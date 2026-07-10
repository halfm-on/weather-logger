import requests


def get_current_temperature(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

    data = response.json()
    return data["current"]["temperature_2m"]


if __name__ == "__main__":
    # Toronto's coordinates
    temp = get_current_temperature(43.7, -79.42)
    print(f"Current temperature: {temp}°C")