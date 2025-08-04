from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_store_checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product("Sauce Labs Backpack")
    products.add_product("Sauce Labs Bolt T-Shirt")
    products.add_product("Sauce Labs Onesie")
    products.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_info("Test", "User", "12345")

    total = checkout.get_total()
    assert total.endswith("$58.29")

    driver.quit()
