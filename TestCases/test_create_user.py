import json

import jsonpath
import requests

url = "https://reqres.in/api/users"

def test_create_new_user():

    # read data from json
    file =  open('CreateUser.json','r')
    data = file.read()

    obj = json.loads(data)
    # print(obj)

    # making post request with json
    response = requests.post(url,obj)
    # print(response.content)

    # validating response code
    assert response.status_code==201

    # fetch header from response
    print(response.headers.get('Content_length'))

    # parse response to json format
    response_json = json.loads(response.text)

    # pick id using json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])