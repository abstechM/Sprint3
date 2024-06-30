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
        driver.find_element(Locators.LK_BUTTOM).click()
        driver.find_element(Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(Locators.ENT_BUTT_LOGIN).click()
        #Проверяем, что вместо кнопки войти теперь кнопка оформить запказ
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//main//div/button'))).text == "Оформить заказ"

    #Вход через кнопку Войти
    def test_enter_button(self, driver):
        driver.find_element(Locators.ENTER_BUTTON).click()
        driver.find_element(Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(Locators.ENT_BUTT_LOGIN).click()
        # Проверяем, что вместо кнопки войти теперь кнопка оформить запказ
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//main//div/button'))).text == "Оформить заказ"

    #Вход через регитсрацию
    def test_regist_button(self, driver):
        email = faker.email()
        password = 123456
        driver.find_element(Locators.ENTER_BUTTON).click()
        driver.find_element(By.XPATH, '//a[@href = "/register"]').click()
        driver.find_element(By.XPATH, '//form/fieldset[1]//input').send_keys('Alexander')
        driver.find_element(By.XPATH, '//form/fieldset[2]//input').send_keys(email)
        driver.find_element(By.XPATH, '//form/fieldset[3]//input').send_keys(password)
        driver.find_element(Locators.ENT_BUTT_LOGIN).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Вход')))
        driver.find_element(Locators.EMAIL).send_keys(email)
        driver.find_element(Locators.PASSWORD).send_keys(password)
        driver.find_element(Locators.ENT_BUTT_LOGIN).click()
        # Проверяем, что вместо кнопки войти теперь кнопка оформить заказ
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//main//div/button'))).text == "Оформить заказ"

    #Вход через восстановление пароля
    def test_psw_recovey(self, driver):
        email = faker.email()
        driver.find_element(Locators.ENTER_BUTTON).click()
        driver.find_element(By.XPATH, '//a[@href = "/forgot-password"]').click()
        driver.find_element(By.XPATH, '//main//div/div/input').send_keys(email)
        driver.find_element(By.XPATH, '//form/button').click()
        assert driver.find_element(By.XPATH, '//main/div/h2').text == "Восстановление пароля"
