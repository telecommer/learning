import requests
import json
url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/site"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZTlkYmI3NzdjZDQ3ZTAwNGM2N2RkMGUiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVkYzQ0NGQ1MTQ4NWM1MDA0YzBmYjIxMiJdLCJ0ZW5hbnRJZCI6IjVkYzQ0NGQzMTQ4NWM1MDA0YzBmYjIwYiIsImV4cCI6MTU5Mzg2NTU3NCwiaWF0IjoxNTkzODYxOTc0LCJqdGkiOiJmZTExZTY0Ny0zOGJiLTRjNzMtOWI0YS0wOTA4ZDE0Yzg2NTQiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.WVgl5A0tC4TwftTszGj3lechUJduh20TqAhCUCu83e1pz_T34ZeDJPvkTVB_gIO7qcNoZOX1DORhwCDjm_oPIqZmhL96VbJc0B_I0xLTNTniFn3SeCVzYNoQAXCDWCILcmwRmXjpKefSt5_g4XULHc7AxEs0wY-Hm097vJ3j9K0KP0e1KXeYVQ8RvKwQJ1-XfyxuGJDAeUA5s4jRsBh8YjgNRB1bdqMpoNbiULrjOTlljZX-WuAJU2OlpOehsnuIyeCpH2gC9NLqHCiQG5mKGDqtZLgXfE5GCSm16FkF0GsjCWr7UVPZ-fGvezm_K7Sl_o9IfCz0TigWhL2LqTtfxw'
}

response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8'))
json_object=json.loads(response.text.encode('utf8'))
print(json.dumps(json_object, sort_keys=True, indent=4))

site_names = json_object['response']
for sitename in site_names:
  print('Site Name:' + sitename['name'] + '\t site_id:' + sitename['id'])