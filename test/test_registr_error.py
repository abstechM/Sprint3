from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        driver.find_element(*Locators.INPUT_NAME_REG).send_keys('Alexander')
        driver.find_element(*Locators.INPUT_EMAIL_REG).send_keys(email)
        driver.find_element(*Locators.INPUT_PSW_REG).send_keys(password)
        driver.find_element(*Locators.ENT_BUTT_LOGIN).click()
        error_pwd = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ATTENT_ERROR)).text
        assert error_pwd == "Некорректный пароль"