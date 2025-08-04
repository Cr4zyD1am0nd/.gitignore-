from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.calculator_page import CalculatorPage


def test_calculator_addition():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    page = CalculatorPage(driver)
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    WebDriverWait(driver, 50).until(lambda d: page.get_result() == "15")

    assert page.get_result() == "15"
    driver.quit()
