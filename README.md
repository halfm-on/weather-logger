# Weather Logger

A command-line tool that fetches live weather data from a free API and logs it to a local SQLite database, so you can track temperature history over time for a set of cities.

## Features

- Fetches real-time temperature data from the [Open-Meteo API](https://open-meteo.com/) (no API key required)
- Stores each reading in a local SQLite database with a timestamp
- Query logged data by city
- Clear logs when needed
- Handles network errors and bad API responses gracefully
- Fully unit tested, including mocked API tests (no network calls needed to run the test suite)

## Project Structure
weather-logger/
├── project.py          # Main entry point — fetches and logs weather for defined cities
├── weather_api.py       # Handles requests to the Open-Meteo API
├── database.py           # Handles all SQLite database operations
├── db_setup.py            # One-time script to create the database and table
├── test_database.py        # Unit tests for database.py
├── test_weather_api.py      # Unit tests for weather_api.py (uses mocking)
├── requirements.txt
└── README.md

## Setup

1. Clone the repository:
```bash
   git clone https://github.com/halfm-on/weather-logger.git
   cd weather-logger
```

2. Install dependencies:
```bash
   pip3 install -r requirements.txt
```

3. Create the database:
```bash
   python3 db_setup.py
```

## Usage

Run the main script to fetch and log weather for the cities defined in `project.py`:

```bash
python3 project.py
```

This will print each logged reading, followed by everything currently stored in the database.

### Adding more cities

Cities are defined in `project.py` as a dictionary of coordinates:

```python
CITIES = {
    "Toronto": (43.7, -79.42),
    "Vancouver": (49.28, -123.12),
    "Montreal": (45.5, -73.57),
}
```

Add any city by including its latitude and longitude.

### Querying and clearing logs

These functions are available in `database.py` and can be imported and used directly:

```python
from database import get_all_logs, get_logs_by_city, clear_logs

get_all_logs()               # returns every logged entry
get_logs_by_city("Toronto")  # returns entries for one city
clear_logs()                 # deletes all logged entries
```

## Running Tests

The project uses `pytest`, including mocked tests for the API so no live network calls are made during testing.

```bash
python3 -m pytest -v
```

## What I Learned

This project was built to practice combining SQLite databases with external API requests in Python, including:
- Structuring reusable database functions with parameterized SQL queries
- Handling network/API errors with try/except
- Writing unit tests with `pytest`, including mocking external API calls with `unittest.mock`

## License

This project is open source and available under the MIT License.