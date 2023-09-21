
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

service_obj= Service()
d = webdriver.Firefox(service= service_obj)
d.get("https://rahulshettyacademy.com/angularpractice/")

d.find_element(By.NAME, "name").send_keys("ketan")
d.find_element(By.NAME,"email").send_keys("example@gmail.com")
d.find_element(By.ID,"exampleInputPassword1").send_keys("123")
d.find_element(By.ID,"exampleCheck1").click()

#static Dropdown

dropdown1 = Select(d.find_element(By.ID,"exampleFormControlSelect1"))
dropdown1.select_by_visible_text("Female")
#dropdown1.select_by_index(0)

#Xpath-- //tagname[@attribute='value'] -->  //input[@type='submit']
# CSS -- tagname[attribute='value'] --> //input[@type='submit']
d.find_element(By.XPATH,"//input[@type='submit']").click()
msg = d.find_element(By.CLASS_NAME,"alert-success").text
print(msg)

assert "Success" in msg

d.close()
