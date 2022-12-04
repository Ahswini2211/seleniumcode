from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://Facebook.com")

driver.find_element(By.NAME,"loging").send_keys("welcome to automation class")
driver.find_element(By.NAME,"btnk1").click()



print("test completed")

driver.close()
driver.quit()