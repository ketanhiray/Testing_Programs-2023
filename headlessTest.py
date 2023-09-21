from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

firefox_options = webdriver.FirefoxOptions()
firefox_options.arguments("headless")
firefox_options.add_argument("--ignore-certificates-errors")

service_obj = Service()
d = webdriver.Firefox(service=service_obj)
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.execute_script("window.scrollBy(0,document.body.scrollHeight)")
d.get_screenshot_as_file("javasctiptscreen.png")