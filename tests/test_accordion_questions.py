import pytest
import allure
from pages.main_page import MainPage

@allure.feature("Вопросы о важном")
class TestAccordionQuestions:
    @allure.title("Проверка ответа на вопрос 1")
    def test_question_1(self, driver, base_url):
        page = MainPage(driver, base_url)
        page._open(base_url)
        page.click_question_1()
        actual_text = page.get_answer_text_1()
        assert actual_text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title("Проверка ответа на вопрос 2")
    def test_question_2(self, driver, base_url):
        page = MainPage(driver, base_url)
        page._open(base_url)
        page.click_question_2()
        actual_text = page.get_answer_text_2()
        assert actual_text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    @allure.title("Проверка ответа на вопрос 3")
    def test_question_3(self, driver, base_url):
        page = MainPage(driver, base_url)
        page._open(base_url)
        page.click_question_3()
        actual_text = page.get_answer_text_3()
        assert actual_text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title("Проверка ответа на вопрос 4")
    def test_question_4(self, driver, base_url):
        page = MainPage(driver, base_url)
        page._open(base_url)
        page.click_question_4()
        actual_text = page.get_answer_text_4()
        assert actual_text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title("Проверка ответа на вопрос 5")
    def test_question_5(self, driver, base_url):
        page = MainPage(driver, base_url)
        page._open(base_url)
        page.click_question_5()
        actual_text = page.get_answer_text_5()
        assert actual_text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    @allure.title("Проверка ответа на вопрос 6")
    def test_question_6(self, driver, base_url):
        page = MainPage(driver, base_url)
        page._open(base_url)
        page.click_question_6()
        actual_text = page.get_answer_text_6()
        assert actual_text == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @allure.title("Проверка ответа на вопрос 7")
    def test_question_7(self, driver, base_url):
        page = MainPage(driver, base_url)
        page._open(base_url)
        page.click_question_7()
        actual_text = page.get_answer_text_7()
        assert actual_text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title("Проверка ответа на вопрос 8")
    def test_question_8(self, driver, base_url):
        page = MainPage(driver, base_url)
        page._open(base_url)
        page.click_question_8()
        actual_text = page.get_answer_text_8()
        assert actual_text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        