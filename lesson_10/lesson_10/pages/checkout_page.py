from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class CheckoutPage(BasePage):
    """Класс для работы со страницей оформления заказа."""

    # Локаторы элементов
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: Экземпляр веб-драйвера.
        """
        super().__init__(driver)

    def fill_info(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполнение информации для оформления заказа.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param postal_code: Почтовый индекс.
        """
        self._input_text(self.FIRST_NAME_INPUT, first_name)
        self._input_text(self.LAST_NAME_INPUT, last_name)
        self._input_text(self.POSTAL_CODE_INPUT, postal_code)
        self._click_element(self.CONTINUE_BUTTON)

    def get_total(self) -> str:
        """
        Получение общей суммы заказа.

        :return: Текст общей суммы.
        """
        total_element = self._find_element(self.TOTAL_LABEL)
        return total_element.text
