from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.common.autocomplete_input import AutocompleteInput
from components.common.input import Input
from components.modals.pickup_point_modal import PickupPointModal
from utils.xpath import has_class


class DeliveryInformation(BaseComponent):
    # Locators
    PICKUP_POINT_MODAL_LOCATOR = (
        By.XPATH,
        f'//div[@id = "widgetPointsModal"]' f'//div[{has_class("modal-content")}]',
    )
    COURIER_ADDRESS_INPUT_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("fields-courier")}]'
        f'//div[{has_class("form-floating")}]'
        f'[.//input[@id = "property_ADDRESS"]]',
    )
    COURIER_ZIP_CODE_INPUT_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("fields-courier")}]'
        f'//div[{has_class("form-floating")}]'
        f'[.//input[@id = "property_ZIP"]]',
    )

    # Components
    @property
    def pickup_point_modal(self):
        return PickupPointModal(self, self.PICKUP_POINT_MODAL_LOCATOR)

    @property
    def address(self):
        return AutocompleteInput(self, self.COURIER_ADDRESS_INPUT_LOCATOR)

    @property
    def zip_code(self):
        return Input(self, self.COURIER_ZIP_CODE_INPUT_LOCATOR)
