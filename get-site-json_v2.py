#!/usr/bin/env python
import json, requests
def dna_authentication_func():
    #DNA get authentication token
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    dna_token = json.loads(response.text.encode('utf8'))
    #print(json.dumps(dna_token, sort_keys=True, indent=1))
    token=dna_token['Token']
    #print(token)
    return token


#USE to GET request
def dna_session(token):
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/site"

    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'X-Auth-Token': token
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    json_object=json.loads(response.text.encode('utf8'))
    print(json.dumps(json_object, sort_keys=True, indent=4))
    #Site names on devnet DNA
    return json_object

def data_processing(json_data):
    site_names = json_data['response']
    for sitename in site_names:
      print('Site Name:' + sitename['name'] + '\t site_id:' + sitename['id'])

def main():
    token=dna_authentication_func()
    json_data=dna_session(token)
    data_processing(json_data)
if __name__ == '__main__':
    main()
