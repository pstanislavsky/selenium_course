from selenium.webdriver.common.by import By

from base.components.base_filter import BaseFilter
from components.common.radio_selector import RadioSelector
from utils.xpath import has_class


class RadioFilter(BaseFilter):
    # Data
    OPTION_LOCATOR = (By.XPATH, f'.//div[{has_class("smart-filter__value")}]')
    OPTION_TEXT_LOCATOR = (
        By.XPATH,
        f'.//span[{has_class("smart-filter__label-text")}]',
    )

    # Components
    @property
    def options(self):
        return RadioSelector(
            self,
            self.MENU_LOCATOR,
            self.OPTION_LOCATOR,
            self.OPTION_TEXT_LOCATOR,
        )

    # Properties
    @property
    def selected_option(self):
        return self.options.selected_option

    # Checks
    def is_option_enabled(self, option):
        return self.options.is_option_enabled(option)

    def is_option_selected(self, option):
        return self.options.is_option_selected(option)

    # Actions
    def select_option(self, option):
        if self.options.is_option_selected(option):
            return

        self.options.select_option(option)
        self.wait_page_stable()
