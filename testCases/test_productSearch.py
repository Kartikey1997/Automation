import pytest
import time
from testCases.conftest import setup
from selenium import webdriver
from pageObjects.loginPage import Login
from pageObjects.productPage import Product
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_login:
    baseURL = ReadConfig.get_URL()
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()
    product_name = ReadConfig.get_product_name()
    user = ReadConfig.get_userid()

    logger = LogGen.loggen()

    @pytest.mark.sanity
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
            self.logger.info("============= User verified ============")
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_loginpage.png")
            self.logger.error("============ User not verified, Test_002_product FAILED ============")
            assert False

        lst = ["bbeedd","test chair","aallmm","table qweq"]

        self.pr = Product(self.driver)
        self.pr.searchProduct(self.product_name)
        time.sleep(3)
        self.logger.info("============= Product Sreached using text box ============")
        self.driver.find_element_by_xpath("/html/body/main/div/div[1]/div[5]/div[4]/form/div[2]/div[1]/div[1]/div[2]/div[1]/a").click()
        product_details = self.driver.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]").text
        if (product_details == "Product Details"):
            self.logger.info("============= Product Page Launched ============")
            self.logger.info("============ Test_002_product_search, PASSED ============")
        else:
            self.logger.info("============= Product Page not Launched ============")
            self.logger.info("============ Test_002_product_search, FAILED ============")
            self.driver.save_screenshot(".\\screenshots\\" + "test_productSearch.png")

        time.sleep(2)
        for i in lst:
            self.driver.find_element_by_id("global_search").send_keys(i)
            self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/div[1]/form/input[1]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("/html/body/main/div/div[1]/div[5]/div[4]/form/div[2]/div[1]/div[1]/div[2]/div[1]/a").click()
            product_details = self.driver.find_element_by_xpath("/html/body/main/div[3]/div/div[1]/div[1]").text
            if (product_details == "Product Details"):
                self.logger.info("============= Product Page Launched ============")
                self.logger.info("============ Test_002_product_search, PASSED ============")
            else:
                self.logger.info("============= Product Page not Launched ============")
                self.logger.info("============ Test_002_product_search, FAILED ============")
                self.driver.save_screenshot(".\\screenshots\\" + "test_productSearch.png")

        time.sleep(2)
        self.driver.close()

