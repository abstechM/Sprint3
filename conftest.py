import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser

    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LK_BUTTOM).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'name'))).send_keys(Constants.EMAIL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'Пароль'))).send_keys(Constants.PASSWORD)
    driver.find_element(By.XPATH, '//main/div/form/button').click()
    return driver