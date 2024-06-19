from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.paths import ProfilePage, HeaderElement, ConstructorPage
from global_params import base_url, login_url, profile_url
from utils.helpers import click_on_element


def test_from_main_page_to_profile(driver, login_manager):
    driver.get(login_url)

    login_manager.login()

    click_on_element(driver, HeaderElement.profile_btn)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ProfilePage.save_btn)))

    assert driver.current_url == profile_url


def test_from_profile_to_main_page_via_constructor_btn(driver, login_manager):
    driver.get(login_url)

    login_manager.login()

    click_on_element(driver, HeaderElement.profile_btn)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ProfilePage.save_btn))
    )

    click_on_element(driver, HeaderElement.constructor_btn)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.create_order_btn))
    )

    assert driver.current_url == base_url


def test_from_profile_to_main_page_via_logo(driver, login_manager):
    driver.get(login_url)

    login_manager.login()

    click_on_element(driver, HeaderElement.profile_btn)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ProfilePage.save_btn)))

    driver.find_element(By.XPATH, HeaderElement.logo).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.create_order_btn)))

    assert driver.current_url == base_url
