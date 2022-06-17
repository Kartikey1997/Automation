from utilities.customLogger import LogGen
import time
import random

class Add_Client:
    logger = LogGen.loggen()
    ClientBtn_xpath="//*[@id='sidebar-nav']/li[5]/a/span[2]"
    AddNewClient_xpath="/html/body/main/section/div[2]/div[1]/div[2]/a/span[2]"
    BusinessName_name="business_name"
    ClientName_name="client_name"
    Mobile_name="mobile"
    Email_name="email"
    Address_name="address"
    City_name="city"
    State_name="state"
    Country_name="country"
    GST_name="gst_number"
    SubmitBtn_xpath="//*[@id='add_client']/button"

    business_list = ["SwipeWire", "SecureSmarter", "Dwellsmith", "SalePush", "Formonix", "Branding", "Cloudrevel",
                     "Seekingon", "Medicing", "Crowdstage", "Hiphonic", "QuickSpace", "MetConnect", "Rentoor",
                     "Kiddily"]
    client_list = ["Aakav Kumar", "Aakesh Maurya", "Aarav Chand", "Advik Kaushik", "Chaitanya Seth", "Hredhaan Mishra",
                   "Hemang Kumar", "Inesh Pandey", "Ishaan Kapoor", "Jairaj Singh", "Jihan Khan", "Lekh Gaumat",
                   "Lohit Pal", "Ramesh Gupta", "Rituraj Upadhyay"]
    street_list = ["10, S. K. Dev Rd, Sree Bhumi", "A/5, Jay Prabhat Cop House, Sahakar Nagar",
                   "R.K.G. Industrial Estate, Ganapathy", "D-2/20, Mayapuri", "4b/18, Tilak Nagar",
                   "59, Khanna Estate, Kurla Andheri Road", "1 Minesh Park, Chandawarkar Lane",
                   "8, Devdhara, Laxmibai Lad Rd.", "C-1, Phase Ii, Apmc Market-1, Sector 19",
                   "2nd Flr, R No 205/6, Kapol Bank", "B1/f1, Sector-9, Opp Apna Bazar",
                   "710, International Trade Tower", "137 A, Mayur Vihar", "27 Patil Sainath Plaza",
                   "173, Udyog Bhavan"]
    city_list = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune", "Jaipur",
                 "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane"]
    i = random.randrange(0, 14)
    business = business_list[i] + " Pvt. Ltd."
    client = client_list[i]
    street = street_list[i]
    city = city_list[i]
    country = "India"
    mob = random.randrange(9000000000, 9999999999)
    email = str(mob) + "trade@gmail.com"
    num = random.randrange(1111, 9999)
    gst = "22ABCDE" + str(num) + "F2Z5"

    def __init__(self,driver):
        self.driver = driver

    def tradekhataButton(self):
        self.driver.find_element_by_xpath("/html/body/header/div[4]/div/div[2]/a[2]").click()
        self.logger.info("************TradeKhata Button Pressed*************")

    def client_btn(self):
        self.driver.find_element_by_xpath(self.ClientBtn_xpath).click()
        time.sleep(2)
        self.logger.info("************ Client Button Pressed*************")

    def addNewClientDescription(self):
        self.driver.find_element_by_xpath(self.AddNewClient_xpath).click()
        time.sleep(2)
        self.logger.info("************ Add New Client Button Pressed*************")
        self.driver.find_element_by_name(self.BusinessName_name).send_keys(self.business)
        self.logger.info("************ Business name entered *************")
        self.driver.find_element_by_name(self.ClientName_name).send_keys(self.client)
        self.logger.info("************* Client Name Entered ************")
        self.driver.find_element_by_name(self.Mobile_name).send_keys(self.mob)
        self.logger.info("************Mobile number entered************")
        self.driver.find_element_by_name(self.Email_name).send_keys(self.email)
        self.logger.info("************* Email Id Entered************")
        self.driver.find_element_by_name(self.Address_name).send_keys(self.street)
        self.logger.info("************* Address Entered ************")
        self.driver.find_element_by_name(self.City_name).send_keys(self.city)
        self.logger.info("************* City Entered ************")
        self.driver.find_element_by_name(self.Country_name).send_keys(self.country)
        self.logger.info("************* Country Entered ************")
        self.driver.find_element_by_name(self.GST_name).send_keys(self.gst)
        self.logger.info("************* GST Entered ************")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.SubmitBtn_xpath).click()
        self.logger.info("************ Add Client Button Pressed ************")
        time.sleep(2)