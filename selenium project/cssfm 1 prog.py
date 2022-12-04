from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://login.salesforce.com")


driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("ashchikhalkhunde@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("12345")

driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "a[id='forgot_password_link']").click()

print("test completed")

#driver.close()
#driver.quit()