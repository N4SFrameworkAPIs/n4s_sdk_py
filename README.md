# N4S.io Py SDK

A collection of Python SDKs for interacting with N4S.io Antibot APIs.

## Installation

To install the `n4s-sdk` package, use pip to download it directly from the GitHub repository. Note that this is a private repository, so you need to be authorized to access it. Contact the author for access credentials.

### Install the Latest Version
```bash
pip install git+https://github.com/chiefratz/n4s_sdk_py.git
```

## Usage Examples
Quick and easy steps to get started with our APIs Framework.

### Using `dynamicsdk`

This SDK returns you the DynamicValues of your current Akamai Session, needed for the SensorData generation.<br>
For more details refer directly to [N4S.io DynamicValues API Documentation](https://n4s.gitbook.io/n4s.io/akamai-web-api-guide/dynamic-values-api-documentation).

```bash
from dynamicsdk import DynamicClient
import requests
import os

#Settings
api_key = 'xxx-xxx-xxx-xxx-xxxx-xxxx'       #replace it with your N4S.io API-KEY

api_url = 'https://APIurl.random/path'      #replace it with N4S.io Dynamic Values API Endpoint

akamai_script = '...'                       #fill it with the Akamai Script of your session

#Set the client
client = DynamicClient(api_key=api_key, api_url=api_url)

#Require the API
try:
    response = client.send_dynamic_data(akamai_script)
    print("Response from API:", response)
except Exception as e:
    print(f"Error: {e}")
```

### Using `sensordatasdk`
This SDK returns you a valid SensorData needed for the antibot solving.<br>
For more details refer directly to [N4S.io SensorData API Documentation](https://n4s.gitbook.io/n4s.io/akamai-web-api-guide/sensordata-v3.0-api-documentation).
```bash
from sensordatasdk import SensorDataClient, SensorData
import requests
import os

#Settings
api_key = 'xxx-xxx-xxx-xxx-xxxx-xxxx'       #replace it with your N4S.io API-KEY

api_url = 'https://APIurl.random/path'      #replace it with N4S.io SensorData Web API Endpoint

#Set the client
client = SensorDataClient(api_key=api_key, api_url=api_url)

#Set your session payload
sensor_data = SensorData(
    targetURL="https://www.example.com/some-path",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    abck="...",
    bm_sz="...",    
    dynamic={...},   #replace it with the previously obtained Dynamic values
    req_number=0
)

#Require the API
try:
    response = client.send_sensor_data(sensor_data)
    print("Response from API:", response)
except Exception as e:
    print(f"Error: {e}")

```
