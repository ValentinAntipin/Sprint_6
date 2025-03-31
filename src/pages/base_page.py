from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value, timeout=10):
        #Ожидание присутствия элемента на странице с увеличенным временем
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        #Клик на элемент, используя явное ожидание
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value)))
        element.click()

    def get_element_text(self, by, value):
        #Получение текста элемента с ожиданием его появления
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
        return element.text

    def scroll_to_element(self, by, value):
        #Прокрутка страницы до элемента с ожиданием доступности для клика
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((by, value)))  # Ожидаем кликабельности
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_bottom(self):
        #Прокрутка страницы до самого низа
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")