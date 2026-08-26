from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.parsers import normalize_text
from utils.xpath import has_class, has_text


class AutocompleteInput(BaseComponent):
    # Locators
    INPUT_LOCATOR = (By.XPATH, f'.//input[{has_class("suggestions-input")}]')
    MENU_LOCATOR = (By.XPATH, f'.//div[{has_class("suggestions-suggestions")}]')
    OPTION_LOCATOR = (By.XPATH, f'.//div[{has_class("suggestions-suggestion")}]')

    def _get_option_locator(self, option):
        return (By.XPATH, f'{self.OPTION_LOCATOR[1]}//' f'[{has_text(option)}]')

    # Properties
    @property
    def value(self):
        return normalize_text(
            self.get_element(self.INPUT_LOCATOR).get_attribute('value')
        )

    @property
    def is_open(self):
        return self.is_visible(self.MENU_LOCATOR)

    # Actions
    def select_option(self, option):
        pass
