from typing import Iterable
from pandas import Series


def phone_formatter(phones: Series, strip: Iterable) -> Series:
    phones = phones.astype(str)
    for expression in strip:
        phones = phones.str.replace(expression, '', regex=True)
    return phones
