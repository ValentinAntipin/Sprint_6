from src.pages.success_page import SuccessPage
from src.pages.order_page import OrderPage
from src.pages.home_page import HomePage
from allure import title
from src.data import order_data
from src.config import Config
import pytest

@pytest.mark.usefixtures("driver")
class TestOrderFlow:

    @pytest.mark.parametrize("name, surname, address, station, phone, date, rental_period, color", order_data)
    @title("Тест на успешную регистрацию")
    def test_order_flow(self, driver, name, surname, address, station, phone, date, rental_period, color):
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


@pytest.mark.usefixtures("driver")
class TestLogoNavigation:

    @title("Тест на переходы с ЛОГОТИПА")
    def test_logo_navigation(self, driver):
        main_page = HomePage(driver)

        # Проверка перехода на главную страницу Самоката
        main_page.click_logo_samokat()
        assert main_page.get_url() == Config.URL('/'), "Не удалось перейти на главную страницу Самоката"

        # Проверка перехода на страницу Яндекс Дзена
        main_page.click_logo_yandex()

        # Переключаемся на новое окно через методы BasePage
        main_page.switch_to_window(1)

        # Проверяем, что открылся правильный URL для Яндекс Дзена
        assert main_page.get_url() == Config.URL2('/'), "Не удалось открыть Яндекс Дзен"

        # Закрываем текущее окно и переключаемся обратно на первое
        main_page.close_current_window()
        main_page.switch_to_window(0)