from selenium.webdriver.common.by import By

from utils.helpers import login, logout
from utils.paths import LoginPage, ConstructorPage


def test_successful_logout(setup):
    driver = setup
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, ConstructorPage.login_to_account_btn).click()
    login(driver)
    logout(driver)
    assert driver.find_element(By.XPATH, LoginPage.login_btn).text == 'Войти'
