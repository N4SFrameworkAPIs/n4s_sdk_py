import requests
from typing import Dict, Any
from .exceptions import Reese84Error, Reese84ConnectionError, Reese84APIError
from .models import Reese84Payload

class Reese84Client:
    def __init__(self, api_key: str, api_url: str):
        """Initialize the Reese84 client with api_key and api_url.

        Args:
            api_key (str): The API key for authentication.
            api_url (str): The full API URL provided by the client.
        """
        self.api_key = api_key
        self.api_url = api_url.rstrip('/')
        self.headers = {
            "X-API-KEY": f"{self.api_key}",
        }

    def send_payload(self, payload: Reese84Payload) -> Dict[str, Any]:
        """Send the JSON payload to the server.

        Args:
            payload (Reese84Payload): The validated payload object.

        Returns:
            Dict[str, Any]: The JSON response from the server.

        Raises:
            Reese84ConnectionError: For connection or network errors.
            Reese84APIError: For errors returned by the API (e.g., 4xx, 5xx).
            Reese84Error: For generic errors.
        """
        payload.validate()  # Validate before sending
        try:
            response = requests.post(
                self.api_url,  # Use the full api_url provided by the client
                headers=self.headers,
                json=payload.to_dict()  # Convert to dict for JSON serialization
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError as e:
            raise Reese84ConnectionError(f"Connection error: {str(e)}")
        except requests.exceptions.HTTPError as e:
            raise Reese84APIError(f"API error: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise Reese84Error(f"Error sending payload: {str(e)}")