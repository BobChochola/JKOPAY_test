import requests
import pytest

API_URL = "https://api.example/service/login"

def test_login_successful():    
    payload = {
        "Account": "valid_account",
        "LoginAuth": "valid_login_auth",
        "Datetime": "2023-06-12T:11:22:33"
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Login successful"

def test_account_number():
    payload = {
        "Account": str(12345),
        "LoginAuth": "example_login_auth"
    }
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Login successful"

def test_login_less_datatime_successful():
    payload = {
        "Account": "valid_account",
        "LoginAuth": "valid_login_auth"
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Login successful"

def test_datetime_invalid_successful():
    payload = {
        "Account": "example_account"
        "LoginAuth": "example_login_auth",
        "Datetime": "abc123"
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Login successful"

@pytest.fixture
def test_endpoint_not_found():
    invalid_endpoint = "https://api.example/service/invalid_endpoint"
    payload = {
        "Account": "example_account",
        "LoginAuth": "example_login_auth"
    }
    response = requests.post(invalid_endpoint, json=payload)
    
    assert response.status_code == 404
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Error"