# client.py
import requests

def get_data():
    response = requests.get("https://counter-api-5xwn.onrender.com/hit/namespace1/key1")
    return response.json()

# Get the JSON response and print it to the console
response_data = get_data()
print(response_data)
