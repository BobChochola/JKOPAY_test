# JKOPAY_test

### 1

### 2

Login API Testing
This project includes tests for the login API. The tests are divided into two files: test_login.py and test_login_api.py.

test_login.py
This file contains tests that focus on verifying error scenarios and invalid inputs during the login process.

Functions:
test_login_empty_account: Tests the case when the account field is empty, expecting a 400 error response with the corresponding error code and message.
test_login_missing_fields: Tests the case when the login_auth field is missing, expecting a 400 error response with the corresponding error code and message.
test_login_null_account: Tests the case when the account field is null, expecting a 400 error response with the corresponding error code and message.
test_login_null_loginauth: Tests the case when the login_auth field is null, expecting a 400 error response with the corresponding error code and message.
test_login_invalid_credentials: Tests the case when invalid account credentials are provided, expecting a 401 error response with the corresponding error code and message.
test_login_subscription_failed: Tests the case when the subscription fails, expecting a 402 error response with the corresponding error code and message.
test_login_invalid_request: Tests the case when an invalid request method (GET) is used, expecting a 405 error response with the corresponding error code and message.
test_parameter_max_length: Tests the case when the input parameters exceed the maximum length limit, expecting a 400 error response with the corresponding error code and message.
test_login_api.py
This file contains tests that focus on successful login scenarios and valid inputs.

Functions:
test_login_successful: Tests a successful login scenario with valid account credentials, expecting a 200 response with the corresponding success code and message.
test_account_number: Tests the case when the account field is provided as a number, expecting a 200 response with the corresponding success code and message.
test_login_less_datatime_successful: Tests a successful login scenario with valid account credentials, excluding the optional datetime field. Expects a 200 response with the corresponding success code and message.
test_datetime_invalid_successful: Tests a successful login scenario with valid account credentials but an invalid datetime format. Expects a 200 response with the corresponding success code and message.
test_endpoint_not_found: Tests the case when an invalid endpoint is used for the login API, expecting a 404 error response.
Please refer to the respective test functions for more detailed information on each test case.
