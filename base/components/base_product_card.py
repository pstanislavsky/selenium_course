from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.common.quantity_selector import QuantitySelector
from utils.parsers import parse_integer


class BaseProductCard(BaseComponent):
    # Data
    PRODUCT_PAGE_CLASS = None

    # Locators
    NAME_LOCATOR = None
    PRICE_LOCATOR = None
    QUANTITY_SELECTOR_LOCATOR = (By.XPATH, './/div[@data-entity = "quantity-block"]')

    # Components
    @property
    def quantity_selector(self):
        return QuantitySelector(self, self.QUANTITY_SELECTOR_LOCATOR)

    # Properties
    @property
    def link(self):
        return self.get_element(self.NAME_LOCATOR).get_attribute('href')

    @property
    def name(self):
        return self.get_text(self.NAME_LOCATOR)

    @property
    def price(self):
        return parse_integer(self.get_text(self.PRICE_LOCATOR), suffix='₽')

    # Actions
    def open(self):
        link = self.link
        self.click_element(self.NAME_LOCATOR)

        return self.PRODUCT_PAGE_CLASS(self.driver, link)
