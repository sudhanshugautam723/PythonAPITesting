import requests
import json
import jsonpath

# API_URL
url = "https://reqres.in/api/users"

# Read input json file
file = open('G:\\PycharmProjects\\PythonWithAllure\\API_Automation\\Get_Request\\CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make Post request with json input body
response = requests.post(url, request_json)
print(response.content)

# Validating Response code
assert response.status_code == 201

# Fetch Header from response
print(response.headers.get("job"))

# Parse response to json format
response_json = json.loads(response.text)

# Pick id using json path
id = jsonpath.jsonpath(response_json, "id")
print(id[0])
