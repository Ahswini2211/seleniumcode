from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, "input#txtusername").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input#txtpassword").send_keys("admin123")

driver.find_element(By.CSS_SELECTOR, "input#btnLogin.button").click()
driver.find_element(By.CSS_SELECTOR, "div#forgotpasswordLink").click()

print("test completed")

#driver.close()
#driver.quit()