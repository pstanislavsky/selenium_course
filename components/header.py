from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.catalog_menu import CatalogMenu
from utils.xpath import has_class


class Header(BaseComponent):
    """Компонент хедера страниц интернет-магазина."""

    # Locators
    CATALOG_MENU_LOCATOR = (By.XPATH, f'.//li[{has_class("catalog-menu")}]')
    LOGIN_BUTTON_LOCATOR = (
        By.XPATH,
        f'.//a[{has_class("user-profile__login-link--desktop")}]',
    )
    PROFILE_BUTTON_LOCATOR = (
        By.XPATH,
        f'.//a[{has_class("user-profile__link--desktop")}]',
    )
    FAVORITES_BUTTON_LOCATOR = (By.XPATH, f'.//a[{has_class("favorites-link")}]')
    CART_BUTTON_LOCATOR = (By.XPATH, './/a[@data-entity = "header-cart"]')
    CART_COUNTER_LOCATOR = (By.XPATH, './/span[@data-block-id = "counter"]')

    # Components
    @property
    def catalog_menu(self):
        return CatalogMenu(self, self.CATALOG_MENU_LOCATOR)

    # Properties
    @property
    def is_logged_in(self):
        return self.is_visible(self.PROFILE_BUTTON_LOCATOR)

    @property
    def cart_counter(self):
        if self.is_visible(self.CART_COUNTER_LOCATOR):
            return int(self.get_text(self.CART_COUNTER_LOCATOR))
        else:
            return 0

    # Actions
    def open_login_modal(self):
        self.click_element(self.LOGIN_BUTTON_LOCATOR)

    def open_cart(self):
        self.click_element(self.CART_BUTTON_LOCATOR)
