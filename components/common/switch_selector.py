from selenium.common.exceptions import (
    ElementNotInteractableException,
    WebDriverException,
)
from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent


class SwitchSelector(BaseComponent):
    # Locators
    SWITCH_LOCATOR = (By.XPATH, './/input[@role = "switch"]')

    # Properties
    @property
    def is_enabled(self):
        return self.get_element(self.SWITCH_LOCATOR, timeout=1).is_enabled()

    @property
    def is_on(self):
        return self.get_element(self.SWITCH_LOCATOR, timeout=1).is_selected()

    # Actions
    def enable(self):
        if self.is_on:
            return False

        if not self.is_enabled:
            raise ElementNotInteractableException(
                'Switch control is disabled and cannot be turned on.'
            )

        self.click_element(self.SWITCH_LOCATOR)

        if not self.is_on:
            raise WebDriverException(
                f'Switch control was not turned on after clicking on it.'
            )

        return True

    def disable(self):
        if not self.is_on:
            return False

        if not self.is_enabled:
            raise ElementNotInteractableException(
                'Switch control is disabled and cannot be turned off.'
            )

        self.click_element(self.SWITCH_LOCATOR)

        if self.is_on:
            raise WebDriverException(
                f'Switch control was not turned off after clicking on it.'
            )

        return True
