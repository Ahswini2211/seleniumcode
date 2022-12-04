from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("admin")
driver.find_element(By.XPATH,"//*[@id='app'']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[1]").send_keys("admin123")


driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p").click()

print("test completed")
#driver.close()
#driver.quit()