from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://login.salesforce.com")

driver.find_element(By.XPATH,"//*[@id='username']").send_keys("welcome to automation class")
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("1234")

driver.find_element(By.XPATH,"//*[@id='login']").click()
driver.find_element(By.XPATH,"//*[@id='Forgot your password']").click()


print("Test completed")
#driver.close()
#driver.quit()