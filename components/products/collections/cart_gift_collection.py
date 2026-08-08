from selenium.webdriver.common.by import By

from base.components.base_product_collection import BaseProductCollection
from components.products.cards.gifts.chocolate_cart_gift_card import (
    ChocolateCartGiftCard,
)
from components.products.cards.gifts.dried_fruits_cart_gift_card import (
    DriedFruitsCartGiftCard,
)
from components.products.cards.gifts.roasted_coffee_cart_gift_card import (
    RoastedCoffeeCartGiftCard,
)
from components.products.cards.gifts.tea_cart_gift_card import (
    TeaCartGiftCard,
)


class CartGiftCollection(BaseProductCollection):
    # Data
    CARD_ID_ATTRIBUTE = 'data-index'
    CARD_NAME_LINK_CLASS = 'basket-item__name-title'
    CARD_CLASS_MAP = {
        'roasted': RoastedCoffeeCartGiftCard,
        'cocoa': ChocolateCartGiftCard,
        'tea': TeaCartGiftCard,
        'nuts-dried-fruits': DriedFruitsCartGiftCard,
    }

    # Locators
    CARD_LOCATOR = (
        By.XPATH,
        './/div[@data-id = "gifts"]//div[@data-entity = "item"]',
    )
