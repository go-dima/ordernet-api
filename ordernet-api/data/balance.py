class Balance:
    def __init__(self, init_json):
        self.portfolio_value = init_json['o']
        self.remaining_cash = init_json['a']