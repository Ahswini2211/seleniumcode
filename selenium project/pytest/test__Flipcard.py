from selenium import webdriver
from selenium.webdriver.common.by import By

import time
def test_setup():
    global webdriver
    driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
    driver.implicity_wait(10)
    driver.maximize_window()

def test_login():
    driver.get("https://www.flipkart.com")
    driver.find_element(By.NAME,"q").send_keys("kurti")
    driver.find_element(By.NAME,"")
