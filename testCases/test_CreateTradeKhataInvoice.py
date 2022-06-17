import pytest
import time
import datetime
import random
from _datetime import datetime
from testCases.conftest import setup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pageObjects.loginPage import Login
from pageObjects.tradeKhataInvoice import Invoice
from pageObjects.sendEnquiry import Inquiry
from pageObjects.productPage import Product
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.common.exceptions import NoSuchElementException

class Test_TradeKhataInvoice:
    baseURL = ReadConfig.get_URL()
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()
    product_name = ReadConfig.get_product_redButton()
    user = ReadConfig.get_userid()

    logger = LogGen.loggen()

    @pytest.mark.invoice                    ############# TC marked as regression, marking is given when a specific TC should run only
    def test_008_CreateInvoice(self,setup):                  ############Always define a testcase function with its initials as "test"


        self.logger.info("Test_008_CreateInvoice ************")
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
            assert False

        '''self.driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/a[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='main-wrapper']/section/div[2]/div[1]/div[2]/a/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_name("invoice_no").clear()
        a = random.randrange(100000,999999)
        self.driver.find_element_by_name("invoice_no").send_keys(a)
        time.sleep(1)
        self.driver.find_element_by_name("invoice_due_date").send_keys("12/31/2022")
        element1 = self.driver.find_element_by_xpath("//*[text()='Billed To']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element1)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='s2id_customers-select']").click()
        self.driver.find_element_by_id("s2id_autogen2_search").send_keys(Keys.RETURN)
        self.driver.find_element_by_xpath("//*[@id='select2-chosen-3']").click()
        self.driver.find_element_by_id("s2id_autogen3_search").send_keys("Maha")
        self.driver.find_element_by_id("s2id_autogen3_search").send_keys(Keys.RETURN)
        self.driver.find_element_by_name("item_name_1").send_keys("MyTestProduct_XYZ")
        self.driver.find_element_by_name("hsn_sac_1").send_keys("321")
        self.driver.find_element_by_name("quantity_1").send_keys("10")
        self.driver.find_element_by_name("rate_1").send_keys("500")
        self.driver.find_element_by_name("gst_percentage_1").send_keys("2")
        time.sleep(2)
        element2 = self.driver.find_element_by_xpath("//*[text()='Terms and Conditions']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element2)
        time.sleep(2)
        self.driver.find_element_by_name("tnc").send_keys("Testing Only!!!!!!!!!!!!Testing Only!!!!!!!!!!!!Testing Only!!!!!!!!!!!!Testing Only!!!!!!!!!!!!Testing Only!!!!!!!!!!!!")
        self.driver.find_element_by_xpath("//*[@id='create_invoice']/div/div[11]/a/span[2]").click()
        self.driver.find_element_by_xpath("//*[@id='create_invoice']/div/div[11]/ul/li[2]/span[2]/textarea").send_keys("My Invoice!!!!My Invoice!!!!My Invoice!!!!My Invoice!!!!My Invoice!!!!")
        self.driver.find_element_by_xpath("//*[@id='create_invoice']/div/div[12]/a/span[2]").click()
        self.driver.find_element_by_name("additional_notes").send_keys("This is a testing description!!!!!!This is a testing description!!!!!!This is a testing description!!!!!!This is a testing description!!!!!!")
        self.driver.find_element_by_xpath("//*[@id='create_invoice']/div/div[13]/a/span[2]").click()
        self.driver.find_element_by_name("signature-file").send_keys("/home/admin7/PycharmProjects/TI_AutomaTion/test_data/sign.png")
        self.driver.find_element_by_name("inq_email").send_keys("testmailer@testing.com")
        self.driver.find_element_by_name("inq_mobile").send_keys("5544332211")
        self.driver.find_element_by_xpath("//*[@id='create_invoice']/div/div[15]/input").click()'''
        self.inv=Invoice(self.driver)
        self.inv.openTradeKhata()
        self.inv.InvoiceDetails()
        self.inv.createInvoice()
        time.sleep(3)
        successTest = self.driver.find_element_by_xpath("//*[@id='nofity']/div/div/div/div[2]/p").text
        if(successTest=="Invoice created successfully"):
            self.logger.info("============Invoice Created Successfully============")
            assert True
        else:
            timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
            self.driver.save_screenshot("./screenshots/" + "tradekhata_invoice-" + timestr + ".png")
            self.logger.error("=============Invoice not created, screenshot generated==============")
            self.driver.close()
            assert False

        self.inv.closeSuccessPopUp()
        self.inv.setPaymentOptions()
        #self.inv.autoReminder()         #################uncomment the line to enable auto-reminder for the invoice
        self.driver.close()
