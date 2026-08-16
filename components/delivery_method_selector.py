from selenium.webdriver.common.by import By

from components.common.radio_selector import RadioSelector
from utils.parsers import parse_integer, normalize_text
from utils.xpath import has_class, has_text


class DeliveryMethodSelector(RadioSelector):
    def __init__(self, parent, root_locator):
        super().__init__(
            parent, root_locator, self.OPTION_LOCATOR, self.OPTION_NAME_LOCATOR
        )

    # Locators
    OPTION_LOCATOR = (By.XPATH, f'.//div[{has_class("delivery-item")}]')
    OPTION_NAME_LOCATOR = (By.XPATH, './/span[@data-id = "name"]')
    OPTION_DESCRIPTION_LOCATOR = (By.XPATH, './/span[@data-id = "description"]')

    def _get_option_radio_locator(self, option):
        option_name, option_description = option

        return (
            By.XPATH,
            f'{self.option_locator[1]}'
            f'[{self.option_name_locator[1]}[{has_text(option_name)}]]'
            f'[{self.OPTION_DESCRIPTION_LOCATOR[1]}[{has_text(option_description)}]]'
            f'//input[@type = "radio"]',
        )

    def _get_option_label_locator(self, option):
        option_name, option_description = option

        return (
            By.XPATH,
            f'{self.option_locator[1]}'
            f'[{self.option_name_locator[1]}[{has_text(option_name)}]]'
            f'[{self.OPTION_DESCRIPTION_LOCATOR[1]}[{has_text(option_description)}]]'
            f'//label[{has_class("delivery-item__label")}]',
        )

    # Properties
    @property
    def selected_option(self):
        option_names = [
            option_name.text.strip()
            for option_name in self.get_elements(self.option_name_locator)
        ]
        option_descriptions = [
            normalize_text(option_description.text)
            for option_description in self.get_elements(self.OPTION_DESCRIPTION_LOCATOR)
        ]
        options = list(zip(option_names, option_descriptions, strict=True))

        for option in options:
            if self.is_option_selected(option):
                return option

        return None

    @property
    def selected_option_price(self):
        selected_option = self.selected_option

        if selected_option is None:
            return None

        option_price_locator = (
            By.XPATH,
            f'{self._get_option_label_locator(selected_option)[1]}'
            f'//span[@data-id = "price"]',
        )

        option_price = self.get_text(option_price_locator)

        if option_price == 'Бесплатно':
            return 0

        return parse_integer(option_price, suffix='₽')
