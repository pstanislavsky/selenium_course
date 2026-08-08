from selenium.common.exceptions import (
    ElementNotInteractableException,
)
from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.xpath import has_class, has_text


class DropdownSelector(BaseComponent):
    # Locators
    DROPDOWN_LOCATOR = (By.XPATH, f'.//button[{has_class("dropdown-toggle")}]')
    MENU_LOCATOR = (By.XPATH, f'.//ul[{has_class("dropdown-menu")}]')

    def _get_option_locator(self, option):
        return (
            By.XPATH,
            f'{self.MENU_LOCATOR[1]}'
            f'//button[@data-action = "set-option"]'
            f'[.//span[{has_text(option)}]]',
        )

    # Properties
    @property
    def is_enabled(self):
        return self.get_element(self.DROPDOWN_LOCATOR, timeout=1).is_enabled()

    @property
    def selected_option(self):
        return self.get_text(self.DROPDOWN_LOCATOR)

    # Actions
    def select_option(self, option):
        if not self.is_enabled:
            raise ElementNotInteractableException(
                f'Dropdown control is disabled and option "{option}" cannot be selected.'
            )

        self.click_element(self.DROPDOWN_LOCATOR)
        self.get_element(self.MENU_LOCATOR)

        if not self.get_element(self._get_option_locator(option)).is_enabled():
            raise ElementNotInteractableException(
                f'Dropdown option "{option}" is disabled and cannot be selected.'
            )

        self.click_element(self._get_option_locator(option))
