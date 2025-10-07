import requests
from typing import Dict, Any
from .models import SensorData
from .exceptions import ValidationError, APIError

class SensorDataClient:
    def __init__(self, api_key: str, api_url: str):
        """Initialize the SensorDataClient.

        Args:
            api_key: The API key for authentication
            api_url: The URL of the API (must be provided by the user)

        Raises:
            ValidationError: If the API key or api_url is not provided
        """
        if not api_key:
            raise ValidationError("API key is required")
        if not api_url:
            raise ValidationError("api_url is required")
        self.api_key = api_key
        self.api_url = api_url.rstrip('/')
        self.headers = {"X-API-KEY": self.api_key}

    def send_sensor_data(self, sensor_data: SensorData) -> Dict[str, Any]:
        """Send sensor data to the API.

        Args:
            sensor_data: SensorData object containing the required fields

        Returns:
            Dict containing the API response

        Raises:
            ValidationError: If the sensor_data is invalid
            APIError: If the API request fails
        """
        try:
            sensor_data.validate()
        except ValueError as e:
            raise ValidationError(str(e))

        try:
            response = requests.post(
                self.api_url,
                json=sensor_data.to_dict(),
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise APIError(f"API request failed: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise APIError(f"Network error: {str(e)}")