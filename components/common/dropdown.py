from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from base.components.base_component import BaseComponent
from utils.parsers import normalize_text
from utils.xpath import has_class, has_text


class Dropdown(BaseComponent):
    def __init__(self, parent, root_locator, menu_option_locator):
        super().__init__(parent, root_locator)
        self.menu_option_locator = menu_option_locator

    # Locators
    SELECT_LOCATOR = (By.XPATH, './/select')
    TOGGLE_LOCATOR = (By.XPATH, './/*[@data-bs-toggle = "dropdown"]')
    MENU_LOCATOR = (By.XPATH, f'.//ul[{has_class("dropdown-menu")}]')

    def _get_select_option_locator(self, option):
        return (
            By.XPATH,
            f'{self.SELECT_LOCATOR[1]}' f'//option[{has_text(option)}]',
        )

    def _get_menu_option_locator(self, option_value):
        return (
            By.XPATH,
            f'{self.menu_option_locator[1]}'
            f'[@data-value = "{option_value}" or '
            f'@data-id = "{option_value}"]',
        )

    # Properties
    @property
    def selected_option(self):
        selected_option = Select(
            self.get_present_element(self.SELECT_LOCATOR)
        ).first_selected_option

        return normalize_text(selected_option.get_property('textContent'))

    @property
    def is_enabled(self):
        return self.get_present_element(self.SELECT_LOCATOR, timeout=1).is_enabled()

    @property
    def is_open(self):
        return self.is_visible(self.MENU_LOCATOR)

    # Checks
    def is_option_selected(self, option):
        return self.get_present_element(
            self._get_select_option_locator(option)
        ).is_selected()

    # Actions
    def open(self):
        if not self.is_open:
            self.click_element(self.TOGGLE_LOCATOR)

        self.get_element(self.MENU_LOCATOR)

    def close(self):
        if self.is_open:
            self.click_element(self.TOGGLE_LOCATOR)

        self.wait_until_not_visible(self.MENU_LOCATOR)

    def select_option(self, option):
        """Selects the first option containing the given unique text fragment."""

        select_option_locator = self._get_select_option_locator(option)

        if not self.is_present(select_option_locator):
            raise ValueError(f'Dropdown option "{option}" was not found.')

        if self.is_option_selected(option):
            return False

        if not self.is_enabled:
            raise ElementNotInteractableException(
                f'Dropdown control is disabled and option "{option}" cannot be selected.'
            )

        option_value = self.get_present_element(select_option_locator).get_attribute(
            'value'
        )
        menu_option_locator = self._get_menu_option_locator(option_value)

        if not self.get_present_element(menu_option_locator).is_enabled():
            raise ElementNotInteractableException(
                f'Dropdown option "{option}" is disabled and cannot be selected.'
            )

        self.open()

        if not self.is_visible(menu_option_locator):
            self.close()
            raise ValueError(f'Dropdown option "{option}" was not found.')

        self.click_element(menu_option_locator)
        self.wait_until_not_visible(self.MENU_LOCATOR)

        return True
