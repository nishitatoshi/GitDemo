from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")  #use frame id to detect frame
driver.find_element(By.CLASS_NAME,"mce-content-body").clear()
driver.find_element(By.ID,"tinymce").send_keys("Iam able to automate frames")

driver.switch_to.default_content()  #come back to normal browser
print(driver.find_element(By.CSS_SELECTOR,"h3").text)