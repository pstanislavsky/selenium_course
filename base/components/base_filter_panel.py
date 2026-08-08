from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.filters.controls.range_filter import RangeFilter
from components.filters.controls.switch_filter import SwitchFilter
from utils.xpath import has_class


class BaseFilterPanel(BaseComponent):
    # Locators
    PRICE_FILTER_LOCATOR = (By.XPATH, './/div[@data-code = "PRICE"]')
    SHOW_BOUGHT_FILTER_LOCATOR = (
        By.XPATH,
        './/div[@data-code = "SHOW_BOUGHT"]',
    )
    HIDE_BOUGHT_FILTER_LOCATOR = (
        By.XPATH,
        './/div[@data-code = "HIDE_BOUGHT"]',
    )
    SHOW_UNAVAILABLE_FILTER_LOCATOR = (
        By.XPATH,
        './/div[@data-code = "SHOW_UNAVAILABLE"]',
    )
    RESET_FILTER_BUTTON_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("smart-filter__reset")}]'
        f'//button[@data-action = "filter-reset"]',
    )

    # Components
    @property
    def price(self):
        return RangeFilter(self, self.PRICE_FILTER_LOCATOR)

    @property
    def show_bought(self):
        return SwitchFilter(self, self.SHOW_BOUGHT_FILTER_LOCATOR)

    @property
    def hide_bought(self):
        return SwitchFilter(self, self.HIDE_BOUGHT_FILTER_LOCATOR)

    @property
    def show_unavailable(self):
        return SwitchFilter(self, self.SHOW_UNAVAILABLE_FILTER_LOCATOR)

    # Actions
    def reset(self):
        self.click_element(self.RESET_FILTER_BUTTON_LOCATOR)
        self.wait_page_stable()
