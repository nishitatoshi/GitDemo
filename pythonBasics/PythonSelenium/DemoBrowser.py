from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver
# service_obj=Service("D:\chromedriver.exe");
#driver = webdriver.Chrome(service=service_obj)

#edge driver
service_obj = Service("D:\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://courses.rahulshettyacademy.com/p/python-sdet-automation-testing")
driver.minimize_window()
driver.refresh()
driver.back()
driver.forward()
driver.close()