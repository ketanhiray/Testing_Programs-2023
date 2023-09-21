from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service_obj = Service()
driver = webdriver.Firefox(service=service_obj) # for firefox browser
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.close()
