from selenium.webdriver.common.by import By

from base.pages.base_page import BasePage
from components.products.collections.cart_gift_collection import CartGiftCollection
from components.products.collections.cart_product_collection import (
    CartProductCollection,
)
from utils.parsers import parse_int
from utils.xpath import has_class


class CartPage(BasePage):
    # Data
    URL = 'https://www.torrefacto.ru/personal/cart/'

    # Locators
    PRODUCT_GRID_LOCATOR = (By.XPATH, '//div[@data-id = "basket-content-block"]')
    TOTAL_PRICE_LOCATOR = (By.XPATH, '//div[@data-block-id = "total"]')
    TOTAL_QUANTITY_LOCATOR = (By.XPATH, '//span[@data-block-id = "summary-quantity"]')
    TOTAL_WEIGHT_LOCATOR = (By.XPATH, '//div[@data-block-id = "weight"]')
    DISCOUNT_INPUT_LOCATOR = (By.XPATH, '//input[@id = "discount-coupon"]')
    CHECKOUT_BUTTON_LOCATOR = (By.XPATH, f'//a[{has_class("basket__submit-btn")}]')

    # Components
    @property
    def products(self):
        return CartProductCollection(self, self.PRODUCT_GRID_LOCATOR)

    @property
    def gifts(self):
        return CartGiftCollection(self, self.PRODUCT_GRID_LOCATOR)

    # Properties
    @property
    def is_empty(self):
        return self.products.count == 0

    @property
    def total_price(self):
        return parse_int(self.get_text(self.TOTAL_PRICE_LOCATOR), suffix='₽')

    @property
    def total_quantity(self):
        return int(self.get_text(self.TOTAL_QUANTITY_LOCATOR))

    @property
    def total_weight(self):
        return parse_int(self.get_text(self.TOTAL_WEIGHT_LOCATOR), suffix='г')

    # Actions
    def clear(self):
        self.products.remove_all()

    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON_LOCATOR)
