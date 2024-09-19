# test_cart.py

import pytest
from Pages.HomePage import HomePage
from Pages.CartPage import CartPage
from Utilities.logUtil import Logger

logger = Logger('TestLogger')

def test_add_to_cart(browser, login):
    home_page = HomePage(browser)
    logger.logger.info("Adding first product to the cart")

    # Add first product to cart
    buttons = home_page.get_add_to_cart_buttons()
    assert len(buttons) > 0, "No 'Add to Cart' buttons found."
    buttons[0].click()
    logger.logger.info("Added product to cart")

    # Capture the name of the first product
    first_product_name = home_page.get_product_names()[0]
    logger.logger.info(f"First product added: {first_product_name}")

    # Navigate to the cart
    home_page.click_cart_icon()
    logger.logger.info("Navigated to the cart")

    # Verify the product is in the cart
    cart_page = CartPage(browser)
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "No items found in the cart."

    # Get the name of the product in the cart and verify it matches
    product_in_cart = cart_page.get_cart_item_names()[0]
    assert first_product_name == product_in_cart, f"Expected product '{first_product_name}' in cart, but got '{product_in_cart}'."

    logger.logger.info(f"Verified the product '{first_product_name}' is in the cart.")
