import requests

headerdata = {'t1':'First_Header', 'T2':'Second_Header'}
response = requests.get('https://httpbin.org/get', headers= headerdata)
print(response.text)