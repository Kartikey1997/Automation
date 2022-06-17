'''import pytest
import time
from _datetime import datetime
from testCases.conftest import setup
from selenium import webdriver
from pageObjects.loginPage import Login
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
    def test_001_login(self,setup):                  ############Always define a testcase function with its initials as "test"


        self.logger.info("Test_001_login ************")
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
        time.sleep(3)
        self.logger.info("************* click login pressed ************")

        try:
            self.logger.info("************* try command executed ************")
            self.driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/div/span[2]/span[1]").text()
        except NoSuchElementException:
            self.driver.get("http://www.tradeindia.com")
            self.driver.execute_script("window.open('https://www.tradeindia.com');")
            self.logger.info("************* New tab opened ************")
            handles = self.driver.window_handles
            time.sleep(2)
            self.driver.close()
            self.logger.info("************* Parent tab closed ************")
            self.driver.switch_to.window(handles[1])
            self.logger.info("************* Focus switched new tab ************")

        time.sleep(2)
        actual_user = self.driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/div/span[2]/span[1]").text
        self.logger.info("************* Xpath handled properly, text grabbed ************")
        if (actual_user == self.user):
            self.logger.info("============ User verified, Test_001_login PASSED ==============")
            assert True
        else:
            timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
            self.driver.save_screenshot("./screenshots/" + "test_loginpage-"+timestr+".png")
            self.logger.error("============= User not verified--SCREENSHOT generated, Test_001_login FAILED ==============")
            self.driver.close()
            assert False


        self.driver.close()'''

'''@pytest.mark.sanity
    def test_002_product_search(self, setup):
        self.logger.info("Test_002_product search ************")
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
        time.sleep(3)
        actual_user = self.driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/div/span[2]/span[1]").text
        if actual_user == self.user:
            self.logger.info("============= User verified, Test_002_product PASSED ============")
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_loginpage.png")
            self.logger.error("============ User not verified, Test_002_product FAILED ============")
            assert False


        self.pr = Product(self.driver)
        self.pr.searchProduct(self.product_name)
        time.sleep(3)
        #self.driver.find_element_by_id("closeFairPopup").click()
        self.driver.find_element_by_xpath("/html/body/main/div/div[1]/div[5]/div[4]/form/div[2]/div[1]/div[1]/div[2]/div[1]/a").click()
        self.driver.close()
        self.logger.info("============ Test_002_product searched, PASSED ============")'''

