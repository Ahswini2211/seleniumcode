
from selenium.webdriver.common.by import By

class Loginpage():

    def __init__(self,driver):
        self.driver = driver
        self.Login_button_linktext = "Login"
        self.Username_textbox_name = "Username"
        self.Password_textbox_name = "Password"
        self.login_button_xpath = "//input[@value='Login']"

    def click_loginn(self):
        self.driver.find_element(By.LINK_TEXT, self.Login_button_linktext).click()

    def enter_username(self,Username):
        self.driver.find_element(By.NAME, self.Username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.Username_textbox_name).send_keys(Username)

    def enter_password(self,Password):
        self.driver.find_element(By.NAME, self.Password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.Password_textbox_name).send_keys(Password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()