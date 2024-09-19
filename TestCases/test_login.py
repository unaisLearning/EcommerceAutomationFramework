# testLogin.py

import pytest
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", True),        # Valid credentials
    ("locked_out_user", "secret_sauce", False),    # Locked-out user
    ("invalid_user", "wrong_password", False)      # Invalid credentials
])
def test_login(username, password, expected, browser):
    login_page = LoginPage(browser)
    login_error = login_page.login(username, password)

    if expected:
        # Validate successful login by checking product list presence
        home_page = HomePage(browser)
        product_list = home_page.get_product_list()
        assert product_list is not None, "Login failed for valid user: Product list not found."
        assert len(product_list.find_elements(By.CLASS_NAME, "inventory_item")) > 0, "No products found after login."
    else:
        # Validate error message for invalid or locked-out users
        assert "Epic sadface" in login_error, "Expected error message not found."
