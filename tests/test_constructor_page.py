import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.helpers import login, logout
from utils.paths import ConstructorPage


def get_element_position(driver, path):
    element_position = driver.find_element(By.XPATH, path).location
    return element_position['y']


def check_tab_is_highlighted(driver, path):
    return 'tab_type_current' in driver.find_element(By.XPATH, path).get_attribute('class')


def test_list_of_components_is_scrolled(setup):
    driver = setup

    driver.get('https://stellarburgers.nomoreparties.site/login')

    login(driver)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.bun_card))
    )

    # Получение позиций элементов до скролла
    bun_default_position = get_element_position(driver, ConstructorPage.bun_card)
    sauce_default_position = get_element_position(driver, ConstructorPage.sauce_card)
    filling_default_position = get_element_position(driver, ConstructorPage.filling_card)

    # Скролл до соуса
    driver.find_element(By.XPATH, ConstructorPage.sauce_tab).click()
    time.sleep(1)

    # Проверка изменения положений элементов и подсветки только активного таба
    assert get_element_position(driver, ConstructorPage.sauce_card) < sauce_default_position
    assert get_element_position(driver, ConstructorPage.bun_card) < bun_default_position
    assert get_element_position(driver, ConstructorPage.filling_card) < filling_default_position
    assert check_tab_is_highlighted(driver, ConstructorPage.sauce_tab)
    assert not check_tab_is_highlighted(driver, ConstructorPage.bun_tab)
    assert not check_tab_is_highlighted(driver, ConstructorPage.filling_tab)

    # Получение позиций для дальнейшего сравнения
    bun_sauce_tab = get_element_position(driver, ConstructorPage.bun_card)
    sauce_sauce_tab = get_element_position(driver, ConstructorPage.sauce_card)
    filling_sauce_tab = get_element_position(driver, ConstructorPage.filling_card)

    # Скролл до начинки
    driver.find_element(By.XPATH, ConstructorPage.filling_tab).click()
    time.sleep(1)

    assert get_element_position(driver, ConstructorPage.sauce_card) < sauce_sauce_tab
    assert get_element_position(driver, ConstructorPage.bun_card) < bun_sauce_tab
    assert get_element_position(driver, ConstructorPage.filling_card) < filling_sauce_tab
    assert check_tab_is_highlighted(driver, ConstructorPage.filling_tab)
    assert not check_tab_is_highlighted(driver, ConstructorPage.sauce_tab)
    assert not check_tab_is_highlighted(driver, ConstructorPage.bun_tab)

    # Скролл до булок
    driver.find_element(By.XPATH, ConstructorPage.bun_tab).click()
    time.sleep(1)

    assert sauce_sauce_tab < get_element_position(driver, ConstructorPage.sauce_card)
    assert bun_sauce_tab < get_element_position(driver, ConstructorPage.bun_card)
    assert filling_sauce_tab < get_element_position(driver, ConstructorPage.filling_card)
    assert check_tab_is_highlighted(driver, ConstructorPage.bun_tab)
    assert not check_tab_is_highlighted(driver, ConstructorPage.sauce_tab)
    assert not check_tab_is_highlighted(driver, ConstructorPage.filling_tab)

    logout(driver)
    