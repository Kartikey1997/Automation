import configparser

config = configparser.RawConfigParser()
config.read("./configurations/config.ini")

class ReadConfig:

    @staticmethod            #to use the getApplicationURL method directly using the class name, without creating class object
    def get_URL():
        url = config.get("common info","baseURL")
        return url

    @staticmethod
    def get_useremail():
        useremail = config.get("common info", "useremail")
        return useremail

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def get_userid():
        userid = config.get("common info", "userid")
        return userid

    @staticmethod
    def get_mobile():
        mob = config.get("common info", "mob")
        return mob

    @staticmethod
    def get_product_name():
        item = config.get("common info", "product_name")
        return item

    @staticmethod
    def get_product_redButton():
        item = config.get("common info", "product_name_For_RedButton")
        return item

    @staticmethod
    def get_product_getLatestPrice():
        item = config.get("common info", "product_name_For_GetLatestPrice")
        return item

    @staticmethod
    def get_product_CompareSimilar():
        item = config.get("common info", "product_name_For_CompareSimilar")
        return item

    @staticmethod
    def get_product_ContactSupplier():
        item = config.get("common info", "product_name_For_ContactSupplier")
        return item

    @staticmethod
    def get_product_YellowBox():
        item = config.get("common info", "product_name_For_YellowBoxEnquiry")
        return item

    @staticmethod
    def get_product_PostBuyReq():
        item = config.get("common info", "product_name_For_PostBuyRequirement")
        return item

    @staticmethod
    def get_product_MoreProducts():
        item = config.get("common info", "product_name_For_MoreProducts")
        return item

    @staticmethod
    def get_productURL_redButton():
        item = config.get("common info", "product_URL_For_RedButton")
        return item

    @staticmethod
    def get_productURL_getLatestPrice():
        item = config.get("common info", "product_URL_For_GetLatestPrice")
        return item

    @staticmethod
    def get_productURL_CompareSimilar():
        item = config.get("common info", "product_URL_For_CompareSimilar")
        return item

    @staticmethod
    def get_productURL_ContactSupplier():
        item = config.get("common info", "product_URL_For_ContactSupplier")
        return item

    @staticmethod
    def get_productURL_YellowBox():
        item = config.get("common info", "product_URL_For_YellowBoxEnquiry")
        return item

    @staticmethod
    def get_productURL_PostBuyReq():
        item = config.get("common info", "product_URL_For_PostBuyRequirement")
        return item

    @staticmethod
    def get_productURL_MoreProducts():
        item = config.get("common info", "product_URL_For_MoreProducts")
        return item

    @staticmethod
    def get_product_addCart():
        item = config.get("common info", "product_name_For_AddToCart")
        return item