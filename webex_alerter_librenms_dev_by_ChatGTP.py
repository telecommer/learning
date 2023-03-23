import requests

# Replace the placeholders with your own values
WEBEX_API_TOKEN = 'your_webex_api_token'
WEBEX_ROOM_ID = 'your_webex_room_id'
LIBRENMS_API_ENDPOINT = 'your_librenms_api_endpoint'

# Query LibreNMS API for alerts
try:
    response = requests.get(f'{LIBRENMS_API_ENDPOINT}/api/v0/alerts')
    response.raise_for_status()
    alerts = response.json()
except (requests.exceptions.RequestException, ValueError) as e:
    print(f'Error retrieving alerts: {e}')
    exit(1)

# Iterate through the alerts and send them to Webex space
for alert in alerts:
    # Extract the relevant information from the alert
    try:
        message = alert['message']
        severity = alert.get('severity', 'Unknown')
        hostname = alert.get('hostname', 'Unknown')
    except KeyError as e:
        print(f'Skipping alert due to missing key: {e}')
        continue

    # Construct the payload for the Webex API
    payload = {
        'roomId': WEBEX_ROOM_ID,
        'text': f'{severity}: {message} (Hostname: {hostname})'
    }

    # Use the Webex API to send the alert message to the designated Webex space
    try:
        response = requests.post(
            'https://webexapis.com/v1/messages',
            headers={'Authorization': f'Bearer {WEBEX_API_TOKEN}'},
            json=payload
        )
        response.raise_for_status()
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f'Error sending Webex message: {e}')
