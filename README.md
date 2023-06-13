# JKOPAY_test

### Question-1:

#### test target：

graph TD
A(Test Method) --> UI Testing
UI Testing --> Boundary Value Testing
A --> Validity Verification
A --> Security Testing
UI Testing --> Cross-Platform Testing
UI Testing --> Stability Testing for Binding and Unbinding
A --> Exception Handling Testing

#### Test Method：

1. UI Testing:

   - Verify the correct display of the payment tool binding interface, including input fields, buttons, error messages, etc.
   - Evaluate the responsiveness and user experience of the interface.

2. Validity Verification:

   - Test the successful payment and accurate transaction recording using valid bank accounts or credit cards.
   - Verify that payment fails and appropriate error messages are displayed when using invalid bank accounts or credit cards.

3. Security Testing:

   - Assess the implementation of security measures such as data encryption and protection against malicious attacks.
   - Verify the app's ability to detect and prevent fraudulent activities, such as credit card theft.

4. Boundary Value Testing:

   - Test the handling of boundary conditions, such as exceeding character limits or entering invalid data formats.
   - Validate the app's behavior with different valid dates for credit cards (future dates, past dates, incorrect date formats).

5. Cross-Platform Testing:

   - Test the consistency and stability of the payment tool binding functionality across different operating systems and devices (iOS, Android).

6. Stability Testing for Binding and Unbinding:

   - Perform multiple consecutive binding and unbinding operations to assess the stability and reliability of the functionality.

7. Exception Handling Testing:
   - Evaluate the app's ability to handle exceptional situations, such as unstable network connections or service interruptions during the payment tool binding process.

#### Test Method Details：

1. UI Testing:

   1. **Input Field Length Validation:**

   - Test scenario: Enter a payment tool information with an excessively long input in the relevant fields.
     `Expected result:` The app should provide a validation error message indicating that the input length exceeds the allowed limit, and the user should be prevented from submitting the form until the input is within the acceptable range.

   2. **Error Handling for Invalid Inputs:**

   - Test scenario: Enter invalid data formats or incorrect information in the payment tool field.
     `Expected result:` The app should display appropriate error messages for each invalid input field.

   3. **Visual Differentiation for Multiple Payment Tools:**

   - Test scenario: Bind both a credit card and a bank account simultaneously.
     `Expected result:` displaying distinct icons or labels

   4. **Responsive Design Testing:**

   - Test scenario: Access the payment tool binding interface on various screen sizes and resolutions.
     `Expected result:` ipad, other mobile and mock on website.

   5. **Boundary Value **

   - future dates, past dates, incorrect date formats, null.
     `Expected result:` failed.

2. Validity Verification:

   1. **Correct Payment Tool Validation:**

   - Test scenario: Bind a payment tool using a valid bank account or credit card.
     `Expected result:` Successful

   2. **Invalid Payment Tool Validation:**

   - Test scenario: Attempt to bind a payment tool using an invalid bank account or credit card.
     `Expected result:` The application should reject the binding of invalid payment tools and display appropriate error messages indicating that the payment cannot be processed.

   3. **Incorrect Format Validation:**

   - Test scenario: Enter incorrect formats or invalid data in the payment tool fields.
     `Expected result:` The application should identify and validate whether the entered format meets the required format.

   4. **Validity of Expiry Date:**

   - Test scenario: Enter different valid dates for credit cards, including past dates, future dates, and incorrect date formats.
     `Expected result:` The application should validate the entered expiry date against the required format and range.

3. Security Testing:

   1. **Preventing CSRF (Cross-Site Request Forgery) Attacks:**

   - Test scenario: Attempt to perform payment tool binding using unauthorized websites or conduct CSRF attacks, aiming to execute operations without the user's knowledge.
     `Expected result:` The application should implement appropriate CSRF protection measures to prevent unauthorized websites or attackers from exploiting.

   2. **Preventing Account Lockouts:**

   - Test scenario: Continuously enter invalid credentials (such as passwords) multiple times and observe how the application handles account lockouts.
     `Expected result:` The application should implement mechanisms to prevent malicious attackers from using brute-force methods to lock user accounts. After a certain number of invalid attempts, the account should be locked for a period of time, and users should be notified of relevant security measures.

4. Cross-Platform Testing:

   1. iOS Testing
   2. Android Testing
   3. Cross-Browser Testing
   4. Different Device Size Testing
   5. Simulator and Real Device Testing

5. Stability Testing for Binding and Unbinding:

   1. **Perform multiple consecutive binding and unbinding operations to assess the stability and reliability of the functionality.**

6. Exceptional Condition Testing:
   1. **Network Connection Abnormality Testing:**
   - Test scenario: Simulate a disconnected network or a low-speed network environment.
     `Expected result`Ensure that the app can handle network connection abnormalities appropriately, such as providing appropriate error messages, automatically synchronizing data once the connection is restored.
   2. **Device Compatibility Testing:**
   - Test scenario: Test the app on different devices or operating system versions.
     `Expected result:` Validate the app's compatibility on different devices or operating system versions, such as ensuring proper screen adjustments, functioning correctly.

### Question-2:

# Login API Testing

This project includes tests for the login API. The tests are divided into two files: `test_login.py` and `test_login_api.py`.

## test_login.py

This file contains tests that focus on verifying error scenarios and invalid inputs during the login process.

### Functions:

- `test_login_empty_account`: Tests the case when the account field is empty, expecting a 400 error response with the corresponding error code and message.
- `test_login_missing_fields`: Tests the case when the login_auth field is missing, expecting a 400 error response with the corresponding error code and message.
- `test_login_null_account`: Tests the case when the account field is null, expecting a 400 error response with the corresponding error code and message.
- `test_login_null_loginauth`: Tests the case when the login_auth field is null, expecting a 400 error response with the corresponding error code and message.
- `test_login_invalid_credentials`: Tests the case when invalid account credentials are provided, expecting a 401 error response with the corresponding error code and message.
- `test_login_subscription_failed`: Tests the case when the subscription fails, expecting a 402 error response with the corresponding error code and message.
- `test_login_invalid_request`: Tests the case when an invalid request method (GET) is used, expecting a 405 error response with the corresponding error code and message.
- `test_parameter_max_length`: Tests the case when the input parameters exceed the maximum length limit, expecting a 400 error response with the corresponding error code and message.

## test_login_api.py

This file contains tests that focus on successful login scenarios and valid inputs.

### Functions:

- `test_login_successful`: Tests a successful login scenario with valid account credentials, expecting a 200 response with the corresponding success code and message.
- `test_account_number`: Tests the case when the account field is provided as a number, expecting a 200 response with the corresponding success code and message.
- `test_login_less_datatime_successful`: Tests a successful login scenario with valid account credentials, excluding the optional datetime field. Expects a 200 response with the corresponding success code and message.
- `test_datetime_invalid_successful`: Tests a successful login scenario with valid account credentials but an invalid datetime format. Expects a 200 response with the corresponding success code and message.
- `test_endpoint_not_found`: Tests the case when an invalid endpoint is used for the login API, expecting a 404 error response.

Please refer to the respective test functions for more detailed information on each test case.
