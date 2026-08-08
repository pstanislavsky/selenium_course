from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.xpath import has_class, text_equals


class CatalogMenu(BaseComponent):
    # Locators
    CATALOG_MENU_BUTTON_LOCATOR = (By.XPATH, './/div[@id = "catalog-menu-button"]')
    CATALOG_MENU_LOCATOR = (
        By.XPATH,
        f'.//div[@id = "overlayCatalogMenu"]'
        f'//ul[{has_class("catalog-nav")}]'
        f'[.//li[{has_class("has-children")}]]',
    )
    COFFEE_BUTTON_LOCATOR = (
        By.XPATH,
        f'.//a[{has_class("nav-link")} and {text_equals("Кофе")}]',
    )
    COFFEE_MENU_LOCATOR = (
        By.XPATH,
        f'{CATALOG_MENU_LOCATOR[1]}'
        f'//li[{COFFEE_BUTTON_LOCATOR[1]}]'
        f'//ul[{has_class("catalog-nav")}]',
    )
    ROASTED_COFFEE_BUTTON_LOCATOR = (
        By.XPATH,
        f'{COFFEE_MENU_LOCATOR[1]}'
        f'//a[{has_class("nav-link")} and {text_equals("Свежеобжаренный кофе")}]',
    )

    # Actions
    def open_roasted_coffee_catalog(self):
        self.click_element(self.CATALOG_MENU_BUTTON_LOCATOR)
        self.get_element(self.CATALOG_MENU_LOCATOR)
        self.hover_element(self.COFFEE_BUTTON_LOCATOR)
        self.get_element(self.COFFEE_MENU_LOCATOR)
        self.click_element(self.ROASTED_COFFEE_BUTTON_LOCATOR)
