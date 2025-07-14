# 06_lesson/task_2_rename_button.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

button = driver.find_element(By.ID, "updatingButton")
button.click()

WebDriverWait(driver, 5).until(
    lambda d: button.get_attribute("value") == "SkyPro"
)

print(button.get_attribute("value"))
driver.quit()
