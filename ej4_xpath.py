import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("https://dev01.sueldosnet.com")
        time.sleep(3)
        
        
    
    