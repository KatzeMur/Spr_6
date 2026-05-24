import pytest
import allure
from constants import BASE_URL
from pages.order_page import OrderPage

class TestPositiveOrder:
    @pytest.mark.parametrize("name, surname, address, metro, phone", [
        ("Катя", "Тестова", "ул. Тестовая, д.10", "Ботанический сад", "89001234567"),
        ("Гарри", "Поттер", "Тисовая ул., д. 4", "Ботанический сад", "87777777777")
    ])
    @allure.feature("Заказ самоката")
    @allure.title("Заказ через кнопку вверху страницы")
    def test_order_from_top(self, driver, name, surname, address, metro, phone):
        page = OrderPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_order_button_top()
        page.fill_name(name)
        page.fill_surname(surname)
        page.fill_address(address)
        page.select_metro(metro)
        page.fill_phone(phone)
        page.click_next_button()
        page.select_rental_period()
        page.select_date()
        page.click_order_final_button()
        page.confirm_order()
        assert page.is_success_modal_visible()

    @pytest.mark.parametrize("name, surname, address, metro, phone", [
        ("Катя", "Тестова", "ул. Тестовая, д.10", "Ботанический сад", "89001234567"),
        ("Гарри", "Поттер", "Тисовая ул., д. 4", "Ботанический сад", "87777777777")
    ])
    @allure.feature("Заказ самоката")
    @allure.title("Заказ через кнопку внизу страницы")
    def test_order_from_bottom(self, driver, name, surname, address, metro, phone):
        page = OrderPage(driver, BASE_URL)
        page._open(BASE_URL)
        page.click_order_button_bottom()
        page.fill_name(name)
        page.fill_surname(surname)
        page.fill_address(address)
        page.select_metro(metro)
        page.fill_phone(phone)
        page.click_next_button()
        page.select_rental_period()
        page.select_date()
        page.click_order_final_button()
        page.confirm_order()
        assert page.is_success_modal_visible()
        