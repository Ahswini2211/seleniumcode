from selenium.webdriver.common.by import By
class Loginpage():
    def __init__(self,driver):
        self.driver = driver
        self.Login_button_linktext = "Login"
        self.username_textbox_name = "Username"
        self.password_textbox_name = "Password"
        self.login_button_xpath = "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]"

    def click_login(self):
        self.driver.find_element(By,LINK_TEXT,self.Login_button_linktext).click()

    def enter_username(self,username):
        self.driver.find_element(By,NAME,self.username_textbox_name).clear()
        self.driver.find_element(By, NAME, self.username_textbox_name).send_keys("Username")


    def enter_password(self,password):
        self.driver.find_element(By,NAME,self.password_textbox_name).clear()
        self.driver.find_element(By, NAME, self.password_textbox_name).send_keys("Username")

    def click_login(self):
        self.driver.find_element(By.XPATH).click()
