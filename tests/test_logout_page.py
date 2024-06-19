from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.paths import LoginPage, ConstructorPage, HeaderElement, ProfilePage
from global_params import base_url, email, password, login_url
from utils.helpers import click_on_element


def test_successful_logout(driver):
    driver.get(base_url)

    # Вход в аккаунт
    click_on_element(driver, ConstructorPage.login_to_account_btn)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginPage.login_btn))
    )
    driver.find_element(By.XPATH, LoginPage.email_field).send_keys(email)
    driver.find_element(By.XPATH, LoginPage.password_field).send_keys(password)
    click_on_element(driver, LoginPage.login_btn)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.create_order_btn))
    )

    # Выход из аккаунта
    click_on_element(driver, HeaderElement.profile_btn)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ProfilePage.logout_btn))
    )

    click_on_element(driver, ProfilePage.logout_btn)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginPage.login_btn))
    )

    assert (driver.find_element(By.XPATH, LoginPage.login_btn).text == 'Войти'
            and driver.current_url == login_url)
