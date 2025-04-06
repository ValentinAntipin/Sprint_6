from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.locators.questions_locators import QuestionsLocators
import allure


class QuestionsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    @allure.step("Открытие вопроса №{question_number}")
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
            question = self.find_element(*locators[question_number])
            self.scroll_to_element(*locators[question_number])
            # Кликаем по элементу
            question.click()
        else:
            raise ValueError(f"Вопрос {question_number} не найден!")

    @allure.step("Открытие вопроса на основе номера")
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
            question = self.find_element(*locators[question_number])
            return question.text  # Возвращаем текст вопроса
        else:
            raise ValueError(f"Вопрос {question_number} не найден!")