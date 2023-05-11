import jsonpath
import requests
import json

# API URL
url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
# print("response", response)

# display response content
# print("response CONTENT", [response.content])

json_response = json.loads(response.text)
print(json_response)
# print(response.content)
# fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])