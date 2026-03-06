import requests

url = "https://www.osintcat.net/api/ip"

headers = {"X-API-KEY": "b1b3544b45801eec39a05db2870569ed624af47osintcat9458d48c8c906fa"}

response = requests.get(url, headers=headers)

print(response.text)