# CartPage.py

from selenium.webdriver.common.by import By
from Utilities.logUtil import Logger


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_price = (By.CLASS_NAME, "inventory_item_price")
        self.checkout_button = (By.ID, "checkout")

    def get_cart_items(self):
        """Return all the items in the cart."""
        return self.driver.find_elements(*self.cart_items)

    def get_cart_item_names(self):
        """Return the names of all items in the cart."""
        return [item.find_element(*self.cart_item_name).text for item in self.get_cart_items()]

    def get_cart_item_prices(self):
        """Return the prices of all items in the cart."""
        return [float(item.find_element(*self.cart_item_price).text.replace("$", "")) for item in self.get_cart_items()]

    def click_checkout(self):
        """Click the checkout button."""
        self.driver.find_element(*self.checkout_button).click()
