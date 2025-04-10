import allure
from src.pages.base_page import BasePage
from src.locators.home_page_locators import HomePageLocators

class HomePage(BasePage):

    # Методы
    def __init__(self, driver):
        super().__init__(driver)

        # Определение локаторов
        self.ORDER_BUTTON_TOP = HomePageLocators.ORDER_BUTTON_TOP
        self.ORDER_BUTTON_BOTTOM = HomePageLocators.ORDER_BUTTON_BOTTOM
        self.LOGO_SAMOKAT = HomePageLocators.LOGO_SAMOKAT
        self.LOGO_YANDEX = HomePageLocators.LOGO_YANDEX

    @allure.step("Нажатие на верхнюю кнопку заказа")
    def click_order_button_top(self):
        self.click_element(*self.ORDER_BUTTON_TOP)

    @allure.step("Нажатие на нижнюю кнопку заказа")
    def click_order_button_bottom(self):
        self.click_element(*self.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажатие на логотип Самокат")
    def click_logo_samokat(self):
        self.click_element(*self.LOGO_SAMOKAT)

    @allure.step("Нажатие на логотип Яндекс")
    def click_logo_yandex(self):
        self.click_element(*self.LOGO_YANDEX)

    @allure.step("Получение текущего URL")
    def get_url(self):
        return self.get_current_url()