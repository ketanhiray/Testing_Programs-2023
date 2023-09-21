from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


service_obj = Service()

d= webdriver.Firefox(service=service_obj)

d.get("https://rahulshettyacademy.com/AutomationPractice/")

radios = d.find_elements(By.XPATH,"//input[@type='radio']")
for i in radios:
    if i.get_attribute("value") == "radio3":
        i.click()
        assert i.is_selected()
        
        break
    