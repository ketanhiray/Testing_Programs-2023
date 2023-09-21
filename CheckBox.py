from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


service_obj =Service()

d = webdriver.Firefox(service= service_obj)

d.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes= d.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option2":
        checkbox.click()
        assert checkbox.is_selected()

        break