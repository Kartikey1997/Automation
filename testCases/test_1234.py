import pytest
import time
from _datetime import datetime
from testCases.conftest import setup
from selenium import webdriver
from pageObjects.loginPage import Login
from pageObjects.tradekhata_AddNewClient import Add_Client
from pageObjects.productPage import Product
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.common.exceptions import NoSuchElementException

class Test_login:
    baseURL = ReadConfig.get_URL()
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()
    product_name = ReadConfig.get_product_name()
    user = ReadConfig.get_userid()

    logger = LogGen.loggen()

    @pytest.mark.regression                    ############# TC marked as regression, marking is given when a specific TC should run only
    def test_122_TradeKhata_AddNewClient(self,setup):                  ############Always define a testcase function with its initials as "test"
        self.logger.info("Test_001_login ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("************* URL Obtained Properly ************")
        self.driver.maximize_window()
        self.logger.info("************* Window maximized ************")
        self.lp = Login(self.driver)
        self.lp.clickHere()
        time.sleep(2)
        self.lp.setUserName(self.username)
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(2)
        self.pl = Add_Client(self.driver)
        self.pl.tradekhataButton()
        self.pl.client_btn()
        self.pl.addNewClient()
        self.driver.close()
