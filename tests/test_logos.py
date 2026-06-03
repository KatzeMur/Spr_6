import pytest
from constants import BASE_URL
from pages.order_page import OrderPage

class TestLogos:
    def test_scooter_logo_redirect(self, driver):
        page = OrderPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_logo_scooter()
        assert page._get_current_url() == BASE_URL

    def test_yandex_logo_redirect(self, driver):
        page = OrderPage(driver, BASE_URL)
        page._open(BASE_URL)
        main_window = page._get_current_window()
        page.click_logo_yandex()
        assert "dzen.ru" in page._get_current_url()
        page._switch_to_window(main_window)
        