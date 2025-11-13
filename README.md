# N4S.io Py SDK

A collection of Python SDKs for interacting with N4S.io Antibot APIs.

## Prerequisites

- A valid API key for our service, obtainable through our [Discord Official Server](https://framework.n4s.xyz/).

## Installation

To install the `n4s-sdk` package, use pip to download it directly from the GitHub repository.

### Install the Latest Version
```bash
pip install git+https://github.com/N4SFrameworkAPIs/n4s_sdk_py.git
```

## Usage Examples
Quick and easy steps to get started with our APIs Framework.

### Using `dynamicsdk`

This SDK returns you the DynamicValues of your current Akamai Session, needed for the SensorData generation.<br>
For more details refer directly to [N4S.io DynamicValues API Documentation](https://n4s.gitbook.io/n4s.io/akamai-web-api-guide/dynamic-values-api-documentation).

```bash
from dynamicsdk import DynamicClient

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

#Settings
api_key = 'xxx-xxx-xxx-xxx-xxxx-xxxx'       #replace it with your N4S.io API-KEY

api_url = 'https://APIurl.random/path'      #replace it with N4S.io SensorData Web API Endpoint

#Set the client
client = SensorDataClient(api_key=api_key, api_url=api_url)

#Set your session payload
sensor_data = SensorData(
    targetURL="https://www.example.com/some-path",
    script_url="your_site_script_url",
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
### Using `sbsdsdk`
This SDK returns you a valid payload needed for the bm_s cookie generation.<br>
For more details refer directly to [N4S.io SbSd Challenge API Documentation](https://n4s.gitbook.io/n4s.io/akamai-web-api-guide/sbsd-challenge-api-documentation).
```bash
from sbsdsdk import SbsdskClient, SbsdskPayload

#Settings
api_key = 'xxx-xxx-xxx-xxx-xxxx-xxxx'       #replace it with your N4S.io API-KEY

api_url = 'https://APIurl.random/path'      #replace it with N4S.io SbSd API Endpoint

#Set the client
client = SbsdskClient(api_key=api_key, api_url=api_url)

#Set your session payload
payload = SbsdskPayload(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    targetURL='https://www.somesite.com/path/path1',
    v_url="...",     #fill it with the SbSd challenge url
    bm_so="...",     #fill it with your bm_so session cookie
    language="en-GB,en;q=0.9",
    script="..."     #fill it with the SbSd script
)

#Require the API
try:
    response = client.send_payload(payload)
    print("Response from API:", response)
except Exception as e:
    print(f"Error: {e}")

```

### Using `reese84sdk`
This SDK returns you a valid payload needed for the Reese84 cookie generation.<br>
For more details refer directly to [N4S.io Reese84 API Documentation](https://n4s.gitbook.io/n4s.io/incapsula-api-guide/reese84-api-documentation-1).
```bash
from reese84sdk import Reese84Client, Reese84Payload

#Settings
api_key = 'xxx-xxx-xxx-xxx-xxxx-xxxx'       #replace it with your N4S.io API-KEY

api_url = 'https://APIurl.random/path'      #replace it with N4S.io Reese84 API Endpoint

#Set the client
client = Reese84Client(api_key=api_key, api_url=api_url)

#Set your session payload
payload = Reese84Payload(
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    url="https://www.somesite/onalbaine-legeance-what-come-Womany-Malcome-to-o/4790704588958611838",
    data="..."    #fill it with the response.text that you get from the GET request to https://www.somesite/onalbaine-legeance-what-come-Womany-Malcome-to-o/4790704588958611838
)

#Require the API
try:
    response = client.send_payload(payload)
    print("Response from API:", response)
except Exception as e:
    print(f"Error: {e}")

```