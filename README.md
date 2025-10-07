## Usage Example (dynamicsdk)

```python
from dynamicsdk import DynamicClient
import requests

url = 'https://www.example.com/data'
headers = {"user-agent": "Mozilla/5.0 ..."}
r = requests.get(url, headers=headers)

# Inizializza il client con l'URL della tua API
client = DynamicClient(api_key="your-api-key", api_url="https://your-api-url/v3_values")

# Valore passato dal cliente (es. il response body)
request_response_body = r.text

# Invia i dati
try:
    response = client.send_dynamic_data(request_response_body)
    print(response)
except Exception as e:
    print(f"Error: {e}")