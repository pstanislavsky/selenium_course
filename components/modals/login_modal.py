from selenium.webdriver.common.by import By

from base.components.base_modal import BaseModal


class LoginModal(BaseModal):
    # Locators
    LOGIN_INPUT_LOCATOR = (By.XPATH, './/input[@id = "USER_LOGIN"]')
    PASSWORD_INPUT_LOCATOR = (By.XPATH, './/input[@id = "USER_PASSWORD"]')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, './/button[@type = "submit"]')

    # Actions
    def log_in(self, login, password):
        self.enter_text(self.LOGIN_INPUT_LOCATOR, login)
        self.enter_text(self.PASSWORD_INPUT_LOCATOR, password)
        self.click_element(self.LOGIN_BUTTON_LOCATOR)
        self.wait_page_stable()
