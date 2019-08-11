from Locators.locators import Locators
class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcom_link_id = Locators.welcom_link_id
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcom_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()

