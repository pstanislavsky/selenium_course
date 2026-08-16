from selenium.webdriver.common.by import By

from base.components.base_cart_item_card import BaseCartItemCard
from utils.parsers import parse_integer
from utils.xpath import has_class


class BaseCartGiftCard(BaseCartItemCard):
    # Locators
    OLD_PRICE_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("basket-item__old-price-value")}]',
    )
    REPLACE_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "replace"]')

    # Properties
    @property
    def old_price(self):
        return parse_integer(self.get_text(self.OLD_PRICE_LOCATOR), suffix='₽')
