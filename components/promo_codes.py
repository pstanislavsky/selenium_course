from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.common.input import Input
from utils.xpath import xpath_string


class PromoCodes(BaseComponent):
    # Locators
    INPUT_LOCATOR = (By.XPATH, './/div[@data-block-id = "coupon-apply-block"]')
    APPLY_BUTTON_LOCATOR = (By.XPATH, './/button[@data-action = "apply-coupon"]')

    def _get_applied_promo_code_locator(self, promo_code):
        return (
            By.XPATH,
            f'.//div[@data-id = "coupon"]'
            f'[@data-value = {xpath_string(promo_code.lower())}]',
        )

    # Components
    @property
    def input(self):
        return Input(self, self.INPUT_LOCATOR)

    # Checks
    def is_applied(self, promo_code):
        return self.is_visible(self._get_applied_promo_code_locator(promo_code))

    # Actions
    def apply(self, promo_code):
        if self.is_applied(promo_code):
            return

        self.input.fill(promo_code)
        self.click_element(self.APPLY_BUTTON_LOCATOR)
        self.wait_page_stable()
        self.get_element(self._get_applied_promo_code_locator(promo_code))

    def remove(self, promo_code):
        if not self.is_applied(promo_code):
            raise NoSuchElementException(
                f'Applied promo code "{promo_code}" was not found.'
            )

        applied_promo_code_locator = self._get_applied_promo_code_locator(promo_code)
        remove_button_locator = (
            By.XPATH,
            f'{applied_promo_code_locator[1]}' f'//div[@data-action = "remove-coupon"]',
        )

        self.click_element(remove_button_locator)
        self.wait_page_stable()
        self.wait_until_not_visible(applied_promo_code_locator)
