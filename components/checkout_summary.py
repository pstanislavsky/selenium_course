from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.parsers import parse_int
from utils.xpath import has_classes


class CheckoutSummary(BaseComponent):
    # Locators
    TOTAL_QUANTITY_LOCATOR = (By.XPATH, './/span[@data-id = "basket-sum-quantity"]')
    BASE_PRICE_LOCATOR = (By.XPATH, './/div[@data-id = "basket-sum"]')
    DISCOUNT_LOCATOR = (By.XPATH, './/div[@data-id = "discount-sum"]')
    DELIVERY_LOCATOR = (By.XPATH, './/div[@data-id = "delivery-sum"]')
    TOTAL_PRICE_LOCATOR = (By.XPATH, './/div[@data-id = "total"]')
    LOADING_INDICATOR_LOCATOR = (
        By.XPATH,
        f'.//div[{has_classes("checkout__order-summary-block-item", "--preloading")}]',
    )

    # Properties
    @property
    def total_quantity(self):
        return int(self.get_text(self.TOTAL_QUANTITY_LOCATOR))

    @property
    def base_price(self):
        return parse_int(self.get_text(self.BASE_PRICE_LOCATOR), suffix='₽')

    @property
    def discount(self):
        if self.is_visible(self.DISCOUNT_LOCATOR):
            return abs(parse_int(self.get_text(self.DISCOUNT_LOCATOR), suffix='₽'))

        return 0

    @property
    def delivery(self):
        value = self.get_text(self.DELIVERY_LOCATOR)

        if value == 'Бесплатно':
            return 0

        return parse_int(value, suffix='₽')

    @property
    def total_price(self):
        return parse_int(self.get_text(self.TOTAL_PRICE_LOCATOR), suffix='₽')

    # Actions
    def wait_until_recalculated(self, appearance_timeout=2, disappearance_timeout=10):
        if not self.is_visible(self.LOADING_INDICATOR_LOCATOR, appearance_timeout):
            return

        self.wait_until_not_visible(
            self.LOADING_INDICATOR_LOCATOR, disappearance_timeout
        )
