import datetime
import random

from selenium.webdriver.common.by import By
from utils.paths import ConstructorPage


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


def get_element_position(driver, path):
    element_position = driver.find_element(By.XPATH, path).location
    return element_position['y']


def is_highlighted(driver, path):
    return 'tab_type_current' in driver.find_element(By.XPATH, path).get_attribute('class')


def has_scrolled(driver, initial_position):
    new_position = get_element_position(driver, ConstructorPage.bun_card)
    return new_position != initial_position


def click_on_element(driver, path):
    element = driver.find_element(By.XPATH, path)
    driver.execute_script("arguments[0].click();", element)
