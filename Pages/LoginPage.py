# LoginPage.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.logUtil import Logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")

    def enter_username(self, username):
        logger = Logger('TestLoginLogger').get_logger()
        logger.info(f"Starting login test with username: {username}")
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        try:
            # Wait for the inventory page to load by checking the URL
            WebDriverWait(self.driver, 10).until(EC.url_contains("inventory.html"))
            return None  # Indicate successful login
        except:
            # If the inventory page doesn't load, capture the error message
            return self.get_error_message()
