from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service()
d = webdriver.Firefox(service=service_obj)
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(d)
# action.double_click(d.find_element(By.))
action.move_to_element(d.find_element(By.ID, "mousehover")).perform()
action.context_click(d.find_element(By.LINK_TEXT, "Top")).perform()
