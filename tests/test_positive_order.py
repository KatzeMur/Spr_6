import pytest
import allure
from pages.order_page import OrderPage
from constants import BASE_URL

class TestPositiveOrder:
    @pytest.mark.parametrize("entry_point", ["top", "bottom"])
    @pytest.mark.parametrize("name, surname, address, metro, phone", [
        ("Катя", "Тестова", "ул. Тестовая, д.10", "Ботанический сад", "89001234567"),
        ("Гарри", "Поттер", "Тисовая ул., д. 4", "Ботанический сад", "87777777777")
    ])
    def test_positive_order(self, driver, entry_point, name, surname, address, metro, phone):
        driver.get(BASE_URL)
        page = OrderPage(driver)
        if entry_point == "top":
            page.click_order_button_top()
        else:
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
    