import os
import time
from _datetime import datetime
from selenium.webdriver.support.ui import Select

class Buy:
    location_id = "user_location"
    search_box_id = "global_search"
    search_button_xpath = "/html/body/main/div[2]/div[3]/div/form/button/span"
    #click_product_xpath = "/html/body/main/div/div[1]/div[5]/div[4]/form/div[2]/div[1]/div[1]/div[2]/div[1]/a"
    click_product_xpath = "//img[@class='product-img-size']"
    shop_online_btn_xpath = "//*[@id='listing_left_filter_frm']/div/div[2]/div/label/span"
    buyNow_btn_id = "buy_now"

    def __init__(self,driver):
        self.driver=driver

    def productSearchForCart(self,item):
        self.driver.find_element_by_id("user_location").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='cities_list']/li[1]/i").click()
        time.sleep(2)
        self.driver.find_element_by_id(self.search_box_id).send_keys(item)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.shop_online_btn_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.click_product_xpath).click()

    def slab(self):
        self.driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/div/div[1]/div/ul/li[1]").click()
        a = self.driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/div/div[1]/div/ul/li[1]").text
        return a

    def addToCart(self):
        self.driver.find_element_by_id(self.buyNow_btn_id).click()
        time.sleep(4)
        a=self.driver.title
        print(a)

        '''a=self.driver.find_element_by_xpath("//*[@id='app-root']/app-root/div/div/app-cart/div/div[2]/div/div/h2").text
        print(a)
        if("My Cart" in a):
            assert True
        else:
            date_folder = datetime.now().strftime("%d-%m-%Y")
            time_now = datetime.now().strftime("%I:%M:%p")
            new_path = os.path.join("./screenshots/", date_folder)
            try:
                os.mkdir(new_path)
            except FileExistsError:
                self.driver.save_screenshot(new_path + "/" + "cart" + time_now + ".png")
            else:
                self.driver.save_screenshot(new_path + "/" + "cart" + time_now + ".png")'''