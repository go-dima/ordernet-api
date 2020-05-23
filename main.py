import json
import os
import urls

import requests
from Account import Account
from Session import Session
from utils import print_all_keys, format_number

session = Session()


def get_account():
    response = requests.get(urls.static_data_url, headers={"Authorization": session.authorization})
    response_data = json.loads(response.text)
    all_data = list(filter(lambda data: data['b'] == 'ACC', response_data))
    account_data = all_data[0]['a'][0]  # Keys: ['_t' type, '_k' key, 'a' address?, 'b' bank?, 'c' not sure]

    account_key = account_data['_k']
    account_number = account_data['a']['b']
    account_owner = account_data['a']['e']
    return Account(account_key, account_number, account_owner)


def get_balance(accountKey: Account):
    response = requests.get(urls.balance_url + accountKey, headers={"Authorization": session.authorization})
    response_data = json.loads(response.text)
    print(f"Portfolio value: {format_number(response_data['a']['o'])}")
    print(f"Remaining cash: {format_number(response_data['a']['a'])}")
    return response_data


def authenticate():
    username = os.environ.get("spark_username", "Username not found")
    password = os.environ.get("spark_password", "Password not found")
    r = requests.post(urls.authenticate_url, json={"username": username, "password": password})
    json_response = json.loads(r.text)
    if r.status_code != 200 or json_response['p'] is False:
        print('Failed to log in. Exiting...')
        exit(-1)
    session.authorization = f"Bearer {json_response['l']}"


if __name__ == "__main__":
    authenticate()
    account = get_account()
    print(account)
    account_balance = get_balance(account.key)['a']
    # print_all_keys(account_balance)
