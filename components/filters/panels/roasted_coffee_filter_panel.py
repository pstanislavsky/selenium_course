from selenium.webdriver.common.by import By

from base.components.base_filter_panel import BaseFilterPanel
from components.filters.controls.radio_filter import RadioFilter
from components.filters.controls.checkbox_filter import CheckboxFilter
from components.filters.controls.range_filter import RangeFilter
from components.filters.controls.switch_filter import SwitchFilter


class RoastedCoffeeFilterPanel(BaseFilterPanel):
    # Locators
    ROAST_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "GRPB"]')
    SUITABLE_FOR_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "ROASTING"]')
    BESTSELLER_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "BESTSELLER"]')
    PACKAGE_SIZE_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "PACKING"]')
    ORIGIN_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "GEOGRAPHY"]')
    ACIDITY_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "K2"]')
    BITTERNESS_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "G"]')
    BODY_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "N"]')
    PROCESSING_METHOD_FILTER_LOCATOR = (
        By.XPATH,
        './/div[@data-code = "PROCESSING_METHOD"]',
    )
    BREWING_METHOD_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "GTV"]')
    COFFEE_TYPE_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "VID_KOFE"]')

    # Components
    @property
    def roast(self):
        return CheckboxFilter(self, self.ROAST_FILTER_LOCATOR)

    @property
    def suitable_for(self):
        return CheckboxFilter(self, self.SUITABLE_FOR_FILTER_LOCATOR)

    @property
    def bestseller(self):
        return SwitchFilter(self, self.BESTSELLER_FILTER_LOCATOR)

    @property
    def package_size(self):
        return RadioFilter(self, self.PACKAGE_SIZE_FILTER_LOCATOR)

    @property
    def origin(self):
        return CheckboxFilter(self, self.ORIGIN_FILTER_LOCATOR)

    @property
    def acidity(self):
        return RangeFilter(self, self.ACIDITY_FILTER_LOCATOR)

    @property
    def bitterness(self):
        return RangeFilter(self, self.BITTERNESS_FILTER_LOCATOR)

    @property
    def body(self):
        return RangeFilter(self, self.BODY_FILTER_LOCATOR)

    @property
    def processing_method(self):
        return CheckboxFilter(self, self.PROCESSING_METHOD_FILTER_LOCATOR)

    @property
    def brewing_method(self):
        return CheckboxFilter(self, self.BREWING_METHOD_FILTER_LOCATOR)

    @property
    def coffee_type(self):
        return CheckboxFilter(self, self.COFFEE_TYPE_FILTER_LOCATOR)
