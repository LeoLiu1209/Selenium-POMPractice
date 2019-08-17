from Locators.locators import Locators

class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
        
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.invalid_span_id = Locators.invalid_span_id
        self.forgetPassword_link_linkText = Locators.forgetPassword_link_linkText

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def click_forgetPasswordLink(self):
        self.driver.find_element_by_link_text(self.forgetPassword_link_linkText).click()

    def getEleAttribute(self, elementID, AttribueName):
        attributeValue = self.driver.find_element_by_id(elementID).get_attribute(AttribueName)
        return attributeValue

    def check_invalid_span_msg(self):
        msg = self.driver.find_element_by_id(self.invalid_span_id).text
        return msg
