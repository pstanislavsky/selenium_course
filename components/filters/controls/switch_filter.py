from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from components.common.switch import Switch
from utils.xpath import has_class


class SwitchFilter(BaseComponent):
    # Locators
    TITLE_LOCATOR = (By.XPATH, f'.//div[{has_class("smart-filter__title")}]')
    SWITCH_LOCATOR = (By.XPATH, f'.//div[{has_class("smart-filter__value")}]')

    # Components
    @property
    def switch(self):
        return Switch(self, self.SWITCH_LOCATOR)

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
    def turn_on(self):
        if self.switch.turn_on():
            self.wait_page_stable()

    def turn_off(self):
        if self.switch.turn_off():
            self.wait_page_stable()
