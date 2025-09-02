import allure
import time
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Store Checkout Process")
class TestStoreCheckout:
    """Тесты процесса оформления заказа в интернет-магазине."""

    @allure.title("Полный процесс оформления заказа")
    @allure.description(
        "Тестирование полного цикла: логин, добавление товаров, "
        "оформление заказа"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_store_checkout(self, driver: WebDriver) -> None:
        """
        Полное тестирование процесса оформления заказа.

        Шаги:
        1. Авторизация в системе
        2. Добавление товаров в корзину
        3. Переход в корзину
        4. Начало оформления заказа
        5. Заполнение информации о покупателе
        6. Проверка общей суммы

        Ожидаемый результат: Общая сумма заказа равна $58.29
        """
        with allure.step("Авторизация с валидными учетными данными"):
            login_page = LoginPage(driver)
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            products_page = ProductsPage(driver)
            products_page.add_product("Sauce Labs Backpack")
            time.sleep(1)  # Пауза между добавлениями
            products_page.add_product("Sauce Labs Bolt T-Shirt")
            time.sleep(1)
            products_page.add_product("Sauce Labs Onesie")
            time.sleep(2)  # Даем время на обновление корзины

        with allure.step("Переход в корзину"):
            products_page.go_to_cart()
            time.sleep(2)  # Добавляем задержку для загрузки страницы корзины

        with allure.step("Начало оформления заказа"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()

        with allure.step("Заполнение информации о покупателе"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_info("Test", "User", "12345")

        with allure.step("Проверка общей суммы заказа"):
            total = checkout_page.get_total()
            assert total.endswith("$58.29"), (
                f"Ожидалась сумма $58.29, но получено: {total}"
            )
