class Account(object):
    def __init__(self, account_key, account_number, account_owner):
        self.key = account_key
        self.number = account_number
        self.owner = account_owner

    def __str__(self):
        return self.key + ", Owner: " + self.owner
