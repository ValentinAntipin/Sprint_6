from src.locators.order_page_locators import NAME_FIELD, SURNAME_FIELD, ADDRESS_FIELD, STATION_FIELD, PHONE_FIELD, SUBMIT_BUTTON, DATE_FIELD, DROPDOWN_FIELD, COLOR_FIELD, ORDER_BUTTON, ORDER2_BUTTON
import allure

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение формы заказа")
    def fill_order_form(self, name, surname, address, station, phone):
        # Заполнение полей формы заказа
        self.driver.find_element(*NAME_FIELD).send_keys(name)
        self.driver.find_element(*SURNAME_FIELD).send_keys(surname)
        self.driver.find_element(*ADDRESS_FIELD).send_keys(address)
        self.driver.find_element(*STATION_FIELD).send_keys(station)
        self.driver.find_element(*PHONE_FIELD).send_keys(phone)

    @allure.step("Нажатие на кнопку 'Далее'")
    def click_submit_button(self):
        # Клик на кнопку далее
        self.driver.find_element(*SUBMIT_BUTTON).click()

    @allure.step("Заполнение дополнительных полей заказа")
    def fill_additional_order_fields(self, date, rental_period, color):
        # Заполнение дополнительных полей заказа: дата, период аренды, цвет
        self.driver.find_element(*DATE_FIELD).send_keys(date)
        self.driver.find_element(*DROPDOWN_FIELD).send_keys(rental_period)
        self.driver.find_element(*COLOR_FIELD).send_keys(color)

    @allure.step("Нажатие кнопки заказать")
    def submit_order(self):
        # Нажатие кнопки заказа
        self.driver.find_element(*ORDER_BUTTON).click()

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        # Подтверждение заказа
        self.driver.find_element(*ORDER2_BUTTON).click()
