from selenium.webdriver.common.by import By

class HomePageLocators:
    # Локаторы для главной страницы
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать'][1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[text()='Заказать'][2]")
    LOGO_SAMOKAT = (By.XPATH, "//a[@href='/']")
    LOGO_YANDEX = (By.XPATH, "//a[@href='https://yandex.ru/']")