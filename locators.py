from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.CLASS_NAME, 'name')
    PASSWORD = (By.XPATH, 'Пароль')
    LK_BUTTOM = (By.LINK_TEXT, 'Личный Кабинет')
    ENTER_BUTTON = (By.XPATH, '//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')