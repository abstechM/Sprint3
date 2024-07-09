from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import Locators


class TestTransit:
    #Проверка отображения начинки
    def test_trnasit_nachinki(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.NACHINKA)).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(
            Locators.SECTION_NACHINKA, 'class', f'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'))

    #Проверка отображения соуса
    def test_trnasit_souce(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SAUCE)).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(
            Locators.SECTION_SAUCE, 'class', f'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'))

    #Проверка отображения булок
    def test_trnasit_bulki(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SAUCE)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BULKA)).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(
            Locators.SECTION_BULKA, 'class', f'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'))