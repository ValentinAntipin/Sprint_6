from conftest import driver
from src.locators.order_page_locators import SUCCESS_MESSAGE

class SuccessPage:
    def __init__(self, driver):
        self.driver = driver

    def is_success_message_present(self):
        try:
            return self.driver.find_element(*SUCCESS_MESSAGE).is_displayed()
        except:
            return False