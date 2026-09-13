from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from components.common.input import Input
from utils.xpath import has_class, has_text


class AutocompleteInput(Input):
    # Locators
    FIELD_LOCATOR = (By.XPATH, f'.//input[{has_class("suggestions-input")}]')
    SUGGESTIONS_LOCATOR = (By.XPATH, f'.//div[{has_class("suggestions-suggestions")}]')

    def _get_suggestion_locator(self, suggestion):
        return (
            By.XPATH,
            f'.//div[{has_class("suggestions-suggestion")}]'
            f'[{has_text(suggestion)}]',
        )

    # Properties
    @property
    def is_open(self):
        return self.is_visible(self.SUGGESTIONS_LOCATOR)

    # Checks
    def has_value(self, value):
        return value == self.value.strip()

    # Actions
    def close(self):
        if self.is_open:
            self.get_element(self.FIELD_LOCATOR).send_keys(Keys.ESCAPE)

        self.wait_until_not_visible(self.SUGGESTIONS_LOCATOR)

    def select_suggestion(self, suggestion):
        """Selects the first suggestion containing the given unique text fragment."""

        if not self.fill(suggestion):
            return False

        self.get_element(self.SUGGESTIONS_LOCATOR)
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
        super().clear()
        self.close()
