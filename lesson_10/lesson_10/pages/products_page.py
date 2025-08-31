from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class ProductsPage(BasePage):
    """Класс для работы со страницей товаров."""

    # Локаторы элементов
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы товаров.

        :param driver: Экземпляр веб-драйвера.
        """
        super().__init__(driver)

    def add_product(self, product_name: str) -> None:
        """
        Добавление товара в корзину.

        :param product_name: Название товара.
        """
        xpath = (f"//div[text()='{product_name}']"
                 "/ancestor::div[@class='inventory_item']//button")
        add_button_locator = (By.XPATH, xpath)
        self._click_element(add_button_locator)

    def go_to_cart(self) -> None:
        """Переход в корзину."""
        self._click_element(self.CART_LINK)
