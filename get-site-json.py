import requests
import json
url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/site"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZTlkYmI3NzdjZDQ3ZTAwNGM2N2RkMGUiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVkYzQ0NGQ1MTQ4NWM1MDA0YzBmYjIxMiJdLCJ0ZW5hbnRJZCI6IjVkYzQ0NGQzMTQ4NWM1MDA0YzBmYjIwYiIsImV4cCI6MTU5Mzg2MDg2NSwiaWF0IjoxNTkzODU3MjY1LCJqdGkiOiI5YjI5ODQzNS00YTBiLTQ3M2MtODViOS0yYTJkOTYzN2JjNmEiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.NpbZ5DNm54_-wg-s1b8uCocvcj069yufUGom35tr6_g9McKoRzaCHKMfkFm2wFkAFcH0IReYoECgr856PeB_EfbC9QywzMBVisKYjl1TGaH5n7ncqnVouADrWv659VelC0pf0nQHNvJhT-u-z8fn_hc3sLaUE8LiJ9yEWW0OHiy6FvMe_hrqeH4FbsKwGXSz-4sBNCy_ebOgNgKpGLOSXCfpk2wy-vFiOklBwpicPpHS9tKjJFErC98fv0ELeGNcjXPtsEE2P5MbwOEyT_oMISir7rJIGZyZ4uZgDkkC4X5c61bfo5DjrKROLszJTACY2Wq9K5_7X6bsrfLuTdzqTQ'
}

response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8'))
json_object=json.loads(response.text.encode('utf8'))
print(json.dumps(json_object, sort_keys=True, indent=4))
