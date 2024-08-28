from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get("https://dev01.sueldosnet.com")

userLogin = driver.find_element(By.ID, 'UserName')
userLogin.send_keys("Testing")

passwordLogin = driver.find_element('By.ID', 'Password')
passwordLogin.send_keys("Testing!123")
userLogin.send_keys(Keys.ENTER)
time.sleep(3)


driver.close()


