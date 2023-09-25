import requests

param = {'name':'testingworld', 'email':'testingworld@gmail.com'}
response = requests.get('https://httpbin.org/get', params = param)
print(response.text)