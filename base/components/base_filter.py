from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.xpath import has_class


class BaseFilter(BaseComponent):
    # Locators
    TITLE_LOCATOR = (By.XPATH, f'.//div[{has_class("smart-filter__title")}]')
    MENU_LOCATOR = (By.XPATH, f'.//div[{has_class("smart-filter__values")}]')

    # Properties
    @property
    def title(self):
        return self.get_text(self.TITLE_LOCATOR)

    @property
    def is_expanded(self):
        return self.is_visible(self.MENU_LOCATOR)

    # Actions
    def expand(self):
        if not self.is_expanded:
            self.click_element(self.TITLE_LOCATOR)

    def collapse(self):
        if self.is_expanded:
            self.click_element(self.TITLE_LOCATOR)
