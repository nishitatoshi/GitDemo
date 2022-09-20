from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserSortedVeggieList = []

#ALGORITHM
#click on col header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#collect all veggie names -> browserSortedVeggieList
    #$x(xpath) syntax to check locator in broeser console
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")

for ele in veggieWebElements:
    browserSortedVeggieList.append(ele.text)

originalBrowserSortedList = browserSortedVeggieList.copy()

#sort browserSortedVeggieList  -> newSortedList
browserSortedVeggieList.sort()

#assert browserSortedVeggieList == newSortedList
assert originalBrowserSortedList == browserSortedVeggieList