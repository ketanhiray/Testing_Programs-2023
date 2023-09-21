from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service()
d = webdriver.Firefox(service=service_obj)
d.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserSortedVeggies = []

#click on column header
d.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#collect all veggie name -> BrowserSortedVeggieList (A,B,C)

veggieWebElements =d.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

#sort this BrowserSortedVeggieList => newSortedList -> (A,B,C)
browserSortedVeggies.sort()
assert  browserSortedVeggies == originalBrowserSortedList