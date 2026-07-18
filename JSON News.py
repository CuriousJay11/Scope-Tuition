import requests

url = "https://hn.algolia.com/api/v1/search?query=python"

response = requests.get(url)

data = response.json()

print("Python News")
print("------------")

for news in data["hits"][:5]:
    print(news["title"])