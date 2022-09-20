# Import the 'modules' that are required for execution

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib3
import warnings

#Set capabilities for testing on Chrome
ch_caps = {
    "build" : "Testing using Chrome on Windows",
    "name" : "Testing on Chrome using Selenium Grid",
    "platform" : "Windows 10",
    "browserName" : "Chrome",
    "version" : "71.0",
    "selenium_version" : "3.13.0",
    "chrome.driver" : 2.42
}

#Set capabilities for testing on Firefox
ff_caps = {
    "build" : "Testing using Firefox on Windows",
    "name" : "Testing on Firefox using Selenium Grid",
    "platform" : "Windows 10",
    "browserName" : "Firefox",
    "version" : "64.0",
}


# Details can be sourced from https://automation.lambdatest.com/
user_name = "nishita.toshi"
app_key = "Y6dgbtq82ulnfn4SgS1IAnY1YjXVpgIzkN5Pmt1oXQKp5Rzk0X"

#Fixture for Firefox
@pytest.fixture(params=["chrome", "firefox"],scope="class")
def driver_init(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    if request.param == "chrome":
    #Remote WebDriver implementation
        #web_driver = webdriver.Remote(
            #command_executor='http://107.108.86.20:4444/wd/hub',
            #desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        web_driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=ch_caps)
    if request.param == "firefox":
    #Remote WebDriver implementation
        #web_driver = webdriver.Remote(
        #    command_executor='http://107.108.86.20:4444/wd/hub',
        #    desired_capabilities={'browserName': 'firefox'})
        web_driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=ff_caps)
    request.cls.driver = web_driver
    yield
    # web_driver.close()
    #print(self.driver.title)
    sleep(5)
    web_driver.close()
    web_driver.quit()

@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
        def test_open_url(self):
            self.driver.get("https://www.lambdatest.com/")
            print(self.driver.title)

            sleep(5)