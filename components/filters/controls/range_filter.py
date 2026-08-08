from selenium.webdriver.common.by import By

from base.components.base_filter import BaseFilter
from utils.xpath import has_class


class RangeFilter(BaseFilter):
    # Locators
    MIN_VALUE_INPUT_LOCATOR = (By.XPATH, './/input[contains(@id, "MIN")]')
    MAX_VALUE_INPUT_LOCATOR = (By.XPATH, './/input[contains(@id, "MAX")]')
    MIN_VALUE_SLIDER_HANDLE_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("min-slider-handle")}]',
    )
    MAX_VALUE_SLIDER_HANDLE_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("max-slider-handle")}]',
    )

    # Properties
    @property
    def min_value(self):
        return int(
            self.get_element(self.MIN_VALUE_INPUT_LOCATOR).get_attribute('value')
        )

    @property
    def max_value(self):
        return int(
            self.get_element(self.MAX_VALUE_INPUT_LOCATOR).get_attribute('value')
        )

    # Actions
    def set_min_value(self, value):
        self.enter_text_and_submit(self.MIN_VALUE_INPUT_LOCATOR, value)
        self.wait_page_stable()

    def set_max_value(self, value):
        self.enter_text_and_submit(self.MAX_VALUE_INPUT_LOCATOR, value)
        self.wait_page_stable()

    def set_range(self, min_value, max_value):
        self.set_min_value(min_value)
        self.set_max_value(max_value)

    def move_min_value_slider_handle(self, offset):
        self.drag_element_by_offset(
            self.MIN_VALUE_SLIDER_HANDLE_LOCATOR, x_offset=offset, y_offset=0
        )
        self.wait_page_stable()

    def move_max_value_slider_handle(self, offset):
        self.drag_element_by_offset(
            self.MAX_VALUE_SLIDER_HANDLE_LOCATOR, x_offset=offset, y_offset=0
        )
        self.wait_page_stable()
