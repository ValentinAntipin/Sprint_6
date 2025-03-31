from conftest import driver
from src.pages.success_page import SuccessPage
from src.pages.order_page import OrderPage
from src.pages.home_page import HomePage




def test_order_flow(driver):
    home_page = HomePage(driver)
    order_page = OrderPage(driver)
    success_page = SuccessPage(driver)

    # Позитивный тест с первым набором данных
    home_page.click_order_button_top()
    order_page.fill_order_form("Иван", "Иванов", "Москва, ул. Пушкина", "Краснопресненская", "1234567890")
    order_page.click_submit_button()
    order_page.fill_additional_order_fields("2025-04-01", "сутки", "черный жемчуг")
    order_page.submit_order()
    order_page.confirm_order()

    assert success_page.is_success_message_present(), "Сообщение об успешном заказе не появилось."

def test_order_flow2(driver):
    home_page = HomePage(driver)
    order_page = OrderPage(driver)
    success_page = SuccessPage(driver)

    # Позитивный тест со вторым набором данных
    home_page.click_order_button_bottom()
    order_page.fill_order_form("Алексей", "Петров", "Москва, ул. Шишкина", "Краснопресненская", "4324567098")
    order_page.click_submit_button()
    order_page.fill_additional_order_fields("2025-04-15", "двое суток", "серая безысходность")
    order_page.submit_order()
    order_page.confirm_order()

    assert success_page.is_success_message_present(), "Сообщение об успешном заказе не появилось."


def test_logo_navigation(driver):
    main_page = HomePage(driver)

    # Проверка перехода на главную страницу Самоката
    main_page.click_logo_samokat()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru", "Не удалось перейти на главную страницу Самоката"

    # Проверка перехода на страницу Яндекс Дзена
    main_page.click_logo_yandex()
    assert driver.current_url == "https://yandex.ru", "Не удалось открыть Яндекс Дзен"