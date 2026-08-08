from selenium.webdriver.common.by import By

from base.pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Data
    URL = 'https://www.torrefacto.ru/personal/checkout/'

    # Locators
    FULL_NAME_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_FIO"]')
    EMAIL_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_EMAIL"]')
    PHONE_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_PHONE"]')
    ADDRESS_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_ADDRESS"]')
    POSTAL_CODE_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_ZIP"]')
