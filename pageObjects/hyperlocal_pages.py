import time
from selenium.webdriver.common.action_chains import ActionChains
from utilities import XLUtils
import random

class Hyperlocal:
    path="/home/admin7/PycharmProjects/TI_AutomaTion/test_data/Login.xlsx"
    sheet="Sheet2"

    def __init__(self,driver):
        self.driver=driver

    def get_cityPage_url(self):
        row=random.randrange(2,51)
        get_row_count=XLUtils.getRowCount(self.path,self.sheet)
        url=XLUtils.readData(self.path,self.sheet,row,1)
        self.driver.get(url)
        time.sleep(2)
        self.driver.maximize_window()

    def get_nearby_section(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath("//*[@id='main_divss']/div[3]/div[1]/div/span")
        action.move_to_element(element).click().perform()
        text=self.driver.find_element_by_xpath("//*[@id='main_divss']/div[3]").text
        list=text.split('\n')
        list_len=len(list)-1
        index=random.randrange(1,list_len)
        self.driver.find_element_by_link_text(list[index]).click()
