#chrome driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#another way for Xpath when thre is no attribute -> traverse from parent element to child (form ->1st div ->input tag) syntax-> //form/div[1]/input
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

#another way for CSS selector -> same as xpath, use space in place of / -> form div:nth-child(2) input
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Helloo@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Helloo@1234")
driver.find_element(By.XPATH, "//button[@type= 'submit']").click()

#to identify element with text (without link) using Xpath -> //button[text()='Save New Password']
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()