from selenium.common.exceptions import (
    ElementNotInteractableException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from base.components.base_component import BaseComponent
from utils.parsers import normalize_text
from utils.xpath import has_class, has_text


class DropdownSelector(BaseComponent):
    def __init__(self, parent, root_locator, option_locator, option_value_attribute):
        super().__init__(parent, root_locator)
        self.option_locator = option_locator
        self.option_value_attribute = option_value_attribute

    # Locators
    SELECT_LOCATOR = (By.XPATH, './/select')
    TOGGLE_LOCATOR = (By.XPATH, './/*[@data-bs-toggle = "dropdown"]')
    MENU_LOCATOR = (By.XPATH, f'.//ul[{has_class("dropdown-menu")}]')

    def _get_option_locator(self, option):
        return (
            By.XPATH,
            f'{self.option_locator[1]}[{has_text(option)}]',
        )

    # Properties
    @property
    def selected_option(self):
        selected_option = Select(
            self.get_present_element(self.SELECT_LOCATOR)
        ).first_selected_option

        return normalize_text(selected_option.get_property('textContent'))

    @property
    def is_enabled(self):
        return self.get_element(self.TOGGLE_LOCATOR, timeout=1).is_enabled()

    # Checks
    def is_option_selected(self, option):
        option_locator = self._get_option_locator(option)
        option_value = self.get_present_element(option_locator).get_attribute(
            self.option_value_attribute
        )

        if option_value is None:
            raise WebDriverException(
                f'Dropdown option "{option}" does not have attribute "{self.option_value_attribute}".'
            )

        selected_value = self.get_present_element(self.SELECT_LOCATOR).get_attribute(
            'value'
        )

        return option_value == selected_value

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
