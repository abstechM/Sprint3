from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Locators



class TestExit:
    #Тестирование Выхода из ЛК
    def test_exit(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LK_BUTTOM)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_EXIT)).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.HEADER_ENT)).text == "Вход"