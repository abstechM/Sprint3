from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import Constants
from locators import Locators
from faker import Faker

faker = Faker()

class TestError:
    #Тест на корроткий пароль
    def test_reg_short_password(self, driver):
        email = faker.email()
        password = "12345"
        # Нажимаем на ЛК
        driver.find_element(*Locators.LK_BUTTOM).click()
        driver.find_element(By.XPATH,"//div/p/a[text()= 'Зарегистрироваться']").click()
        driver.find_element(By.XPATH,'//div/form//fieldset[1]//input').send_keys('Alexander')
        driver.find_element(By.XPATH, '//div/form//fieldset[2]//input').send_keys(email)
        driver.find_element(By.XPATH,'//div/form//fieldset[3]//input').send_keys(password)
        driver.find_element(By.XPATH, '//main/div/form/button').click()
        error_pwd = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//p[@class = "input__error text_type_main-default"]'))).text
        assert error_pwd == "Некорректный пароль"