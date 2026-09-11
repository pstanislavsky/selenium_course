from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.common.autocomplete_input import AutocompleteInput
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

    # Components
    @property
    def address(self):
        return AutocompleteInput(self, self.COURIER_ADDRESS_INPUT_LOCATOR)

    # Properties
    @property
    def zip_code(self):
        return self.get_element(self.COURIER_ZIP_CODE_INPUT_LOCATOR).get_attribute(
            'value'
        )
