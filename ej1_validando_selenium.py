from selenium import webdriver



driver = webdriver.Chrome()
driver.get("http://python.org")
driver.close()
