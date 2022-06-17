import pytest
import os
from datetime import datetime
import time
from testCases.conftest import setup
from selenium import webdriver
from pageObjects.city_pages_visit import city
from pageObjects.checkbox import check_box
from pageObjects.loginPage import Login
from pageObjects.sendEnquiry import Inquiry
from pageObjects.productPage import Product
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_City_Pages:
    logger = LogGen.loggen()

    def test_all_city_pages(self,setup):
        self.driver = setup
        self.type = city(self.driver)
        self.type.manufacturer()
        time.sleep(2)
        self.type.seller()
        time.sleep(2)
        self.driver.close()



