from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import Constants
from faker import Faker

faker = Faker()

class TestRegistration:
    def test_registration_successful(self, driver):
        email = faker.email()
        password = Constants.PASSWORD
        #Нажимаем на ЛК
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

        #Нажимаем регистрация
        driver.find_element(By.XPATH, '//a[@href = "/register"]').click()
        #Вводим имя
        driver.find_element(By.XPATH, '//form/fieldset[1]/div/div/input').send_keys('Alexander')
        #Вводим email
        driver.find_element(By.XPATH, '//form/fieldset[2]/div/div/input').send_keys(email)
        #Вводим пароль
        driver.find_element(By.XPATH, '//form/fieldset[3]/div/div/input').send_keys(password)
        #Нажимаем Зарегистрироваться
        driver.find_element(By.XPATH, '//main/div/form//button').click()

        #Вводим email
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'name'))).send_keys(email)
        #Вводим пароль
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, 'Пароль'))).send_keys(password)
        #Нажмаем войти
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Войти'))).click()



        #Нажимаем на ЛК
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Личный Кабинет'))).click()

        #Проверяем что в личном кабинете есть наш e-mail
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute((By.XPATH, '//input[@type = "text" and @name = "name"]'), 'disable value',f'{email}'))



