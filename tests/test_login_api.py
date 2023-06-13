import requests
import pytest

API_URL = "https://api.example/service/login"

def test_login_successful():
    account = "valid_account" # #bob@gmail.com
    login_auth = "valid_login_auth"
    datetime = "2023-06-12T:11:22:33"
    
    payload = {
        "Account": account,
        "LoginAuth": login_auth,
        "Datetime": datetime
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Login successful"

def test_account_number():
    account = 12345
    login_auth = "example_login_auth"
    payload = {
        "Account": str(account),
        "LoginAuth": login_auth
    }
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Login successful"

def test_login_less_datatime_successful():
    account = "valid_account"
    login_auth = "valid_login_auth"
    
    payload = {
        "Account": account,
        "LoginAuth": login_auth,
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Login successful"

def test_datetime_invalid_successful():
    account = "example_account"
    login_auth = "example_login_auth"
    datetime = "abc123"
    
    payload = {
        "Account": account,
        "LoginAuth": login_auth,
        "Datetime": datetime
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Login successful"

@pytest.fixture
def test_endpoint_not_found():
    invalid_endpoint = "https://api.example/service/invalid_endpoint"
    account = "example_account"
    login_auth = "example_login_auth"
    
    payload = {
        "Account": account,
        "LoginAuth": login_auth
    }
    response = requests.post(invalid_endpoint, json=payload)
    
    assert response.status_code == 404
    result = response.json()
    assert result["Status"] == response.status_code
    assert result["Message"] == "Login successful"