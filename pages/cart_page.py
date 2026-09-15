from selenium.webdriver.common.by import By

from base.pages.base_page import BasePage
from components.cart_summary import CartSummary
from components.products.collections.cart_gift_collection import CartGiftCollection
from components.products.collections.cart_product_collection import (
    CartProductCollection,
)
from components.promo_codes import PromoCodes
from utils.xpath import has_class


class CartPage(BasePage):
    # Data
    URL = 'https://www.torrefacto.ru/personal/cart/'

    # Locators
    ITEMS_GRID_LOCATOR = (By.XPATH, '//div[@data-id = "basket-content-block"]')
    PROMO_CODES_LOCATOR = (By.XPATH, '//div[@data-block-id = "coupon-block"]')
    SUMMARY_LOCATOR = (By.XPATH, f'//div[{has_class("basket__summary")}]')
    CHECKOUT_BUTTON_LOCATOR = (By.XPATH, f'//a[{has_class("basket__submit-btn")}]')

    # Components
    @property
    def products(self):
        return CartProductCollection(self, self.ITEMS_GRID_LOCATOR)

    @property
    def gifts(self):
        return CartGiftCollection(self, self.ITEMS_GRID_LOCATOR)

    @property
    def promo_codes(self):
        return PromoCodes(self, self.PROMO_CODES_LOCATOR)

    @property
    def summary(self):
        return CartSummary(self, self.SUMMARY_LOCATOR)

    # Properties
    @property
    def is_empty(self):
        return self.products.count == 0

    # Actions
    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON_LOCATOR)
