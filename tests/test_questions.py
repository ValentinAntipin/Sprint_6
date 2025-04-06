from src.pages.question_page import QuestionsPage
import allure
import pytest

@allure.feature("Проверка вопросов о важном")
class TestQuestions:

    @pytest.mark.parametrize(
        "question_number, expected_text",
        [
            (1, "Сколько это стоит? И как оплатить?"),
            (2, "Хочу сразу несколько самокатов! Так можно?"),
            (3, "Как рассчитывается время аренды?"),
            (4, "Можно ли заказать самокат прямо на сегодня?"),
            (5, "Можно ли продлить заказ или вернуть самокат раньше?"),
            (6, "Вы привозите зарядку вместе с самокатом?"),
            (7, "Можно ли отменить заказ?"),
            (8, "Я жизу за МКАДом, привезёте?")
        ]
    )
    @allure.story("Проверка вопросов")
    def test_question(self, driver, question_number, expected_text):
        page = QuestionsPage(driver)
        page.open_question(question_number)
        actual_text = page.get_question_text(question_number)
        assert expected_text in actual_text, f"Текст вопроса для {question_number} не совпадает. Ожидалось: {expected_text}, получено: {actual_text}"