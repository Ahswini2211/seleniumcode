from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = "C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://www.flipkart.com")
driver.implicitly_wait(30)

driver.find_element(By.CLASS_NAME, "_2KpZ6l._2doB4z").click()
driver.find_element(By.CLASS_NAME, "_3704LK").send_keys("firestick")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_396cs4._3exPp9")))

print("element is clickable")
element.click()

print("test completed")
driver.close