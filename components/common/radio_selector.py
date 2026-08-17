from selenium.common.exceptions import (
    ElementNotInteractableException,
    WebDriverException,
)
from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.xpath import has_text


class RadioSelector(BaseComponent):
    def __init__(self, parent, root_locator, option_locator, option_name_locator):
        super().__init__(parent, root_locator)
        self.option_locator = option_locator
        self.option_name_locator = option_name_locator

    # Locators
    def _get_option_radio_locator(self, option):
        return (
            By.XPATH,
            f'{self.option_locator[1]}'
            f'[{self.option_name_locator[1]}[{has_text(option)}]]'
            f'//input[@type = "radio"]',
        )

    def _get_option_label_locator(self, option):
        return (
            By.XPATH,
            f'{self.option_locator[1]}'
            f'[{self.option_name_locator[1]}[{has_text(option)}]]'
            f'//label',
        )

    # Properties
    @property
    def selected_option(self):
        for option_name in self.get_elements(self.option_name_locator):
            option_name = option_name.text.strip()

            if self.is_option_selected(option_name):
                return option_name

        return None

    # Checks
    def is_option_enabled(self, option):
        return self.get_present_element(
            self._get_option_radio_locator(option), timeout=1
        ).is_enabled()

    def is_option_selected(self, option):
        return self.get_present_element(
            self._get_option_radio_locator(option), timeout=1
        ).is_selected()

    # Actions
    def select_option(self, option):
        option_label_locator = self._get_option_label_locator(option)

        if not self.is_visible(option_label_locator):
            raise ValueError(f'Radio option "{option}" was not found.')

        if self.is_option_selected(option):
            return False

        if not self.is_option_enabled(option):
            raise ElementNotInteractableException(
                f'Radio option "{option}" is disabled and cannot be selected.'
            )

        self.click_element(option_label_locator)

        if not self.is_option_selected(option):
            raise WebDriverException(
                f'Radio option "{option}" was not selected after clicking its label.'
            )

        return True
