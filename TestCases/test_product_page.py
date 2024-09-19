import pytest
from Pages.HomePage import HomePage

def test_sorting_products(browser):
    home_page = HomePage(browser)

    # Select "Price (low to high)" option
    home_page.select_product_sort_option("Price (low to high)")

    # Assert the active option text
    active_option_text = home_page.get_active_option_text()
    assert active_option_text == "Price (low to high)", f"Expected 'Price (low to high)' but got '{active_option_text}'"

    # Get product prices and assert they are sorted in ascending order
    product_prices = home_page.get_product_prices()
    assert product_prices == sorted(product_prices), "Product prices are not sorted in ascending order"
