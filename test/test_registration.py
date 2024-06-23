from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import Constants
from locators import Locators
from faker import Faker

faker = Faker()

class TestBurgers:
    def test_registration(self, driver):
        email = faker.email()
        password = Constants.PASSWORD
        print(email)
        print(password)
        #Нажимаем на ЛК
        driver.find_element(*Locators.LK_BUTTOM).click()

        #Нажимаем регистрация
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
        #Вводим имя
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Alexander')
        #Вводим email
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)
        #Вводим пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys(password)
        #Нажимаем Зарегистрироваться
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        #Вводим email
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//fieldset[1]/div//input'))).send_keys(email)
        #Вводим пароль
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//fieldset[2]/div//input'))).send_keys(password)
        #Нажмаем войти
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Войти'))).click()



        #Нажимаем на ЛК
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LK_BUTTOM)).click()

        #Проверяем что в личном кабинете есть наш e-mail
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute((By.XPATH, '//ul/li[2]//input'), 'disable value',f'{email}'))



