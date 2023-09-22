# client.py
import requests

def get_data():
    response = requests.get("http://example.com/api/data"")
    return response.json()

# Get the JSON response and print it to the console
response_data = get_data()
print(response_data)
