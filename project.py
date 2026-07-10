from weather_api import get_current_temperature
from database import add_log, get_all_logs, get_logs_by_city


CITIES = {
    "Toronto": (43.7, -79.42),
    "Vancouver": (49.28, -123.12),
    "Montreal": (45.5, -73.57),
}


def log_city_weather(city):
    if city not in CITIES:
        print(f"Unknown city: {city}")
        return

    latitude, longitude = CITIES[city]
    temperature = get_current_temperature(latitude, longitude)

    if temperature is None:
        print(f"Could not fetch weather for {city}")
        return

    add_log(city, temperature)


def main():
    log_city_weather("Toronto")
    log_city_weather("Vancouver")

    print("\nAll logs:")
    for row in get_all_logs():
        print(row)


if __name__ == "__main__":
    main()