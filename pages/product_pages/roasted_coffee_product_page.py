from selenium.webdriver.common.by import By

from base.pages.base_product_page import BaseProductPage
from components.common.radio_selector import RadioSelector
from utils.xpath import has_class, primary_or_fallback


class RoastedCoffeeProductPage(BaseProductPage):
    # Data
    OPTION_NAME_CONDITION = primary_or_fallback(
        has_class("product-card__option-value-label-upper-text"),
        has_class("product-card__option-value-label-text"),
        '..//*',
    )

    # Locators
    NUMBER_LOCATOR = (By.XPATH, f'.//div[{has_class("product-card__number")}]')
    GAS_SELECTOR_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("product-card__option-values--gas")}]',
    )
    GRIND_SELECTOR_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("product-card__option-values--mill")}]',
    )
    PACKAGE_SIZE_SELECTOR_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("product-card__option-values--offer-coffee")}]',
    )
    OPTION_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("product-card__option-value")}]',
    )
    OPTION_NAME_LOCATOR = (By.XPATH, f'.//label//*[{OPTION_NAME_CONDITION}]')

    # Components
    @property
    def gas(self):
        return RadioSelector(
            self,
            self.GAS_SELECTOR_LOCATOR,
            self.OPTION_LOCATOR,
            self.OPTION_NAME_LOCATOR,
        )

    @property
    def grind(self):
        return RadioSelector(
            self,
            self.GRIND_SELECTOR_LOCATOR,
            self.OPTION_LOCATOR,
            self.OPTION_NAME_LOCATOR,
        )

    @property
    def package_size(self):
        return RadioSelector(
            self,
            self.PACKAGE_SIZE_SELECTOR_LOCATOR,
            self.OPTION_LOCATOR,
            self.OPTION_NAME_LOCATOR,
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

    @property
    def coffee_type(self):
        return self.get_text(self._get_characteristic_value_locator('Вид кофе'))

    @property
    def processing_method(self):
        return self.get_text(self._get_characteristic_value_locator('Обработка'))
