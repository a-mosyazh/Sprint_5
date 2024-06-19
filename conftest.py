import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from global_params import email, password
from utils.paths import LoginPage, HeaderElement, ProfilePage, ConstructorPage
from utils.helpers import click_on_element


@pytest.fixture(scope='session')
def driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


class LoginManager:
    def __init__(self, driver):
        self.driver = driver
        self.logged_in = False

    def login(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPage.login_btn))
        )
        self.driver.find_element(By.XPATH, LoginPage.email_field).send_keys(email)
        self.driver.find_element(By.XPATH, LoginPage.password_field).send_keys(password)
        click_on_element(self.driver, LoginPage.login_btn)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.create_order_btn))
        )
        self.logged_in = True

    def logout(self):
        if self.logged_in:
            click_on_element(self.driver, HeaderElement.profile_btn)
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, ProfilePage.logout_btn))
            )
            click_on_element(self.driver, ProfilePage.logout_btn)
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, LoginPage.login_btn))
            )
            self.logged_in = False


@pytest.fixture
def login_manager(driver):
    manager = LoginManager(driver)
    yield manager
    manager.logout()
