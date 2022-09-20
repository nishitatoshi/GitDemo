#chrome driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("D:\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID , Xpath, CSSSelector, name, linktext
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1"). click()


#CSSSelector syntax
# tagname[attribute='value] => input[type='submit'] ***2nd way*** #id ***3rd way*** syntax=> .classname -> .alert-success
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Nishita")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#dd-mm-yyyy format in datepicker
driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys("12-01-2021")

#static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)   #indexes start with 0

#Xpath syntax
# //tagname[@attribute='value] => //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
#test validation
assert "Success" in message


#there could be multiple xpaths with 1 name, CSS by default allots the xpath to 1st element after scanning the page from ledt to right
#suppose if there are 3 elements with same xpath, and you want to address 3rd one, use this
#(//input[@type='submit')[3]
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
