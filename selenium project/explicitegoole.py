from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("welcome to automation class")
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.NAME,"btnk")))

print("element is clickable")
element.click()

print("test completed")