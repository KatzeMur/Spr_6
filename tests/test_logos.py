import pytest
from pages.order_page import OrderPage

class TestLogos:
    def test_scooter_logo_redirect(self, driver, base_url):
        page = OrderPage(driver, base_url)
        page._open(base_url)
        page.click_logo_scooter()
        assert page.get_current_url() == base_url

    def test_yandex_logo_redirect(self, driver, base_url):
        page = OrderPage(driver, base_url)
        page._open(base_url)
        main_window = page._get_current_window()
        page.click_logo_yandex()
        assert "dzen.ru" in page.get_current_url()
        page._switch_to_window(main_window)
        