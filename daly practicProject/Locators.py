from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//daly practicProject//driver//chromedriver.exe")
driver.get("https://www.facebook.com")

driver.find_element(By.NAME,"email").send_keys("Ashwini")
driver.find_element(By.NAME,"pass").send_keys("ash22")
driver.find_element(By.NAME,"login").click()

print("test completed")
driver.close()
driver.quit()

