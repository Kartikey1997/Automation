from _datetime import datetime
from pageObjects.checkbox import check_box
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

class Inquiry:
    logger = LogGen.loggen()
    search_box_id="global_search"
    search_button_xpath="/html/body/main/div[2]/div[3]/div/form/button/span"
    click_product_xpath="/html/body/main/div/div[1]/div[5]/div[4]/form/div[2]/div[1]/div[1]/div[2]/div[1]/a"
    sendEnquiry_redButton_xpath="/html/body/main/div[2]/div/div[2]/div/div[4]/button"
    sendEnquiry_getLatestPrice_xpath="/html/body/main/div[2]/div/div[2]/div/div[2]/button"
    sendEnqBtn_CompareSimilarProducts_xpath="//*[@id='comparison_div']/div/div[2]/div[2]/div[7]/div[3]/button"
    sendEnqContactSupplierBtn_xpath="//button[@class='btn btn-yellow fs-16 wd-100']"
    moreProd_SendEnqBtn_xpath = "//div/div/div[1]/button[@class='btn btn-red']"

    sendEnqYellowBoxBtn_id="seller_inline_send_inq"
    describe_yellowbox_textbox_id="seller_inline_message"
    qty_id="main_quantity_descr"
    unit_id="main_units"
    value_id="main_order_value_inr"
    location_id="main_pref_supp_location"
    urgency_id="main_buying_need"
    regular_xpath="/html/body/div[1]/div/div/div/div/div/form/div/div/div/div[6]/span[2]/label"
    submit_yellowbox_id="main_submit"

    describe_req_textbox_id="sp_popup_message"
    requirementPage_sendEnquiry_button_id="sp_popup_send_inq"
    nextButton_name="send_inq"
    quantity_id="sp_popup_quantity_descr"
    selectUnit_id="sp_popup_units"
    orderValue_id="sp_popup_order_value_inr"
    supplierLoc_id="sp_popup_pref_supp_location"
    reqmentUrgency_id="sp_popup_buying_need"
    radioBtnRegular_xpath="/html/body/main/div[5]/div/div/div[3]/div/div/form/div/div/div/div[6]/span[2]/label"

    postBuyReqBtn_xpath = "/html/body/header/div/div/div[2]/a[1]"           #####Post Buy Requirement Elements######
    product_name_id = "rfq_popup_subject"
    describe_id = "rfq_popup_description"
    qnty_id = "rfq_popup_quantity_descr_home"
    setUnits_id = "rfq_popup_units_home"
    order_val_id = "rfq_popup_order_value_inr_home"
    postBuyReqSubmitBtn_id = "rfq_popup_inq_submit"
    get_location_id = "rfq_popup_pref_supp_location"
    get_urgency_id = "rfq_popup_buying_need"
    get_radioBtn_Regular_id = "//*[@id='rfq_popup_rfi_extra_detail_form']/div/div/div/div[6]/span[2]/label"
    submitBtn_id = "rfq_popup_submit_rfi"

    submit_id="sp_popup_submit"
    submit_id2="sp_popup_submit_rfi"

    timestr = datetime.now().strftime("%d-%m-%Y--%I:%M %p")
    description_RedButton = "!!!!!!!!!!!!!!!!!!!! This is an auto-generated testing enquiry from TradeIndia Development Team. DO NOT REVERT BACK.Server:-Live, Send Enquiry Red Button, Timestamp:-" + timestr + "!!!!!!!!!!!!!!!!!"
    description_GetLatestPrice = "!!!!!!!!!!!!!!!!!!!! This is an auto-generated testing enquiry from TradeIndia Development Team. DO NOT REVERT BACK.Server:-Live, Send Enquiry Get Latest Price, Timestamp:-" + timestr + "!!!!!!!!!!!!!!!!!"
    description_SendEnqBtn_CompareProduct = "!!!!!!!!!!!!!!!!!!!! This is an auto-generated testing enquiry from TradeIndia Development Team. DO NOT REVERT BACK.Server:-Live, Send Enquiry Button Compare With Similar Products, Timestamp:-" + timestr + "!!!!!!!!!!!!!!!!!"
    description_ContactSupplier = "!!!!!!!!!!!!!!!!!!!! This is an auto-generated testing enquiry from TradeIndia Development Team. DO NOT REVERT BACK.Server:-Live, Send Enquiry Contact Supplier, Timestamp:-" + timestr + "!!!!!!!!!!!!!!!!!"
    description_YellowBox = "!!!!!!!!!!!!!!!!!!!! This is an auto-generated testing enquiry from TradeIndia Development Team. DO NOT REVERT BACK.Server:-Live, Send Enquiry to Supplier Yellow Box, Timestamp:-" + timestr + "!!!!!!!!!!!!!****"
    description_PostBuyReq = "!!!!!!!!!!!!!!!!!!!! This is an auto-generated testing enquiry from TradeIndia Development Team. DO NOT REVERT BACK.Server:-Live, Send Enquiry Post Buy Requirement, Timestamp:-" + timestr + "!!!!!!!!!!!!!!!!!"
    description_MoreProducts = "!!!!!!!!!!!!!!!!!!!! This is an auto-generated testing enquiry from TradeIndia Development Team. DO NOT REVERT BACK.Server:-Live, Send Enquiry More Products From This Seller, Timestamp:-" + timestr + "!!!!!!!!!!!!!!!!!"

    def __init__(self,driver):
        self.driver=driver

    def productsearch(self,item):
        self.driver.find_element_by_id(self.search_box_id).send_keys(item)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.click_product_xpath).click()

    def sendEnquiryRED_button(self):
        self.driver.find_element_by_xpath(self.sendEnquiry_redButton_xpath).click()
        self.logger.info("============== Send Enquiry Red Button Clicked =============")
        time.sleep(2)
        self.driver.find_element_by_id(self.describe_req_textbox_id).send_keys(self.description_RedButton)
        self.logger.info("============== Text Data Entered =============")

    def sendEnquiry_GetLatestPrice(self):
        self.driver.find_element_by_xpath(self.sendEnquiry_getLatestPrice_xpath).click()
        self.logger.info("============== Send Enquiry Get Latest Price Link Clicked =============")
        time.sleep(2)
        self.driver.find_element_by_id(self.describe_req_textbox_id).send_keys(self.description_GetLatestPrice)
        self.logger.info("============== Text Data Entered =============")

    def sendEnqBtn_CompareSimilarProducts(self):
        # time.sleep(4)
        # '''element = self.driver.find_element_by_xpath(self.sendEnqBtn_CompareSimilarProducts_xpath)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).click().perform()'''
        # element = self.driver.find_element_by_xpath("//*[text()='Compare With Similar Products']")
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(2)
        #self.driver.execute_script("window.scroll(0,4000);")
        i = 1
        while True:
            val = str(i)
            path = "//*[@id='comparison_div']/div/div[2]/div[2]/div["+val+"]/div[3]/button"
            try:
                a = self.driver.find_element_by_xpath(path).click()
                if(a is None):         ########## "a" will onle be None when element is found
                    break
            except NoSuchElementException:
                pass
            i += 1

        self.logger.info("============== Send Enquiry Compare Similar Clicked =============")
        time.sleep(4)
        self.driver.find_element_by_id(self.describe_req_textbox_id).send_keys(self.description_SendEnqBtn_CompareProduct)
        self.logger.info("============== Text Data Entered =============")
        time.sleep(2)
        self.driver.find_element_by_id(self.requirementPage_sendEnquiry_button_id).click()
        self.logger.info("============== Send Enquiry Button Clicked After Data is Entered =============")

    def sendEnquiry_ContactSupplier(self):
        self.driver.find_element_by_xpath(self.sendEnqContactSupplierBtn_xpath).click()
        self.logger.info("============== Send Enquiry Contact Supplier Clicked =============")
        time.sleep(2)
        self.driver.find_element_by_id(self.describe_req_textbox_id).send_keys(self.description_ContactSupplier)
        self.logger.info("============== Text Data Entered =============")

    def sendEnquiry_YellowBox(self):
        self.driver.execute_script("window.scroll(0, 1500);")
        self.logger.info("============== Page Scrolled till Yellow Enquiry Box Found =============")
        time.sleep(2)
        self.driver.find_element_by_id(self.describe_yellowbox_textbox_id).send_keys(self.description_YellowBox)
        self.logger.info("============== Text Data Entered =============")
        time.sleep(2)
        self.driver.find_element_by_id(self.sendEnqYellowBoxBtn_id).click()
        self.logger.info("============== Send Enquiry Yellow Box Button Clicked =============")

    def sendEnquiry_PostBuyRequirement(self):
        self.driver.find_element_by_xpath(self.postBuyReqBtn_xpath).click()
        self.logger.info("============== Send Enquiry Post Buy Requirement Clicked =============")

    def requirementPageSubmitButton(self,URL):
        time.sleep(2)
        self.driver.find_element_by_id(self.requirementPage_sendEnquiry_button_id).click()
        self.logger.info("============== Send Enquiry Submit Button Clicked =============")
        time.sleep(5)
        self.box = check_box(self.driver)
        self.box.select_check_box(URL)
        self.logger.info("============== Product CheckBox Clicked =============")
        time.sleep(2)
        self.driver.find_element_by_name(self.nextButton_name).click()
        self.logger.info("============== Next Button Clicked After CheckBox Selected =============")

    def descriptionPage(self):
        self.driver.find_element_by_id(self.quantity_id).send_keys(555)
        self.logger.info("============== Quantity Passed =============")
        element_unit = self.driver.find_element_by_id(self.selectUnit_id)
        drp = Select(element_unit)
        drp.select_by_index(5)
        self.logger.info("============== Desired Unit Selected =============")
        element_orderValue = self.driver.find_element_by_id(self.orderValue_id)
        drp = Select(element_orderValue)
        drp.select_by_index(3)
        self.logger.info("============== Desired Order Value Selected =============")
        element_location = self.driver.find_element_by_id(self.supplierLoc_id)
        drp = Select(element_location)
        drp.select_by_index(1)
        self.logger.info("============== Desired Supplier Location Passed =============")
        element_urgency = self.driver.find_element_by_id(self.reqmentUrgency_id)
        drp = Select(element_urgency)
        drp.select_by_index(1)
        self.logger.info("============== Desired Urgency Selected =============")
        self.driver.find_element_by_xpath(self.radioBtnRegular_xpath).click()
        self.logger.info("============== Regular Radio Button Selected =============")

    def descriptionPage_YellowBox(self):
        self.driver.find_element_by_id(self.qty_id).send_keys(333)
        self.logger.info("============== Desired Quantity Passed =============")
        element_unit = self.driver.find_element_by_id(self.unit_id)
        drp = Select(element_unit)
        drp.select_by_index(5)
        self.logger.info("============== Desired Units Selected =============")
        element_orderValue = self.driver.find_element_by_id(self.value_id)
        drp = Select(element_orderValue)
        drp.select_by_index(3)
        self.logger.info("============== Desired Order Value Selected =============")
        element_location = self.driver.find_element_by_id(self.location_id)
        drp = Select(element_location)
        drp.select_by_index(1)
        self.logger.info("============== Desired Supplier Location Passed =============")
        element_urgency = self.driver.find_element_by_id(self.urgency_id)
        drp = Select(element_urgency)
        drp.select_by_index(1)
        self.logger.info("============== Desired Urgency Selected =============")
        self.driver.find_element_by_xpath(self.regular_xpath).click()
        self.logger.info("============== Regular Radio Button Selected =============")

    def descriptionPage_PostBuyReq(self):
        self.driver.find_element_by_id(self.product_name_id).send_keys("Testing Product")
        self.logger.info("============== Text Data Entered =============")
        self.driver.find_element_by_id(self.describe_id).send_keys(self.description_PostBuyReq)
        self.logger.info("============== Description Text Entered =============")
        self.driver.find_element_by_id(self.qnty_id).send_keys(111)
        self.logger.info("============== Desired Quantity Selected =============")
        ele_unit = self.driver.find_element_by_id(self.setUnits_id)
        drp = Select(ele_unit)
        drp.select_by_index(5)
        self.logger.info("============== Desired Units Selected =============")
        ele_value = self.driver.find_element_by_id(self.order_val_id)
        drp = Select(ele_value)
        drp.select_by_index(4)
        self.logger.info("============== Desired Order Value Selected=============")
        time.sleep(5)
        self.driver.find_element_by_id(self.postBuyReqSubmitBtn_id).click()
        self.logger.info("============== Post Buy Requirement Submit Button Clicked =============")
        time.sleep(2)
        ele_location = self.driver.find_element_by_id(self.get_location_id)
        drp = Select(ele_location)
        drp.select_by_index(1)
        self.logger.info("============== Desired Supplier Location Selected =============")
        ele_urgency = self.driver.find_element_by_id(self.get_urgency_id)
        drp = Select(ele_urgency)
        drp.select_by_index(1)
        self.logger.info("============== Desired Urgency Selected =============")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.get_radioBtn_Regular_id).click()
        self.logger.info("============== Regular Radio Button Selected =============")

    def sendEnquiry_moreProductsFromThisSeller(self,URL):
        element = self.driver.find_element_by_xpath("//h3[@class='prime-heading d-block']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.logger.info("============== Page Scrolled till More Products Found =============")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.moreProd_SendEnqBtn_xpath).click()
        self.logger.info("============== More Product Send Enquiry Button Clicked =============")
        time.sleep(2)
        self.driver.find_element_by_id(self.describe_req_textbox_id).send_keys(self.description_MoreProducts)
        self.logger.info("============== Description Data Entered =============")
        time.sleep(2)
        self.driver.find_element_by_id(self.requirementPage_sendEnquiry_button_id).click()
        self.logger.info("============== Send Button CLicked After Data is Entered =============")
        time.sleep(5)
        self.box = check_box(self.driver)
        self.box.select_check_box(URL)
        self.logger.info("============== Desired CheckBox Selected =============")
        time.sleep(2)
        self.driver.find_element_by_name(self.nextButton_name).click()
        self.logger.info("============== Next Button Clicked =============")
        time.sleep(2)
        self.descriptionPage()
        time.sleep(2)
        self.driver.find_element_by_id("sp_popup_submit").click()
        self.logger.info("============== Final Submit Button Clicked =============")

    def submitEnquiry(self):
        self.driver.find_element_by_id(self.submit_id).click()
        self.logger.info("============== Final Submit Button Clicked =============")

    def submitEnquiryCompare(self):
        self.driver.find_element_by_id(self.submit_id2).click()
        self.logger.info("============== Final Submit Button Clicked =============")

    def submitEnquiry_YellowBox(self):
        self.driver.find_element_by_id(self.submit_yellowbox_id).click()
        self.logger.info("============== Final Submit Button Clicked =============")

    def submitEnquiry_PostBuyReq(self):
        self.driver.find_element_by_id(self.submitBtn_id).click()
        self.logger.info("============== Final Submit Button Clicked =============")