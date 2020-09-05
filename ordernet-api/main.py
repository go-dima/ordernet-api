import os
from getpass import getpass

from distlib.compat import raw_input

from SparkClient import SparkClient
from utils import accumulate, print_currency, red_green_color


def get_username():
    user = os.environ.get("spark_username", None)
    if user is None:
        user = raw_input("No username configured, Type username: ")
    return user


def get_password():
    pwd = os.environ.get("spark_password", None)
    if pwd is None:
        pwd = getpass("No password configured, Type password: ")
    return pwd


if __name__ == "__main__":
    username = get_username()
    password = get_password()

    sparkClient = SparkClient(username, password)
    account = sparkClient.get_account()
    balance = sparkClient.get_balance(account.key)
    holdings = sparkClient.get_holdings(account.key)

    print(account)
    print_currency(prefix="Portfolio value", value=balance.portfolio_value)
    print_currency(prefix="Holdings value", value=accumulate(holdings, lambda a: a.current_value))
    print_currency(prefix="Accumulative profit", value=accumulate(holdings, lambda a: a.profit), text_format=red_green_color)
    print_currency(prefix="Remaining cash", value=balance.remaining_cash)

    for holding in holdings:
        print(holding)

