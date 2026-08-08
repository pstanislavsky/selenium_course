from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent


class QuantitySelector(BaseComponent):
    # Locators
    QUANTITY_INPUT_LOCATOR = (By.XPATH, './/input[@data-type = "quantity"]')
    PLUS_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "increase"]')
    MINUS_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "decrease"]')

    # Properties
    @property
    def quantity(self):
        return int(self.get_element(self.QUANTITY_INPUT_LOCATOR).get_attribute('value'))

    # Actions
    def set(self, value):
        value = int(value)

        if value == self.quantity:
            return

        if not self.get_element(self.QUANTITY_INPUT_LOCATOR).is_enabled():
            raise ElementNotInteractableException(
                f'Quantity cannot be set to "{value}" because the quantity input is disabled.'
            )

        self.enter_text_and_submit(self.QUANTITY_INPUT_LOCATOR, str(value))

    def increase(self):
        if not self.get_element(self.PLUS_BUTTON_LOCATOR).is_enabled():
            raise ElementNotInteractableException(
                'Quantity cannot be increased because the increase button is disabled.'
            )

        self.click_element(self.PLUS_BUTTON_LOCATOR)

    def decrease(self):
        if not self.get_element(self.MINUS_BUTTON_LOCATOR).is_enabled():
            raise ElementNotInteractableException(
                'Quantity cannot be decreased because the decrease button is disabled.'
            )

        self.click_element(self.MINUS_BUTTON_LOCATOR)
