from selenium.common.exceptions import (
    ElementNotInteractableException,
    WebDriverException,
)
from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.xpath import has_text


class CheckboxSelector(BaseComponent):
    def __init__(self, parent, root_locator, option_locator, option_text_locator):
        super().__init__(parent, root_locator)
        self.option_locator = option_locator
        self.option_text_locator = option_text_locator

    # Locators
    def _get_option_checkbox_locator(self, option):
        return (
            By.XPATH,
            f'{self.option_locator[1]}'
            f'[{self.option_text_locator[1]}[{has_text(option)}]]'
            f'//input[@type = "checkbox"]',
        )

    def _get_option_label_locator(self, option):
        return (
            By.XPATH,
            f'{self.option_locator[1]}'
            f'[{self.option_text_locator[1]}[{has_text(option)}]]'
            f'//label',
        )

    # Properties
    @property
    def checked_options(self):
        checked_options = []

        for option in self.get_elements(self.option_text_locator):
            option_text = option.text.strip()

            if self.is_option_checked(option_text):
                checked_options.append(option_text)

        return checked_options

    # Checks
    def is_option_enabled(self, option):
        return self.get_present_element(
            self._get_option_checkbox_locator(option), timeout=1
        ).is_enabled()

    def is_option_checked(self, option):
        return self.get_present_element(
            self._get_option_checkbox_locator(option), timeout=1
        ).is_selected()

    # Actions
    def check_option(self, option):
        if self.is_option_checked(option):
            return

        if not self.is_option_enabled(option):
            raise ElementNotInteractableException(
                f'Checkbox option "{option}" is disabled and cannot be checked.'
            )

        self.click_element(self._get_option_label_locator(option))

        if not self.is_option_checked(option):
            raise WebDriverException(
                f'Checkbox option "{option}" was not checked after clicking its label.'
            )

    def uncheck_option(self, option):
        if not self.is_option_checked(option):
            return

        if not self.is_option_enabled(option):
            raise ElementNotInteractableException(
                f'Checkbox option "{option}" is disabled and cannot be unchecked.'
            )

        self.click_element(self._get_option_label_locator(option))

        if self.is_option_checked(option):
            raise WebDriverException(
                f'Checkbox option "{option}" was not unchecked after clicking its label.'
            )
