from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.common.autocomplete_input import AutocompleteInput
from components.common.dropdown_selector import DropdownSelector
from utils.xpath import has_class


class DeliveryInformation(BaseComponent):
    # Locators
    COURIER_ADDRESS_INPUT_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("fields-courier")}]'
        f'//div[{has_class("form-floating")}]'
        f'[.//input[@id = "property_ADDRESS"]]',
    )
    COURIER_ZIP_CODE_INPUT_LOCATOR = (By.XPATH, './/input[@id = "property_ZIP"]')
    COURIER_DELIVERY_DATE_INPUT_LOCATOR = (
        By.XPATH,
        './/input[@id = "property_DELIVERY_DATE"]',
    )
    COURIER_DELIVERY_TIME_DROPDOWN_LOCATOR = (
        By.XPATH,
        f'.//div[@data-id = "user-delivery-time"]'
        f'//div[{has_class("form-dropdown")}]',
    )
    COURIER_DELIVERY_TIME_DROPDOWN_OPTION_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("dropdown-item")}]',
    )

    # Components
    @property
    def address(self):
        return AutocompleteInput(self, self.COURIER_ADDRESS_INPUT_LOCATOR)

    @property
    def delivery_time(self):
        return DropdownSelector(
            self,
            self.COURIER_DELIVERY_TIME_DROPDOWN_LOCATOR,
            self.COURIER_DELIVERY_TIME_DROPDOWN_OPTION_LOCATOR,
        )

    # Properties
    @property
    def zip_code(self):
        return self.get_element(self.COURIER_ZIP_CODE_INPUT_LOCATOR).get_attribute(
            'value'
        )

    # Actions
    def set_zip_code(self, zip_code):
        self.enter_text(self.COURIER_ZIP_CODE_INPUT_LOCATOR, zip_code)
