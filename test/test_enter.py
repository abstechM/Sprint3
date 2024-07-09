from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import Constants
from faker import Faker
from locators import Locators
faker = Faker()
class TestnEnter:
    #Вход чрезе кнопку Личный кабинет
    def test_enter_lk_button(self, driver):
        driver.find_element(*Locators.LK_BUTTOM).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.ENT_BUTT_LOGIN).click()
        #Проверяем, что вместо кнопки войти теперь кнопка оформить запказ
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text == "Оформить заказ"

    #Вход через кнопку Войти
    def test_enter_button(self, driver):
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.ENT_BUTT_LOGIN).click()
        # Проверяем, что вместо кнопки войти теперь кнопка оформить запказ
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text == "Оформить заказ"

    #Вход через регитсрацию
    def test_regist_button(self, driver):
        email = faker.email()
        password = 123456
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        driver.find_element(*Locators.INPUT_NAME_REG).send_keys('Alexander')
        driver.find_element(*Locators.INPUT_EMAIL_REG).send_keys(email)
        driver.find_element(*Locators.INPUT_PSW_REG).send_keys(password)
        driver.find_element(*Locators.ENT_BUTT_LOGIN).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Вход')))
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENT_BUTT_LOGIN).click()
        # Проверяем, что вместо кнопки войти теперь кнопка оформить заказ
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text == "Оформить заказ"

    #Вход через восстановление пароля
    def test_psw_recovey(self, driver):
        email = faker.email()
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.BUTTON_RECOV_PSW).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.ENT_BUTT_LOGIN).click()
        assert driver.find_element(*Locators.HEADER_REC_PWD).text == "Восстановление пароля"
