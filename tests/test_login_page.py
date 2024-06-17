from selenium.webdriver.common.by import By

from utils.helpers import login, logout
from utils.paths import LoginPage, HeaderElement, ConstructorPage


def test_login_via_login_to_account_button_on_main_page(setup):
    driver = setup
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, ConstructorPage.login_to_account_btn).click()
    login(driver)
    logout(driver)


def test_login_via_profile_button(setup):
    driver = setup
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, HeaderElement.profile_btn).click()
    login(driver)
    logout(driver)


def test_login_via_registration_page(setup):
    driver = setup
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(By.XPATH, LoginPage.login_link).click()
    login(driver)
    logout(driver)


def test_login_via_password_recovery_page(setup):
    driver = setup
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

    driver.find_element(By.XPATH, LoginPage.login_link).click()
    login(driver)
    logout(driver)
