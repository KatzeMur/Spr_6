from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def _scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self._execute_script("arguments[0].scrollIntoView();", element)

    def _js_click(self, locator):
        element = self.driver.find_element(*locator)
        self._execute_script("arguments[0].click();", element)

    def _wait_element_visible(self, locator, timeout=5):
        return self._wait_for_condition(locator, EC.visibility_of_element_located, timeout)

    def _wait_element_clickable(self, locator, timeout=5):
        return self._wait_for_condition(locator, EC.element_to_be_clickable, timeout)

    def _execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    def _wait_for_condition(self, locator, condition, timeout=5):
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def _get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def _get_current_url(self):
        return self.driver.current_url

    def _get_current_window(self):
        return self.driver.current_window_handle

    def _get_window_handles(self):
        return self.driver.window_handles

    def _switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def _wait_for_new_window(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)

    def _wait_for_url_contains(self, text, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def _open(self, url):
        """Открывает страницу по указанному URL"""
        self.driver.get(url)
        