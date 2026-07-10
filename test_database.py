import os
import pytest
from database import create_table, add_log, get_all_logs, get_logs_by_city, clear_logs

TEST_DB = "test_weather.db"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Runs before each test
    create_table(TEST_DB)
    yield
    # Runs after each test
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def test_add_log():
    add_log("Toronto", 20.0, db_name=TEST_DB)
    logs = get_all_logs(db_name=TEST_DB)
    assert len(logs) == 1
    assert logs[0][1] == "Toronto"
    assert logs[0][2] == 20.0


def test_get_logs_by_city():
    add_log("Toronto", 20.0, db_name=TEST_DB)
    add_log("Vancouver", 18.0, db_name=TEST_DB)

    toronto_logs = get_logs_by_city("Toronto", db_name=TEST_DB)
    assert len(toronto_logs) == 1
    assert toronto_logs[0][1] == "Toronto"


def test_clear_logs():
    add_log("Toronto", 20.0, db_name=TEST_DB)
    clear_logs(db_name=TEST_DB)
    logs = get_all_logs(db_name=TEST_DB)
    assert len(logs) == 0