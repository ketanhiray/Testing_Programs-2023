from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.maximize.window()
driver.maximize_window()
driver.get("http://www.google.com")

