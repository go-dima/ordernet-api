import os

from SparkClient import SparkClient

if __name__ == "__main__":
    username = os.environ.get("spark_username", "Username not found")
    password = os.environ.get("spark_password", "Password not found")
    sparkClient = SparkClient(username, password)
    account = sparkClient.get_account()
    print(account)
    account_balance = sparkClient.get_balance(account.key)['a']
    # print_all_keys(account_balance)
