# conftest.py

import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def browser():
    """Fixture to set up and tear down the Chrome web browser."""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Uncomment the next line if you want to run tests in headless mode
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)  # Set implicit wait time
    driver.get("https://www.saucedemo.com/")  # Navigate to the base URL
    yield driver  # Provide the WebDriver instance to the test functions
    driver.quit()  # Teardown after tests

@pytest.fixture(scope="function")
def setup_teardown(browser):
    """Fixture to perform setup and teardown for each test."""
    logger.info("Starting test setup")
    yield
    logger.info("Tearing down after test")
    browser.delete_all_cookies()  # Clear cookies after each test

@pytest.fixture(scope="function")
def login(browser):
    """Fixture to log in before a test."""
    logger.info("Attempting to log in")
    login_page = LoginPage(browser)
    login_error = login_page.login("standard_user", "secret_sauce")
    assert login_error is None, f"Login failed with error: {login_error}"
    logger.info("Login successful")
    yield
    logger.info("Logging out after test")
    # Implement logout if necessary
    # For saucedemo.com, you might need to navigate to the menu and click logout
