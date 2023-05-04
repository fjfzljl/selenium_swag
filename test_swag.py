# import student

import pytest
import logging

from collections import namedtuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from libs.login_page import *


Login_Status_Code = namedtuple("Login_Status_Code", ["code", "description"])

LOGIN_UNACCEPT_ERROR = Login_Status_Code(0, "login unaccept error")
LOGIN_SUCCESS = Login_Status_Code(1, "login fail")
LOGIN_FAIL_MEG_MATCH = Login_Status_Code(2, "login fail, display correct message")


def verify_login(suite_setupteardown, eachtest_setupteardown, usernm, passwd, err_msg):
    driver = suite_setupteardown

    logging.info(f"processing arg usernm : {usernm}")
    logging.info(f"processing arg passwd : {passwd}")

    loginpage = LoginPage(driver)

    username = loginpage.get_username()
    username.send_keys(usernm)

    password = loginpage.get_password()
    password.send_keys(passwd)

    login_button = loginpage.get_login_button()
    login_button.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
        )

        logging.info(f"current_url : {driver.current_url}")

        if "inventory" in driver.current_url:
            return LOGIN_SUCCESS

    except Exception as e:  #
        # logging.error(f"Exception : {e}")
        logging.info(f"current_url : {driver.current_url}")
        error_message = loginpage.get_error_message()
        logging.info(f"error_message : {error_message}")

        if error_message == err_msg:
            return LOGIN_FAIL_MEG_MATCH

        logging.error(f"error message not match")
        return LOGIN_UNACCEPT_ERROR

    logging.info(f"current_url : {driver.current_url}")
    return LOGIN_UNACCEPT_ERROR


@pytest.mark.TEST00001
@pytest.mark.parametrize(
    "dstring, usernm, passwd, err_msg, expected_result",
    [
        (
            "TEST00001 : Verify login success : a valid username and password",
            "standard_user",
            "secret_sauce",
            "",
            LOGIN_SUCCESS,
        ),
    ],
)
def test_login_page_success(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    usernm,
    passwd,
    err_msg,
    expected_result,
):
    test_login_page_success.__doc__ = dstring
    actual_result = verify_login(
        suite_setupteardown, eachtest_setupteardown, usernm, passwd, err_msg
    )
    assert actual_result == expected_result


@pytest.mark.TEST00002
@pytest.mark.parametrize(
    "dstring, usernm, passwd, err_msg, expected_result",
    [
        (
            "TEST00002 : Verify login fail and error message : empty password",
            "standard_user",
            "",
            "Epic sadface: Password is required",
            LOGIN_FAIL_MEG_MATCH,
        ),
    ],
)
def test_login_page_empty_password(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    usernm,
    passwd,
    err_msg,
    expected_result,
):
    test_login_page_empty_password.__doc__ = dstring
    actual_result = verify_login(
        suite_setupteardown, eachtest_setupteardown, usernm, passwd, err_msg
    )
    assert actual_result == expected_result


@pytest.mark.TEST00003
@pytest.mark.parametrize(
    "dstring, usernm, passwd, err_msg, expected_result",
    [
        (
            "TEST00003 : Verify login fail and error message : empty username",
            "",
            "secret_sauce",
            "Epic sadface: Username is required",
            LOGIN_FAIL_MEG_MATCH,
        ),
    ],
)
def test_login_page_empty_username(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    usernm,
    passwd,
    err_msg,
    expected_result,
):
    test_login_page_empty_username.__doc__ = dstring
    actual_result = verify_login(
        suite_setupteardown, eachtest_setupteardown, usernm, passwd, err_msg
    )
    assert actual_result == expected_result


@pytest.mark.TEST00004
@pytest.mark.TEST00005
@pytest.mark.TEST00006
@pytest.mark.TEST00007
@pytest.mark.TEST00008
@pytest.mark.TEST00009
@pytest.mark.parametrize(
    "dstring, usernm, passwd, err_msg, expected_result",
    [
        (
            "TEST00004 : Verify login fail and error message : an invalid username",
            "standard_userabc",
            "secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
            LOGIN_FAIL_MEG_MATCH,
        ),
        (
            "TEST00005 : Verify login fail and error message : an invalid password",
            "standard_user",
            "0secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
            LOGIN_FAIL_MEG_MATCH,
        ),
        (
            "TEST00006 : Verify login fail and error message : username ending space",
            "standard_user ",
            "secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
            LOGIN_FAIL_MEG_MATCH,
        ),
        (
            "TEST00007 : Verify login fail and error message : username leading space",
            " standard_user",
            "secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
            LOGIN_FAIL_MEG_MATCH,
        ),
        (
            "TEST00008 : Verify login fail and error message : password ending space",
            "standard_user",
            "secret_sauce  ",
            "Epic sadface: Username and password do not match any user in this service",
            LOGIN_FAIL_MEG_MATCH,
        ),
        (
            "TEST00009 : Verify login fail and error message : password leading space",
            "standard_user",
            "  secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
            LOGIN_FAIL_MEG_MATCH,
        ),
    ],
)
def test_login_page_unmatch(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    usernm,
    passwd,
    err_msg,
    expected_result,
):
    test_login_page_unmatch.__doc__ = dstring
    actual_result = verify_login(
        suite_setupteardown, eachtest_setupteardown, usernm, passwd, err_msg
    )
    assert actual_result == expected_result
