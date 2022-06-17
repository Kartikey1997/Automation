from utilities.customLogger import LogGen
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pytest

path_chrome = "/home/admin7/Downloads/chromedriver_linux64/chromedriver"
path_mozilla = "/home/admin7/Downloads/firefoxdriver_linux64/geckodriver"
logger = LogGen.loggen()

@pytest.fixture()
def setup(browser):
    if browser == "headless":
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(executable_path=path_chrome, options=option)
        logger.info("Script running headless in Chrome")
    elif browser == "firefox" or browser == "mozilla":
        driver = webdriver.Firefox(executable_path=path_mozilla)
        logger.info("Mozilla Firefox Browser Launched")
    else:
        driver = webdriver.Chrome(executable_path=path_chrome)
        logger.info("Chrome Browser Launched")
    return driver

def pytest_addoption(parser):            #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                    #This will return the Browser value to Setup method
    return request.config.getoption("--browser")

################## Pytest HTML Report ###########################
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "TradeIndia Automation"
    config._metadata["Module"] = "Login and Product Page"
    config._metadata["Tester"] = "Kartikey Gupta"

# It is hook for delete/modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
