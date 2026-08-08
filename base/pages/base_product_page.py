from selenium.webdriver.common.by import By

from base.pages.base_page import BasePage
from components.common.quantity_selector import QuantitySelector
from utils.parsers import parse_int, parse_by_pattern
from utils.xpath import has_class, has_text, text_equals


class BaseProductPage(BasePage):
    # Data
    PRICE_PATTERN = r'\d[\d\s]*'

    def __init__(self, driver, url):
        super().__init__(driver)
        self.URL = url

    # Locators
    NAME_LOCATOR = (By.XPATH, f'.//h1[{has_class("product-card__name")}]')
    PRICE_LOCATOR = (By.XPATH, './/span[@data-type = "price"]')
    RATING_LOCATOR = (By.XPATH, './/span[@data-element = "rating-value"]')
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "add-to-cart"]')
    QUANTITY_SELECTOR_LOCATOR = (By.XPATH, './/div[@data-entity = "quantity-block"]')

    def _get_scale_value_locator(self, scale_name):
        return (
            By.XPATH,
            f'.//div[{has_class("scales__item")}]'
            f'[.//div[{has_class("scales__name-text")} and {text_equals(scale_name)}]]'
            f'//span[@data-element = "scale-value"]',
        )

    def _get_characteristic_value_locator(self, characteristic_name):
        return (
            By.XPATH,
            f'.//div[{has_class("characteristics__item")}]'
            f'[.//div[{has_class("characteristic__name")} and {has_text(characteristic_name)}]]'
            f'//div[{has_class("characteristic__value")}]',
        )

    # Components
    @property
    def quantity_selector(self):
        return QuantitySelector(self, self.QUANTITY_SELECTOR_LOCATOR)

    # Properties
    @property
    def name(self):
        return self.get_direct_text(self.NAME_LOCATOR)

    @property
    def price(self):
        return parse_int(
            parse_by_pattern(self.get_text(self.PRICE_LOCATOR), self.PRICE_PATTERN)
        )

    @property
    def quantity(self):
        if self.is_in_cart:
            return self.quantity_selector.quantity
        else:
            return 0

    @property
    def rating(self):
        return float(self.get_text(self.RATING_LOCATOR))

    # Checks
    @property
    def is_in_cart(self):
        return self.quantity_selector.is_displayed

    # Actions
    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON_LOCATOR)
        self.wait_page_stable()
        self.quantity_selector.wait_root_appear()

    def set_quantity(self, value):
        value = int(value)

        if value == self.quantity_selector.quantity:
            return

        self.quantity_selector.set(value)
        self.wait_page_stable()

        if value == 0:
            self.quantity_selector.wait_root_disappear()

    def increase_quantity(self):
        self.quantity_selector.increase()
        self.wait_page_stable()

    def decrease_quantity(self):
        quantity = self.quantity

        self.quantity_selector.decrease()
        self.wait_page_stable()

        if quantity == 1:
            self.quantity_selector.wait_root_disappear()
