import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import json

disable_warnings(InsecureRequestWarning)

# Replace the placeholders with your own values
WEBEX_API_TOKEN = 'NDU4YjZhM2MtYTFmZi00ZmJiLWJmMjAtYmFhZjE4MjI2YzBjNjI2MGNmZDAtN2Fl_PF84_397496bc-dfb9-488f-917c-f6d03bebb97d'
WEBEX_ROOM_ID = 'Y2lzY29zcGFyazovL3VzL1JPT00vZmM4MDlmODAtMmZlYi0xMWViLTgyZjAtYzU0MmRiZWU4MWE5'
LIBRENMS_API_ENDPOINT = 'https://10.6.0.100'
LIBRENMS_API_TOKEN = 'ed4ad5326a43a5f92928b268fc454f4e'

# Query LibreNMS API for alerts
response = requests.get(f'{LIBRENMS_API_ENDPOINT}/api/v0/alerts', headers={'X-Auth-Token': LIBRENMS_API_TOKEN}, verify=False)
alerts = json.loads(response.text.encode('utf8'))
message = ""
severity = ""

# Iterate through the alerts and send them to Webex space
for alert in alerts['alerts']:
    # Extract the relevant information from the alert
    message = alert['hostname']
    severity = alert['severity']
    
    response = requests.get(f'{LIBRENMS_API_ENDPOINT}/api/v0/devices/{message}', headers={'X-Auth-Token': LIBRENMS_API_TOKEN}, verify=False)
    devices = json.loads(response.text.encode('utf8'))
    device = ""
    for device in devices['devices']:
        sysName = device['sysName']
        location = device['location']
        desc = device['sysDescr']

        # Construct the payload for the Webex API
        payload = {
        'roomId': WEBEX_ROOM_ID,
        'text': f'{severity}: {message} \n name : {sysName} \n location : {location} \n description : {desc}'
        }

    # Use the Webex API to send the alert message to the designated Webex space
    response = requests.post(
        'https://webexapis.com/v1/messages',
        headers={'Authorization': f'Bearer {WEBEX_API_TOKEN}'},
        json=payload
    )
