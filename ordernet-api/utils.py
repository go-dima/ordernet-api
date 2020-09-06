# from babel.numbers import format_decimal
import string
from functools import reduce
from typing import List
from colorama import Fore, Style

NIS = '₪'


def print_all_keys(to_print):
    for key in to_print.keys():
        print('key:', key, 'value:', to_print[key])


def format_currency(number):
    # return format_decimal(number, locale='he_IL')
    return f"{number:,.2f}{NIS}"


def accumulate(source: List, property_func):
    return reduce(lambda a, b: a + b, map(property_func, source))


def print_currency(value, prefix: string = "", text_format=lambda a: a):
    print(f"{prefix}: {text_format(format_currency(value))}")


def red_green_color(param):
    if param[0] == '-':
        return Fore.RED + param + Style.RESET_ALL
    return Fore.GREEN + param + Style.RESET_ALL
