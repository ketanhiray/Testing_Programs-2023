from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import time 
from selenium.webdriver.firefox.service import Service


service_obj= Service()
d = webdriver.Firefox(service= service_obj)
d.get("https://rahulshettyacademy.com/dropdownsPractise/")

d.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = d.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")

#print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

print(d.find_element(By.ID,"autosuggest").get_attribute("value"))

assert d.find_element(By.ID,"autosuggest").get_attribute("value") == "India"