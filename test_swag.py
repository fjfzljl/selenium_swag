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


logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger("unit test")


@pytest.mark.TEST00001
@pytest.mark.parametrize(
    "dstring, eachtest_setupteardown, usernm, passwd, check_string, expected_result",
    [
        ("TEST00001 : test get_usernm() return correct usernm", ["debug"], "standard_user", "secret_sauce", "bob", True),
    ],
    indirect=["eachtest_setupteardown"],
)
def test_login_page(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    usernm,
    passwd,
    check_string,
    expected_result,
):
    test_login_page.__doc__ = dstring
    driver = suite_setupteardown
    
    logging.info(f"processing arg usernm : {usernm}")
    logging.info(f"processing arg passwd : {passwd}")
    # logging.info(f"processing arg check_string : {check_string}")
    # sd = student.Student(usernm, passwd)
    # assert (check_string == sd.get_usernm()) == expected_result

    # driver.get("https://www.saucedemo.com/")
    # username = driver.find_element(By.ID, "user-name")
    # username.send_keys("standard_user")
    loginpage = LoginPage(driver)
    
    username = loginpage.get_username()
    username.send_keys(usernm)

    password = loginpage.get_password()
    # password.send_keys("secret_sauce")
    password.send_keys(passwd)

    login_button = loginpage.get_login_button()
    login_button.click()


    print(driver.current_url)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
        )
        
        # time.sleep(10)
        assert "inventory" in driver.current_url
    except Exception as e: #
        logging.error(f"Exception : {e}")

    # finally:
    #     # print('finally')
    #     driver.quit()


    # assert True

