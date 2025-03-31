from conftest import driver
from src.pages.base_page import BasePage
from src.locators.home_page_locators import HomePageLocators

class HomePage(BasePage):

    # Методы
    def __init__(self, driver):
        super().__init__(driver)


    def click_order_button_top(self):
        self.driver.find_element(*self.ORDER_BUTTON_TOP).click()

    def click_order_button_bottom(self):
        self.driver.find_element(*self.ORDER_BUTTON_BOTTOM).click()

    def click_logo_samokat(self):
        self.driver.find_element(*self.LOGO_SAMOKAT).click()

    def click_logo_yandex(self):
        self.driver.find_element(*self.LOGO_YANDEX).click()