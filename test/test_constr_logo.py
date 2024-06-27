from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestConstructer:
    #Тестирование перехода в конструктор
    def test_constr(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Личный Кабинет'))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//li/a[@href = "/"]'))).click()
        assert driver.find_element(By.XPATH, '//main/section/h1').text == "Соберите бургер"
    #Тестирование перехода по ЛОГО
    def test_logo(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Личный Кабинет'))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[@class = "active"]'))).click()
        assert driver.find_element(By.XPATH, '//main/section/h1').text == "Соберите бургер"