from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import Constants
from locators import Locators
from faker import Faker

faker = Faker()

class TestBurgers:
    #Тестирование Выхода из ЛК
    def test_exit(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LK_BUTTOM)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//nav/ul/li[3]/button'))).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//main/div/h2'))).text == "Вход"