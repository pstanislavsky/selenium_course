from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.parsers import parse_integer


class CartSummary(BaseComponent):
    # Locators
    TOTAL_QUANTITY_LOCATOR = (By.XPATH, './/span[@data-block-id = "summary-quantity"]')
    TOTAL_WEIGHT_LOCATOR = (By.XPATH, './/div[@data-block-id = "weight"]')
    BASE_PRICE_LOCATOR = (By.XPATH, './/div[@data-block-id = "base-price"]')
    DISCOUNT_LOCATOR = (By.XPATH, './/div[@data-block-id = "discount"]')
    TOTAL_PRICE_LOCATOR = (By.XPATH, './/div[@data-block-id = "total"]')

    # Properties
    @property
    def total_quantity(self):
        if not self.is_visible(self.TOTAL_QUANTITY_LOCATOR):
            return 0

        return int(self.get_text(self.TOTAL_QUANTITY_LOCATOR))

    @property
    def total_weight(self):
        if not self.is_visible(self.TOTAL_WEIGHT_LOCATOR):
            return 0

        return parse_integer(self.get_text(self.TOTAL_WEIGHT_LOCATOR), suffix='г')

    @property
    def base_price(self):
        if not self.is_visible(self.BASE_PRICE_LOCATOR):
            return 0

        return parse_integer(self.get_text(self.BASE_PRICE_LOCATOR), suffix='₽')

    @property
    def discount(self):
        if not self.is_visible(self.DISCOUNT_LOCATOR):
            return 0

        return abs(parse_integer(self.get_text(self.DISCOUNT_LOCATOR), suffix='₽'))

    @property
    def total_price(self):
        if not self.is_visible(self.TOTAL_PRICE_LOCATOR):
            return 0

        return parse_integer(self.get_text(self.TOTAL_PRICE_LOCATOR), suffix='₽')
