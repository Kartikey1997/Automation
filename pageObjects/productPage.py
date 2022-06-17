from selenium import webdriver
class Product:
    searchbox_id="global_search"
    searchButton_xpath="/html/body/main/div[2]/div[3]/div/form/button/span"
    def __init__(self,driver):
        self.driver=driver

    def searchProduct(self, product_name):
        self.driver.find_element_by_id(self.searchbox_id).clear()
        self.driver.find_element_by_id(self.searchbox_id).send_keys(product_name)
        self.driver.find_element_by_xpath(self.searchButton_xpath).click()


