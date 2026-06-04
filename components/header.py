from selenium.webdriver.common.by import By

from base.base_object import BaseObject

class Header(BaseObject):
    """Компонент хедера страниц интернет-магазина."""

    # Локаторы
    CATALOG_BUTTON_LOCATOR = (By.XPATH, './/div[@id="catalog-menu-button"]')
    COFFEE_BUTTON_LOCATOR = (By.XPATH, './/span[text()="Кофе"]')
    CART_BUTTON_LOCATOR = (By.XPATH, './/a[@class="cart-content"]')

    # Действия
    def click_catalog_button(self):
        self.safe_click_element(self.CATALOG_BUTTON_LOCATOR)

    def click_cart_button(self):
        self.safe_click_element(self.CART_BUTTON_LOCATOR)

    # Сценарии
    def open_coffee_catalog(self):
        self.click_catalog_button()
        self.safe_click_element(self.COFFEE_BUTTON_LOCATOR)

    def open_cart(self):
        self.click_cart_button()