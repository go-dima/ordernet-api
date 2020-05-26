import os

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
    print(account)
    balance = sparkClient.get_balance(account.key)
    print(f"Portfolio value: {format_currency(balance.portfolio_value)}")
    print(f"Remaining cash: {format_currency(balance.remaining_cash)}")
    holdings = sparkClient.get_holdings(account.key)
    for holding in holdings:
        print(holding)
