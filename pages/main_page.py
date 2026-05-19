from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    question_1 = [By.ID, "accordion__heading-0"]
    question_2 = [By.ID, "accordion__heading-1"]
    question_3 = [By.ID, "accordion__heading-2"]
    question_4 = [By.ID, "accordion__heading-3"]
    question_5 = [By.ID, "accordion__heading-4"]
    question_6 = [By.ID, "accordion__heading-5"]
    question_7 = [By.ID, "accordion__heading-6"]
    question_8 = [By.ID, "accordion__heading-7"]

    answer_1 = [By.ID, "accordion__panel-0"]
    answer_2 = [By.ID, "accordion__panel-1"]
    answer_3 = [By.ID, "accordion__panel-2"]
    answer_4 = [By.ID, "accordion__panel-3"]
    answer_5 = [By.ID, "accordion__panel-4"]
    answer_6 = [By.ID, "accordion__panel-5"]
    answer_7 = [By.ID, "accordion__panel-6"]
    answer_8 = [By.ID, "accordion__panel-7"]

    def _scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def _wait_for_answer_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def click_question_1(self):
        self._scroll_to_element(self.question_1)
        self._js_click(self.question_1)

    def click_question_2(self):
        self._scroll_to_element(self.question_2)
        self._js_click(self.question_2)

    def click_question_3(self):
        self._scroll_to_element(self.question_3)
        self._js_click(self.question_3)

    def click_question_4(self):
        self._scroll_to_element(self.question_4)
        self._js_click(self.question_4)

    def click_question_5(self):
        self._scroll_to_element(self.question_5)
        self._js_click(self.question_5)

    def click_question_6(self):
        self._scroll_to_element(self.question_6)
        self._js_click(self.question_6)

    def click_question_7(self):
        self._scroll_to_element(self.question_7)
        self._js_click(self.question_7)

    def click_question_8(self):
        self._scroll_to_element(self.question_8)
        self._js_click(self.question_8)

    def get_answer_text_1(self):
        self._wait_for_answer_visible(self.answer_1)
        return self.driver.find_element(*self.answer_1).text

    def get_answer_text_2(self):
        self._wait_for_answer_visible(self.answer_2)
        return self.driver.find_element(*self.answer_2).text

    def get_answer_text_3(self):
        self._wait_for_answer_visible(self.answer_3)
        return self.driver.find_element(*self.answer_3).text

    def get_answer_text_4(self):
        self._wait_for_answer_visible(self.answer_4)
        return self.driver.find_element(*self.answer_4).text

    def get_answer_text_5(self):
        self._wait_for_answer_visible(self.answer_5)
        return self.driver.find_element(*self.answer_5).text

    def get_answer_text_6(self):
        self._wait_for_answer_visible(self.answer_6)
        return self.driver.find_element(*self.answer_6).text

    def get_answer_text_7(self):
        self._wait_for_answer_visible(self.answer_7)
        return self.driver.find_element(*self.answer_7).text

    def get_answer_text_8(self):
        self._wait_for_answer_visible(self.answer_8)
        return self.driver.find_element(*self.answer_8).text
    