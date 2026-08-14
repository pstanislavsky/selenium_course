from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By

from components.common.dropdown_selector import DropdownSelector


class SearchableDropdownSelector(DropdownSelector):
    # Locators
    TOGGLE_LOCATOR = (By.XPATH, './/input[@role = "combobox"]')
    MENU_LOCATOR = (By.XPATH, './/div[@role = "listbox"]')

    # Actions
    def select_option(self, option):
        if not self.is_enabled:
            raise ElementNotInteractableException(
                f'Dropdown control is disabled and option "{option}" cannot be selected.'
            )

        self.enter_text(self.TOGGLE_LOCATOR, option)
        self.get_element(self.MENU_LOCATOR)

        option_locator = self._get_option_locator(option)

        if not self.get_element(option_locator).is_enabled():
            raise ElementNotInteractableException(
                f'Dropdown option "{option}" is disabled and cannot be selected.'
            )

        self.click_element(option_locator)
