import os
from _datetime import datetime
from utilities.customLogger import LogGen

class check_box:
    color_xpath = "//*[@id='usage1_29']"
    design_xpath = "//*[@id='usage1_1321']"
    form_xpath = "//*[@id='usage1_81']"
    logger = LogGen.loggen()

    def __init__(self,driver):
        self.driver = driver

    def select_check_box(self, url):
        if ("pots" in url):
            self.driver.find_element_by_xpath(self.color_xpath).click()
        elif("table" in url):
            self.driver.find_element_by_xpath(self.design_xpath).click()
        elif("bbeedd" in url):
            self.driver.find_element_by_xpath(self.design_xpath).click()
        elif("paint" in url):
            self.driver.find_element_by_xpath(self.form_xpath).click()
        else:
            pass

    def take_screenshot(self,message,type,enq_name):
        if (message == "Thank you" or message == "Thank You"):
            messageLog1 = "*************** "+enq_name+", PASSED *************"
            self.logger.info("=============Thank You Box Appeared, Inquiry Submitted ============")
            self.logger.info(messageLog1)
            assert True
        else:
            name = type
            # self.driver.close()
            date_folder = datetime.now().strftime("%d-%m-%Y")
            time_now = datetime.now().strftime("%I:%M:%p")
            new_path = os.path.join("./screenshots/", date_folder)
            try:
                os.mkdir(new_path)
            except FileExistsError:
                self.driver.save_screenshot(new_path + "/" + name + time_now + ".png")
            else:
                self.driver.save_screenshot(new_path + "/" + name + time_now + ".png")

            messageLog2 = "*************** " + enq_name + ", FAILED *************"
            self.logger.info("============= THANK YOU BOX DID NOT APPEAR, SCREENSHOT TAKEN ============")
            self.logger.info(messageLog2)
            assert False


    def take_shot(self,inq_type):
        date_folder = datetime.now().strftime("%d-%m-%Y")
        time_now = datetime.now().strftime("%I:%M:%p")
        new_path = os.path.join("./screenshots/", date_folder)
        try:
            os.mkdir(new_path)
        except FileExistsError:
            self.driver.save_screenshot(new_path + "/" + inq_type + time_now + ".png")
        else:
            self.driver.save_screenshot(new_path + "/" + inq_type + time_now + ".png")
