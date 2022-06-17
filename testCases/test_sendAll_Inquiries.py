import pytest
import os
from datetime import datetime
import time
from testCases.conftest import setup
from selenium import webdriver
from pageObjects.checkbox import check_box
from pageObjects.loginPage import Login
from pageObjects.sendEnquiry import Inquiry
from pageObjects.productPage import Product
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

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


    def test_All_Enquiries_Simultaneously(self, setup):       ###session starts here
        self.logger.info("Test_0012_MoreProductsFromThisSeller_Inquiry ************")
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

        '''try:
            self.driver.get(self.url1)             ###More Products from this seller
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_moreProductsFromThisSeller(self.url1)
            time.sleep(6)
            inq_type = "more_prod"
            enquiry_name = "TEST MORE PRODUCTS FROM THIS SELLER"
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            screenshot = check_box(self.driver)
            screenshot.take_screenshot(revertmsg,inq_type,enquiry_name)
        except NoSuchElementException or ElementNotInteractableException:
            inq_type = "more_prod"
            shot = check_box(self.driver)
            shot.take_shot(inq_type)
            time.sleep(2)
            self.logger.info(e)
            self.logger.info("!!!!!!!!!!!!!! THANK YOU BOX DID NOT APPEAR !!!!!!!!!!!!!!!")
            self.logger.info("!!!!!!!!!!!!!! EXCEPTION OCCURED, SCREENSHOT TAKEN !!!!!!!!!!!!!")

        try:
            self.driver.get(self.url2)               ###Red Button Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiryRED_button()
            time.sleep(2)
            self.itemInquiry.requirementPageSubmitButton(self.url2)
            time.sleep(2)
            self.itemInquiry.descriptionPage()
            self.logger.info("============= Description of product entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry()
            time.sleep(6)
            inq_type = "red_btn"
            enquiry_name = "TEST RED BUTTON ENQUIRY"
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            screenshot = check_box(self.driver)
            screenshot.take_screenshot(revertmsg, inq_type, enquiry_name)
        except NoSuchElementException or ElementNotInteractableException:
            inq_type = "red_btn"
            shot = check_box(self.driver)
            shot.take_shot(inq_type)
            time.sleep(2)
            self.logger.info(e)
            self.logger.info("!!!!!!!!!!!!!! THANK YOU BOX DID NOT APPEAR !!!!!!!!!!!!!!!")
            self.logger.info("!!!!!!!!!!!!!! EXCEPTION OCCURED, SCREENSHOT TAKEN !!!!!!!!!!!!!")


        try:
            self.driver.get(self.url3)           ###Contact Supplier Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_ContactSupplier()
            time.sleep(2)
            self.itemInquiry.requirementPageSubmitButton(self.url3)
            time.sleep(2)
            self.itemInquiry.descriptionPage()
            self.logger.info("============= Description of product entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry()
            time.sleep(6)
            inq_type = "contact_supp"
            enquiry_name = "TEST CONTACT SUPPLIER INQUIRY"
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            screenshot = check_box(self.driver)
            screenshot.take_screenshot(revertmsg, inq_type, enquiry_name)
        except NoSuchElementException or ElementNotInteractableException as e:
            inq_type = "contact_supp"
            shot = check_box(self.driver)
            shot.take_shot(inq_type)
            time.sleep(2)
            self.logger.info(e)
            self.logger.info("!!!!!!!!!!!!!! THANK YOU BOX DID NOT APPEAR !!!!!!!!!!!!!!!")
            self.logger.info("!!!!!!!!!!!!!! EXCEPTION OCCURED, SCREENSHOT TAKEN !!!!!!!!!!!!!")

        try:
            self.driver.get(self.url4)          ###Get Latest Price Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_GetLatestPrice()
            time.sleep(2)
            self.itemInquiry.requirementPageSubmitButton(self.url4)
            time.sleep(2)
            self.itemInquiry.descriptionPage()
            self.logger.info("============= Description of product entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry()
            time.sleep(6)
            inq_type = "get_latest"
            enquiry_name = "TEST GET LATEST PRICE INQUIRY"
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            screenshot = check_box(self.driver)
            screenshot.take_screenshot(revertmsg, inq_type, enquiry_name)
        except NoSuchElementException or ElementNotInteractableException as e:
            inq_type = "get_latest"
            shot = check_box(self.driver)
            shot.take_shot(inq_type)
            time.sleep(2)
            self.logger.info(e)
            self.logger.info("!!!!!!!!!!!!!! THANK YOU BOX DID NOT APPEAR !!!!!!!!!!!!!!!")
            self.logger.info("!!!!!!!!!!!!!! EXCEPTION OCCURED, SCREENSHOT TAKEN !!!!!!!!!!!!!")

        try:
            self.driver.get(self.url5)                 ###Yellow Box Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_YellowBox()
            time.sleep(4)
            self.itemInquiry.descriptionPage_YellowBox()
            self.logger.info("============= Description of product entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry_YellowBox()
            time.sleep(6)
            inq_type = "yellow_box"
            enquiry_name = "TEST YELLOW BOX INQUIRY"
            revertmsg = self.driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div/span").text
            screenshot = check_box(self.driver)
            screenshot.take_screenshot(revertmsg, inq_type, enquiry_name)
        except NoSuchElementException or ElementNotInteractableException as e:
            inq_type = "yellow_box"
            shot = check_box(self.driver)
            shot.take_shot(inq_type)
            time.sleep(2)
            self.logger.info(e)
            self.logger.info("!!!!!!!!!!!!!! THANK YOU BOX DID NOT APPEAR !!!!!!!!!!!!!!!")
            self.logger.info("!!!!!!!!!!!!!! EXCEPTION OCCURED, SCREENSHOT TAKEN !!!!!!!!!!!!!")

        try:
            self.driver.get(self.url6)           ###Post Buy Requirement Enquiry
            time.sleep(2)
            self.itemInquiry = Inquiry(self.driver)
            self.itemInquiry.sendEnquiry_PostBuyRequirement()
            time.sleep(2)
            self.itemInquiry.descriptionPage_PostBuyReq()
            self.logger.info("============= Description entered properly ============")
            time.sleep(2)
            self.itemInquiry.submitEnquiry_PostBuyReq()
            time.sleep(6)
            revertmsg = self.driver.find_element_by_xpath("//*[@id='rfq_popup_thanks_page']/div/div/div/div[2]").text
            inq_type = "post_buy"
            enquiry_name = "TEST POST BUY REQUIREMENT INQUIRY"
            screenshot = check_box(self.driver)
            screenshot.take_screenshot(revertmsg, inq_type, enquiry_name)
        except NoSuchElementException or ElementNotInteractableException as e:
            inq_type = "post_buy"
            shot = check_box(self.driver)
            shot.take_shot(inq_type)
            time.sleep(2)
            self.logger.info(e)
            self.logger.info("!!!!!!!!!!!!!! THANK YOU BOX DID NOT APPEAR !!!!!!!!!!!!!!!")
            self.logger.info("!!!!!!!!!!!!!! EXCEPTION OCCURED, SCREENSHOT TAKEN !!!!!!!!!!!!!")'''

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
            time.sleep(6)
            revertmsg = self.driver.find_element_by_xpath(" /html/body/main/div[5]/div/div/div[4]/div/div/div/div[2]").text
            inq_type = "compare_simi-"
            enquiry_name = "Test SendEnqBtn Compare Similar Products"
            self.screenshot = check_box(self.driver)
            self.screenshot.take_screenshot(revertmsg, inq_type, enquiry_name)
        except NoSuchElementException or ElementNotInteractableException as e:
            inq_type = "compare_simi"
            shot = check_box(self.driver)
            shot.take_shot(inq_type)
            time.sleep(2)
            self.logger.info(e)
            self.logger.info("!!!!!!!!!!!!!! THANK YOU BOX DID NOT APPEAR !!!!!!!!!!!!!!!")
            self.logger.info("!!!!!!!!!!!!!! EXCEPTION OCCURED, SCREENSHOT TAKEN !!!!!!!!!!!!!")

        #self.driver.close()
