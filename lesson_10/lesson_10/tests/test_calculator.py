import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.calculator_page import CalculatorPage


@allure.feature("Calculator Operations")
class TestCalculator:
    """Тесты для функциональности калькулятора."""

    @allure.title("Тест сложения чисел с задержкой")
    @allure.description(
        "Проверка корректности сложения двух чисел "
        "с установленной задержкой вычислений"
    )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_calculator_addition(self, driver: WebDriver) -> None:
        """
        Тестирование операции сложения в медленном калькуляторе.

        Шаги:
        1. Установить задержку вычислений
        2. Ввести первое число
        3. Выбрать операцию сложения
        4. Ввести второе число
        5. Запустить вычисление
        6. Проверить результат

        Ожидаемый результат: 7 + 8 = 15
        """
        calculator_page = CalculatorPage(driver)

        with allure.step("Установить задержку вычислений в 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Ввести число 7"):
            calculator_page.click_button("7")

        with allure.step("Выбрать операцию сложения"):
            calculator_page.click_button("+")

        with allure.step("Ввести число 8"):
            calculator_page.click_button("8")

        with allure.step("Запустить вычисление"):
            calculator_page.click_button("=")

        with allure.step("Дождаться результата и проверить его"):
            WebDriverWait(driver, 50).until(
                lambda d: calculator_page.get_result() == "15"
            )
            assert calculator_page.get_result() == "15", (
                f"Ожидался результат '15', "
                f"но получен '{calculator_page.get_result()}'"
            )
