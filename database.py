import sqlite3
from datetime import datetime

DB_NAME = "weather.db"


def add_log(city, temperature, db_name=DB_NAME):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    timestamp = datetime.now().isoformat()

    cursor.execute(
        "INSERT INTO logs (city, temperature, timestamp) VALUES (?, ?, ?)",
        (city, temperature, timestamp)
    )

    connection.commit()
    connection.close()
    print(f"Logged: {city} - {temperature}°C at {timestamp}")


def get_all_logs(db_name=DB_NAME):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM logs")
    rows = cursor.fetchall()

    connection.close()
    return rows


def get_logs_by_city(city, db_name=DB_NAME):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM logs WHERE city = ?", (city,))
    rows = cursor.fetchall()

    connection.close()
    return rows


def clear_logs(db_name=DB_NAME):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM logs")

    connection.commit()
    connection.close()
    print("All logs cleared.")

def create_table(db_name=DB_NAME):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()