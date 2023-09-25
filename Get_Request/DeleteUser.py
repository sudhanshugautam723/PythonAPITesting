import requests

# API_URL
url = "https://reqres.in/api/users/2"

# # Sent Get request
response = requests.delete(url)

# Fetch Response Code
print(response.status_code)  # 204 incase of delete
assert response.status_code == 204