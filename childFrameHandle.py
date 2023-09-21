from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service()
d = webdriver.Firefox(service=service_obj)
d.implicitly_wait(5)

d.get("https://the-internet.herokuapp.com/iframe")
d.switch_to.frame("mce_0_ifr")
d.find_element(By.ID,"tinymce").clear()
d.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")
d.switch_to.default_content()
print(d.find_element(By.CSS_SELECTOR,"h3").text)