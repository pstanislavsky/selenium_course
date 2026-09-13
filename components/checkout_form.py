from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.common.input import Input
from components.common.searchable_dropdown import SearchableDropdown
from components.delivery_information import DeliveryInformation
from components.delivery_method_selector import DeliveryMethodGroup
from utils.xpath import has_class


class CheckoutForm(BaseComponent):
    # Locators
    FULL_NAME_INPUT_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("form-floating")}]' f'[.//input[@id = "property_FIO"]]',
    )
    EMAIL_INPUT_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("form-floating")}]' f'[.//input[@id = "property_EMAIL"]]',
    )
    PHONE_INPUT_LOCATOR = (
        By.XPATH,
        f'.//div[{has_class("form-floating")}]' f'[.//input[@id = "property_PHONE"]]',
    )
    CITY_DROPDOWN_LOCATOR = (
        By.XPATH,
        f'.//div[@data-type = "location"]' f'//div[{has_class("form-dropdown")}]',
    )
    DELIVERY_LOCATOR = (By.XPATH, './/div[@data-entity = "delivery-block"]')
    DELIVERY_INFORMATION_LOCATOR = (By.XPATH, './/div[@data-type = "delivery-info"]')

    # Components
    @property
    def full_name(self):
        return Input(self, self.FULL_NAME_INPUT_LOCATOR)

    @property
    def email(self):
        return Input(self, self.EMAIL_INPUT_LOCATOR)

    @property
    def phone(self):
        return Input(self, self.PHONE_INPUT_LOCATOR)

    @property
    def city(self):
        return SearchableDropdown(self, self.CITY_DROPDOWN_LOCATOR)

    @property
    def delivery(self):
        return DeliveryMethodGroup(self, self.DELIVERY_LOCATOR)

    @property
    def delivery_information(self):
        return DeliveryInformation(self, self.DELIVERY_INFORMATION_LOCATOR)
