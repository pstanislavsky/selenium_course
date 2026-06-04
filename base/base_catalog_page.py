from selenium.webdriver.common.by import By

from base.base_page import BasePage


class BaseCatalogPage(BasePage):
    """Базовый класс для страниц каталога интернет-магазина."""

    # Локаторы
    PAGE_TITLE_LOCATOR = (By.XPATH, '//div[@class="heading__inner"]/h1')

    def get_product_card_locator_by_index(self, index):
        return (By.XPATH, f'(//div[@class="items__item"])[{index}]')

    def get_filter_value_locator(self, filter_name, filter_value):
        return (By.XPATH, (f'//div[contains(@class, "smart-filter__item")]'
                           f'[.//span[normalize-space()="{filter_name}"]]'
                           f'//label[contains(@class, "smart-filter__label")]'
                           f'[.//span[contains(normalize-space(), "{filter_value}")]]'))

    # Геттеры
    def get_product_card_by_index(self, index):
        return self.get_element(self.get_product_card_locator_by_index(index))

    # Действия
    def select_filter(self, filter_name, filter_value):
        self.safe_click_element(self.get_filter_value_locator(filter_name, filter_value))