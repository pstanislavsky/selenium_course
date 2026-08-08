from base.components.base_cart_product_card import BaseCartProductCard
from pages.product_pages.roasted_coffee_product_page import RoastedCoffeeProductPage
from utils.parsers import parse_int


class RoastedCoffeeCartProductCard(BaseCartProductCard):
    # Data
    PRODUCT_PAGE_CLASS = RoastedCoffeeProductPage

    # Properties
    @property
    def package_size(self):
        return parse_int(
            self.get_text(self._get_option_value_locator('Упаковка')), suffix='г'
        )

    @property
    def gas(self):
        return self.get_text(self._get_option_value_locator('Азотирование'))

    @property
    def grind(self):
        return self.get_text(self._get_option_value_locator('Помол'))
