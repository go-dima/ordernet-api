import os

from SparkClient import SparkClient
from utils import format_currency

if __name__ == "__main__":
    username = os.environ.get("spark_username", "Username not found")
    password = os.environ.get("spark_password", "Password not found")
    sparkClient = SparkClient(username, password)
    account = sparkClient.get_account()
    print(account)
    balance = sparkClient.get_balance(account.key)
    print(f"Portfolio value: {format_currency(balance.portfolio_value)}")
    print(f"Remaining cash: {format_currency(balance.remaining_cash)}")
    holdings = sparkClient.get_holdings(account.key)
    for holding in holdings:
        print(holding)
