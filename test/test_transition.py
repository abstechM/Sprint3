from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class TestTransit:
    #Проверка отображения начинки
    def test_trnasit_nachinki(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//section/div//div[3]/span'))).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(
            (By.XPATH, '//section/div//div[3]'), 'class', f'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'))

    #Проверка отображения соуса
    def test_trnasit_souce(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//section/div//div[2]/span'))).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(
            (By.XPATH, '//section/div//div[2]'), 'class', f'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'))

    #Проверка отображения начинки
    def test_trnasit_bulki(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//section/div//div[2]/span'))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//section/div//div[1]/span'))).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(
            (By.XPATH, '//section/div//div[1]'), 'class', f'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'))