import os

from SparkClient import SparkClient

if __name__ == "__main__":
    username = os.environ.get("spark_username", "Username not found")
    password = os.environ.get("spark_password", "Password not found")
    sparkClient = SparkClient(username, password)
    account = sparkClient.get_account()
    print(account)
    sparkClient.get_balance(account.key)
    holdings = sparkClient.get_holdings(account.key)
    for holding in holdings:
        print(holding)
