import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Generator


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Фикстура для создания и закрытия веб-драйвера."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
