import pytest
import time
from _datetime import datetime
from testCases.conftest import setup
from selenium import webdriver
from pageObjects.loginPage import Login
from pageObjects.sendEnquiry import Inquiry
from pageObjects.addToCart import Buy
from pageObjects.productPage import Product
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.common.exceptions import NoSuchElementException

class Test_BuyNow:
    baseURL = ReadConfig.get_URL()
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()
    product_name = ReadConfig.get_product_addCart()
    user = ReadConfig.get_userid()

    logger = LogGen.loggen()

    @pytest.mark.addcart                    ############# TC marked as regression, marking is given when a specific TC should run only
    def test_007_addToCart(self,setup):                  ############Always define a testcase function with its initials as "test"


        self.logger.info("Test_007_addToCart ************")
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

        '''try:
            self.logger.info("************* try command executed ************")
            txt=self.driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/div/span[2]/span[1]").text
        except NoSuchElementException:
            self.driver.execute_script("window.open('https://www.tradeindia.com');")
            self.logger.info("************* New tab opened ************")
            handles = self.driver.window_handles
            time.sleep(2)
            self.driver.close()
            self.logger.info("************* Parent tab closed ************")
            self.driver.switch_to.window(handles[1])
            self.logger.info("************* Focus switched on new tab ************")
        time.sleep(2)
        actual_user = self.driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/div/span[2]/span[1]").text
        self.logger.info("************* Xpath handled properly, text grabbed ************")
        if (actual_user == self.user):
            self.logger.info("============ User verified, Login Succeed ==============")
            assert True
        else:
            timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
            self.driver.save_screenshot("./screenshots/" + "test_loginpage-"+timestr+".png")
            self.logger.error("============= User not verified, Invalid Login!!!, screenshot generated  ==============")
            self.driver.close()
            assert False'''

        self.buynow = Buy(self.driver)
        self.buynow.productSearchForCart(self.product_name)
        self.logger.info("============= Desire Product Searched ============")
        time.sleep(2)
        product_details = self.driver.find_element_by_xpath("//div[1]/div[1]/div[1][@class='prime-heading']").text
        print(product_details)
        if (product_details == "Product Details"):
            self.logger.info("============= Product Page Launched ============")
            self.logger.info("============ Product Searched ============")
        else:
            self.logger.info("============= Product Page not Launched ============")
            self.logger.info("============ Product Not Found, screenshot generated ============")
            timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
            self.driver.save_screenshot("./screenshots/" + "test_product search-" + timestr + ".png")


        self.buynow.addToCart()

        self.driver.close()