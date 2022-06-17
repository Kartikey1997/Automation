from selenium import webdriver
class Login:
    clickhere_linktext="Click here"
    textbox_username_id="email_mobile"
    textbox_password_id="password"
    initiallogin_button_id="lgn"
    finallogin_button_id="submit_email"

    def __init__(self,driver):
        self.driver=driver

    def clickHere(self):
        self.driver.find_element_by_link_text(self.clickhere_linktext).click()

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        self.driver.find_element_by_id(self.initiallogin_button_id).click()

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.finallogin_button_id).click()


