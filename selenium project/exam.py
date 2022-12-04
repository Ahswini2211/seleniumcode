from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
driver.get("http://automationpractice.com")

driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()

driver.find_element(By.XPATH,"//*[@id='email']").send_keys("ashchikhalkhunde@gmail.com")
driver.find_element(By.XPATH,"//*[@id='passwd']").send_keys("12345")
driver.find_element(By.XPATH,"//*[@id='SubmitLogin']/span").click()



driver.find_element(By.XPATH,"//*[@id='block_top_menu']/ul/li[1]/a").click()
driver.find_element(By.XPATH,"//*[@id='center_column']/ul/li[2]/div/div[1]/div/a[1]/img").click()
driver.find_element(By.XPATH,"//@id='add_to_card']/button/span").click()


driver.implicitly_wait(300)
driver.find_element(By.XPATH,"//*[@id='layer_cart]/div[1]/div[2]/div[4]/a/span").click()

driver.implicitly_wait(300)
driver.find_element(By.XPATH,"//*[@id='center_column']/p[2]/a[1]/span").click()


driver.implicitly_wait(300)
driver.find_element(By.XPATH,"//*[@id='center_column']/form/p/button/span").click()

driver.find_element(By.XPATH,"//*[@id='cgv']").click()

driver.implicitly_wait(300)
driver.find_element(By.XPATH,"//*[@id='form']/p/button/span").click()

driver.find_element(By.XPATH,"//*[@id='HOOK_PAYMENT']/div[2]/div/p/a").click()

driver.find_element(By.XPATH,"//*[@id='cart_navigation']/button/span").click()

print("test copleted")



#driver.close()
#driver.quit()


