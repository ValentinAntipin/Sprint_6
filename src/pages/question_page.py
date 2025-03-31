from conftest import driver
from telnetlib import EC
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from src.pages.base_page import BasePage
from src.locators.questions_locator import By, QuestionsLocators


class QuestionsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_element(self, element):
        #Прокрутка страницы до указанного элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_question(self, question_number: int):
        # Локаторы для каждого вопроса
        locators = {
            1: QuestionsLocators.QUESTION_1,
            2: QuestionsLocators.QUESTION_2,
            3: QuestionsLocators.QUESTION_3,
            4: QuestionsLocators.QUESTION_4,
            5: QuestionsLocators.QUESTION_5,
            6: QuestionsLocators.QUESTION_6,
            7: QuestionsLocators.QUESTION_7,
            8: QuestionsLocators.QUESTION_8,
        }

        if question_number in locators:
            # Находим элемент
            question = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locators[question_number])
            )

            # Прокручиваем страницу до элемента
            self.scroll_to_element(question)

            # Кликаем по элементу
            question.click()
        else:
            raise ValueError(f"Вопрос {question_number} не найден!")

    def get_question_text(self, question_number: int):
        # Получаем текст вопроса на основе номера
        locators = {
            1: QuestionsLocators.QUESTION_1,
            2: QuestionsLocators.QUESTION_2,
            3: QuestionsLocators.QUESTION_3,
            4: QuestionsLocators.QUESTION_4,
            5: QuestionsLocators.QUESTION_5,
            6: QuestionsLocators.QUESTION_6,
            7: QuestionsLocators.QUESTION_7,
            8: QuestionsLocators.QUESTION_8,
        }

        if question_number in locators:
            question = self.driver.find_element(*locators[question_number])
            return question.text  # Возвращаем текст вопроса
        else:
            raise ValueError(f"Вопрос {question_number} не найден!")