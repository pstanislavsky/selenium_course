from selenium.webdriver.common.by import By

from base.base_product_card import BaseProductCard


class CoffeeProductCard(BaseProductCard):
    # Локаторы
    GRIND_DROPDOWN_LOCATOR = (By.XPATH, './/div[contains(@class, "option-mill")]//button')
    ACIDITY_LOCATOR = (By.XPATH, './/div[@class="scales__item"]'
                                 '[.//div[normalize-space()="Кислинка"]]'
                                 '//div[@class="scales__value-text"]')
    BITTERNESS_LOCATOR = (By.XPATH, './/div[@class="scales__item"]'
                                    '[.//div[normalize-space()="Горчинка"]]'
                                    '//div[@class="scales__value-text"]')
    BODY_LOCATOR = (By.XPATH, './/div[@class="scales__item"]'
                              '[.//div[normalize-space()="Насыщенность"]]'
                              '//div[@class="scales__value-text"]')

    def get_grind_value_locator(self, value):
        return (By.XPATH, f'.//div[contains(@class, "option-mill")]'
                          f'//ul[contains(@class, "dropdown-menu")]'
                          f'//button[contains(normalize-space(), "{value}")]')

    # Действия
    def select_grind_size(self, grind_size):
        self.safe_click_element(self.GRIND_DROPDOWN_LOCATOR)
        self.safe_click_element(self.get_grind_value_locator(grind_size))

    def get_coffee_acidity(self):
        return self.get_text(self.ACIDITY_LOCATOR)

    def get_coffee_bitterness(self):
        return self.get_text(self.BITTERNESS_LOCATOR)

    def get_coffee_body(self):
        return self.get_text(self.BODY_LOCATOR)