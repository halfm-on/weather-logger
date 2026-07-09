import sqlite3

def main():
    connection = sqlite3.connect("weather.db")
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
    print("Database and table created successfully.")


if __name__ == "__main__":
    main()