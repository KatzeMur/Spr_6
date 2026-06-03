from pages.locators.main_locators import (
    MAIN_QUESTION_1, MAIN_QUESTION_2, MAIN_QUESTION_3, MAIN_QUESTION_4,
    MAIN_QUESTION_5, MAIN_QUESTION_6, MAIN_QUESTION_7, MAIN_QUESTION_8,
    MAIN_ANSWER_1, MAIN_ANSWER_2, MAIN_ANSWER_3, MAIN_ANSWER_4,
    MAIN_ANSWER_5, MAIN_ANSWER_6, MAIN_ANSWER_7, MAIN_ANSWER_8
)
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def click_question_1(self):
        self._scroll_to_element(MAIN_QUESTION_1)
        self._js_click(MAIN_QUESTION_1)

    def click_question_2(self):
        self._scroll_to_element(MAIN_QUESTION_2)
        self._js_click(MAIN_QUESTION_2)

    def click_question_3(self):
        self._scroll_to_element(MAIN_QUESTION_3)
        self._js_click(MAIN_QUESTION_3)

    def click_question_4(self):
        self._scroll_to_element(MAIN_QUESTION_4)
        self._js_click(MAIN_QUESTION_4)

    def click_question_5(self):
        self._scroll_to_element(MAIN_QUESTION_5)
        self._js_click(MAIN_QUESTION_5)

    def click_question_6(self):
        self._scroll_to_element(MAIN_QUESTION_6)
        self._js_click(MAIN_QUESTION_6)

    def click_question_7(self):
        self._scroll_to_element(MAIN_QUESTION_7)
        self._js_click(MAIN_QUESTION_7)

    def click_question_8(self):
        self._scroll_to_element(MAIN_QUESTION_8)
        self._js_click(MAIN_QUESTION_8)

    def get_answer_text_1(self):
        self._wait_element_visible(MAIN_ANSWER_1)
        return self._get_element_text(MAIN_ANSWER_1)

    def get_answer_text_2(self):
        self._wait_element_visible(MAIN_ANSWER_2)
        return self._get_element_text(MAIN_ANSWER_2)

    def get_answer_text_3(self):
        self._wait_element_visible(MAIN_ANSWER_3)
        return self._get_element_text(MAIN_ANSWER_3)

    def get_answer_text_4(self):
        self._wait_element_visible(MAIN_ANSWER_4)
        return self._get_element_text(MAIN_ANSWER_4)

    def get_answer_text_5(self):
        self._wait_element_visible(MAIN_ANSWER_5)
        return self._get_element_text(MAIN_ANSWER_5)

    def get_answer_text_6(self):
        self._wait_element_visible(MAIN_ANSWER_6)
        return self._get_element_text(MAIN_ANSWER_6)

    def get_answer_text_7(self):
        self._wait_element_visible(MAIN_ANSWER_7)
        return self._get_element_text(MAIN_ANSWER_7)

    def get_answer_text_8(self):
        self._wait_element_visible(MAIN_ANSWER_8)
        return self._get_element_text(MAIN_ANSWER_8)
    