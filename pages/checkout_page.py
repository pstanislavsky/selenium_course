from selenium.webdriver.common.by import By

from base.pages.base_page import BasePage
from components.checkout_summary import CheckoutSummary
from components.common.radio_selector import RadioSelector
from components.common.searchable_dropdown_selector import SearchableDropdownSelector
from components.delivery_method_selector import DeliveryMethodSelector
from utils.xpath import has_class, has_text


class CheckoutPage(BasePage):
    # Data
    URL = 'https://www.torrefacto.ru/personal/checkout/'

    # Locators
    SUMMARY_LOCATOR = (
        By.XPATH,
        f'//div[{has_class("checkout__order-summary-block-items")}]',
    )
    FULL_NAME_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_FIO"]')
    EMAIL_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_EMAIL"]')
    PHONE_INPUT_LOCATOR = (By.XPATH, '//input[@id = "property_PHONE"]')
    CITY_DROPDOWN_LOCATOR = (
        By.XPATH,
        f'//div[@data-type = "location"]' f'//div[{has_class("form-dropdown")}]',
    )
    CITY_DROPDOWN_OPTION_LOCATOR = (By.XPATH, './/div[@role = "option"]')
    DELIVERY_LOCATOR = (By.XPATH, '//div[@data-entity = "delivery-block"]')

    # Components
    @property
    def summary(self):
        return CheckoutSummary(self, self.SUMMARY_LOCATOR)

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
    def fill_personal_information(self, full_name, email, phone):
        self.enter_text(self.FULL_NAME_INPUT_LOCATOR, full_name)
        self.enter_text(self.EMAIL_INPUT_LOCATOR, email)
        self.enter_text(self.PHONE_INPUT_LOCATOR, phone)

    def select_city(self, city_name):
        self.city.select_option(city_name)
        self.wait_page_stable()
        self.summary.wait_until_recalculated()

    def select_delivery_method(self, delivery_provider, delivery_type):
        self.delivery.select_option((delivery_provider, delivery_type))
        self.summary.wait_until_recalculated()
