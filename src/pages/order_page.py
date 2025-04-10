from src.locators.order_page_locators import NAME_FIELD, SURNAME_FIELD, ADDRESS_FIELD, STATION_FIELD, PHONE_FIELD, SUBMIT_BUTTON, DATE_FIELD, DROPDOWN_FIELD, COLOR_SCOOTER_BLACK, COLOR_SCOOTER_GREY, ORDER_BUTTON, ORDER2_BUTTON
import allure
from src.pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнение формы заказа")
    def fill_order_form(self, name, surname, address, station, phone):
        # Заполнение полей формы заказа
        self.fill_input(NAME_FIELD, name)
        self.fill_input(SURNAME_FIELD, surname)
        self.fill_input(ADDRESS_FIELD, address)
        self.fill_input(STATION_FIELD, station)
        self.fill_input(PHONE_FIELD, phone)

    @allure.step("Нажатие на кнопку 'Далее'")
    def click_submit_button(self):
        # Клик на кнопку далее
        self.click_element(*SUBMIT_BUTTON)

    @allure.step("Заполнение дополнительных полей заказа")
    def fill_additional_order_fields(self, date, rental_period, color):
        # Заполнение дополнительных полей заказа: дата, период аренды, цвет
        self.fill_input(DATE_FIELD, date)
        self.fill_input(DROPDOWN_FIELD, rental_period)
        self.fill_input(COLOR_SCOOTER_BLACK, color)
        self.fill_input(COLOR_SCOOTER_GREY, color)

    @allure.step("Нажатие кнопки заказать")
    def submit_order(self):
        # Нажатие кнопки заказа
        self.click_element(*ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        # Подтверждение заказа
        self.click_element(*ORDER2_BUTTON)