#chrome driver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5) #global timeout....max wait is of 5 sec, but if all elements have appeared in 2 sec , it will continue and save 3 sec
#implicit wait doesn't work for find elements...so use sleep for it
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

#implicit wait only waits for single element..as soon as it sees the element it passes it, in case of find_elements,
#a list of elements is expected. But initially if selenium finds empty list or list with one element it will pass it without waiting for entire list
#instead we use time.sleep or explicit wait fo these special conditions
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0

#chaining xpath...results already has path , so we'll chain the remaining path from sub div to add to cart button.
for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()

time.sleep(5)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)