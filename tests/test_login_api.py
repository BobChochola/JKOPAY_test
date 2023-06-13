import requests
import pytest

def api_url():
    return "https://api.example/service/login"

def test_login_successful(api_url):
    account = "valid_account" # #bob@gmail.com
    login_auth = "valid_login_auth"
    datetime = "2023-06-12"
    
    payload = {
        "Account": account,
        "LoginAuth": login_auth,
        "Datetime": datetime
    }
    response = requests.post(api_url, json=payload)
    
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == 200
    assert result["Message"] == "Login successful"

def test_account_number(api_url):
    account = 12345
    login_auth = "example_login_auth"
    payload = {
        "Account": str(account),
        "LoginAuth": login_auth
    }
    response = requests.post(api_url, json=payload)
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == 200
    assert result["Message"] == "Login successful"

def test_login_less_datatime_successful(api_url):
    account = "valid_account"
    login_auth = "valid_login_auth"
    
    payload = {
        "Account": account,
        "LoginAuth": login_auth,
    }
    response = requests.post(api_url, json=payload)
    
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == 200
    assert result["Message"] == "Login successful"

    def test_datetime_invalid_successful(api_url):
    account = "example_account"
    login_auth = "example_login_auth"
    datetime = "abc123"
    
    payload = {
        "Account": account,
        "LoginAuth": login_auth,
        "Datetime": datetime
    }
    response = requests.post(api_url, json=payload)
    
    assert response.status_code == 200
    
    result = response.json()
    assert result["Status"] == 200
    assert result["Message"] == "Login successful"

    import requests
import pytest

@pytest.fixture
def test_endpoint_not_found(api_url):
    invalid_endpoint = "https://api.example/service/invalid_endpoint"
    account = "example_account"
    login_auth = "example_login_auth"
    
    payload = {
        "Account": account,
        "LoginAuth": login_auth
    }
    response = requests.post(invalid_endpoint, json=payload)
    
    assert response.status_code == 404