from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
    
    def get_username(self):
        return self.driver.find_element(By.ID, "user-name")
    
    def get_password(self):
        return self.driver.find_element(By.ID, "password")
    
    def get_login_button(self):
        return self.driver.find_element(By.ID, "login-button")
