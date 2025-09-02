from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class LoginPage(BasePage):
    """Класс для работы со страницей логина."""

    # Локаторы элементов
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.

        :param driver: Экземпляр веб-драйвера.
        """
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполнение входа в систему.

        :param username: Имя пользователя.
        :param password: Пароль.
        """
        self._input_text(self.USERNAME_INPUT, username)
        self._input_text(self.PASSWORD_INPUT, password)
        self._click_element(self.LOGIN_BUTTON)
