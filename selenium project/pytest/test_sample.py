from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProject/selenium project/driver/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")

def test_login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()

    x = driver.title
    assert x == "OrangeHRM"



# def test_teardown(test_setup):
#     driver.close()
#     driver.quit()
#     print("test done")