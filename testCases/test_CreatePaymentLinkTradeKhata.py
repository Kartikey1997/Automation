import pytest
import time
from _datetime import datetime
from testCases.conftest import setup
from selenium import webdriver
from pageObjects.loginPage import Login
from pageObjects.tradekhata_AddNewClient import Add_Client
from pageObjects.tradekhata_CreatPaymentLink import NewPaymentLink
from pageObjects.productPage import Product
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.common.exceptions import NoSuchElementException

class Test_Client:
    baseURL = ReadConfig.get_URL()
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()
    product_name = ReadConfig.get_product_redButton()
    user = ReadConfig.get_userid()

    logger = LogGen.loggen()

    @pytest.mark.khata                   ############# TC marked as regression, marking is given when a specific TC should run only
    def test_123_AddNewClient(self,setup):                  ############Always define a testcase function with its initials as "test"

        self.logger.info("Test_123_RED_Add new client ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("************* URL Obtained Properly ************")
        self.driver.maximize_window()
        self.logger.info("************* Window maximized ************")
        self.lp = Login(self.driver)
        self.lp.clickHere()
        self.logger.info("************* Click here clicked ************")
        self.lp.setUserName(self.username)
        self.logger.info("************* Useremail entered properly ************")
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.logger.info("************* Password entered properly ************")
        self.lp.clickLogin()
        time.sleep(2)
        self.logger.info("************* click login pressed ************")

        self.trade = Add_Client(self.driver)
        self.trade.tradekhataButton()
        self.payLink = NewPaymentLink(self.driver)
        self.payLink.onlinePaymentBtn()
        time.sleep(2)
        self.payLink.paymentDescription()
        time.sleep(2)
        self.payLink.set_AutoReminderInPaymentLink()
        time.sleep(2)
        self.payLink.createPaymentBtn()
        time.sleep(4)
        self.driver.close()
