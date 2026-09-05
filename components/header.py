from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.catalog_menu import CatalogMenu
from utils.xpath import has_class


class Header(BaseComponent):
    """Компонент хедера страниц интернет-магазина."""

    # Locators
    CATALOG_MENU_LOCATOR = (By.XPATH, f'.//li[{has_class("catalog-menu")}]')
    CART_BUTTON_LOCATOR = (By.XPATH, './/a[@data-entity = "header-cart"]')
    CART_COUNTER_LOCATOR = (By.XPATH, './/span[@data-block-id = "counter"]')

    # Components
    @property
    def catalog_menu(self):
        return CatalogMenu(self, self.CATALOG_MENU_LOCATOR)

    # Properties
    @property
    def cart_counter(self):
        if self.is_visible(self.CART_COUNTER_LOCATOR):
            return int(self.get_text(self.CART_COUNTER_LOCATOR))
        else:
            return 0

    # Actions
    def open_cart(self):
        self.click_element(self.CART_BUTTON_LOCATOR)
