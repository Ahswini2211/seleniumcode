from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import webdriverwait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="")
driver.get("")
driver.find_element().send_keys()
wait = webdriverwait(driver,10)
element = wait.UNTIL(EC.element_to_be_clickable(By.))