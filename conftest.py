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
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL)).send_keys(Constants.EMAIL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PASSWORD)).send_keys(Constants.PASSWORD)
    driver.find_element(Locators.ENT_BUTT_LOGIN).click()
    return driver