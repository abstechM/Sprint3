from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.CLASS_NAME, 'name')
    PASSWORD = (By.XPATH, 'Пароль')
    #Кнопка личный кабинет
    LK_BUTTOM = (By.LINK_TEXT, 'Личный Кабинет')
    #Кнопка войти на главной старницу
    ENTER_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg')
    #Кнопка войти из страницы авторизации
    ENT_BUTT_LOGIN = (By.CLASS_NAME, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa')