import requests
url = "https://wttr.in/Delhi?format=j1"
response = requests.get(url) # Sends get request to API

print(response.status_code)
data = response.json()
print(data)

#200 = Sucess
#404 = Not found
#500 = Server Error
#401 = Unauthorised

