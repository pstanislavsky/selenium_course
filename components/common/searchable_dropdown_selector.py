from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from components.common.dropdown_selector import DropdownSelector
from utils.xpath import has_class, has_classes, has_text


class SearchableDropdownSelector(DropdownSelector):
    def __init__(self, parent, root_locator):
        super().__init__(parent, root_locator, self.MENU_OPTION_LOCATOR)

    # Locators
    TOGGLE_LOCATOR = (By.XPATH, f'.//div[{has_class("ts-control")}]')
    INPUT_LOCATOR = (By.XPATH, './/input[@role = "combobox"]')
    MENU_LOCATOR = (By.XPATH, './/div[@role = "listbox"]')
    MENU_OPTION_LOCATOR = (By.XPATH, './/div[@role = "option"]')
    LOADING_INDICATOR_LOCATOR = (
        By.XPATH,
        f'.//div[{has_classes("ts-wrapper", "loading")}]',
    )
    NO_RESULTS_INDICATOR_LOCATOR = (By.XPATH, f'.//div[{has_class("no-results")}]')

    def _get_menu_option_locator(self, option):
        return (
            By.XPATH,
            f'{self.menu_option_locator[1]}' f'[{has_text(option)}]',
        )

    # Checks
    def is_option_selected(self, option):
        return option in self.selected_option

    # Actions
    def close(self):
        if self.is_open:
            self.get_element(self.INPUT_LOCATOR).send_keys(Keys.ESCAPE)

        self.wait_until_not_visible(self.MENU_LOCATOR)

    def select_option(self, option):
        """Selects the first option containing the given unique text fragment."""

        if self.is_option_selected(option):
            return False

        if not self.is_enabled:
            raise ElementNotInteractableException(
                f'Dropdown control is disabled and option "{option}" cannot be selected.'
            )

        self.open()
        self.enter_text(self.INPUT_LOCATOR, option)
        self.wait_until_menu_loaded()

        if self.is_visible(self.NO_RESULTS_INDICATOR_LOCATOR):
            self.close()
            raise ValueError(f'Dropdown option "{option}" was not found.')

        option_locator = self._get_menu_option_locator(option)

        if not self.is_visible(option_locator):
            self.close()
            raise ValueError(f'Dropdown option "{option}" was not found.')

        self.click_element(option_locator)

        return True

    def wait_until_menu_loaded(self, appearance_timeout=2, disappearance_timeout=10):
        if not self.is_visible(
            self.LOADING_INDICATOR_LOCATOR, timeout=appearance_timeout
        ):
            return

        self.wait_until_not_visible(
            self.LOADING_INDICATOR_LOCATOR, timeout=disappearance_timeout
        )
