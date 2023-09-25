import requests
import json
import jsonpath

# API_URL
url = "https://reqres.in/api/users/2"

# Read input json file
file = open('G:\\PycharmProjects\\PythonWithAllure\\API_Automation\\Get_Request\\CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make Put request with json input body
response = requests.put(url, request_json)
# print(response.content)

# Validating Response code
assert response.status_code == 200

# Parse response content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])


