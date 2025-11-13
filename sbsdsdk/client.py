import requests
from typing import Any, Dict

from .exceptions import SbsdskAPIError, SbsdskConnectionError, SbsdskError
from .models import SbsdskPayload


class SbsdskClient:
    def __init__(self, api_key: str, api_url: str):
        """Initialize the Sbsdsk client.

        Args:
            api_key: API key used for authentication.
            api_url: Full endpoint URL (e.g. https://api.sbsd.com/v1/solve).
        """
        self.api_key = api_key
        self.api_url = api_url.rstrip("/")
        self.headers = {
            "X-API-KEY": self.api_key,
        }

    def send_payload(self, payload: SbsdskPayload) -> Dict[str, Any]:
        """Send the payload to the SbSd API to solve the challenge.

        Args:
            payload: Validated payload object.

        Returns:
            JSON response from the server (expected to contain a valid bm_s cookie).

        Raises:
            SbsdskConnectionError: Network/connection issues.
            SbsdskAPIError: HTTP errors returned by the API.
            SbsdskError: Any other request-related error.
        """
        payload.validate()
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload.to_dict(),
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError as e:
            raise SbsdskConnectionError(f"Connection error: {e}")
        except requests.exceptions.HTTPError as e:
            raise SbsdskAPIError(
                f"API error {e.response.status_code}: {e.response.text}"
            )
        except requests.exceptions.RequestException as e:
            raise SbsdskError(f"Request error: {e}")