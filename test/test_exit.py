from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Locators



class TestExit:
    #Тестирование Выхода из ЛК
    def test_exit(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Личный Кабинет'))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'Account_button__14Yp3 text text_type_main-medium text_color_inactive'))).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//main/div/h2'))).text == "Вход"