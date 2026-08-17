from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.common.searchable_dropdown_selector import SearchableDropdownSelector
from components.delivery_method_selector import DeliveryMethodSelector
from utils.xpath import has_class


class CheckoutForm(BaseComponent):
    # Locators
    FULL_NAME_INPUT_LOCATOR = (By.XPATH, './/input[@id = "property_FIO"]')
    EMAIL_INPUT_LOCATOR = (By.XPATH, './/input[@id = "property_EMAIL"]')
    PHONE_INPUT_LOCATOR = (By.XPATH, './/input[@id = "property_PHONE"]')
    CITY_DROPDOWN_LOCATOR = (
        By.XPATH,
        f'.//div[@data-type = "location"]' f'//div[{has_class("form-dropdown")}]',
    )
    CITY_DROPDOWN_OPTION_LOCATOR = (By.XPATH, './/div[@role = "option"]')
    DELIVERY_LOCATOR = (By.XPATH, './/div[@data-entity = "delivery-block"]')

    # Components
    @property
    def city(self):
        return SearchableDropdownSelector(
            self, self.CITY_DROPDOWN_LOCATOR, self.CITY_DROPDOWN_OPTION_LOCATOR
        )

    @property
    def delivery(self):
        return DeliveryMethodSelector(self, self.DELIVERY_LOCATOR)

    # Properties
    @property
    def full_name(self):
        value = self.get_element(self.FULL_NAME_INPUT_LOCATOR).get_attribute('value')

        if not value:
            return None

        return value

    @property
    def email(self):
        value = self.get_element(self.EMAIL_INPUT_LOCATOR).get_attribute('value')

        if not value:
            return None

        return value

    @property
    def phone(self):
        value = self.get_element(self.PHONE_INPUT_LOCATOR).get_attribute('value')

        if not value:
            return None

        return value

    # Actions
    def set_full_name(self, full_name):
        self.enter_text(self.FULL_NAME_INPUT_LOCATOR, full_name)

    def set_email(self, email):
        self.enter_text(self.EMAIL_INPUT_LOCATOR, email)

    def set_phone(self, phone):
        self.enter_text(self.PHONE_INPUT_LOCATOR, phone)
