import re


def parse_int(text, suffix=None) -> int:
    minus_sign_translation = str.maketrans(
        {
            '\u2012': '-',
            '\u2013': '-',
            '\u2014': '-',
            '\u2212': '-',
        }
    )

    value = text.strip().translate(minus_sign_translation)

    if suffix is not None:
        value = value.removesuffix(suffix)

    return int(''.join(value.split()))


def parse_by_pattern(text, pattern) -> str | None:
    match = re.search(pattern, text)

    if match is None:
        return None

    return match.group()
