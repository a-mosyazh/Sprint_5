from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.paths import RegistrationPage, LoginPage
from utils.helpers import generate_email, generate_password
from global_params import register_url, login_url


def test_validation_registration(driver):
    driver.get(register_url)

    name_field = driver.find_element(By.XPATH, RegistrationPage.name_field)
    email_field = driver.find_element(By.XPATH, RegistrationPage.email_field)
    password_field = driver.find_element(By.XPATH, RegistrationPage.password_field)
    register_btn = driver.find_element(By.XPATH, RegistrationPage.register_btn)

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(register_btn))

    # Проверка того, что пароль должен быть больше 6 символов
    name_field.send_keys('Test User')
    email_field.send_keys(generate_email())
    password_field.send_keys('q')
    register_btn.click()

    assert driver.find_element(By.CSS_SELECTOR, '.input__error.text_type_main-default').text == 'Некорректный пароль'


def test_successful_registration(driver):
    driver.get(register_url)
    driver.refresh()

    name_field = driver.find_element(By.XPATH, RegistrationPage.name_field)
    email_field = driver.find_element(By.XPATH, RegistrationPage.email_field)
    password_field = driver.find_element(By.XPATH, RegistrationPage.password_field)
    register_btn = driver.find_element(By.XPATH, RegistrationPage.register_btn)

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(register_btn))

    name_field.send_keys('Test User')
    email_field.send_keys(generate_email())
    password_field.send_keys(generate_password())

    register_btn.click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginPage.login_btn)))

    assert (driver.find_element(By.XPATH, LoginPage.login_btn).text == 'Войти'
            and driver.current_url == login_url)
