from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service()
d = webdriver.Firefox(service=service_obj)
d.get("https://rahulshettyacademy.com/angularpractice/")
d.find_element(By.LINK_TEXT,"Shop").click()
products = d.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

d.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
d.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
d.find_element(By.ID,"country").send_keys("ind")

wait = WebDriverWait(d,10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
d.find_element(By.LINK_TEXT,"India").click()
d.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
d.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successText = d.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you!" in successText

d.close()
