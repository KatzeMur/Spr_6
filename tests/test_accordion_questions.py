import pytest
import allure
from constants import BASE_URL
from data.accordion_expected_answers import (
    EXPECTED_ANSWER_1, EXPECTED_ANSWER_2, EXPECTED_ANSWER_3, EXPECTED_ANSWER_4,
    EXPECTED_ANSWER_5, EXPECTED_ANSWER_6, EXPECTED_ANSWER_7, EXPECTED_ANSWER_8
)
from pages.main_page import MainPage

@allure.feature("Вопросы о важном")
class TestAccordionQuestions:
    @allure.title("Проверка ответа на вопрос 1")
    def test_question_1(self, driver):
        page = MainPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_question_1()
        actual_text = page.get_answer_text_1()
        assert actual_text == EXPECTED_ANSWER_1

    @allure.title("Проверка ответа на вопрос 2")
    def test_question_2(self, driver):
        page = MainPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_question_2()
        actual_text = page.get_answer_text_2()
        assert actual_text == EXPECTED_ANSWER_2

    @allure.title("Проверка ответа на вопрос 3")
    def test_question_3(self, driver):
        page = MainPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_question_3()
        actual_text = page.get_answer_text_3()
        assert actual_text == EXPECTED_ANSWER_3

    @allure.title("Проверка ответа на вопрос 4")
    def test_question_4(self, driver):
        page = MainPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_question_4()
        actual_text = page.get_answer_text_4()
        assert actual_text == EXPECTED_ANSWER_4

    @allure.title("Проверка ответа на вопрос 5")
    def test_question_5(self, driver):
        page = MainPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_question_5()
        actual_text = page.get_answer_text_5()
        assert actual_text == EXPECTED_ANSWER_5

    @allure.title("Проверка ответа на вопрос 6")
    def test_question_6(self, driver):
        page = MainPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_question_6()
        actual_text = page.get_answer_text_6()
        assert actual_text == EXPECTED_ANSWER_6

    @allure.title("Проверка ответа на вопрос 7")
    def test_question_7(self, driver):
        page = MainPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_question_7()
        actual_text = page.get_answer_text_7()
        assert actual_text == EXPECTED_ANSWER_7

    @allure.title("Проверка ответа на вопрос 8")
    def test_question_8(self, driver):
        page = MainPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_question_8()
        actual_text = page.get_answer_text_8()
        assert actual_text == EXPECTED_ANSWER_8
        