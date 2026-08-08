import re


def parse_int(text, suffix=None) -> int:
    value = text.strip()

    if suffix is not None:
        value = value.removesuffix(suffix)

    return int(''.join(value.split()))


def parse_by_pattern(text, pattern) -> str | None:
    match = re.search(pattern, text)

    if match is None:
        return None

    return match.group()
