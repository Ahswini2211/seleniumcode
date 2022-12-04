
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://login.salesforce.com")

driver.find_element(By.CSS_SELECTOR, "input#username.input.r4.wide.mb16.mt8.username").send_keys("welcome to automation class")
driver.find_element(By.CSS_SELECTOR, "input#password.input.r4.wid.mb16.mt8.password").send_keys("1234")

driver.find_element(By.CSS_SELECTOR, "input#login.button.r4.wide.primary").click()
driver.find_element(By.CSS_SELECTOR, "a#forgot_password_link.fl.small").click()


print("Test completed")
driver.close()
driver.qute()