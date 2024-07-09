from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Locators

class TestConstructer:
    #Тестирование перехода в конструктор
    def test_constr(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LK_BUTTOM)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_CONSTR)).click()
        assert driver.find_element(Locators.HEADER).text == "Соберите бургер"
    #Тестирование перехода по ЛОГО
    def test_logo(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LK_BUTTOM)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGO)).click()
        assert driver.find_element(Locators.HEADER).text == "Соберите бургер"