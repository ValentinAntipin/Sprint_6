from src.locators.order_page_locators import SUCCESS_MESSAGE
import allure
from src.pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка успешности оформления заказа")
    def is_success_message_present(self):
        # Проверка, что заказ был успешно оформлен
        try:
            self.find_element(*SUCCESS_MESSAGE)
            return True
        except NoSuchElementException:
            return False
