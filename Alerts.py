from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obj= Service()

d = webdriver.Firefox(service=service_obj)
name= "Ketan"
d.get("https://rahulshettyacademy.com/AutomationPractice/")

d.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
d.find_element(By.ID,"alertbtn").click()
alert = d.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
#assert.True name in alertText
alert.accept()

