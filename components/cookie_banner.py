from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.xpath import text_equals


class CookieBanner(BaseComponent):
    # Locators
    ACCEPT_BUTTON_LOCATOR = (By.XPATH, f'.//button[{text_equals("Принять")}]')

    # Actions
    def accept_cookie_consent(self):
        self.click_element(self.ACCEPT_BUTTON_LOCATOR)
        self.wait_root_disappear()
