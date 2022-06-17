#!/usr/bin/python3
import random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import logging
from _datetime import datetime
from selenium.webdriver.chrome.options import Options
class LogGen:

    '''@staticmethod
    def loggen():
        timestr = datetime.now().strftime("%d-%m-%Y--%I:%M %p")
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename="/home/admin7/Documents/Housekeeping_logs/ChronJob-"+timestr+".log",
                                       mode="w")
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger'''



options = Options()
options.headless = False
#log = LogGen.loggen()

driver = webdriver.Chrome(executable_path="/home/admin7/Downloads/chromedriver_linux64/chromedriver",options=options)
driver.get("https://www.tradeindia.com/Seller/Agriculture/Fresh-Vegetables/")
driver.maximize_window()
#driver.find_element(By.XPATH,"/html/body/main/div[2]/div[3]/div[2]/div/a[1]").send_keys(Keys.COMMAND+'t')
cities = driver.find_element_by_xpath("/html/body/main/div[2]/div[7]").text
a = cities.split("\n")
print(a)
# a.remove('All Results')
# a.reverse()
# print(a)
# i = random.randrange(0,len(a))
# city_xpath = "//*[text()='"+a[i]+"']"
# print(city_xpath)
# driver.execute_script("alert('HI KARTIKEY');")
# driver.switch_to_alert().accept()
# driver.execute_script("alert('Hi Welcome to TradeIndia Housekeeping');")
# time.sleep(2)
# driver.switch_to_alert().send_keys("Hello Kartikey")
# driver.switch_to_alert().accept()
'''driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[3]/form/div[1]/input").send_keys("I-HONOIDA33036")
driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[3]/form/div[2]/input").send_keys("levels.*bauer")
driver.find_element_by_name("Login").click()
time.sleep(2)
driver.get("http://housekeeping.tradeindia.com/housekeeping/")
time.sleep(2)
driver.get("http://housekeeping.tradeindia.com/housekeeping/")
time.sleep(2)
driver.get("http://housekeeping.tradeindia.com/housekeeping/my_area/holidays.html")
time.sleep(2)
driver.execute_script("window.scroll(0, 500);")
a = driver.find_element_by_xpath("/html/body/div[2]/table[3]/tbody/tr[1]").text
b = driver.find_element_by_xpath("/html/body/div[2]/table[3]/tbody/tr[33]").text
print(a)
print(b)
log.info(a)
log.info(b)'''
#driver.find_element_by_xpath("")
# driver.find_element_by_name("submit").click()
# a=driver.find_element_by_xpath("/html/body/div[2]/center/form").text
# log.info(a)
# print(a)
# driver.get("https://demoqa.com/slider")
# time.sleep(2)
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, 'someid')))

# driver.get("https://demoqa.com/buttons")
# driver.maximize_window()
# # time.sleep(5)
# driver.execute_script("window.scroll(0, 4000);")
                             #############handling a drop box without select class
'''ele = driver.find_elements_by_xpath("//*[@id='post-2646']/div[2]/div/div/div/p/select")
print(ele)
for i in range(len(ele)):
    a = ele[i].text
    print(a)
c=a.split("\n")
print(c)
for j in range(len(c)):
    if(c[j]=="India"):
        Dropdown_Element = driver.find_element_by_xpath("//*[text()='India']").click()
        print(Dropdown_Element)
        actions = ActionChains(driver)
        actions.click(on_element=Dropdown_Element).perform()'''

# click = driver.find_element_by_id("Gt12R")
# click.send_keys(Keys.RETURN)

'''c = driver.find_element_by_xpath("//*[@id='tree-node']/ol/li/span/label/span[3]").text
print(c)
if(c=="Home"):
    driver.find_element_by_xpath("//*[@id='tree-node']/ol/li/span/label/span[3]").click()'''



'''action = ActionChains(driver)
ele = driver.find_element_by_xpath("//*[@id='sliderContainer']/div[1]/span/input")
ele1 = driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/ul/li[1]/span[1]")
ele2 = driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/ul/li[1]/ul/li[3]/a")
ele3 = driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/ul/li[1]/ul/li[2]/a")
ele4 = driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/ul/li[1]/ul/li[1]/a")
lst = [ele4,ele3,ele2]
for i in lst:
    action.move_to_element(ele1).move_to_element(i).perform()
    time.sleep(2)'''
