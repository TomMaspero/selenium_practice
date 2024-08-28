import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
    
    def test_login(self):
        driver = self.driver
        driver.get("https://dev01.sueldosnet.com")
        self.assertIn("SueldosNet", driver.title)
        userLogin = driver.find_element(By.ID, 'UserName')
        userLogin.send_keys("root")
        passwordLogin = driver.find_element(By.ID, 'Password')
        passwordLogin.send_keys("uS3rr00T#padev24")
        userLogin.send_keys(Keys.ENTER)
        time.sleep(1)
        empresaLogin = driver.find_element(By.ID, "EmpresaNombre")
        empresaLogin.clear()
        empresaLogin.send_keys("Tomás Empresa")
        buttonVer = driver.find_element(By.Class, "btn btn-default dropdown-toggle")
        empresaOpc = driver.find_element(By.XPATH)
        buttonVer.click()
        time.sleep(1)
        empresaLogin.send_keys(Keys.ENTER)
        time.sleep(3)
        assert "No se encontro el elemento: " not in driver.page_source
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()