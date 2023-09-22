# test_contract.py
import pytest
from client import get_data

def test_contract():
    # Define the expected contract
    expected_data = {
        'value': int,
        'timestamp': str,  # Assuming it's a string in the specified format

        }
    
    # Make a request to the server and get the actual data
    actual_data = get_data()
    
    # Check data types and format
    assert isinstance(actual_data['value'], expected_data['value'])
    assert isinstance(actual_data['timestamp'], expected_data['timestamp'])
