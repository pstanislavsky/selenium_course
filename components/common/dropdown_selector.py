from selenium.common.exceptions import (
    ElementNotInteractableException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from base.components.base_component import BaseComponent
from utils.xpath import has_class, has_text


class DropdownSelector(BaseComponent):
    # Locators
    SELECT_LOCATOR = (By.XPATH, f'.//select')
    TOGGLE_LOCATOR = (By.XPATH, f'.//*[@data-bs-toggle = "dropdown"]')
    MENU_LOCATOR = (By.XPATH, f'.//ul[{has_class("dropdown-menu")}]')

    def _get_option_locator(self, option):
        return (
            By.XPATH,
            f'{self.MENU_LOCATOR[1]}' f'//li//*[{has_text(option)}]',
        )

    # Properties
    @property
    def is_enabled(self):
        return self.get_element(self.TOGGLE_LOCATOR, timeout=1).is_enabled()

    @property
    def selected_option(self):
        selected_option = Select(
            self.get_present_element(self.SELECT_LOCATOR)
        ).first_selected_option

        return selected_option.get_property('textContent').strip()

    # Actions
    def select_option(self, option):
        if not self.is_enabled:
            raise ElementNotInteractableException(
                f'Dropdown control is disabled and option "{option}" cannot be selected.'
            )

        self.click_element(self.TOGGLE_LOCATOR)
        self.get_element(self.MENU_LOCATOR)

        if not self.get_element(self._get_option_locator(option)).is_enabled():
            raise ElementNotInteractableException(
                f'Dropdown option "{option}" is disabled and cannot be selected.'
            )

        self.click_element(self._get_option_locator(option))
