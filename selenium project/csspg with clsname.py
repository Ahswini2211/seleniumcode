from selenium import webdriver
from  selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://login.salesforce.com")


driver.find_element(By.CSS_SELECTOR,"input.input.r4.wide.mb16.mt8.username").send_keys("ashwini")
driver.find_element(By.CSS_SELECTOR,"input.input.r4.wide.mb16.mt8.password").send_keys("2211")

driver.find_element(By.CSS_SELECTOR,"input.button.r4.wide.primary").click()
driver.find_element(By.CSS_SELECTOR,"a.fl.small").click()

print("test completed")
#driver.close()
#driver.quit()





