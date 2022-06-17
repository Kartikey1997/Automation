import random
import time
from _datetime import datetime
from pageObjects.checkbox import check_box
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class city:
    logger = LogGen.loggen()
    base_urls_orig = ["https://orig-www.tradeindia.com/Seller/Agriculture/Fresh-Vegetables/","https://orig-www.tradeindia.com/Seller/Food-Beverage/Spices-Seasonings/","https://orig-www.tradeindia.com/Seller/Food-Beverage/Frozen-Dried-Fruit/","https://orig-www.tradeindia.com/Seller/Office-School-Supplies/Stationery-Items/","https://orig-www.tradeindia.com/Seller/Computer-Hardware-Software/Data-Storage-Devices/","https://orig-www.tradeindia.com/Seller/Electronics-Electrical-Supplies/LED-Products/","https://orig-www.tradeindia.com/Seller/Home-Textiles-Furnishings/Carpets/","https://orig-www.tradeindia.com/Seller/Jewelry-Gemstones/Silver-Sterling-Silver-Jewelry/"]
    base_urls_beta = ["https://beta-stag.tradeindia.com/Seller/Agriculture/Fresh-Vegetables/","https://beta-stag.tradeindia.com/Seller/Food-Beverage/Spices-Seasonings/","https://beta-stag.tradeindia.com/Seller/Food-Beverage/Frozen-Dried-Fruit/","https://beta-stag.tradeindia.com/Seller/Office-School-Supplies/Stationery-Items/","https://beta-stag.tradeindia.com/Seller/Computer-Hardware-Software/Data-Storage-Devices/","https://beta-stag.tradeindia.com/Seller/Electronics-Electrical-Supplies/LED-Products/","https://beta-stag.tradeindia.com/Seller/Home-Textiles-Furnishings/Carpets/","https://beta-stag.tradeindia.com/Seller/Jewelry-Gemstones/Silver-Sterling-Silver-Jewelry/"]
    soloing_xpath1 = "//*[text()='Spring Onion' or text()='Turmeric' or text()='Dried Fruits' or text()='Promotional Playing Cards' or text()='Dvd Ram' or text()='Led Torch Light' or text()='Silk Carpet' or text()='Silver Rings']"
    soloing_xpath2 = "//*[text()='Red Onion' or text()='Ground Spices' or text()='Dried Plum' or text()='Promotional Diaries' or text()='Used Ram' or text()='Led Rope Light' or text()='Designer Carpet' or text()='Silver Necklaces']"
    allResult_xpath = "//*[text()='All Results']"

    def __init__(self,driver):
        self.driver = driver

    def select_city(self):
        a = self.driver.find_element_by_xpath("/html/body/main/div[2]/div[3]/div[2]/div").text
        cities_list = a.split("\n")
        cities_list.remove('All Results')
        cities_list.reverse()
        i = random.randrange(0,len(cities_list))
        city_xpath = "//*[text()='"+cities_list[i]+"']"
        return city_xpath

    def select_url(self):
        urls_list = self.base_urls_beta
        urls_list.reverse()
        j = random.randrange(0, len(urls_list))
        return urls_list[j]

    def manufacturer(self):
        self.logger.info("------------- TESTING FOR MANUFACTURER CITY PAGES -------------")
        url = self.select_url()
        self.driver.get(url)
        self.driver.maximize_window()
        self.logger.info("========== URL opened window maximized ==========")
        time.sleep(2)
        self.driver.execute_script("alert('Testing Now For MANUFACTURER City Pages');")
        time.sleep(2)
        self.logger.info("========== Alert Appeared ==========")
        self.driver.switch_to_alert().accept()
        self.logger.info("========== Alert Accepted ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.soloing_xpath1).click()
        self.logger.info("========== Soloing Button Selected ==========")
        time.sleep(2)
        city1= self.select_city()
        self.driver.find_element_by_xpath(city1).click()
        time.sleep(2)
        self.logger.info("========== City Selected from filter ==========")
        city2 = self.select_city()
        self.driver.find_element_by_xpath(city2).click()
        self.logger.info("========== City selected from filter ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Result selected ==========")
        time.sleep(2)

        url = self.select_url()
        self.driver.get(url)
        self.logger.info("========== New URL opened ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.soloing_xpath2).click()
        self.logger.info("========== Soloing Button Selected ==========")
        time.sleep(2)
        city3 = self.select_city()
        self.driver.find_element_by_xpath(city3).click()
        self.logger.info("========== City Selected from filter ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Results selected ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Results selected ==========")
        time.sleep(2)

        url = self.select_url()
        self.driver.get(url)
        self.logger.info("========== New URL opened ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.soloing_xpath1).click()
        self.logger.info("========== Soloing Button selected ==========")
        time.sleep(2)
        city1 = self.select_city()
        self.driver.find_element_by_xpath(city1).click()
        self.logger.info("========== City Selected from filter ==========")
        time.sleep(2)
        city2 = self.select_city()
        self.driver.find_element_by_xpath(city2).click()
        self.logger.info("========== City Selected from filter ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Results selected ==========")
        time.sleep(2)


        url2 = self.select_url()
        self.driver.get(url2)
        self.logger.info("========== New URL opened ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.soloing_xpath2).click()
        self.logger.info("========== Soloing Button Selected ==========")
        time.sleep(2)
        city3 = self.select_city()
        self.driver.find_element_by_xpath(city3).click()
        self.logger.info("========== City Selected from filters ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Results selected ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Results selected ==========")
        time.sleep(2)

    def seller(self):
        self.logger.info("------------TESTING FOR SELLER CITY PAGES-------------")
        url = self.select_url()
        self.driver.get(url)
        self.driver.maximize_window()
        self.logger.info("========== New URL opened ==========")
        time.sleep(2)
        self.driver.execute_script("alert('Testing Now For SELLER City Pages');")
        self.logger.info("========== Alert Appeared ==========")
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        self.logger.info("========== Alert Accepted ==========")
        time.sleep(2)
        city1 = self.select_city()
        self.driver.find_element_by_xpath(city1).click()
        self.logger.info("========== City Selected from filter ==========")
        time.sleep(2)
        city2 = self.select_city()
        self.driver.find_element_by_xpath(city2).click()
        self.logger.info("========== City Selected from filter  ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Result selected  ==========")
        time.sleep(2)

        url = self.select_url()
        self.driver.get(url)
        self.logger.info("========== New URL opened ==========")
        time.sleep(2)
        city3 = self.select_city()
        self.driver.find_element_by_xpath(city3).click()
        self.logger.info("========== City Selected from filter ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Result selected ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Result selected ==========")
        time.sleep(2)
        city3 = self.select_city()
        self.driver.find_element_by_xpath(city3).click()
        self.logger.info("========== City Selected from filter ==========")
        time.sleep(2)

        url = self.select_url()
        self.driver.get(url)
        self.logger.info("========== New URL opened ==========")
        time.sleep(2)
        city1 = self.select_city()
        self.driver.find_element_by_xpath(city1).click()
        self.logger.info("========== City Selected from filter ==========")
        time.sleep(2)
        city2 = self.select_city()
        self.driver.find_element_by_xpath(city2).click()
        self.logger.info("========== City Selected from filter ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Result selected ==========")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.allResult_xpath).click()
        self.logger.info("========== All Result selected ==========")
        time.sleep(2)
        city3 = self.select_city()
        self.driver.find_element_by_xpath(city3).click()
        self.logger.info("========== City Selected from filter ==========")
