from selenium.webdriver.chrome.service import Service
from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#scrolling in console of webpage using JS
#window.scrollBy(0,600)   -> scrolls down via y axis to 600 px
#window.scrollBy(0,document.body.scrollHeight)     -> to scroll to bottom of page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")