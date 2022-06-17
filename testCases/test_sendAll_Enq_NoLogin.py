import pytest
import time
from _datetime import datetime
from testCases.conftest import setup
from selenium import webdriver
from pageObjects.loginPage import Login
from pageObjects.sendEnquiryNoLogin import Inquiry
from pageObjects.productPage import Product
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.common.exceptions import NoSuchElementException

class Test_All_Enquiry:
    baseURL = ReadConfig.get_URL()
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()
    product_name = ReadConfig.get_product_MoreProducts()
    user = ReadConfig.get_userid()
    url1 = ReadConfig.get_productURL_MoreProducts()
    url2 = ReadConfig.get_productURL_redButton()
    url3 = ReadConfig.get_productURL_ContactSupplier()
    url4 = ReadConfig.get_productURL_getLatestPrice()
    url5 = ReadConfig.get_productURL_YellowBox()
    url6 = ReadConfig.get_productURL_PostBuyReq()
    url7 = ReadConfig.get_productURL_CompareSimilar()
    logger = LogGen.loggen()

    def test_All_Enquiries_Simultaneously(self,setup):       ###session starts here
        self.logger.info("Test_0012_MoreProductsFromThisSeller_Inquiry ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("************* URL Obtained Properly ************")
        self.driver.maximize_window()
        self.logger.info("************* Window maximized ************")

        try:
            self.driver.get(self.url1)             ###More Products from this seller
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_moreProductsFromThisSeller(self.url1)
            time.sleep(2)
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            if (revertmsg == "Thank you"):
                self.logger.info("=============Thank You Page Appeared, Inquiry Submitted ============")
                self.logger.info("************** TEST MORE PRODUCTS FROM THIS SELLER, PASSED ============")
                assert True
            else:
                self.logger.info("============= More Products From This Seller not Submitted, screenshot generated ============")
                self.logger.info("************** Test_0012_MoreProductsFromThisSeller_Inquiry, FAILED **************")
                timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
                self.driver.save_screenshot("./screenshots/" + "test_sendInquiry-" + timestr + ".png")
                self.driver.close()
                assert False
        except NoSuchElementException:
            pass

        try:
            self.driver.get(self.url2)               ###Red Button Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiryRED_button()
            self.logger.info("============= Send Inquiry Red Button Clicked ============")
            time.sleep(2)
            self.itemInquiry.requirementPageSubmitButton(self.url2)
            self.logger.info("============= Requirement Page Submit Button Pressed  ============")
            time.sleep(2)
            self.itemInquiry.descriptionPage()
            self.logger.info("============= Description of product entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry()
            self.logger.info("============= Final Enquiry Submit Button Pressed ============")
            time.sleep(2)
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            if (revertmsg == "Thank you"):
                self.logger.info("=============Thank You Page Appeared, Inquiry Submitted ============")
                self.logger.info("**************** TEST RED BUTTON ENQUIRY, PASSED **************")
                assert True
            else:
                self.logger.info("============= Red Button Inquiry not Submitted, screenshot generated ============")
                self.logger.info("************* Test_RED_ButtonInquiry, FAILED ***************")
                timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
                self.driver.save_screenshot("./screenshots/" + "test_sendInquiry-" + timestr + ".png")
                self.driver.close()
                assert False
        except NoSuchElementException:
            pass

        try:
            self.driver.get(self.url3)           ###Contact Supplier Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_ContactSupplier()
            self.logger.info("============= Send Inquiry Contact Supplier Button Clicked ============")
            time.sleep(2)
            self.itemInquiry.requirementPageSubmitButton(self.url3)
            self.logger.info("============= Requirement Page Submit Button Pressed  ============")
            time.sleep(2)
            self.itemInquiry.descriptionPage()
            self.logger.info("============= Description of product entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry()
            self.logger.info("============= Final Enquiry Submit Button Pressed ============")
            time.sleep(2)
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            if (revertmsg == "Thank you"):
                self.logger.info("=============Thank You Page Appeared, Inquiry Submitted ============")
                self.logger.info("************* TEST CONTACT SUPPLIER INQUIRY, PASSED *************")
                assert True
            else:
                self.logger.info("============= Contact Supplier Inquiry not Submitted, screenshot generated ============")
                self.logger.info("************** Test_ContactSupplier_Inquiry, FAILED *************")
                timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
                self.driver.save_screenshot("./screenshots/" + "test_sendInquiry-" + timestr + ".png")
                self.driver.close()
                assert False
        except NoSuchElementException:
            pass

        try:
            self.driver.get(self.url4)          ###Get Latest Price Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_GetLatestPrice()
            self.logger.info("============= Send Inquiry Get Latest Price Link Clicked ============")
            time.sleep(2)
            self.itemInquiry.requirementPageSubmitButton(self.url4)
            self.logger.info("============= Requirement Page Submit Button Pressed  ============")
            time.sleep(2)
            self.itemInquiry.descriptionPage()
            self.logger.info("============= Description of product entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry()
            self.logger.info("============= Final Enquiry Submit Button Pressed ============")
            time.sleep(2)
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            if (revertmsg == "Thank you"):
                self.logger.info("=============Thank You Page Appeared, Inquiry Submitted ============")
                self.logger.info("************* TEST GET LATEST PRICE INQUIRY, PASSED *************")
                assert True
            else:
                self.logger.info("============= Get Latest Price Inquiry not Submitted, screenshot generated ============")
                self.logger.info("************* Test_GetLatestPrice_Inquiry, FAILED *************")
                timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
                self.driver.save_screenshot("./screenshots/" + "test_sendInquiry-" + timestr + ".png")
                self.driver.close()
                assert False
        except NoSuchElementException:
            pass

        try:
            self.driver.get(self.url5)                 ###Yellow Box Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_YellowBox()
            self.logger.info(
                "=============Product Page Scrolled and Send Inquiry In Yellow Box Button Clicked ============")
            time.sleep(2)
            self.itemInquiry.descriptionPage_YellowBox()
            self.logger.info("============= Description of product entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry_YellowBox()
            self.logger.info("============= Final Enquiry Submit Button Pressed ============")
            time.sleep(2)
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            if (revertmsg == "Thank you"):
                self.logger.info("=============Thank You Page Appeared, Inquiry Submitted ============")
                self.logger.info("************* TEST YELLOW BOX INQUIRY, PASSED *************")
                assert True
            else:
                self.logger.info("============= Yellow Box Inquiry not Submitted, screenshot generated ============")
                self.logger.info("************* Test_YellowBox_Inquiry, FAILED *************")
                timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
                self.driver.save_screenshot("./screenshots/" + "test_sendInquiry-" + timestr + ".png")
                self.driver.close()
                assert False
        except NoSuchElementException:
            pass

        try:
            self.driver.get(self.url6)           ###Post Buy Requirement Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_PostBuyRequirement()
            self.logger.info("============= Post Buy Requirement Button Clicked ============")
            time.sleep(2)
            self.itemInquiry.descriptionPage_PostBuyReq()
            self.logger.info("============= Description entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry_PostBuyReq()
            self.logger.info("============= Post Buy Requirement Submit Button Pressed ============")
            time.sleep(2)
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[6]/div/div/div/div[2]").text
            if (revertmsg == "Thank You"):
                self.logger.info("=============Thank You Page Appeared,Post Buy Requirement Inquiry Submitted ============")
                self.logger.info("************* TEST POST BUY REQUIREMENT INQUIRY, PASSED *************")
                assert True
            else:
                self.logger.info("============= Post Buy Requirement Inquiry not Submitted, screenshot generated ============")
                self.logger.info("************* Test_Post_Buy_RequirementInquiry, FAILED *************")
                timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
                self.driver.save_screenshot("./screenshots/" + "test_sendInquiry-" + timestr + ".png")
                self.driver.close()
                assert False
        except NoSuchElementException:
            pass

        try:
            self.driver.get(self.url7)           ###Compare Similar Products Enquiry
            time.sleep(4)
            try:
                element1 = self.driver.find_element_by_xpath("//*[text()='Compare With Similar Products']")
                self.driver.execute_script("arguments[0].scrollIntoView();", element1)
                time.sleep(2)
            except NoSuchElementException:
                self.driver.get(self.url3)      ###Contact Supplier URL fetched(BBEEEDD) since element not found in above URL
                time.sleep(4)
                element2 = self.driver.find_element_by_xpath("//*[text()='Compare With Similar Products']")
                self.driver.execute_script("arguments[0].scrollIntoView();", element2)
                time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnqBtn_CompareSimilarProducts()
            self.logger.info("============= Page scrolled to Compare Similar Product Section, Send Inquiry Button Clicked ============")
            time.sleep(6)
            self.itemInquiry.descriptionPage()
            self.logger.info("============= Description of product entered properly ============")
            time.sleep(4)
            self.itemInquiry.submitEnquiryCompare()
            self.logger.info("============= Final Enquiry Submit Button Pressed ============")
            time.sleep(2)
            revertmsg = self.driver.find_element_by_xpath(" /html/body/main/div[5]/div/div/div[4]/div/div/div/div[2]").text
            if (revertmsg == "Thank You"):
                self.logger.info("=============Thank You Box Appeared, Inquiry Submitted ============")
                self.logger.info("************* TEST COMPARE SIMILAR PRODUCTS INQUIRY, PASSED *************")
                assert True
            else:
                self.logger.info("============= Inquiry from Compare with Similar Products not Submitted, screenshot generated ============")
                self.logger.info("************* Test_SendEnqBtn_CompareSimilarProducts, FAILED *************")
                timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
                self.driver.save_screenshot("./screenshots/" + "test_sendInquiry-" + timestr + ".png")
                self.driver.close()
                assert False
        except NoSuchElementException:
            pass

        self.driver.close()

