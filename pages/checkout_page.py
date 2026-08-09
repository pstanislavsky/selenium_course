from selenium.webdriver.common.by import By

from base.pages.base_page import BasePage
from utils.parsers import parse_int


class CheckoutPage(BasePage):
    # Data
    URL = 'https://www.torrefacto.ru/personal/checkout/'

    # Locators
    TOTAL_QUANTITY_LOCATOR = (By.XPATH, '//span[@data-id = "basket-sum-quantity"]')
    BASE_PRICE_LOCATOR = (By.XPATH, '//div[@data-id = "basket-sum"]')
    DISCOUNT_LOCATOR = (By.XPATH, '//div[@data-id = "discount-sum"]')
    DELIVERY_LOCATOR = (By.XPATH, '//div[@data-id = "delivery-sum"]')
    TOTAL_PRICE_LOCATOR = (By.XPATH, '//div[@data-id = "total"]')
    FULL_NAME_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_FIO"]')
    EMAIL_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_EMAIL"]')
    PHONE_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_PHONE"]')

    # Properties
    @property
    def total_quantity(self):
        return int(self.get_text(self.TOTAL_QUANTITY_LOCATOR))

    @property
    def base_price(self):
        return parse_int(self.get_text(self.BASE_PRICE_LOCATOR), suffix='₽')

    @property
    def discount(self):
        if self.is_visible(self.DISCOUNT_LOCATOR):
            return abs(parse_int(self.get_text(self.DISCOUNT_LOCATOR), suffix='₽'))

        return 0

    @property
    def delivery(self):
        text = self.get_text(self.DELIVERY_LOCATOR)

        if text == 'Бесплатно':
            return 0

        return parse_int(text, suffix='₽')

    @property
    def total_price(self):
        return parse_int(self.get_text(self.TOTAL_PRICE_LOCATOR), suffix='₽')

    # Actions
    def fill_personal_info(self, full_name, email, phone):
        pass
