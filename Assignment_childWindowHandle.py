from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service()
d = webdriver.Firefox(service=service_obj)
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/loginpagePractise/")
d.find_element(By.CSS_SELECTOR,".blinkingText").click()
windowsOpened =d.window_handles

d.switch_to.window(windowsOpened[1])
print(d.find_element(By.CSS_SELECTOR,"a[href='mailto:mentor@rahulshettyacademy.com']").text)
username= d.find_element(By.CSS_SELECTOR,"a[href='mailto:mentor@rahulshettyacademy.com']").text
#message = d.find_element(By.CSS_SELECTOR, ".red").text
#var = message.split("at")[1].strip().split(" ")[0]

d.switch_to.window(windowsOpened[0])
d.find_element(By.ID,"username").send_keys(username)
d.find_element(By.ID,"signInBtn").click()
print(d.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text)
