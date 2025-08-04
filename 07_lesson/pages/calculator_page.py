from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = driver.find_element(By.ID, "delay")
        self.result = driver.find_element(By.CSS_SELECTOR, ".screen")

    def set_delay(self, seconds):
        self.delay_input.clear()
        self.delay_input.send_keys(str(seconds))

    def click_button(self, value):
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    def get_result(self):
        return self.result.text