# action.click_and_hold(ele).move_by_offset(-250,0).release().perform()
# action.click_and_hold(ele).move_by_offset(250, 0).release().perform()
#handles=driver.window_handles
driver.execute_script("window.scroll(0,3000);")
#driver.find_element_by_xpath("/html/body/main/div[4]/div/div[2]/div[2]/div[8]/div[3]/button").click()
#driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/div/div[2]/button").click()
#element = driver.find_element_by_xpath("//*[text()='Compare With Similar Products']")
#actions = ActionChains(driver)
#actions.move_to_element(element)
#actions.context_click(on_element=element).perform()
'''driver.execute_script("arguments[0].scrollIntoView();", element)
try:
    driver.find_element_by_xpath("//*[@id='comparison_div']/div/div[2]/div[2]/div[8]/div[3]/button").click()
except NoSuchElementException:
    try:
        driver.find_element_by_xpath("//*[@id='comparison_div']/div/div[2]/div[2]/div[7]/div[3]/button").click()
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath("//*[@id='comparison_div']/div/div[2]/div[2]/div[5]/div[3]/button").click()
        except NoSuchElementException:
            try:
                driver.find_element_by_xpath("//*[@id='comparison_div']/div/div[2]/div[2]/div[6]/div[3]/button").click()
            except NoSuchElementException:
                pass

time.sleep(2)
driver.close()
#driver.find_element_by_xpath("//*[@id='comparison_div']/div/div[2]/div[2]/div[8]/div[3]/button").click()
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[starts-with(@id,'comparison_div')]"))).click()
time.sleep(2)
flag = "/html/body/main/div[10]/div[1]/div/div"
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scroll(0, 4000);")
def test_001_flipkart():
        driver = webdriver.Chrome(executable_path="/home/admin7/Downloads/chromedriver_linux64/chromedriver")
        driver.get("http://www.flipkart.com")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
        time.sleep(2)
        driver.find_element_by_name("q").send_keys("Leather Shoes")
        driver.find_element_by_class_name("_34RNph").click()
        
driver.execute_script("window.open('https://www.facebook.com');")   #to open URL in new Tab
handles=driver.window_handles
print(handles)
time.sleep(3)
driver.close()
time.sleep(2)
driver.switch_to.window(handles[1])
driver.find_element_by_name("login").click()
time.sleep(2)
driver.quit()

from utilities import XLUtils

path = "/home/admin7/Downloads/Login.xlsx"
rows_num=XLUtils.getRowCount(path,"Sheet1")
print(rows_num)
for i in range(3,rows_num+1):
    data=XLUtils.readData(path,"Sheet1",i,1)
    print(data)
from _datetime import datetime

timestr = datetime.now().strftime("%d-%m-%Y--%I:%M:%p")
a="Sheet"
print(a+timestr)'''
#driver.find_element_by_id("user_location").click()
#driver.find_element_by_xpath("//*[@id='cities_list']/li[1]/i").click()
#drp = Select(element)
#drp.select_by_index(4)
'''print(b)
if(b in a):
    print("correct slab quantity added to the cart")
else:
    print("incorrect slab quantity added to the cart")

driver.close()
import datetime
now_year = datetime.datetime.now().year
now_month = datetime.datetime.now().month
now_day = datetime.datetime.now().day
if (1<=now_month<=9):
    now_month_str = str(now_month + 3)
    now_day_str = str(now_day)
    now_year_str = str(now_year)
    due_date = now_month_str+"/"+now_day_str+"/"+now_year_str
    print(due_date)
else:
    now_month_str = str(now_month)
    now_day_str = str(now_day)
    now_year_str = str(now_year+1)
    due_date = now_month_str + "/" + now_day_str + "/" + now_year_str
    print(due_date)'''
'''import pytest

@pytest.mark.parametrize("num1, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num1, output):
   assert 11*num1 == output'''

