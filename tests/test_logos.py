import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import OrderPage
from constants import BASE_URL

class TestLogos:
    def test_scooter_logo_redirect(self, driver):
        driver.get(BASE_URL)
        page = OrderPage(driver)
        page.click_logo_scooter()
        assert page.get_current_url() == BASE_URL

    def test_yandex_logo_redirect(self, driver):
        driver.get(BASE_URL)
        page = OrderPage(driver)
        main_window = driver.current_window_handle
        page.click_logo_yandex()
        WebDriverWait(driver, 10).until(
            EC.number_of_windows_to_be(2)
        )
        for window in driver.window_handles:
            if window != main_window:
                driver.switch_to.window(window)
                break
        WebDriverWait(driver, 10).until(
            EC.url_contains("dzen.ru")
        )
        assert "dzen.ru" in page.get_current_url()
        driver.switch_to.window(main_window)