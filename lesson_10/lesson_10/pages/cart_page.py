from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class CartPage(BasePage):
    """Класс для работы со страницей корзины."""

    # Локаторы элементов
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр веб-драйвера.
        """
        super().__init__(driver)

    def click_checkout(self) -> None:
        """Нажатие кнопки оформления заказа."""
        self._click_element(self.CHECKOUT_BUTTON)
