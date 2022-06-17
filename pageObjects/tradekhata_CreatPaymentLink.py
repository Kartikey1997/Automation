import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class NewPaymentLink:
    client_list = ["Aakav Kumar", "Aakesh Maurya", "Aarav Chand", "Advik Kaushik", "Chaitanya Seth", "Nisha Mishra",
                   "Hemang Kumar", "Inesh Pandey", "Ishaan Kapoor", "Mridu Singh", "Jihan Khan", "Lekh Gaumat",
                   "Lohit Pal", "Ramesh Gupta", "Rituraj Upadhyay"]
    amount = random.randrange(1000, 5000)
    i = random.randrange(0, 14)
    client = client_list[i]
    mob = random.randrange(9000000000, 9999999999)
    email = str(mob) + "trade@gmail.com"

    def __init__(self,driver):
        self.driver = driver

    def onlinePaymentBtn(self):
        self.driver.find_element_by_xpath("//*[@id='sidebar-nav']/li[4]/a/span[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='main-wrapper']/section/div[2]/div[3]/div[1]/div[2]/a").click()

    def paymentDescription(self):
        self.driver.find_element_by_xpath("//*[@id='order_amount']").send_keys(self.amount)
        self.driver.find_element_by_xpath("//*[@id='name']").send_keys(self.client)
        self.driver.find_element_by_xpath("//*[@id='mobile']").send_keys(self.mob)
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys(self.email)
        self.driver.find_element_by_xpath("//*[@id='notif_mobile']").send_keys(self.mob)
        self.driver.find_element_by_xpath("//*[@id='paymentLinkForm']/div[1]/div[1]/div[7]/div/textarea").send_keys("This is a auto-generated payment link, TESTING purpose only!!!!!!")

    def set_AutoReminderInPaymentLink(self):
        self.driver.find_element_by_xpath("//*[@id='enableAutoReminder']").click()
        i=random.randrange(1,3)
        element = self.driver.find_element_by_xpath("//*[@id='paymentLinkForm']/div[1]/div[2]/div/div/div[2]/div[2]/div/select")
        drp = Select(element)
        drp.select_by_index(i)
        self.driver.find_element_by_xpath("//*[@id='emailReminder']").click()
        self.driver.find_element_by_xpath("//*[@id='whatsappReminder']").click()
        self.driver.find_element_by_xpath("//*[@id='smsReminder']").click()

    def createPaymentBtn(self):
        self.driver.find_element_by_xpath("//*[@id='paymentLinkForm']/div[2]/button").click()
