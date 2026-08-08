from selenium.webdriver.common.by import By

from base.components.base_product_card import BaseProductCard
from utils.parsers import parse_by_pattern
from utils.xpath import has_class, text_equals


class BaseCartItemCard(BaseProductCard):
    # Data
    NUMBER_PATTERN = r'^[A-Z]+\+?\s*[0-9]+'

    # Locators
    NAME_LOCATOR = (By.XPATH, f'.//a[{has_class("basket-item__name-title")}]')
    PRICE_LOCATOR = (By.XPATH, f'.//div[{has_class("basket-item__price-value")}]')

    def _get_option_value_locator(self, option_name):
        return (
            By.XPATH,
            f'.//div[{has_class("basket-item__option")}]'
            f'[.//div[{has_class("basket-item__option-name")} and {text_equals(option_name)}]]'
            f'//div[{has_class("basket-item__option-value")}]',
        )

    # Properties
    @property
    def display_name(self):
        return self.get_text(self.NAME_LOCATOR)

    @property
    def number(self):
        return parse_by_pattern(self.display_name, self.NUMBER_PATTERN)

    @property
    def name(self):
        display_name = self.display_name
        number = parse_by_pattern(display_name, self.NUMBER_PATTERN)

        if number is None:
            return display_name

        return display_name.removeprefix(number).strip()

    @property
    def quantity(self):
        return self.quantity_selector.quantity
