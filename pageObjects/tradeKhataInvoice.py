from _datetime import datetime
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Invoice:
    TradeKhataButton_xpath="/html/body/header/div[4]/div/div[2]/a[2]"
    CreateNewInvoiceBtn_Xpath="//*[@id='main-wrapper']/section/div[2]/div[1]/div[2]/a/span[1]"
    invoiceNo_name="invoice_no"
    invoiceDueDate_name="invoice_due_date"
    billedTo_Box_xpath="//*[@id='s2id_customers-select']"
    billedTo_Enter_id="s2id_autogen2_search"
    stateCode_xpath="//*[@id='select2-chosen-3']"
    stateCode_Enter_id="s2id_autogen3_search"
    item_name="item_name_1"
    sac_name="hsn_sac_1"
    quantity_name="quantity_1"
    price_name="rate_1"
    gst_name="gst_percentage_1"
    terms_name="tnc"
    addTerms_xpath="//*[@id='create_invoice']/div/div[11]/a/span[2]"
    newTermBox_xpath="//*[@id='create_invoice']/div/div[11]/ul/li[2]/span[2]/textarea"
    addDescription_xpath="//*[@id='create_invoice']/div/div[12]/a/span[2]"
    additionalNotes_name="additional_notes"
    addSignBtn_xpath="//*[@id='create_invoice']/div/div[13]/a/span[2]"
    uploadSign_name="signature-file"
    enquiryEmail_name="inq_email"
    enquiryMobile_name="inq_mobile"



    def __init__(self, driver):
        self.driver = driver

    def openTradeKhata(self):
        self.driver.find_element_by_xpath(self.TradeKhataButton_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.CreateNewInvoiceBtn_Xpath).click()
        time.sleep(2)

    def InvoiceDetails(self):
        self.driver.find_element_by_name(self.invoiceNo_name).clear()
        a = random.randrange(100000, 999999)
        self.driver.find_element_by_name(self.invoiceNo_name).send_keys(a)
        time.sleep(1)
        self.driver.find_element_by_name(self.invoiceDueDate_name).send_keys("12/31/2022")
        element1 = self.driver.find_element_by_xpath("//*[text()='Billed To']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element1)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.billedTo_Box_xpath).click()
        self.driver.find_element_by_id(self.billedTo_Enter_id).send_keys(Keys.RETURN)
        self.driver.find_element_by_xpath(self.stateCode_xpath).click()
        self.driver.find_element_by_id(self.stateCode_Enter_id).send_keys("Maha")
        self.driver.find_element_by_id(self.stateCode_Enter_id).send_keys(Keys.RETURN)
        self.driver.find_element_by_name(self.item_name).send_keys("MyTestProduct_XYZ")
        self.driver.find_element_by_name(self.sac_name).send_keys("321")
        self.driver.find_element_by_name(self.quantity_name).send_keys("10")
        self.driver.find_element_by_name(self.price_name).send_keys("500")
        self.driver.find_element_by_name(self.gst_name).send_keys("2")
        time.sleep(2)
        element2 = self.driver.find_element_by_xpath("//*[text()='Terms and Conditions']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element2)
        time.sleep(2)
        timestr = datetime.now().strftime("%d-%m-%Y--%I:%M %p")
        term1=timestr+"--Testing Only!!!!!!!!!!!!Testing Only!!!!!!!!!!!!Testing Only!!!!!!!!!!!!Testing Only!!!!!!!!!!!!Testing Only!!!!!!!!!!!!"
        self.driver.find_element_by_name(self.terms_name).send_keys(term1)
        self.driver.find_element_by_xpath(self.addTerms_xpath).click()
        self.driver.find_element_by_xpath(self.newTermBox_xpath).send_keys("My Invoice!!!!My Invoice!!!!My Invoice!!!!My Invoice!!!!My Invoice!!!!")
        self.driver.find_element_by_xpath(self.addDescription_xpath).click()
        self.driver.find_element_by_name(self.additionalNotes_name).send_keys("This is a testing description!!!!!!This is a testing description!!!!!!This is a testing description!!!!!!This is a testing description!!!!!!")
        self.driver.find_element_by_xpath(self.addSignBtn_xpath).click()
        self.driver.find_element_by_name(self.uploadSign_name).send_keys("/home/admin7/PycharmProjects/TI_AutomaTion/test_data/sign.png")
        self.driver.find_element_by_name(self.enquiryEmail_name).send_keys("testmailer@testing.com")
        self.driver.find_element_by_name(self.enquiryMobile_name).send_keys("5544332211")
        time.sleep(2)

    def createInvoice(self):
        self.driver.find_element_by_xpath("//*[@id='create_invoice']/div/div[15]/input").click()
        time.sleep(2)

    def closeSuccessPopUp(self):
        self.driver.find_element_by_xpath("//*[@id='nofity']/div/div/div/div[1]/a").click()
        time.sleep(2)

    def setPaymentOptions(self):
        self.driver.find_element_by_xpath("//*[@id='main-wrapper']/section/div[2]/form/div/div/div/div[2]/div[3]/label/span").click()
        self.driver.find_element_by_xpath("//*[@id='main-wrapper']/section/div[2]/form/div/div/div/div[3]/div[3]/label/span").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_xpath("//*[@id='main-wrapper']/section/div[2]/form/div/div/div/div[4]/div[3]/label/span").click()
        self.driver.find_element_by_xpath("//*[@id='main-wrapper']/section/div[2]/form/div/div/div/div[5]/div[3]/label/span").click()
        time.sleep(2)
        self.driver.find_element_by_name("continue").click()
        time.sleep(2)

    def autoReminder(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_name("enableAutoReminder").click()
        frequency = self.driver.find_element_by_name("reminderFrequency")
        drp = Select(frequency)
        drp.select_by_index(2)
        self.driver.find_element_by_name("emailReminder").click()
        self.driver.find_element_by_name("whatsappReminder").click()
        self.driver.find_element_by_name("smsReminder").click()
        self.driver.find_element_by_xpath("//*[@id='autoReminder']/button").click()
        successTest = self.driver.find_element_by_xpath("//*[@id='nofity']/div/div/div/div[2]/p").text
        if (successTest == "Auto Reminder settings updated"):
            #self.logger.info("============Invoice Created Successfully============")
            assert True
        else:
            timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
            self.driver.save_screenshot("./screenshots/" + "tradekhata_invoice-" + timestr + ".png")
            #self.logger.error("=============Invoice not created, screenshot generated==============")
            # self.driver.close()
            assert False