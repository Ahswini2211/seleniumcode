from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")

driver.implicitly_wait(10)

driver.get("https://facebook.com")
driver.find_element(By.NAME,"Email").send_keys("welcome to automation")
driver.find_element(By.NAME,"pass").send_keys("abcd")

driver.find_element(By.NAME,"login").click()


print("test completed")
driver.close()
driver.quit()




















