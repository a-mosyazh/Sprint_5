from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from global_params import name, email
from utils.helpers import login, logout
from utils.paths import ProfilePage, HeaderElement, ConstructorPage


def test_from_main_page_to_profile(setup):
    driver = setup

    driver.get('https://stellarburgers.nomoreparties.site/login')

    login(driver)

    driver.find_element(By.XPATH, HeaderElement.profile_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ProfilePage.save_btn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    assert driver.find_element(By.XPATH, ProfilePage.name_field).get_attribute('value') == name
    assert driver.find_element(By.XPATH, ProfilePage.name_field).get_attribute('disabled') == 'true'
    assert driver.find_element(By.XPATH, ProfilePage.email_field).get_attribute('value') == email
    assert driver.find_element(By.XPATH, ProfilePage.email_field).get_attribute('disabled') == 'true'
    assert driver.find_element(By.XPATH, ProfilePage.password_field).get_attribute('value') == '*****'
    assert driver.find_element(By.XPATH, ProfilePage.password_field).get_attribute('disabled') == 'true'

    logout(driver)


def test_from_profile_to_main_page_via_constructor_btn(setup):
    driver = setup

    driver.get('https://stellarburgers.nomoreparties.site/login')

    login(driver)

    driver.find_element(By.XPATH, HeaderElement.profile_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ProfilePage.save_btn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    driver.find_element(By.XPATH, HeaderElement.constructor_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.create_order_btn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    logout(driver)


def test_from_profile_to_main_page_via_logo(setup):
    driver = setup

    driver.get('https://stellarburgers.nomoreparties.site/login')

    login(driver)

    driver.find_element(By.XPATH, HeaderElement.profile_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ProfilePage.save_btn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    driver.find_element(By.XPATH, HeaderElement.logo).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.create_order_btn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    logout(driver)
    