# from babel.numbers import format_decimal


NIS = '₪'


def print_all_keys(to_print):
    for key in to_print.keys():
        print('key:', key, 'value:', to_print[key])


def format_currency(number):
    # return format_decimal(number, locale='he_IL')
    return f"{number:,.2f}{NIS}"
