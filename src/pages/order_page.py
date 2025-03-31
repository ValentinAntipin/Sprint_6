from conftest import driver
from src.locators.order_page_locators import NAME_FIELD, SURNAME_FIELD, ADDRESS_FIELD, STATION_FIELD, PHONE_FIELD, SUBMIT_BUTTON, DATE_FIELD, DROPDOWN_FIELD, COLOR_FIELD, ORDER_BUTTON, ORDER2_BUTTON


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_order_form(self, name, surname, address, station, phone):
        self.driver.find_element(*NAME_FIELD).send_keys(name)
        self.driver.find_element(*SURNAME_FIELD).send_keys(surname)
        self.driver.find_element(*ADDRESS_FIELD).send_keys(address)
        self.driver.find_element(*STATION_FIELD).send_keys(station)
        self.driver.find_element(*PHONE_FIELD).send_keys(phone)

    def click_submit_button(self):
        self.driver.find_element(*SUBMIT_BUTTON).click()

    def fill_additional_order_fields(self, date, rental_period, color):
        self.driver.find_element(*DATE_FIELD).send_keys(date)
        self.driver.find_element(*DROPDOWN_FIELD).send_keys(rental_period)
        self.driver.find_element(*COLOR_FIELD).send_keys(color)

    def submit_order(self):
        self.driver.find_element(*ORDER_BUTTON).click()

    def confirm_order(self):
        self.driver.find_element(*ORDER2_BUTTON).click()

    # Методы
    def fill_order_form(self, name, surname, address, station, phone, ):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)

    def submit_order(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def is_order_success(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).is_displayed()