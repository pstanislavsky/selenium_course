from base.components.base_cart_gift_card import BaseCartGiftCard
from utils.parsers import parse_int


class TeaCartGiftCard(BaseCartGiftCard):
    # Properties
    @property
    def package_size(self):
        return parse_int(
            self.get_text(self._get_option_value_locator('Упаковка')), suffix='г'
        )

    @property
    def harvest(self):
        return self.get_text(self._get_option_value_locator('Урожай'))
