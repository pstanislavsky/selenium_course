from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.common.switch_selector import SwitchSelector
from utils.xpath import has_class


class SwitchFilter(BaseComponent):
    # Locators
    TITLE_LOCATOR = (By.XPATH, f'.//div[{has_class("smart-filter__title")}]')
    SWITCH_LOCATOR = (By.XPATH, f'.//div[{has_class("smart-filter__value")}]')

    # Components
    @property
    def switch(self):
        return SwitchSelector(self, self.SWITCH_LOCATOR)

    # Properties
    @property
    def title(self):
        return self.get_text(self.TITLE_LOCATOR)

    @property
    def is_enabled(self):
        return self.switch.is_enabled

    @property
    def is_on(self):
        return self.switch.is_on

    # Actions
    def enable(self):
        if self.switch.is_on:
            return

        self.switch.enable()
        self.wait_page_stable()

    def disable(self):
        if not self.switch.is_on:
            return

        self.switch.disable()
        self.wait_page_stable()
