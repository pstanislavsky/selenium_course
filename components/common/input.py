from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent


class Input(BaseComponent):
    # Locators
    FIELD_LOCATOR = (By.XPATH, './/input | .//textarea')
    CLEAR_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "clear-field"]')

    # Properties
    @property
    def value(self):
        return self.get_element(self.FIELD_LOCATOR).get_attribute('value')

    @property
    def is_enabled(self):
        return self.get_element(self.FIELD_LOCATOR).is_enabled()

    # Checks
    def has_value(self, value):
        return value == self.value

    # Actions
    def fill(self, value):
        if self.has_value(value):
            return False

        if not self.is_enabled:
            raise ElementNotInteractableException(
                f'Input field is disabled and value "{value}" cannot be entered.'
            )

        self.enter_text(self.FIELD_LOCATOR, value)

        return True

    def clear(self):
        if self.is_visible(self.CLEAR_BUTTON_LOCATOR):
            self.click_element(self.CLEAR_BUTTON_LOCATOR)
        else:
            self.get_element(self.FIELD_LOCATOR).clear()
