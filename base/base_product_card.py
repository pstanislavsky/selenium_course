from selenium.webdriver.common.by import By

from base.base_component import BaseComponent


class BaseProductCard(BaseComponent):
    """Базовый класс для карточки продукта."""

    # Локаторы
    PRODUCT_NAME_LOCATOR = (By.XPATH, './/a[@class="item-name "]')
    PRODUCT_PRICE_LOCATOR = (By.XPATH, './/div[@class="item-price__price "]')
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH, './/button[contains(@class, "add-to-cart")]')

    def get_size_value_locator(self, size):
        return (By.XPATH, f'.//div[contains(@class, "item-offers")]'
                          f'//label[.//span[contains(normalize-space(), "{size}")]]')

    # Действия
    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME_LOCATOR)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE_LOCATOR)

    def select_product_size(self, size):
        self.safe_click_element(self.get_size_value_locator(size))

    def add_product_to_cart(self):
        self.safe_click_element(self.ADD_TO_CART_BUTTON_LOCATOR)