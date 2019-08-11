from selenium import webdriver
import time
import unittest
import os, sys
sys.path.append(os.path.abspath('..'))
from pages.loginPage import LoginPage
from pages.homePage import HomePage


class LoginTetst(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main()   