from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.paths import LoginPage, HeaderElement, ConstructorPage
from global_params import base_url, register_url, forgot_password_url
from utils.helpers import click_on_element


def test_login_via_login_to_account_button_on_main_page(driver, login_manager):
    driver.get(base_url)

    click_on_element(driver, ConstructorPage.login_to_account_btn)

    login_manager.login()

    assert (driver.find_element(By.XPATH, ConstructorPage.create_order_btn).text == 'Оформить заказ'
            and driver.current_url == base_url)


def test_login_via_profile_button(driver, login_manager):
    driver.get(base_url)

    click_on_element(driver, HeaderElement.profile_btn)

    login_manager.login()

    assert (driver.find_element(By.XPATH, ConstructorPage.create_order_btn).text == 'Оформить заказ'
            and driver.current_url == base_url)


def test_login_via_registration_page(driver, login_manager):
    driver.get(register_url)
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginPage.login_link))
    )

    click_on_element(driver, LoginPage.login_link)

    login_manager.login()

    assert (driver.find_element(By.XPATH, ConstructorPage.create_order_btn).text == 'Оформить заказ'
            and driver.current_url == base_url)


def test_login_via_password_recovery_page(driver, login_manager):
    driver.get(forgot_password_url)

    click_on_element(driver, LoginPage.login_link)

    login_manager.login()

    assert (driver.find_element(By.XPATH, ConstructorPage.create_order_btn).text == 'Оформить заказ'
            and driver.current_url == base_url)
