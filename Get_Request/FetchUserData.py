# reqres.in for free rest api
import requests

# API_URL
url = "https://reqres.in/api/users?page=2"

# # Sent Get request
response = requests.get(url)
print(response)

# Display Response Content
print(response.content)

# validate statuscode
print(response.status_code)
assert response.status_code == 200


# Fetch responce header
print(response.headers)
print(response.headers.get("Date"))
print(response.headers.get("Server"))

# Fetch cookies
print(response.cookies)
# Fetch encoding
print(response.encoding)
print(response.elapsed)