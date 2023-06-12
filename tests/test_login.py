import requests
import pytest

def api_url():
    return "https://api.example/service/login"

def test_login_empty_account(api_url):

    login_auth = "valid_login_auth"

payload = {
    "Account": "", # "miss account"
    "LoginAuth": login_auth
}

response = requests.post(api_url, json=payload)

assert response.status_code == 400

result = response.json()
assert result["Status"] == "ErrorCode_02" # 400
assert result["Message"] == "提示錯誤訊息 02" #login_auth is required, or Missing required parameters

def test_login_missing_fields(api_url):

   account = "valid_account"

    payload = {
        "Account": account,
        "LoginAuth": "" # "miss auth"
    }

    response = requests.post(api_url, json=payload)

    assert response.status_code == 400
    
    result = response.json()
    assert result["Status"] == "ErrorCode_02" # 400
    assert result["Message"] == "提示錯誤訊息 02" #login_auth is required, or Missing required parameters

def test_login_null_account(api_url):x
    
    login_auth = "valid_login_auth"

    payload = {
    "Account": None,
    "LoginAuth": login_auth
    }

    response = requests.post(api_url, json=payload)

    assert response.status_code == 400

    result = response.json()
    assert result["Status"] == "ErrorCode_02" #400
    assert result["Message"] == "提示錯誤訊息 02" #login_auth is required, or Missing required parameters

def test_login_null_loginauth(api_url):
    
    account = "valid_account"

    payload = {
    "Account": account,
    "LoginAuth": None
    }

    response = requests.post(api_url, json=payload)

    assert response.status_code == 400

    result = response.json()
    assert result["Status"] == "ErrorCode_02" #400
    assert result["Message"] == "提示錯誤訊息 02" #login_auth is required, or Missing required parameters

def test_login_invalid_credentials(api_url):

    account = "invalid_account" #bob@gmail.com not exist, bob@123, 123@123
    login_auth = "invalid_login_auth"
    datetime = "2023-06-12"

    payload = {
        "Account": account,
        "LoginAuth": login_auth,
        "Datetime": datetime
    }

    response = requests.post(api_url, json=payload)

    assert response.status_code == 401

    result = response.json()
    assert result["Status"] == "ErrorCode_01" #401
    assert result["Message"] == "提示錯誤訊息 01" #account or login_auth are invalid

    def test_login_subscription_failed(api_url):
    account = "example_account"
    login_auth = "example_invalid_auth"
    payload = {
        "Account": account,
        "LoginAuth": login_auth
    }
    response = requests.post(api_url, json=payload)
    assert response.status_code == 402
    
    result = response.json()
    assert result["Status"] == 402
    assert result["Message"] == "payment required"


def test_login_invalid_request(api_url):

    payload = {
        "Account": "valid_account",
        "LoginAuth": "valid_auth"
    }

    response = requests.get(api_url, json=payload)

    assert response.status_code == 405 
    result = response.json()
    assert result["Status"] == "ErrorCode_03" # 405
    assert result["Message"] == "提示錯誤訊息 03" #this api can not support .get

@pytest.mark.parametrize("parameter_name, parameter_value, max_length", [
    ("Account", "example_account", 20),
    ("LoginAuth", "example_login_auth", 36),
    ("Datetime", "2023-06-12", 20)
])
def test_parameter_max_length(api_url, parameter_name, parameter_value, max_length):
    parameter_value = parameter_value * (max_length + 1)
    
    payload = {
        parameter_name: parameter_value
    }
    response = requests.post(api_url, json=payload)
    
    assert response.status_code == 400
    
    result = response.json()
    assert result["Status"] == "ErrorCode_02" # 400
    assert result["Message"] == "提示錯誤訊息 02" #login_auth is required, or Missing required parameters or "over max length"
