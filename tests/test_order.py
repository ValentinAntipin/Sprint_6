from src.pages.success_page import SuccessPage
from src.pages.order_page import OrderPage
from src.pages.home_page import HomePage
from allure import title
from src.data import order_data
import pytest



@pytest.mark.parametrize("name, surname, address, station, phone, date, rental_period, color", order_data)
@title("Тест на успешную регистрацию")
def test_order_flow(driver, name, surname, address, station, phone, date, rental_period, color):
    home_page = HomePage(driver)
    order_page = OrderPage(driver)
    success_page = SuccessPage(driver)

    # Позитивный тест с набором данных
    home_page.click_order_button_top()
    order_page.fill_order_form(name, surname, address, station, phone)
    order_page.click_submit_button()
    order_page.fill_additional_order_fields(date, rental_period, color)
    order_page.submit_order()
    order_page.confirm_order()

    assert success_page.is_success_message_present(), "Сообщение об успешном заказе не появилось."

@title("Тест на переходы с ЛОГОТИПА")
def test_logo_navigation(driver):
    main_page = HomePage(driver)

    #Проверка перехода на главную страницу Самоката
    main_page.click_logo_samokat()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Не удалось перейти на главную страницу Самоката"

    # Проверка перехода на страницу Яндекс Дзена
    main_page.click_logo_yandex()
    assert driver.current_url == "https://yandex.ru", "Не удалось открыть Яндекс Дзен"