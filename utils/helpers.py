import datetime
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from global_params import email, password
from utils.paths import LoginPage, ConstructorPage, HeaderElement, ProfilePage


def login(driver):
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginPage.login_btn))
    )

    assert driver.find_element(By.XPATH, LoginPage.login_btn).text == 'Войти'

    driver.find_element(By.XPATH, LoginPage.email_field).send_keys(email)
    driver.find_element(By.XPATH, LoginPage.password_field).send_keys(password)
    driver.find_element(By.XPATH, LoginPage.login_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.create_order_btn))
    )
    assert driver.find_element(By.XPATH, ConstructorPage.create_order_btn).text == 'Оформить заказ'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def logout(driver):
    driver.find_element(By.XPATH, HeaderElement.profile_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ProfilePage.logout_btn))
    )
    driver.find_element(By.XPATH, ProfilePage.logout_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginPage.login_btn))
    )
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def generate_email():
    now = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(now)
    unique_part = str(timestamp).replace('.', '')
    generated_email = f'test_user_{unique_part}@example.ru'
    return generated_email


def generate_password():
    generated_password = ''
    for r in range(8):
        letters_upper = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
        letters_lower = 'abcdefghijklmnopqrstuvwxyz'
        numbers = str(random.randint(1, 9))
        symbols = "!@#$%()&^%<>.,/?]["
        elements = [letters_upper, letters_lower, numbers, symbols]
        new_symbol = random.choice(random.choice(elements))
        generated_password = str(generated_password) + str(new_symbol)
    return generated_password
