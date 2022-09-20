from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME,"blinkingText").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])  #switching to child window

email = driver.find_element(By.XPATH,"//div[@class='page-wrapper']//div[@class='container']//div[@class='row']//div[@class='col-md-8']//p[@class='im-para red']//strong").text
# print(email)
driver.close()

driver.switch_to.window(windowsOpened[0])  #switching to parent window
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

##############################################Rahul Shetty's Solution###########################################################
# driver.switch_to.window(windowsOpened[1])
# message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("at")[1].strip().split(" ")[0]
# driver.close()
# driver.switch_to.window(windowsOpened[0])
# driver.find_element(By.ID, "username").send_keys(var)
# driver.find_element(By.ID, "password").send_keys(var)
# driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
# wait = WebDriverWait(driver,10)
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
# print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
