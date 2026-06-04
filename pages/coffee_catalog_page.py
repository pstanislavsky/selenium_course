from base.base_catalog_page import BaseCatalogPage


class CoffeeCatalogPage(BaseCatalogPage):
    """Страница интернет-магазина с каталогом кофе."""

    # Данные
    PAGE_URL = 'https://www.torrefacto.ru/catalog/roasted/'
    PAGE_TITLE = 'Жареный кофе в зернах от Torrefacto'

    # Действия
    def select_medium_roast_level(self):
        self.select_filter('Обжарка', 'Средняя обжарка')