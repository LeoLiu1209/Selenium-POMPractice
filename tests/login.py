from selenium import webdriver
import time
import unittest
import os, sys
sys.path.append(os.path.abspath('..'))
from pages.loginPage import LoginPage
from pages.homePage import HomePage
import HtmlTestRunner

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
    def test_Login_invalid_username(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        
        msg = login.check_invalid_span_msg()
        self.assertEqual(msg, "Invalid credentials")
        time.sleep(2)
    def test_Login_invalid_password(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("123")
        login.click_login()

        msg = login.check_invalid_span_msg()
        self.assertEqual(msg, "Invalid credentials")
        time.sleep(2)
    
    def test_Login_invalid_username_and_password(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("cc123")
        login.enter_password("cc123")
        login.click_login()

        msg = login.check_invalid_span_msg()
        self.assertEqual(msg, "Invalid credentials")
        time.sleep(2)

    def test_Login_empty_username(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)

        login.enter_username("")
        login.enter_password("admin123")
        login.click_login()

        msg = login.check_invalid_span_msg()
        self.assertEqual(msg, "Username cannot be empty")
        time.sleep(2)

    def test_Login_empty_password(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        
        login.enter_username("Admin1")
        login.enter_password("")
        login.click_login()

        msg = login.check_invalid_span_msg()
        self.assertEqual(msg, "Password cannot be empty")
        time.sleep(2)       
    def test_PasswordFiled_is_encrypted(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com")
        login = LoginPage(driver)

        attributeValue = login.getEleAttribute("txtPassword", "type")
        self.assertEqual(attributeValue, "password")
        time.sleep(2)

    def test_redirect_to_correct_ForgetPasswordPage(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com")
        login = LoginPage(driver)

        login.click_forgetPasswordLink()
        forgetPasswordURL = "https://opensource-demo.orangehrmlive.com/index.php/auth/requestPasswordResetCode"
        currentURL = driver.current_url
        self.assertEqual(currentURL, forgetPasswordURL)
    
    def test_Logout_redirected_to_loginPage(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        currentURL = driver.current_url
        loginURL = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
        self.assertEqual(currentURL, loginURL)
    
    # def test_LoginPage_shouldContain_basicElements(self):
    #     driver = self.driver

    #     driver.get("https://opensource-demo.orangehrmlive.com")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))   