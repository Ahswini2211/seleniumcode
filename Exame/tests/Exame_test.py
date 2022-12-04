from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.LoginPage import Loginpage
from pages.SignupPage import SignUp
from pages.LogoutPage import LogoutPage

class Testitera():
    @pytest.fixture(scope="session")
    def test_setup(self):
        global driver
        driver = selenium.webdriver.Chrome(executable_path="C://Users//user//PycharmProject//Exame//Drivers//chromedriver.exe")
        driver.implicity_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test done")

    def test_Signup(self,test_setup):
        driver.get("https://itera-qa.azurewebsites.net/")
        signup = SignUp(driver)
        signup.click_Sinup()
        signup.enter_firstname("Ashwini")
        signup.enter_surname("Somankar")
        signup.enter_e_post("marusova@lyricspad.net")
        signup.enter_mobile(9175619126)
        signup.enter_username("ashwini")
        signup.enter_password("ashwini@11")
        signup.enter_confirmpassword("ashwini@11")
        signup.click_submit()

    def test_Login(self,test_setup):
        Login = Loginpage(driver)
        Login.click_login()
        Login.enter_username("ashwini")
        Login.enter_password("ashwini@11")
        Login.click_login()

    def test_title(self,test_setup):
        x = driver.title
        assert x == "_Testautomation practice page"

    def test_Logout(self,test_setup):
        Logout = LogoutPage(driver)
        Logout.click_logout()





