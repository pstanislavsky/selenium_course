from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.parsers import normalize_text
from utils.xpath import has_class, has_text


class AutocompleteInput(BaseComponent):
    # Locators
    INPUT_LOCATOR = (By.XPATH, f'.//input[{has_class("suggestions-input")}]')
    MENU_LOCATOR = (By.XPATH, f'.//div[{has_class("suggestions-suggestions")}]')
    SUGGESTION_LOCATOR = (By.XPATH, f'.//div[{has_class("suggestions-suggestion")}]')
    CLEAR_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "clear-field"]')

    def _get_suggestion_locator(self, option):
        return (By.XPATH, f'{self.SUGGESTION_LOCATOR[1]}[{has_text(option)}]')

    # Properties
    @property
    def selected_option(self):
        return normalize_text(
            self.get_element(self.INPUT_LOCATOR).get_attribute('value')
        )

    @property
    def is_open(self):
        return self.is_visible(self.MENU_LOCATOR)

    # Checks
    def is_option_selected(self, option):
        return option == self.selected_option

    # Actions
    def select_option(self, option):
        if self.is_option_selected(option):
            return False

        self.enter_text(self.INPUT_LOCATOR, option)
        self.get_element(self.MENU_LOCATOR)

        option_locator = self._get_suggestion_locator(option)

        try:
            self.get_element(option_locator)
        except TimeoutError:
            self.clear()
            raise ValueError(f'Autocomplete suggestion "{option}" was not found.')

        self.click_element(option_locator)

        return True

    def clear(self):
        if self.is_visible(self.CLEAR_BUTTON_LOCATOR):
            self.click_element(self.CLEAR_BUTTON_LOCATOR)

        self.wait_until_not_visible(self.MENU_LOCATOR)
