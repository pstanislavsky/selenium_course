from urllib.parse import urlparse

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.components.base_component import BaseComponent
from utils.xpath import has_text, has_class


class BaseProductCollection(BaseComponent):
    def __len__(self):
        return self.count

    def __getitem__(self, index):
        return self.get_card_by_index(index)

    def __iter__(self):
        for card in self.get_all_cards():
            yield card

    # Data
    CARD_ID_ATTRIBUTE = None
    CARD_NAME_LINK_CLASS = None
    CARD_CLASS_MAP = None

    # Locators
    CARD_LOCATOR = None

    def _get_card_locator_by_name(self, product_name):
        return (
            By.XPATH,
            f'{self.CARD_LOCATOR[1]}'
            f'[.//a[{has_class(self.CARD_NAME_LINK_CLASS)} and {has_text(product_name)}]]',
        )

    def _get_card_locator_by_position(self, position):
        return (By.XPATH, f'({self.CARD_LOCATOR[1]})[{position}]')

    # Properties
    @property
    def count(self):
        try:
            return len(self.get_elements(self.CARD_LOCATOR, timeout=1))
        except TimeoutException:
            return 0

    # Actions
    def get_card_by_name(self, product_name):
        return self._get_card_by_locator(self._get_card_locator_by_name(product_name))

    def get_card_by_index(self, index):
        count = self.count

        if not -count <= index < count:
            raise IndexError(f'Product card index out of range: {index}.')

        if index < 0:
            index += count

        return self._get_card_by_position(index + 1)

    def get_all_cards(self):
        return [
            self._get_card_by_position(position)
            for position in range(1, self.count + 1)
        ]

    def _get_card_by_position(self, position):
        return self._get_card_by_locator(self._get_card_locator_by_position(position))

    def _get_card_by_locator(self, card_locator):
        card_id = self.get_element(card_locator).get_attribute(self.CARD_ID_ATTRIBUTE)
        card_locator = (
            By.XPATH,
            f'{self.CARD_LOCATOR[1]}' f'[@{self.CARD_ID_ATTRIBUTE} = "{card_id}"]',
        )
        card_class = self._get_card_class_by_locator(card_locator)

        return card_class(self, card_locator)

    def _get_card_class_by_locator(self, card_locator):
        card_link_locator = (
            By.XPATH,
            f'{card_locator[1]}' f'//a[{has_class(self.CARD_NAME_LINK_CLASS)}]',
        )
        card_link = self.get_element(card_link_locator).get_attribute('href')
        card_category = urlparse(card_link).path.strip('/').split('/')[1]

        try:
            return self.CARD_CLASS_MAP[card_category]
        except KeyError as error:
            raise KeyError(
                f'Card class is not mapped for category "{card_category}". '
                f'Available categories: {tuple(self.CARD_CLASS_MAP)}.'
            ) from error
