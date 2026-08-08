from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent


class BaseModal(BaseComponent):
    # Locators
    CLOSE_BUTTON_LOCATOR = (By.XPATH, './/button[@data-bs-dismiss = "modal"]')

    # Actions
    def close(self):
        self.click_element(self.CLOSE_BUTTON_LOCATOR)
        self.wait_root_disappear()
