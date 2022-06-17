import time
from utilities.readProperties import ReadConfig
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen
from testCases.conftest import setup
from selenium.common.exceptions import NoSuchElementException
from _datetime import datetime

class Login:

    logger = LogGen.loggen()

    clickhere_linktext="Click here"
    textbox_username_id="email_mobile"
    textbox_password_id="password"
    initiallogin_button_id="lgn"
    finallogin_button_id="submit_email"
    username_xpath=""

    '''baseURL = ReadConfig.get_URL()
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()
    product_name = ReadConfig.get_product_name()'''
    user = ReadConfig.get_userid()

    def __init__(self,driver):
        self.driver=driver

    def clickHere(self):
        self.driver.find_element_by_link_text(self.clickhere_linktext).click()
        time.sleep(2)

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_id(self.initiallogin_button_id).click()

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
        time.sleep(2)

    def clickLogin(self):
        self.driver.find_element_by_id(self.finallogin_button_id).click()
        self.logger.info("************* click login pressed ************")
        time.sleep(5)
        self.driver.get("https://www.tradeindia.com")

        '''try:
            self.logger.info("************* try command executed ************")
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[4]/div/div[2]/div/span[2]/span[1]")))
            #txt = self.driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/div/span[2]/span[1]").text
        except NoSuchElementException:
            self.driver.get("https://www.tradeindia.com")
            # self.driver.execute_script("window.open('https://www.tradeindia.com');")
            # self.logger.info("************* New tab opened ************")
            # handles = self.driver.window_handles
            # time.sleep(2)
            # self.driver.close()
            # self.logger.info("************* Parent tab closed ************")
            # self.driver.switch_to.window(handles[1])
            # self.logger.info("************* Focus switched on new tab ************")'''

        time.sleep(2)
        actual_user = self.driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/div/span[2]/span[1]").text
        self.logger.info("************* Xpath handled properly, text grabbed ************")
        print(actual_user,self.user)
        if (actual_user == self.user):
            self.logger.info("============ User verified, Login Succeed ==============")
            assert True
        else:
            timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
            self.driver.save_screenshot("./screenshots/" + "test_loginpage-" + timestr + ".png")
            self.logger.error("============= User not verified, Invalid Login!!!, screenshot generated  ==============")
            self.driver.close()
            assert False

    def clickLoginDDT(self):
        self.driver.find_element_by_id(self.finallogin_button_id).click()
        time.sleep(5)
        self.logger.info("************* click login pressed ************")