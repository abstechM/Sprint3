from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import Locators


class TestTransit:
    #Проверка отображения начинки
    def test_trnasit_nachinki(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.NACHINKA)).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SECTION_NACHINKA))

    #Проверка отображения соуса
    def test_trnasit_souce(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SAUCE)).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SECTION_SAUCE))

    #Проверка отображения булок
    def test_trnasit_bulki(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SAUCE)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BULKA)).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SECTION_BULKA))