import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Укажите путь к драйверу, если нужно
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru")  # Страница приложения самокаты
    print(driver.title)
    yield driver
    driver.quit()