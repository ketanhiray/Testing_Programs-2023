from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sevice_obj =Service()

d= webdriver.Firefox(service=sevice_obj)
#d = webdriver.Chrome(service=sevice_obj)
d.implicitly_wait(5)
d.get("https://rahulshettyacademy.com/seleniumPractise/#/")

d.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

results = d.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH,"div/button").click()

d.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
d.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Sum validation
prices =d.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum =0
for price in prices:
    sum= sum + int(price.text)

print(sum)
totalAmount = int(d.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == totalAmount



d.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
d.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(d,10)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(d.find_element(By.CLASS_NAME,"promoInfo").text)
d.find_element(By.XPATH,"//button[normalize-space()='Place Order']").click()