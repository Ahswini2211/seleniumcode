from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://login.salesforce.com")

driver.find_element(By.XPATH,"//input[@type='email']").send_keys("ASHWINI")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("2211")

driver.find_element(By.XPATH,"//input[@type='submit']").click()
#driver.find_element(By.XPATH,"//a[@id='forgot_password_link']").click()

print(" test completed")
#driver.close()
#driver.qute()

