# selenium_swag
Use selenium test https://www.saucedemo.com/ login page

## This test can run in macOS. Install requirement
```shell
make install
```

OR

```shell
pip install -r requirements.txt
```


## How to run the tests in macOS
```shell
make test
```

OR

```shell
python3 start_tests.py
```

OR run only selected test cases

```shell
python3 start_tests.py -t TEST00001
```

## How to view the report
The test report should save in pytest_report.html


## File Structure
- starts_tests.py : main function to start the test
- test_swag.py : all test cases
- libs/login_page.py : swag page class, get all the useful elements
- conftest.py : includes test setup, teardown, and test report setting
- pytest.ini : explain the test cases mark

## sample test cases explain
TEST00001 : Verify a valid username and password to log in
TEST00001 ~ TEST00009 : Verify different reasons for login failure, display expected error messages

