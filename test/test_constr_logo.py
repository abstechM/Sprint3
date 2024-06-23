from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import Constants
from locators import Locators
from faker import Faker

faker = Faker()

class TestBurgers:
    #Тестирование перехода в конструктор
    def test_constr(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LK_BUTTOM)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//header//ul/li[1]/a'))).click()
        assert driver.find_element(By.XPATH, '//main/section/h1').text == "Соберите бургер"
    #Тестирование перехода по ЛОГО
    def test_logo(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LK_BUTTOM)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//header/nav/div/a'))).click()
        assert driver.find_element(By.XPATH, '//main/section/h1').text == "Соберите бургер"