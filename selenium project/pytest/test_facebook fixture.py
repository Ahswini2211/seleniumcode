from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//selenium project//driver//chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test done")

def test_login():
    driver.get("https://www.facebook.com")
    driver.find_element(By.NAME,"email").send_keys("ashwini ")
    driver.find_element(By.NAME,"pass").send_keys("admin123")
    driver.find_element(By.CLASS_NAME ,"_42ft._4jy0._6lth._4jy6._4jy1.selected._51sy").click()


    x = driver.title
    assert x == "Facebook"



