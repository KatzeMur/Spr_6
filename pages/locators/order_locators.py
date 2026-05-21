from selenium.webdriver.common.by import By

ORDER_BUTTON_TOP = (By.CSS_SELECTOR, "button.Button_Button__ra12g:not(.Button_UltraBig__UU3Lp)")
ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[last()]")

ORDER_INPUT_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
ORDER_INPUT_SURNAME = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
ORDER_INPUT_ADDRESS = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
ORDER_INPUT_METRO = (By.CSS_SELECTOR, 'input.select-search__input[placeholder="* Станция метро"]')
ORDER_INPUT_PHONE = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
ORDER_BUTTON_NEXT = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")

ORDER_DROPDOWN_RENTAL_PERIOD = (By.CSS_SELECTOR, "div.Dropdown-placeholder")
ORDER_INPUT_DATE = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
ORDER_BUTTON_ORDER_FINAL = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Middle__1CSJM')]")

ORDER_MODAL_CONFIRM = (By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")
ORDER_BUTTON_MODAL_YES = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Да']")
ORDER_MODAL_SUCCESS = (By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")
ORDER_MODAL_SUCCESS_TEXT = (By.CSS_SELECTOR, "div.Order_Text__2broi")

ORDER_LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
ORDER_LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
