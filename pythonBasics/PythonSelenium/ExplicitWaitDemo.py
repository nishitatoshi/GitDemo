#chrome driver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0

# time.sleep(3)
#//div[@class='products']//div[@class='product']//h4[@class='product-name'] --->  result.find_element(By.XPATH,"//h4[@class='product-name']")
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
# actualLists = driver.find_elements(By.XPATH,"//div[@class='products']//div[@class='product']//h4[@class='product-name']")
# print(len(actualLists)) #error
# print(actualLists)      #error
#
# cartList = []
# for actualList in actualLists:
#     cartList = actualList.text
# print(len(cartList))

# cartList = []
# for result in results:
#     cartList = result.find_element(By.XPATH,"h4").text
# print(len(cartList))

# counter = 0
# for actualList in actualLists:
#     print("entered for loop1")
#     for expectedList in expectedLists:
#         if actualList == expectedList:
#             counter = counter + 1
#             continue
#         else:
#             print("list not matched")
# assert counter == 3


# if len(expectedLists)==len(actualLists) and expectedLists == actualLists:
#     print("list matched")
# else:
#     print("not matched")

#chaining xpath...results already has path , so we'll chain the remaining path from sub div to add to cart button.
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert expectedList == actualList


driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Total valiidation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = int(driver.find_element(By.CLASS_NAME,"totAmt").text)
assert sum == totalAmount



driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()

#Explicit wait - we write it for special codes which can take more time than other elements to load
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

totalAfterDiscount = float(driver.find_element(By.CLASS_NAME,"discountAmt").text)
print(totalAfterDiscount)
assert totalAfterDiscount < totalAmount