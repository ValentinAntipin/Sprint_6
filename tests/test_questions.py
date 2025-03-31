from conftest import driver
from src.pages.question_page import QuestionsPage
import allure

@allure.feature("Проверка вопросов о важном")
class TestQuestions:

    @allure.story("Проверка вопроса 1")
    def test_question_1(self, driver):
        page = QuestionsPage(driver)
        page.open_question(1)
        assert "Сколько это стоит? И как оплатить?" in page.get_question_text(1)

    @allure.story("Проверка вопроса 2")
    def test_question_2(self, driver):
        page = QuestionsPage(driver)
        page.open_question(2)
        assert "Хочу сразу несколько самокатов! Так можно?" in page.get_question_text(2)

    @allure.story("Проверка вопроса 3")
    def test_question_3(self, driver):
        page = QuestionsPage(driver)
        page.open_question(3)
        text = page.get_question_text(3)
        assert "Как рассчитывается время аренды?" in page.get_question_text(3)

    @allure.story("Проверка вопроса 4")
    def test_question_4(self, driver):
        page = QuestionsPage(driver)
        page.open_question(4)
        assert "Можно ли заказать самокат прямо на сегодня?" in page.get_question_text(4)

    @allure.story("Проверка вопроса 5")
    def test_question_5(self, driver):
        page = QuestionsPage(driver)
        page.open_question(5)
        assert "Можно ли продлить заказ или вернуть самокат раньше?" in page.get_question_text(5)

    @allure.story("Проверка вопроса 6")
    def test_question_6(self, driver):
        page = QuestionsPage(driver)
        page.open_question(6)
        assert "Вы привозите зарядку вместе с самокатом?" in page.get_question_text(6)

    @allure.story("Проверка вопроса 7")
    def test_question_7(self, driver):
        page = QuestionsPage(driver)
        page.open_question(7)
        assert "Можно ли отменить заказ?" in page.get_question_text(7)

    @allure.story("Проверка вопроса 8")
    def test_question_8(self, driver):
        page = QuestionsPage(driver)
        page.open_question(8)
        assert "Я жизу за МКАДом, привезёте?" in page.get_question_text(8)