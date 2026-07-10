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

def get_all_logs():
    connection = sqlite3.connect("weather.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM logs")
    rows = cursor.fetchall()

    connection.close()
    return rows


def get_logs_by_city(city):
    connection = sqlite3.connect("weather.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM logs WHERE city = ?", (city,))
    rows = cursor.fetchall()

    connection.close()
    return rows


if __name__ == "__main__":
    add_log("Toronto", 22.5)
    add_log("New York", 20.0)

    print("\nAll logs:")
    for row in get_all_logs():
        print(row)

    print("\nToronto logs:")
    for row in get_logs_by_city("Toronto"):
        print(row)