from selenium.webdriver.common.by import By

from base.components.base_cart_item_card import BaseCartItemCard
from utils.parsers import parse_int
from utils.xpath import has_class


class BaseCartProductCard(BaseCartItemCard):
    # Locators
    PRICE_PER_UNIT_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("basket-item__price-per-unit")}]',
    )
    SAVE_FOR_LATER_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "shelve"]')
    REMOVE_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "remove"]')

    # Properties
    @property
    def price_per_unit(self):
        return parse_int(self.get_text(self.PRICE_PER_UNIT_LOCATOR), '₽ / шт.')

    # Actions
    def save_for_later(self):
        self.click_element(self.SAVE_FOR_LATER_BUTTON_LOCATOR)
        self.wait_page_stable()
        self.wait_root_disappear()

    def remove_from_cart(self):
        self.click_element(self.REMOVE_BUTTON_LOCATOR)
        self.wait_page_stable()
        self.wait_root_disappear()

    def set_quantity(self, value):
        value = int(value)

        if value == self.quantity_selector.quantity:
            return

        self.quantity_selector.set(value)
        self.wait_page_stable()

        if value == 0:
            self.wait_root_disappear()

    def increase_quantity(self):
        self.quantity_selector.increase()
        self.wait_page_stable()

    def decrease_quantity(self):
        quantity = self.quantity

        self.quantity_selector.decrease()
        self.wait_page_stable()

        if quantity == 1:
            self.wait_root_disappear()
