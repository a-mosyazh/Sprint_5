import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def setup():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')  # Этот параметр и ниже оставлены для удобства
    # chrome_options.add_argument('--window-size=800,600')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
