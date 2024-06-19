from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.helpers import get_element_position, is_highlighted, has_scrolled, click_on_element
from utils.paths import ConstructorPage
from global_params import base_url


def test_list_of_components_is_scrolled_to_sauce(driver):
    driver.get(base_url)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.bun_card))
    )

    # Получение позиции для дальнейшего сравнения
    bun_default_position = get_element_position(driver, ConstructorPage.bun_card)

    # Скролл до соуса
    click_on_element(driver, ConstructorPage.sauce_tab)

    WebDriverWait(driver, 10).until(lambda d: has_scrolled(d, bun_default_position))
    WebDriverWait(driver, 10).until(lambda d: is_highlighted(d, ConstructorPage.sauce_tab))

    assert (get_element_position(driver, ConstructorPage.bun_card) < bun_default_position
            and is_highlighted(driver, ConstructorPage.sauce_tab))


def test_list_of_components_is_scrolled_to_filling(driver):
    driver.get(base_url)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.bun_card))
    )

    # Получение позиции для дальнейшего сравнения
    bun_default_position = get_element_position(driver, ConstructorPage.bun_card)

    # Скролл до начинки
    click_on_element(driver, ConstructorPage.filling_tab)

    WebDriverWait(driver, 10).until(lambda d: has_scrolled(d, bun_default_position))
    WebDriverWait(driver, 10).until(lambda d: is_highlighted(d, ConstructorPage.filling_tab))

    assert (get_element_position(driver, ConstructorPage.bun_card) < bun_default_position
            and is_highlighted(driver, ConstructorPage.filling_tab))


def test_list_of_components_is_scrolled_to_bun(driver):
    driver.get(base_url)

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ConstructorPage.bun_card))
    )

    # Скролл до начинки
    click_on_element(driver, ConstructorPage.filling_tab)

    WebDriverWait(driver, 10).until(lambda d: is_highlighted(d, ConstructorPage.filling_tab))

    # Получение позиции для дальнейшего сравнения
    bun_sauce_tab = get_element_position(driver, ConstructorPage.bun_card)

    # Скролл до булок
    click_on_element(driver, ConstructorPage.bun_tab)

    WebDriverWait(driver, 10).until(lambda d: has_scrolled(d, bun_sauce_tab))
    WebDriverWait(driver, 10).until(lambda d: is_highlighted(d, ConstructorPage.bun_tab))
    WebDriverWait(driver, 10).until(lambda d: not is_highlighted(d, ConstructorPage.filling_tab))

    assert (bun_sauce_tab != get_element_position(driver, ConstructorPage.bun_card)
            and is_highlighted(driver, ConstructorPage.bun_tab))
