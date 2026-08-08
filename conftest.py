import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    # options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()
