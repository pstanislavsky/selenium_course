from selenium.webdriver.common.by import By

from base.components.base_product_card import BaseProductCard
from utils.xpath import has_class, text_equals


class BaseCatalogProductCard(BaseProductCard):
    # Locators
    NAME_LOCATOR = (By.XPATH, f'.//a[{has_class("item-name")}]')
    PRICE_LOCATOR = (By.XPATH, f'.//div[{has_class("item-price__price")}]')
    RATING_LOCATOR = (By.XPATH, f'.//span[{has_class("item-rating__value")}]')
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "add-to-cart"]')

    def _get_scale_value_locator(self, scale_name):
        return (
            By.XPATH,
            f'.//div[{has_class("scales__item")}]'
            f'[.//div[{has_class("scales__name")} and {text_equals(scale_name)}]]'
            f'//div[{has_class("scales__value-text")}]',
        )

    # Properties
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
