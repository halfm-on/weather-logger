import sqlite3
from datetime import datetime


def add_log(city, temperature):
    connection = sqlite3.connect("weather.db")
    cursor = connection.cursor()

    timestamp = datetime.now().isoformat()

    cursor.execute(
        "INSERT INTO logs (city, temperature, timestamp) VALUES (?, ?, ?)",
        (city, temperature, timestamp)
    )

    connection.commit()
    connection.close()
    print(f"Logged: {city} - {temperature}°C at {timestamp}")


if __name__ == "__main__":
    add_log("Toronto", 22.5)