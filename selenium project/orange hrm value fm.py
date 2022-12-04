from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, "input[name = 'username')").send_keys('Admin')
driver.find_element(By.CSS_SELECTOR, "input[type = 'password')").send_keys('admin123')

driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
driver.find_element(By.CSS_SELECTOR, "p [class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()

print("test completed")

#driver.close()
#driver.quit()