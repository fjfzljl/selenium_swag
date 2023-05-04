#import student

import pytest
import os
import logging
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from libs.login_page import *


# logger = logging.getLogger("unit test")
def verify_login(suite_setupteardown,
    eachtest_setupteardown,
    usernm,
    passwd):
    
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
        logging.error(f"Exception : {e}")
        return False
    
    return "inventory" in driver.current_url


@pytest.mark.TEST00001
@pytest.mark.TEST00002
@pytest.mark.parametrize(
    "dstring, eachtest_setupteardown, usernm, passwd, expected_result",
    [
        ("TEST00001 : Verify that you can enter a valid username and password to log in to the website", ["debug"], "standard_user", "secret_sauce", True),
        ("TEST00002 : Verify that you cannot log in with an invalid username and password combination.", ["debug"], "standard_userabc", "secret_sauce", False),
    ],
    indirect=["eachtest_setupteardown"],
)
def test_login_page(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    usernm,
    passwd,
    expected_result,
):
    test_login_page.__doc__ = dstring
    # driver = suite_setupteardown
    actual_result = verify_login(suite_setupteardown, eachtest_setupteardown, usernm, passwd)
    assert actual_result == expected_result
    