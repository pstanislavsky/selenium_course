from selenium.webdriver.common.by import By

from base.components.base_filter import BaseFilter
from components.common.checkbox_selector import CheckboxSelector
from utils.xpath import has_class


class CheckboxFilter(BaseFilter):
    # Locators
    OPTION_LOCATOR = (By.XPATH, f'.//div[{has_class("smart-filter__value")}]')
    OPTION_NAME_LOCATOR = (
        By.XPATH,
        f'.//span[{has_class("smart-filter__label-text")}]',
    )

    # Components
    @property
    def options(self):
        return CheckboxSelector(
            self,
            self.MENU_LOCATOR,
            self.OPTION_LOCATOR,
            self.OPTION_NAME_LOCATOR,
        )

    # Properties
    @property
    def checked_options(self):
        return self.options.checked_options

    # Checks
    def is_option_enabled(self, option):
        return self.options.is_option_enabled(option)

    def is_option_checked(self, option):
        return self.options.is_option_checked(option)

    # Actions
    def check_option(self, option):
        if self.options.check_option(option):
            self.wait_page_stable()

    def uncheck_option(self, option):
        if self.options.uncheck_option(option):
            self.wait_page_stable()
