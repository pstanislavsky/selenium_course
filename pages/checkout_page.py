from selenium.webdriver.common.by import By

from base.pages.base_page import BasePage
from components.checkout_form import CheckoutForm
from components.checkout_summary import CheckoutSummary
from utils.xpath import has_class


class CheckoutPage(BasePage):
    # Data
    URL = 'https://www.torrefacto.ru/personal/checkout/'

    # Locators
    FORM_LOCATOR = (By.XPATH, '//form[@id = "order-form"]')
    SUMMARY_LOCATOR = (
        By.XPATH,
        f'//div[{has_class("checkout__order-summary-block-items")}]',
    )

    # Components
    @property
    def form(self):
        return CheckoutForm(self, self.FORM_LOCATOR)

    @property
    def summary(self):
        return CheckoutSummary(self, self.SUMMARY_LOCATOR)

    # Actions
    def fill_personal_information(self, full_name, email, phone):
        self.form.set_full_name(full_name)
        self.form.set_email(email)
        self.form.set_phone(phone)

    def select_city(self, city_name):
        self.form.city.select_option(city_name)
        self.wait_page_stable()
        self.summary.wait_until_recalculated()

    def select_delivery_method(self, delivery_provider, delivery_type):
        if self.form.delivery.select_option((delivery_provider, delivery_type)):
            self.summary.wait_until_recalculated()
