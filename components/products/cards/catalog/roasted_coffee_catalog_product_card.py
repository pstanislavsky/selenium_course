from selenium.webdriver.common.by import By

from base.components.base_catalog_product_card import BaseCatalogProductCard
from components.common.dropdown_selector import DropdownSelector
from components.common.radio_selector import RadioSelector
from pages.product_pages.roasted_coffee_product_page import RoastedCoffeeProductPage
from utils.xpath import has_class


class RoastedCoffeeCatalogProductCard(BaseCatalogProductCard):
    # Data
    PRODUCT_PAGE_CLASS = RoastedCoffeeProductPage

    # Locators
    NUMBER_LOCATOR = (By.XPATH, f'.//a[{has_class("item-number")}]')
    PACKAGE_SIZE_SELECTOR_LOCATOR = (By.XPATH, f'.//div[{has_class("item-offers")}]')
    PACKAGE_SIZE_OPTION_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("item-offers__offer")}]',
    )
    PACKAGE_SIZE_OPTION_NAME_LOCATOR = (
        By.XPATH,
        f'.//span[{has_class("item-offers__label-text")}]',
    )
    GAS_DROPDOWN_LOCATOR = (By.XPATH, f'.//div[{has_class("option-gas")}]')
    GRIND_DROPDOWN_LOCATOR = (By.XPATH, f'.//div[{has_class("option-mill")}]')
    DROPDOWN_OPTION_LOCATOR = (By.XPATH, f'.//button[@data-action = "set-option"]')

    # Components
    @property
    def package_size(self):
        return RadioSelector(
            self,
            self.PACKAGE_SIZE_SELECTOR_LOCATOR,
            self.PACKAGE_SIZE_OPTION_LOCATOR,
            self.PACKAGE_SIZE_OPTION_NAME_LOCATOR,
        )

    @property
    def gas(self):
        return DropdownSelector(
            self, self.GAS_DROPDOWN_LOCATOR, self.DROPDOWN_OPTION_LOCATOR
        )

    @property
    def grind(self):
        return DropdownSelector(
            self, self.GRIND_DROPDOWN_LOCATOR, self.DROPDOWN_OPTION_LOCATOR
        )

    # Properties
    @property
    def number(self):
        return self.get_text(self.NUMBER_LOCATOR)

    @property
    def acidity(self):
        return int(self.get_text(self._get_scale_value_locator('Кислинка')))

    @property
    def bitterness(self):
        return int(self.get_text(self._get_scale_value_locator('Горчинка')))

    @property
    def body(self):
        return int(self.get_text(self._get_scale_value_locator('Насыщенность')))
