from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj= Service()
d = webdriver.Firefox(service= service_obj)
d.get("https://rahulshettyacademy.com/angularpractice/")

d.find_element(By.NAME, "name").send_keys("ketan")
d.find_element(By.NAME,"email").send_keys("example@gmail.com")
d.find_element(By.ID,"exampleInputPassword1").send_keys("123")
d.find_element(By.ID,"exampleCheck1").click()
