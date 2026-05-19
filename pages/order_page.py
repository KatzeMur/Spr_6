from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # Локаторы 
    order_button_top = [By.CSS_SELECTOR, "button.Button_Button__ra12g:not(.Button_UltraBig__UU3Lp)"]
    order_button_bottom = [By.XPATH, "(//button[text()='Заказать'])[last()]"]

    input_name = [By.CSS_SELECTOR, 'input[placeholder="* Имя"]']
    input_surname = [By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]']
    input_address = [By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]']
    input_metro = [By.CSS_SELECTOR, 'input.select-search__input[placeholder="* Станция метро"]']
    input_phone = [By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]']
    button_next = [By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM"]

    dropdown_rental_period = [By.CSS_SELECTOR, "div.Dropdown-placeholder"]
    input_date = [By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]']
    button_order_final = [By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Middle__1CSJM')]"]

    modal_confirm = [By.CSS_SELECTOR, "div.Order_Modal__YZ-d3"]
    button_modal_yes = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Да']"]
    modal_success = [By.CSS_SELECTOR, "div.Order_Modal__YZ-d3"]
    modal_success_text = [By.CSS_SELECTOR, "div.Order_Text__2broi"]

    logo_scooter = [By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR"]
    logo_yandex = [By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI"]

    # Вспомогательные методы 
    def _scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def _wait_element_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _wait_element_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )

    # Действия на странице 
    def click_order_button_top(self):
        self._scroll_to_element(self.order_button_top)
        self._js_click(self.order_button_top)

    def click_order_button_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.order_button_bottom)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def click_next_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_next)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("document.querySelector('.Header_Header__214zg').style.pointerEvents = 'none';")
        element.click()

    def fill_name(self, text):
        field = self._wait_element_clickable(self.input_name)
        field.clear()
        field.send_keys(text)

    def fill_surname(self, text):
        field = self._wait_element_clickable(self.input_surname)
        field.clear()
        field.send_keys(text)

    def fill_address(self, text):
        field = self._wait_element_clickable(self.input_address)
        field.clear()
        field.send_keys(text)

    def select_metro(self, text):
        field = self._wait_element_clickable(self.input_metro)
        field.clear()
        field.send_keys(text)
        dropdown_option = (By.CSS_SELECTOR, "button.select-search__option")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(dropdown_option)
        ).click()

    def fill_phone(self, text):
        field = self._wait_element_clickable(self.input_phone)
        field.clear()
        field.send_keys(text)

    def select_rental_period(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.dropdown_rental_period)
        ).click()
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.Dropdown-option"))
        )
        option.click()

    def select_date(self):
        self._js_click(self.input_date)
        day = (By.CSS_SELECTOR, "div.react-datepicker__day[aria-disabled='false']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(day)
        ).click()

    def click_order_final_button(self):
        self._js_click(self.button_order_final)

    def confirm_order(self):
        self._wait_element_visible(self.modal_confirm)
        self._js_click(self.button_modal_yes)

    def is_success_modal_visible(self):
        return self._wait_element_visible(self.modal_success).is_displayed()

    def get_success_order_number(self):
        text = self._wait_element_visible(self.modal_success_text).text
        match = re.search(r'\d+', text)
        return match.group() if match else None

    def click_logo_scooter(self):
        self._js_click(self.logo_scooter)

    def click_logo_yandex(self):
        self._js_click(self.logo_yandex)
        WebDriverWait(self.driver, 5).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        