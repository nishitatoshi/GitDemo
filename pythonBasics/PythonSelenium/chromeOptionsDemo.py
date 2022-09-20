from selenium.webdriver.chrome.service import Service
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice")

print(driver.title)