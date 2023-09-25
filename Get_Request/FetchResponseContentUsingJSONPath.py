import requests
import json
import jsonpath
# API_URL
url = "https://reqres.in/api/users?page=2"

# Sent Get request
response = requests.get(url)

# Parse response to JSON Content
json_response = json.loads(response.text)
# print(json_response)

# Fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')  # jsonpath return a list
print(pages[0])

for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')  # jsonpath return a list
    print(first_name[0])