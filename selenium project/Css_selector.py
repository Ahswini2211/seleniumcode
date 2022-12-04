from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//daly practicProject//driver//chromedriver.exe")
driver.get("https://login.salesforce.com")

driver.find_element(By.CSS_SELECTOR,"input#username.input.r4.wide.mb16.mt8.username").send_keys("Ashwini")
driver.find_element(By.CSS_SELECTOR,"input#pw.input.r4.wide.mb16.mt8.password").send_keys("345111")
driver.find_element(By.CSS_SELECTOR,"input#Login.button.r4.wide.primary").click()
driver.find_element(By.CSS_SELECTOR,"a#forgot_password_link.fl.small").click()

print("test completed")
driver.close()
driver.quit()