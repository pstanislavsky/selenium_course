def has_class(class_name):
    return f'contains(concat(" ", normalize-space(@class), " "), " {class_name} ")'


def has_text(text):
    return f'contains(normalize-space(), "{text}")'


def text_equals(text):
    return f'normalize-space() = "{text}"'


def svg_icon(icon_class):
    return f'*[local-name() = "svg"][{has_class(icon_class)}]'


def primary_or_fallback(primary_condition, fallback_condition, primary_search_path):
    return (
        f'{primary_condition}'
        f' or ('
        f'{fallback_condition} and not({primary_search_path}[{primary_condition}])'
        f')'
    )
