from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц проекта."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация базовой страницы.

        :param driver: Экземпляр веб-драйвера.
        """
        self.driver = driver

    def _find_element(
        self, locator: tuple[str, str], timeout: int = 10
    ) -> WebElement:
        """
        Внутренний метод для поиска элемента с ожиданием.

        :param locator: Кортеж (By, значение) для поиска элемента.
        :param timeout: Время ожидания в секундах.
        :return: Найденный элемент WebElement.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Element with locator {locator} not found"
        )

    def _click_element(self, locator: tuple[str, str]) -> None:
        """
        Клик по элементу.

        :param locator: Кортеж (By, значение) для поиска элемента.
        """
        element = self._find_element(locator)
        element.click()

    def _input_text(self, locator: tuple[str, str], text: str) -> None:
        """
        Ввод текста в поле.

        :param locator: Кортеж (By, значение) для поиска элемента.
        :param text: Текст для ввода.
        """
        element = self._find_element(locator)
        element.clear()
        element.send_keys(text)
