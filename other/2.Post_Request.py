import requests

data = {
    "title": "Учусь REST API",
    "body": "REST API — это круто!",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts", json=data
)

print(
    f'Created post: {response.json()}'
)
