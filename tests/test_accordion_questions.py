import pytest
import allure
from pages.main_page import MainPage
from constants import BASE_URL

@pytest.mark.parametrize("click_method, get_method, expected_text", [
    ("click_question_1", "get_answer_text_1", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    ("click_question_2", "get_answer_text_2", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    ("click_question_3", "get_answer_text_3", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    ("click_question_4", "get_answer_text_4", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    ("click_question_5", "get_answer_text_5", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    ("click_question_6", "get_answer_text_6", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    ("click_question_7", "get_answer_text_7", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    ("click_question_8", "get_answer_text_8", "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
])
@allure.feature("Вопросы о важном")
@allure.title("Проверка раскрытия вопроса в аккордеоне")
@allure.description("Тест проверяет, что при клике на вопрос раскрывается правильный ответ")
def test_accordion_question(driver, click_method, get_method, expected_text):
    driver.get(BASE_URL)
    page = MainPage(driver)
    getattr(page, click_method)()
    actual_text = getattr(page, get_method)()
    assert actual_text == expected_text, f"Ожидался текст: {expected_text}, но получен: {actual_text}"
    