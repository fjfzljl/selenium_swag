#import student

import pytest
# import os
import logging
# import time

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from libs.login_page import *


# logger = logging.getLogger("unit test")
def verify_login(suite_setupteardown,
    eachtest_setupteardown,
    usernm,
    passwd,
    err_msg):
    
    driver = suite_setupteardown
    
    logging.info(f"processing arg usernm : {usernm}")
    logging.info(f"processing arg passwd : {passwd}")

    loginpage = LoginPage(driver)
    
    username = loginpage.get_username()
    username.send_keys(usernm)

    password = loginpage.get_password()
    # password.send_keys("secret_sauce")
    password.send_keys(passwd)

    login_button = loginpage.get_login_button()
    login_button.click()



    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
        )
        
        # time.sleep(10)
        logging.info(f'{driver.current_url}')


    except Exception as e: #
        # logging.error(f"Exception : {e}")
        logging.info(f'{driver.current_url}')
        error_message = loginpage.get_error_message()
        logging.info(f'error_message : {error_message}')
        
        if error_message == err_msg:
            return True
        logging.error(f'error message not match')
        return False
    
    logging.info(f'{driver.current_url}')
    return "inventory" in driver.current_url


@pytest.mark.TEST00001
@pytest.mark.TEST00002
@pytest.mark.TEST00003
@pytest.mark.TEST00004
@pytest.mark.TEST00005
@pytest.mark.TEST00006
@pytest.mark.TEST00007
@pytest.mark.TEST00008
@pytest.mark.TEST00009
@pytest.mark.parametrize(
    "dstring, eachtest_setupteardown, usernm, passwd, err_msg, expected_result",
    [
        ("TEST00001 : Verify login success : a valid username and password", ["debug"], "standard_user", "secret_sauce", "", True),
        ("TEST00002 : Verify login fail and error message : an invalid username", ["debug"], "standard_userabc", "secret_sauce", "Epic sadface: Username and password do not match any user in this service", True),
        ("TEST00003 : Verify login fail and error message : an invalid password", ["debug"], "standard_user", "0secret_sauce", "Epic sadface: Username and password do not match any user in this service", True),
        ("TEST00004 : Verify login fail and error message : empty password", ["debug"], "standard_user", "", "Epic sadface: Password is required", True),
        ("TEST00005 : Verify login fail and error message : empty username", ["debug"], "", "secret_sauce", "Epic sadface: Username is required", True),
        ("TEST00006 : Verify login fail and error message : username ending space", ["debug"], "standard_user ", "secret_sauce", "Epic sadface: Username and password do not match any user in this service", True),
        ("TEST00007 : Verify login fail and error message : username leading space", ["debug"], " standard_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service", True),
        ("TEST00008 : Verify login fail and error message : password ending space", ["debug"], "standard_user", "secret_sauce  ", "Epic sadface: Username and password do not match any user in this service", True),
        ("TEST00009 : Verify login fail and error message : password leading space", ["debug"], "standard_user", "  secret_sauce", "Epic sadface: Username and password do not match any user in this service", True),
    ],
    indirect=["eachtest_setupteardown"],
)
def test_login_page(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    usernm,
    passwd,
    err_msg,
    expected_result,
):
    test_login_page.__doc__ = dstring
    # driver = suite_setupteardown
    actual_result = verify_login(suite_setupteardown, eachtest_setupteardown, usernm, passwd, err_msg)
    assert actual_result == expected_result
    