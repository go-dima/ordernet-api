import os
from functools import reduce
from getpass import getpass

from distlib.compat import raw_input

from SparkClient import SparkClient
from utils import format_currency


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
    print(f"Portfolio value: {format_currency(balance.portfolio_value)}")
    print(f"Holdings value: {format_currency(reduce(lambda a, b: a+b, map(lambda a: a.current_value, holdings)))}")
    print(f"Accumulative profit: {format_currency(reduce(lambda a, b: a + b, map(lambda a: a.profit, holdings)))}")
    print(f"Remaining cash: {format_currency(balance.remaining_cash)}")

    for holding in holdings:
        print(holding)
