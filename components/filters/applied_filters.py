from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.xpath import has_class, has_text


class AppliedFilters(BaseComponent):
    # Locators
    SCROLLABLE_LIST_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("smart-filter__applied-list")}]',
    )
    CLEAR_ALL_CHIP_LOCATOR = (
        By.XPATH,
        './/button[@data-action = "filter-reset"]',
    )

    def _get_filter_chip_locator(self, filter_name, option=None):
        if option is None:
            text_condition = has_text(filter_name)
        else:
            text_condition = f'{has_text(filter_name)} and {has_text(option)}'

        return (
            By.XPATH,
            f'.//button[@data-action = "filter-remove"]'
            f'[.//span[{has_class("smart-filter__applied-item-text")} and {text_condition}]]',
        )

    # Checks
    def is_applied(self, filter_name, option=None):
        return self.is_present(self._get_filter_chip_locator(filter_name, option))

    # Actions
    def remove(self, filter_name, option=None):
        chip_locator = self._get_filter_chip_locator(filter_name, option)

        if not self.is_present(chip_locator):
            raise NoSuchElementException(
                f'Applied filter was not found: filter_name="{filter_name}", option="{option}".'
            )

        control_locator = (
            By.XPATH,
            f'{chip_locator[1]}' f'//*[local-name() = "use"]',
        )

        self.drag_horizontally_to_element(self.SCROLLABLE_LIST_LOCATOR, chip_locator)
        self.click_element(control_locator)
        self.wait_page_stable()

    def clear_all(self):
        if not self.is_present(self.CLEAR_ALL_CHIP_LOCATOR):
            raise NoSuchElementException(
                'Clear-all button was not found. There may be no applied filters.'
            )

        control_locator = (
            By.XPATH,
            f'{self.CLEAR_ALL_CHIP_LOCATOR[1]}' f'//*[local-name() = "use"]',
        )

        self.drag_horizontally_to_element(
            self.SCROLLABLE_LIST_LOCATOR, self.CLEAR_ALL_CHIP_LOCATOR
        )
        self.click_element(control_locator)
        self.wait_page_stable()
