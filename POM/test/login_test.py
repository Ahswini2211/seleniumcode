from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.Loginpage import Loginpage
from pages.Singuppage import signUp
from pages.logoutpage import logOut

class Testitera():

    @pytest.fixture(scope="session")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C://Users//user//PycharmProject//POM//driver//chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test done")

    def test_signup(self,test_setup):
        driver.get("https://itera-qa.azurewebsites.net/")
        signup = signUp(driver)
        signup.click_signup()
        signup.enter_firstname("Vincen")
        signup.enter_surname("Vegga")
        signup.enter_e_post("marusova@lyricspad.net")
        signup.enter_mobile("+1 202-918-2132")
        signup.enter_username("VincenVegga")
        signup.enter_password("Dummy@123")
        signup.enter_confirmpassowrd("Dummy@123")
        signup.click_submit()

        #driver.implicitly_wait(30)

    def test_login(self, test_setup):
        login = Loginpage(driver)
        login.click_loginn()
        login.enter_username("VincenVegga")
        login.enter_password("Dummy@123")
        login.click_login()

    def test_title(self, test_setup):
        x = driver.title
        assert x == "- Testautomation practice page"

    def test_logout(self, test_setup):
        logout = logOut(driver)
        logout.click_logout()