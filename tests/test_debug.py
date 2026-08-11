from time import sleep

from pages.catalog_pages.roasted_coffee_catalog_page import RoastedCoffeeCatalogPage
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.cart_page import CartPage

email = 'hivernampbtwjcxvrb@kjkpc.net'
password = 'qwerty'
discount_code = 'NEW15'


def test_debug(set_up):
    driver = set_up
    main_page = MainPage(driver)
    coffee_catalog = RoastedCoffeeCatalogPage(driver)
    cart = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    main_page.open()
    main_page.cookie_banner.accept_cookie_consent()
    # main_page.log_in(email, password)

    main_page.header.catalog_menu.open_roasted_coffee_catalog()
    # coffee_catalog.filters.roast.check_option('Средняя обжарка')
    # coffee_catalog.filters.roast.check_option('Самая темная обжарка')
    coffee_catalog.filters.roast.check_option('Темная обжарка')
    # coffee_catalog.filters.suitable_for.check_option('Для фильтра')
    coffee_catalog.filters.suitable_for.check_option('Для эспрессо')
    coffee_catalog.filters.bestseller.enable()
    coffee_catalog.filters.price.set_max_value(3000)
    # coffee_catalog.filters.price.set_range(200, 2000)
    coffee_catalog.filters.package_size.select_option('500 г')
    # coffee_catalog.filters.origin.check_option('Африка')
    coffee_catalog.filters.origin.check_option('Лат. Америка')
    # coffee_catalog.filters.origin.check_option('Азия')
    # coffee_catalog.filters.processing_method.check_option('Сухая')
    # coffee_catalog.filters.brewing_method.check_option('Фильтр-кофе')
    coffee_catalog.filters.brewing_method.check_option('Эспрессо')
    coffee_catalog.filters.coffee_type.check_option('Арабика')
    print(
        (
            'Простая обжарка:',
            coffee_catalog.applied_filters.is_applied('Обжарка'),
        )
    )
    print(
        (
            'Подходит с параметром:',
            coffee_catalog.applied_filters.is_applied('Подходит', 'Для фильтра'),
        )
    )
    print(
        (
            'Вид кофе последним:',
            coffee_catalog.applied_filters.is_applied('Вид кофе', 'Арабика'),
        )
    )
    print(('География:', coffee_catalog.applied_filters.is_applied('География')))

    coffee_catalog.applied_filters.remove('Вид кофе')
    coffee_catalog.filters.coffee_type.check_option('Арабика')
    coffee_catalog.applied_filters.remove('Обжарка')
    coffee_catalog.filters.roast.check_option('Темная обжарка')
    # coffee_catalog.applied_filters.clear_all()
    # coffee_catalog.filters.roast.check_option('Средняя обжарка')
    # coffee_catalog.filters.suitable_for.check_option('Для фильтра')
    # coffee_catalog.filters.price.set_max_value(2000)
    # coffee_catalog.filters.origin.check_option('Лат. Америка')

    print(
        'Фильтры:',
        [
            (
                coffee_catalog.filters.roast.title,
                coffee_catalog.filters.roast.checked_options,
            ),
            (
                coffee_catalog.filters.suitable_for.title,
                coffee_catalog.filters.suitable_for.checked_options,
            ),
            (
                coffee_catalog.filters.bestseller.title,
                coffee_catalog.filters.bestseller.is_on,
            ),
            (
                coffee_catalog.filters.price.title,
                (
                    coffee_catalog.filters.price.min_value,
                    coffee_catalog.filters.price.max_value,
                ),
            ),
            (
                coffee_catalog.filters.package_size.title,
                coffee_catalog.filters.package_size.selected_option,
            ),
            (
                coffee_catalog.filters.origin.title,
                coffee_catalog.filters.origin.checked_options,
            ),
            (
                coffee_catalog.filters.brewing_method.title,
                coffee_catalog.filters.brewing_method.checked_options,
            ),
            (
                coffee_catalog.filters.coffee_type.title,
                coffee_catalog.filters.coffee_type.checked_options,
            ),
        ],
    )
    print('В каталоге всего:', coffee_catalog.products.count)

    for card in coffee_catalog.products:
        card.package_size.select_option('500 г')
        card.gas.select_option('С азотом')
        # card.grind.select_option('Мелкий помол')
        card.add_to_cart()
        card.increase_quantity()
        card.decrease_quantity()
        card.set_quantity('5')
        print(
            [
                'В каталоге:',
                card.link,
                card.name,
                card.number,
                card.price,
                card.rating,
                (card.acidity, card.bitterness, card.body),
                card.package_size.selected_option,
                card.gas.selected_option,
                card.grind.selected_option,
                card.quantity,
            ]
        )
    coffee_catalog.applied_filters.clear_all()
    card = coffee_catalog.products.get_card_by_name('Азиатская смесь')
    product_page = card.open()
    product_page.package_size.select_option('500 г')
    # product_page.grind.select_option('В зернах')
    product_page.gas.select_option('С азотом')
    product_page.add_to_cart()
    product_page.increase_quantity()
    product_page.decrease_quantity()
    product_page.set_quantity('5')
    print(
        [
            'На отдельной странице:',
            product_page.URL,
            product_page.name,
            product_page.number,
            product_page.price,
            product_page.rating,
            (product_page.acidity, product_page.bitterness, product_page.body),
            (product_page.processing_method, product_page.coffee_type),
            product_page.package_size.selected_option,
            product_page.gas.selected_option,
            product_page.grind.selected_option,
            product_page.quantity,
        ]
    )

    coffee_catalog.header.open_cart()
    for card in cart.products:
        card.increase_quantity()
        card.decrease_quantity()
        card.set_quantity('10')
        print(
            [
                'В корзине:',
                card.link,
                card.display_name,
                card.number,
                card.name,
                (card.price, card.price_per_unit),
                card.quantity,
                card.package_size,
                card.gas,
                card.grind,
            ]
        )
    print('Корзина пуста:', cart.is_empty)
    for gift in cart.gifts:
        print(
            [
                'Подарок:',
                gift.link,
                gift.display_name,
                gift.number,
                gift.name,
                (gift.price, gift.old_price),
                gift.quantity,
            ]
        )
        for attr in ('package_size', 'grind', 'harvest'):
            if hasattr(gift, attr):
                print(f'Плюс: "{attr}" = "{getattr(gift, attr)}"')
    print(cart.products[-1].name, 'через индекс!')
    print('Корзина пуста:', cart.is_empty)
    cart.apply_discount(discount_code)
    cart.remove_discount(discount_code)
    cart.apply_discount(discount_code)
    print(
        [
            'Корзина:',
            cart.total_quantity,
            cart.total_weight,
            ('Base:', cart.base_price),
            ('Discount:', cart.discount),
            ('Total:', cart.total_price),
        ]
    )
    # cart.clear()

    cart.proceed_to_checkout()
    print(
        [
            'Чекаунт:',
            checkout_page.total_quantity,
            ('Base:', checkout_page.base_price),
            ('Discount:', checkout_page.discount),
            ('Delivery:', checkout_page.delivery),
            ('Total:', checkout_page.total_price),
        ]
    )
    sleep(2)
