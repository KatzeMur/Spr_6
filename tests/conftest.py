import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="function")
def driver():
    service = Service(GeckoDriverManager().install())
    browser = webdriver.Firefox(service=service)
    browser.maximize_window()
    yield browser
    try:
        browser.quit()
    except Exception:
        pass
    