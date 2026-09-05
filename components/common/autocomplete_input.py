from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.components.base_component import BaseComponent
from utils.parsers import normalize_text
from utils.xpath import has_class, has_text


class AutocompleteInput(BaseComponent):
    # Locators
    INPUT_LOCATOR = (By.XPATH, f'.//input[{has_class("suggestions-input")}]')
    MENU_LOCATOR = (By.XPATH, f'.//div[{has_class("suggestions-suggestions")}]')
    SUGGESTION_LOCATOR = (By.XPATH, f'.//div[{has_class("suggestions-suggestion")}]')
    CLEAR_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "clear-field"]')

    def _get_suggestion_locator(self, suggestion):
        return (By.XPATH, f'{self.SUGGESTION_LOCATOR[1]}[{has_text(suggestion)}]')

    # Properties
    @property
    def value(self):
        return normalize_text(
            self.get_element(self.INPUT_LOCATOR).get_attribute('value')
        )

    @property
    def is_open(self):
        return self.is_visible(self.MENU_LOCATOR)

    # Checks
    def has_value(self, value):
        return normalize_text(value) == self.value

    # Actions
    def close(self):
        if self.is_open:
            self.get_element(self.INPUT_LOCATOR).send_keys(Keys.ESCAPE)

        self.wait_until_not_visible(self.MENU_LOCATOR)

    def select_suggestion(self, suggestion):
        """Selects the first suggestion containing the given unique text fragment."""

        if self.has_value(suggestion):
            return False

        self.enter_text(self.INPUT_LOCATOR, suggestion)

        suggestion_locator = self._get_suggestion_locator(suggestion)

        try:
            self.get_element(suggestion_locator)
        except TimeoutException:
            self.clear()
            raise ValueError(f'Autocomplete suggestion "{suggestion}" was not found.')

        self.click_element(suggestion_locator)
        self.close()

        return True

    def clear(self):
        if self.is_visible(self.CLEAR_BUTTON_LOCATOR):
            self.click_element(self.CLEAR_BUTTON_LOCATOR)

        self.close()
