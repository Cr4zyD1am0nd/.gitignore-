# 06_lesson/task_3_wait_images.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
driver.get(url)


WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img[src^='https']"))
)

images = driver.find_elements(By.CSS_SELECTOR, "img[src^='https']")
print(images[2].get_attribute("src"))
driver.quit()
