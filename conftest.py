import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from src.config import Config
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="function")
def driver():

    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(15)
    driver.get(Config.URL)  # Страница приложения самокаты

    yield driver
    driver.quit()