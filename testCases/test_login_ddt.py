import pytest
import time
from _datetime import datetime
from testCases.conftest import setup
from selenium import webdriver
from pageObjects.loginPage import Login
from pageObjects.productPage import Product
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from selenium.common.exceptions import NoSuchElementException

class Test_login_DDT:
    baseURL = ReadConfig.get_URL()
    path = "/home/admin7/PycharmProjects/TI_AutomaTion/test_data/Login.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.sanityorregression
    def test_001_login_ddt(self):                  ############Always define a testcase function with its initials as "test"
        #lst_status = []
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows", self.rows)
        for row in range(3, self.rows+1):

            self.logger.info("Test_001_login_DDT ****************")
            self.driver = webdriver.Chrome(executable_path="/home/admin7/Downloads/chromedriver_linux64/chromedriver")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.lp = Login(self.driver)
            self.lp.clickHere()
            self.logger.info("************* Click here clicked ************")

                                ############ Data from Excel
            self.usermail = XLUtils.readData(self.path,"Sheet1",row,1)
            self.userpassword = XLUtils.readData(self.path, "Sheet1", row, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", row, 3)
            timestr = datetime.now().strftime("%d-%m-%Y--%I:%M %p")
            XLUtils.writeData(self.path, "Sheet1", row, 6, timestr)

            #self.new_data = XLUtils.writeData(self.path,"Sheet1",)
            self.lp.setUserName(self.usermail)
            time.sleep(2)
            txt = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/form/div[1]/span").text
            if(txt == "Email Id does not exist."):
                self.logger.info("============== Login Stopped, Email Id does not exist. =============")
                XLUtils.writeData(self.path, "Sheet1", row, 4, "Fail, Invalid Email")
            else:
                time.sleep(2)
                self.lp.setPassword(self.userpassword)
                self.lp.clickLoginDDT()
                time.sleep(2)
                try:
                    txt2 = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/form/div[1]/span").text
                    if (txt2 == "Sorry, There is some error. Please check your details or contact helpdesk"):
                        self.logger.info("============= Login Stopped, Incorrect Password. ============")
                        XLUtils.writeData(self.path, "Sheet1", row, 4, "Fail, Invalid Password")
                    else:
                        pass

                except NoSuchElementException:
                    self.logger.info("============== Login Successful. ==============")
                    if(self.exp == "Pass"):
                        XLUtils.writeData(self.path, "Sheet1", row, 4, "Pass, Identified User")
                        self.logger.info("************* Valid User from Database************")
                    else:
                        XLUtils.writeData(self.path, "Sheet1", row, 4, "Pass, Unidentified User")
                        self.logger.info("************* Invalid User, No History in Database************")


            self.actual = XLUtils.readData(self.path,"Sheet1",row,4)
            if(self.exp == "Pass" and "Pass" in self.actual):
                XLUtils.writeData(self.path, "Sheet1", row, 5, "PASS")
            elif(self.exp == "Fail" and "Fail" in self.actual):
                XLUtils.writeData(self.path, "Sheet1", row, 5, "PASS")
            else:
                XLUtils.writeData(self.path, "Sheet1", row, 5, "FAIL")

            time.sleep(1)
            self.driver.close()


        self.logger.info("=============== Test_001_login_DDT Completed ================")
