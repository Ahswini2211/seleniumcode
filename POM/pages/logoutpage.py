from selenium.webdriver.common.by import By


class logOut():

    def __init__(self,driver):
        self.driver = driver

        self.logout_button_class = "nav-link"


    def click_logout(self):
        self.driver.find_element(By.CLASS_NAME, self.logout_button_class).click()