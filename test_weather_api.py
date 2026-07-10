from unittest.mock import patch, Mock
import requests
from weather_api import get_current_temperature


@patch("weather_api.requests.get")
def test_get_current_temperature_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "current": {"temperature_2m": 22.5}
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    temp = get_current_temperature(43.7, -79.42)
    assert temp == 22.5


@patch("weather_api.requests.get")
def test_get_current_temperature_handles_error(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("Network error")

    temp = get_current_temperature(43.7, -79.42)
    assert temp is None