from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Utilities.logUtil import Logger


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.product_list = (By.CLASS_NAME, "inventory_list")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.product_sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.product_name = (By.CLASS_NAME, "inventory_item_name")
        self.active_option = (By.CLASS_NAME, "active_option")
        self.product_price = (By.CLASS_NAME, "inventory_item_price")
        self.logger = Logger('HomePageLogger').get_logger()  # Get the logger instance

    def get_product_list(self):
        return self.driver.find_element(*self.product_list)

    def get_add_to_cart_buttons(self):
        return self.driver.find_elements(*self.add_to_cart_buttons)

    def click_cart_icon(self):
        self.driver.find_element(*self.cart_icon).click()

    def select_product_sort_option(self, option):
        dropdown = Select(self.driver.find_element(*self.product_sort_dropdown))
        dropdown.select_by_visible_text(option)

    def get_active_option_text(self):
        return self.driver.find_element(*self.active_option).text

    def get_product_names(self):
        return [element.text for element in self.driver.find_elements(*self.product_name)]

    def get_product_prices(self):
        self.logger.info("get product pages")
        prices = self.driver.find_elements(*self.product_price)
        return [float(price.text.replace("$", "")) for price in prices]
