from selenium.common.exceptions import (
    ElementNotInteractableException,
    WebDriverException,
)
from selenium.webdriver.common.by import By

from components.common.dropdown_selector import DropdownSelector
from utils.xpath import has_class, has_classes


class SearchableDropdownSelector(DropdownSelector):
    # Locators
    TOGGLE_LOCATOR = (By.XPATH, f'.//div[{has_class("ts-control")}]')
    INPUT_LOCATOR = (By.XPATH, './/input[@role = "combobox"]')
    MENU_LOCATOR = (By.XPATH, './/div[@role = "listbox"]')
    LOADING_INDICATOR_LOCATOR = (
        By.XPATH,
        f'.//div[{has_classes("ts-wrapper", "loading")}]',
    )

    # Properties
    @property
    def is_enabled(self):
        return self.get_present_element(self.SELECT_LOCATOR, timeout=1).is_enabled()

    # Actions
    def select_option(self, option):
        if self.is_option_selected(option):
            return False

        if not self.is_enabled:
            raise ElementNotInteractableException(
                f'Dropdown control is disabled and option "{option}" cannot be selected.'
            )

        self.click_element(self.TOGGLE_LOCATOR)
        self.get_element(self.MENU_LOCATOR)
        self.enter_text(self.INPUT_LOCATOR, option)
        if self.is_visible(self.LOADING_INDICATOR_LOCATOR, timeout=2):
            self.wait_until_not_visible(self.LOADING_INDICATOR_LOCATOR, timeout=15)

        option_locator = self._get_option_locator(option)

        if not self.is_visible(option_locator):
            raise ValueError(f'Dropdown option "{option}" was not found.')

        if not self.get_element(option_locator).is_enabled():
            raise ElementNotInteractableException(
                f'Dropdown option "{option}" is disabled and cannot be selected.'
            )

        self.click_element(option_locator)

        if not self.is_option_selected(option):
            raise WebDriverException(
                f'Dropdown option "{option}" was not selected after clicking on it.'
            )

        return True
