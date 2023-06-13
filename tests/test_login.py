import requests
import pytest

API_URL = "https://api.example/service/login"

def test_login_empty_account():
    payload = {
    "Account": "", # "miss account"
    "LoginAuth": "valid_login_auth"
    }

    response = requests.post(API_URL, json=payload)

    assert response.status_code == 400

    result = response.json()
    assert result["Status"] == "response.status_code
    assert result["Message"] == "Invalid Account Number"

def test_login_missing_fields():
    payload = {
        "Account": "valid_account",
        "LoginAuth": "" # "miss auth"
    }

    response = requests.post(API_URL, json=payload)

    assert response.status_code == 400
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Invalid LoginAuth"

def test_login_null_account():
    payload = {
    "Account": None,
    "LoginAuth": "valid_login_auth"
    }

    response = requests.post(API_URL, json=payload)

    assert response.status_code == 400

    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Invalid Account Number"

def test_login_null_loginauth():
    payload = {
    "Account": "valid_account",
    "LoginAuth": None
    }

    response = requests.post(API_URL, json=payload)

    assert response.status_code == 400

    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Invalid LoginAuth"

def test_login_invalid_credentials():
    payload = {
        "Account": "invalid_account", # bob@gmail.com not exist, bob@123, 123@123
        "LoginAuth": "invalid_login_auth",
        "Datetime": "2023-06-12"
    }

    response = requests.post(API_URL, json=payload)

    assert response.status_code == 401

    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Invalid Account Number"

def test_login_subscription_failed():
    payload = {
        "Account": "example_account",
        "LoginAuth": "example_invalid_auth"
    }
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 402
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "payment required"


def test_login_invalid_request():
    payload = {
        "Account": "valid_account",
        "LoginAuth": "valid_auth"
    }

    response = requests.get(API_URL, json=payload)

    assert response.status_code == 405 
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Method Not Allowed"

@pytest.mark.parametrize("parameter_name, parameter_value, max_length", [
    ("Account", "example_account", 20),
    ("LoginAuth", "example_login_auth", 36),
    ("Datetime", "2023-06-12", 20)
])
def test_parameter_max_length(parameter_name, parameter_value, max_length):
    parameter_value = parameter_value * (max_length + 1)
    
    payload = {
        parameter_name: parameter_value
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 400
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Missing required parameters or over max length"
