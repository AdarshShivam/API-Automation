import json

import jsonpath
import requests

url = "https://reqres.in/api/users/2"

# read data from json
file =  open('CreateUser.json','r')
data = file.read()

obj = json.loads(data)
# print(obj)

# making post request with json
response = requests.put(url,obj)
# print(response.content)

# validating response code
assert response.status_code==200

# fetch header from response
# print(response.headers.get('Content_length'))
#
# parse response to json format
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])

# # pick id using json path
# id = jsonpath.jsonpath(response_json, 'id')
# print(id[0])