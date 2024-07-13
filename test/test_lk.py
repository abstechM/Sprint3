from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import Constants
from locators import Locators



class TestLk:
    #Тестирование того, что мы находимся в ЛК
    def test_area_lk(self, login):
        driver = login
        email = Constants.EMAIL
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LK_BUTTOM)).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.INPUT_LK, 'disable value',f'{email}'))

