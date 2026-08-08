from selenium.webdriver.common.by import By

from base.components.base_product_collection import BaseProductCollection
from components.products.cards.cart.roasted_coffee_cart_product_card import (
    RoastedCoffeeCartProductCard,
)


class CartProductCollection(BaseProductCollection):
    # Data
    CARD_ID_ATTRIBUTE = 'data-basket-id'
    CARD_NAME_LINK_CLASS = 'basket-item__name-title'
    CARD_CLASS_MAP = {
        'roasted': RoastedCoffeeCartProductCard,
    }

    # Locators
    CARD_LOCATOR = (
        By.XPATH,
        './/div[@data-id = "items"]//div[@data-entity = "item"]',
    )

    # Actions
    def remove_all(self):
        for card in self.get_all_cards():
            card.remove_from_cart()
