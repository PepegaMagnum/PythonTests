import requests
import json
import jsonpath

url = "http://sk-cat-stg.safekiddo.net/public-cat/api/v1/categorize-url"
auth_input = ('test', '123')

response = requests.get(url, auth=auth_input,
                        params={"url": "https://amazon.com"},
                        headers={"AuthHash": "9c43cab5c30322557c4725192141bb22bb6af8b19746a518ebd5d1378a90ce77",
                                 "Idempotency-Key": "XXXX-XXXX-XXXX-1235"},
                        verify=False,
                        allow_redirects=False)

print(response.content)
print(response.status_code)

response_json = json.loads(response.text)
website = jsonpath.jsonpath(response_json, "categorizedWebsite")

print(website[0]['categories'])
