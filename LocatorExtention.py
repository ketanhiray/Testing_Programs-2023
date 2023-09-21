from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
d = webdriver.Firefox(service=service_obj)

d.get("https://rahulshettyacademy.com/client")

d.find_element(By.LINK_TEXT,"Forgot password?").click()

d.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
d.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@123")
d.find_element(By.ID,"confirmPassword").send_keys("Hello@123")
d.find_element(By.XPATH,"//button[@type='submit']").click()