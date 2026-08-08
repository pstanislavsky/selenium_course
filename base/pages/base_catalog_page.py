from selenium.webdriver.common.by import By

from base.pages.base_page import BasePage
from components.filters.applied_filters import AppliedFilters
from components.products.collections.catalog_product_collection import CatalogProductCollection
from utils.xpath import has_class


class BaseCatalogPage(BasePage):
    # Data
    FILTER_PANEL_CLASS = None

    # Locators
    PRODUCT_GRID_LOCATOR = (By.XPATH, '//div[@data-section = "items"]')
    FILTER_PANEL_LOCATOR = (By.XPATH, f'//div[{has_class("smart-filter")}]')
    APPLIED_FILTERS_LOCATOR = (By.XPATH, './/div[@data-section = "filter-applied"]')

    # Components
    @property
    def products(self):
        return CatalogProductCollection(self, self.PRODUCT_GRID_LOCATOR)

    @property
    def filters(self):
        return self.FILTER_PANEL_CLASS(self, self.FILTER_PANEL_LOCATOR)

    @property
    def applied_filters(self):
        return AppliedFilters(self, self.APPLIED_FILTERS_LOCATOR)
