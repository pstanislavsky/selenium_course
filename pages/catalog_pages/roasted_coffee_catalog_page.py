from base.pages.base_catalog_page import BaseCatalogPage
from components.filters.panels.roasted_coffee_filter_panel import (
    RoastedCoffeeFilterPanel,
)


class RoastedCoffeeCatalogPage(BaseCatalogPage):
    """Страница интернет-магазина с каталогом кофе."""

    # Data
    URL = 'https://www.torrefacto.ru/catalog/roasted/'
    FILTER_PANEL_CLASS = RoastedCoffeeFilterPanel
