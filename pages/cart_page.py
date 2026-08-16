from selenium.webdriver.common.by import By

from base.pages.base_page import BasePage
from components.products.collections.cart_gift_collection import CartGiftCollection
from components.products.collections.cart_product_collection import (
    CartProductCollection,
)
from utils.parsers import parse_integer
from utils.xpath import has_class, text_equals, svg_icon


class CartPage(BasePage):
    # Data
    URL = 'https://www.torrefacto.ru/personal/cart/'

    # Locators
    ITEMS_GRID_LOCATOR = (By.XPATH, '//div[@data-id = "basket-content-block"]')
    TOTAL_QUANTITY_LOCATOR = (By.XPATH, '//span[@data-block-id = "summary-quantity"]')
    TOTAL_WEIGHT_LOCATOR = (By.XPATH, '//div[@data-block-id = "weight"]')
    BASE_PRICE_LOCATOR = (By.XPATH, '//div[@data-block-id = "base-price"]')
    DISCOUNT_LOCATOR = (By.XPATH, '//div[@data-block-id = "discount"]')
    TOTAL_PRICE_LOCATOR = (By.XPATH, '//div[@data-block-id = "total"]')
    DISCOUNT_CODE_INPUT_LOCATOR = (By.XPATH, '//input[@id = "discount-coupon"]')
    APPLY_DISCOUNT_BUTTON_LOCATOR = (
        By.XPATH,
        '//button[@data-action = "apply-coupon"]',
    )
    CHECKOUT_BUTTON_LOCATOR = (By.XPATH, f'//a[{has_class("basket__submit-btn")}]')

    def _get_applied_discount_locator(self, discount_code):
        return (
            By.XPATH,
            f'//div[@data-id = "coupon"]'
            f'[.//span[{has_class("coupons-block__item-name")} and {text_equals(discount_code)}]]',
        )

    # Components
    @property
    def products(self):
        return CartProductCollection(self, self.ITEMS_GRID_LOCATOR)

    @property
    def gifts(self):
        return CartGiftCollection(self, self.ITEMS_GRID_LOCATOR)

    # Properties
    @property
    def is_empty(self):
        return self.products.count == 0

    @property
    def total_quantity(self):
        if self.is_empty:
            return 0

        return int(self.get_text(self.TOTAL_QUANTITY_LOCATOR))

    @property
    def total_weight(self):
        if self.is_empty:
            return 0

        return parse_integer(self.get_text(self.TOTAL_WEIGHT_LOCATOR), suffix='г')

    @property
    def base_price(self):
        if self.is_empty:
            return 0

        return parse_integer(self.get_text(self.BASE_PRICE_LOCATOR), suffix='₽')

    @property
    def discount(self):
        if self.is_visible(self.DISCOUNT_LOCATOR):
            return abs(parse_integer(self.get_text(self.DISCOUNT_LOCATOR), suffix='₽'))

        return 0

    @property
    def total_price(self):
        if self.is_empty:
            return 0

        return parse_integer(self.get_text(self.TOTAL_PRICE_LOCATOR), suffix='₽')

    # Actions
    def clear(self):
        self.products.remove_all()

    def apply_discount(self, discount_code):
        self.enter_text(self.DISCOUNT_CODE_INPUT_LOCATOR, discount_code)
        self.click_element(self.APPLY_DISCOUNT_BUTTON_LOCATOR)
        self.wait_page_stable()
        self.get_element(self._get_applied_discount_locator(discount_code))

    def remove_discount(self, discount_code):
        applied_discount_locator = self._get_applied_discount_locator(discount_code)
        remove_button_locator = (
            By.XPATH,
            f'{applied_discount_locator[1]}//{svg_icon("icon-close")}',
        )
        self.click_element(remove_button_locator)
        self.wait_page_stable()
        self.wait_until_not_visible(applied_discount_locator)

    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON_LOCATOR)
