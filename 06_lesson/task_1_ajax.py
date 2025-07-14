# 06_lesson/task_1_ajax.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

result = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)

print(result.text)
driver.quit()
