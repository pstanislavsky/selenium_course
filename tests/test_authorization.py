from pages.main_page import MainPage
from pages.coffee_catalog_page import CoffeeCatalogPage
from components.coffee_product_card import CoffeeProductCard


def test_authorization(set_up):
    driver = set_up
    main_page = MainPage(driver)
    coffee_catalog = CoffeeCatalogPage(driver)


    main_page.open()
    main_page.header.open_coffee_catalog()
    coffee_catalog.should_be_opened()
    coffee_catalog.select_medium_roast_level()
    # coffee_catalog.select_filter('География', 'Эфиопия')
    card = CoffeeProductCard(coffee_catalog.get_product_card_by_index(1))
    print(card.get_product_name())
    print(card.get_product_price())
    #card.select_product_size('500 г')
    card.select_grind_size('Мелкий помол')
    coffee_catalog.wait(2)
    card.add_product_to_cart()
    coffee_catalog.wait(2)
    coffee_catalog.header.open_cart()

    coffee_catalog.wait(5)