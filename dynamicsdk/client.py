import requests
import base64
from typing import Dict, Any, Optional
from .exceptions import ValidationError, APIError

class DynamicClient:
    def __init__(self, api_key: str, api_url: Optional[str] = None):
        """Initialize the DynamicClient.

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

    def send_dynamic_data(self, request_response_body: Optional[str] = None) -> Dict[str, Any]:
        """Send dynamic data to the API.

        Args:
            request_response_body: The response body provided by the customer (will be base64 encoded)

        Returns:
            Dict containing the API response

        Raises:
            ValidationError: If the request_response_body is not provided or invalid
            APIError: If the API request fails
        """
        if not request_response_body:
            raise ValidationError("request_response_body is required")

        # Crea il payload con 'script' codificato in base64
        data = {
            'script': base64.b64encode(request_response_body.encode('utf-8')).decode('utf-8')
        }

        try:
            response = requests.post(
                self.api_url,
                json=data,
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise APIError(f"API request failed: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise APIError(f"Network error: {str(e)}")