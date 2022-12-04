from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://login.salesforce.com")


driver.find_element(By.CSS_SELECTOR, "input#username").send_keys("ashchikhalkhunde@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("12345")

driver.find_element(By.CSS_SELECTOR,"input#Login").click()
driver.find_element(By.CSS_SELECTOR, "a# forgot_password_link").click()

print("test completed")

#driver.close()
#driver.quit()