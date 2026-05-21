from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
from pages.locators.order_locators import (
    ORDER_BUTTON_TOP, ORDER_BUTTON_BOTTOM,
    ORDER_INPUT_NAME, ORDER_INPUT_SURNAME, ORDER_INPUT_ADDRESS, ORDER_INPUT_METRO, ORDER_INPUT_PHONE,
    ORDER_BUTTON_NEXT,
    ORDER_DROPDOWN_RENTAL_PERIOD, ORDER_INPUT_DATE, ORDER_BUTTON_ORDER_FINAL,
    ORDER_MODAL_CONFIRM, ORDER_BUTTON_MODAL_YES,
    ORDER_MODAL_SUCCESS, ORDER_MODAL_SUCCESS_TEXT,
    ORDER_LOGO_SCOOTER, ORDER_LOGO_YANDEX
)
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def click_order_button_top(self):
        self._scroll_to_element(ORDER_BUTTON_TOP)
        self._js_click(ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self._execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = self._wait_for_condition(ORDER_BUTTON_BOTTOM, EC.presence_of_element_located, 15)
        self._execute_script("arguments[0].click();", element)

    def click_next_button(self):
        element = self._wait_element_clickable(ORDER_BUTTON_NEXT)
        self._execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self._execute_script("document.querySelector('.Header_Header__214zg').style.pointerEvents = 'none';")
        element.click()

    def fill_name(self, text):
        field = self._wait_element_clickable(ORDER_INPUT_NAME)
        field.clear()
        field.send_keys(text)

    def fill_surname(self, text):
        field = self._wait_element_clickable(ORDER_INPUT_SURNAME)
        field.clear()
        field.send_keys(text)

    def fill_address(self, text):
        field = self._wait_element_clickable(ORDER_INPUT_ADDRESS)
        field.clear()
        field.send_keys(text)

    def select_metro(self, text):
        field = self._wait_element_clickable(ORDER_INPUT_METRO)
        field.clear()
        field.send_keys(text)
        dropdown_option = (By.CSS_SELECTOR, "button.select-search__option")
        self._wait_element_clickable(dropdown_option).click()

    def fill_phone(self, text):
        field = self._wait_element_clickable(ORDER_INPUT_PHONE)
        field.clear()
        field.send_keys(text)

    def select_rental_period(self):
        self._wait_element_clickable(ORDER_DROPDOWN_RENTAL_PERIOD).click()
        option = self._wait_element_clickable((By.CSS_SELECTOR, "div.Dropdown-option"))
        option.click()

    def select_date(self):
        self._js_click(ORDER_INPUT_DATE)
        day = (By.CSS_SELECTOR, "div.react-datepicker__day[aria-disabled='false']")
        self._wait_element_clickable(day).click()

    def click_order_final_button(self):
        self._js_click(ORDER_BUTTON_ORDER_FINAL)

    def confirm_order(self):
        self._wait_element_visible(ORDER_MODAL_CONFIRM)
        self._js_click(ORDER_BUTTON_MODAL_YES)

    def is_success_modal_visible(self):
        return self._wait_element_visible(ORDER_MODAL_SUCCESS).is_displayed()

    def get_success_order_number(self):
        text = self._get_element_text(ORDER_MODAL_SUCCESS_TEXT)
        match = re.search(r'\d+', text)
        return match.group() if match else None

    def click_logo_scooter(self):
        self._js_click(ORDER_LOGO_SCOOTER)

    def click_logo_yandex(self):
        self._js_click(ORDER_LOGO_YANDEX)
        self._wait_for_new_window()
        self._switch_to_window(self._get_window_handles()[-1])
        self._wait_for_url_contains("dzen.ru")

    def get_current_url(self):
        return self._get_current_url()

    def switch_to_main_window(self):
        self._switch_to_window(self._get_window_handles()[0])
