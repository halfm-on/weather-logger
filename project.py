import argparse
from weather_api import get_current_temperature
from database import add_log, get_all_logs, get_logs_by_city, clear_logs


def log_weather(city, latitude, longitude):
    temperature = get_current_temperature(latitude, longitude)

    if temperature is None:
        print(f"Could not fetch weather for {city}")
        return

    add_log(city, temperature)


def view_logs(city=None):
    logs = get_logs_by_city(city) if city else get_all_logs()

    if not logs:
        print("No logs found.")
        return

    for log_id, log_city, temperature, timestamp in logs:
        print(f"[{log_id}] {log_city}: {temperature}°C at {timestamp}")


def main():
    parser = argparse.ArgumentParser(description="Log and view weather data.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    log_parser = subparsers.add_parser("log", help="Fetch and log weather for a city")
    log_parser.add_argument("city", help="City name, e.g. Toronto")
    log_parser.add_argument("latitude", type=float, help="Latitude, e.g. 43.7")
    log_parser.add_argument("longitude", type=float, help="Longitude, e.g. -79.42")

    view_parser = subparsers.add_parser("view", help="View logged weather data")
    view_parser.add_argument("--city", help="Filter by city name", default=None)

    subparsers.add_parser("clear", help="Clear all logged data")

    args = parser.parse_args()

    if args.command == "log":
        log_weather(args.city, args.latitude, args.longitude)
    elif args.command == "view":
        view_logs(args.city)
    elif args.command == "clear":
        clear_logs()


if __name__ == "__main__":
    main()