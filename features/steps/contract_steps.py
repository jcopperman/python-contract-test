# features\steps\contract_steps.py
from behave import given, when, then
import requests

@given('the API is available')
def step_given_api_available(context):
    url = "https://counter-api-5xwn.onrender.com/"  # Replace with the actual API URL

    try:
        response = requests.get(url)
        assert response.status_code == 200  # Check for a status code of 200
    except requests.exceptions.RequestException as e:
        raise AssertionError(f"API is not available: {e}")

@when('a request is made to the API')
def step_when_request_made(context):
    context.response = requests.get("https://counter-api-5xwn.onrender.com/hit/namespace1/key1")
    context.response_data = context.response.json()

@then('the response should adhere to the contract')
def step_then_response_adheres_to_contract(context):
    # Define the expected contract
    expected_data = {
        'value': int,
        'timestamp': str,  # Assuming it's a string in the specified format
    }

    # Check data types and format
    assert isinstance(context.response_data['value'], expected_data['value'])
    assert isinstance(context.response_data['timestamp'], expected_data['timestamp'])

    # Optionally, you can also check the format of the timestamp
    # You can use regular expressions for this, e.g., using the 're' module
    # Example:
    # assert re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z', context.response_data['timestamp'])