from base.components.base_cart_gift_card import BaseCartGiftCard
from pages.product_pages.roasted_coffee_product_page import RoastedCoffeeProductPage
from utils.parsers import parse_integer


class RoastedCoffeeCartGiftCard(BaseCartGiftCard):
    # Data
    PRODUCT_PAGE_CLASS = RoastedCoffeeProductPage

    # Properties
    @property
    def package_size(self):
        return parse_integer(
            self.get_text(self._get_option_value_locator('Упаковка')), suffix='г'
        )

    @property
    def grind(self):
        return self.get_text(self._get_option_value_locator('Помол'))
