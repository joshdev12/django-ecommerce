import requests


headers = {
    'Authorization': 'Token fc0c4ec7423b3a309c0f7fd01255be87ac3d9cac',
    'Content-type': 'application/json'
}

response = requests.get('http://127.0.0.1:8000/', headers=headers)

print(response)
print(response.reason)
print(response.json())