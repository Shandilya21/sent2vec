import requests

url = "http://localhost:8000/generate_random_array/"
headers = {"Accept": "application/json"}
payload = {
    "sentence": "My Name is John",
    "dim": 100
}

response = requests.post(url, headers=headers, json=payload)
print(response.content.decode("utf-8"))  # This will print the response content
