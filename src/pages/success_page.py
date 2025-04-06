from src.locators.order_page_locators import SUCCESS_MESSAGE
import allure
from src.pages.base_page import BasePage

class SuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка успешности оформления заказа")
    def is_success_message_present(self):
        # Проверка, что заказ был успешно оформлен
        try:
            return self.driver.find_element(*SUCCESS_MESSAGE).is_displayed()
        except:
            return False