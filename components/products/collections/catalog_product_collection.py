from selenium.webdriver.common.by import By

from base.components.base_product_collection import BaseProductCollection
from components.products.cards.catalog.roasted_coffee_catalog_product_card import (
    RoastedCoffeeCatalogProductCard,
)
from utils.xpath import has_class


class CatalogProductCollection(BaseProductCollection):
    # Data
    CARD_ID_ATTRIBUTE = 'data-item-id'
    CARD_NAME_LINK_CLASS = 'item-name'
    CARD_CLASS_MAP = {
        'roasted': RoastedCoffeeCatalogProductCard,
    }

    # Locators
    CARD_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("items__list-group")}]' f'//div[@data-entity = "item"]',
    )
