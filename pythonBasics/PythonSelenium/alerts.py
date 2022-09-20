#chrome driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Nishita"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert     #switch to alert mode
alertText = alert.text
print(alertText)
assert name in alertText #validating if name is present in alert msg
alert.accept() #clicks on ok button in pop up box