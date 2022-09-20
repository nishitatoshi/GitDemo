from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])  #switching to child window
print(driver.find_element(By.TAG_NAME,"h3").text)
# driver.close() #child window closes

driver.switch_to.window(windowsOpened[0])  #switching to parent window
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text