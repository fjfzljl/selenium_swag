# selenium_swag
use selenium test https://www.saucedemo.com/

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

## sample test cases explain
TEST00001 : Verify a valid username and password to log in
TEST00001 ~ TEST00009 : Verify different reasons for login failure, display expected error messages

