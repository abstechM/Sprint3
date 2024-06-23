from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.XPATH, '//form/fieldset[1]//input')
    PASSWORD = (By.XPATH, '//form/fieldset[2]//input')
    LK_BUTTOM = (By.XPATH, '//header/nav/a')
    ENTER_BUTTON = (By.XPATH, '//main/section[2]/div/button')