import json

import requests
import urls
from Account import Account
from utils import format_currency


class SparkClient:
    def __init__(self, username, password):
        r = requests.post(urls.authenticate_url, json={"username": username, "password": password})
        json_response = json.loads(r.text)
        if json_response['a'] != "Success":
            print('Failed to log in. Exiting...')
            exit(-1)
        self.authorization = f"Bearer {json_response['l']}"

    def get_account(self):
        response = requests.get(urls.static_data_url, headers={"Authorization": self.authorization})
        response_data = json.loads(response.text)
        all_data = list(filter(lambda data: data['b'] == 'ACC', response_data))
        account_data = all_data[0]['a'][0]  # Keys: ['_t' type, '_k' key, 'a' address?, 'b' bank?, 'c' not sure]

        account_key = account_data['_k']
        account_number = account_data['a']['b']
        account_owner = account_data['a']['e']
        return Account(account_key, account_number, account_owner)

    def get_balance(self, accountKey):
        response = requests.get(urls.balance_url + accountKey, headers={"Authorization": self.authorization})
        response_data = json.loads(response.text)
        print(f"Portfolio value: {format_currency(response_data['a']['o'])}")
        print(f"Remaining cash: {format_currency(response_data['a']['a'])}")
        return response_data
