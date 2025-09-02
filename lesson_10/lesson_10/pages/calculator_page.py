from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class CalculatorPage(BasePage):
    """Класс для работы со страницей калькулятора."""

    # Локаторы элементов
    DELAY_INPUT = (By.ID, "delay")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: Экземпляр веб-драйвера.
        """
        super().__init__(driver)
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, seconds: int) -> None:
        """
        Установка задержки вычислений.

        :param seconds: Количество секунд задержки.
        """
        self._input_text(self.DELAY_INPUT, str(seconds))

    def click_button(self, value: str) -> None:
        """
        Нажатие кнопки калькулятора.

        :param value: Значение кнопки (цифра или оператор).
        """
        button_locator = (By.XPATH, f"//span[text()='{value}']")
        self._click_element(button_locator)

    def get_result(self) -> str:
        """
        Получение результата вычислений.

        :return: Текст результата.
        """
        result_element = self._find_element(self.RESULT)
        return result_element.text
