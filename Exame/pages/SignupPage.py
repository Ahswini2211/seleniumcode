from selenium.webdriver.common.by import By

class SignUp():
    def __init__(self,driver):
        self.driver = driver

        self.sign_button_xpath = "//*[@id='navbarColor01']/form/ul/li[1]/a"
        self.firstname_textbox_name = "FirstName"
        self.surname_textbox_name = "Surname"
        self.e_post_textbox_name = "E_post"
        self.mobile_textbox_name = "Mobile"
        self.username_textbox_name = "Username"
        self.passsword_textbox_name = "Password"
        self.confirmpassword_textbox_name = "ConfirmPassword"
        self.submit_button_id = "submit"


    def  click_Sinup(self):

        self.driver.find_element(By,XPATH,self.sign_button_xpath).click()

    def enter_firstname(self,firstname):

        self.driver.find_element(By,NAME,self.firstname_textbox_name).clear()
        self.driver.find_element(By,NAME,self.surname_textbox_name).send_keys("firstname")

    def enter_surname(self,surname):

        self.driver.find_element(By,NAME,self.surname_textbox_name).clear()
        self.driver.find_element(By,NAME,self.surname_textbox_name).send_keys("surname")

    def enter_e_post(self,e_post):

        self.driver.find_element(By,NAME,self.e_post_textbox_name).clear()
        self.driver.find_element(By,NAME,self.e_post_textbox_name).send_keys("e_post")

    def enter_mobile(self,mobile):

        self.driver.find_element(By,NAME,self.mobile_textbox_name).clear()
        self.driver.find_element(By,NAME,self.mobile_textbox_name).send_keys("mobile")

    def enter_username(self,username):
        self.driver.find_element(By,NAME,  self.username_textbox_name).clear()
        self.driver.find_element(By,NAME,self.username_textbox_name).send_keys("username")

    def enter_password(self,password):
        self.driver.find_element(By,NAME,  self.passsword_textbox_name).clear()
        self.driver.find_element(By,NAME,self.passsword_textbox_name).send_keys("password")

    def enter_confirmpassword(self,confirmpassword):
        self.driver.find_element(By,NAME,  self.confirmpassword_textbox_name).clear()
        self.driver.find_element(By,NAME,self.confirmpassword_textbox_name).send_keys("confimpassword")

    def click_submit(self):
        self.driver.find_element(By,ID,self.submit_button_id).click()

