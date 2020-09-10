from string import Template

broker = "meitav"
url = f"https://spark{broker}.ordernet.co.il/api"

# API
authenticate_url = f"{url}/Auth/Authenticate"
static_data_url = f"{url}/DataProvider/GetStaticData"

balance_url = f"{url}/Account/GetAccountSecurities?accountKey="  # GET
monthly_yields_url = Template(f"{url}/Account/GetAccountMonthlyYields?accountKey=$account&year=$year")  # GET
holdings_url = f"{url}/Account/GetHoldings?accountKey="  # GET

user_personalization_url = f"{url}/UserPersonalization"
get_status_url = f"{user_personalization_url}/GetStatus"
tab_module_settings_url = f"{user_personalization_url}/UpdateTabModuleSetting"
transactions_url = f"{url}/GetAccountTransactions"
personal_url = (
    Template(f"{transactions_url}?accountKey=$account&endDate=$untilT00:00:00.000Z&startDate=$fromT00:00:00.000Z"))

# Subscribe
subscribe_url = f"{url}/subscription/subscribe"
unsubscribe_url = f"{url}/subscription/unsubscribe"

# Personalized
home_page_url = tab_module_settings_url + "?tmId=iyxnf0"
my_account_url = tab_module_settings_url + "?tmId=syl5va"
my_account_balance__tab_url = tab_module_settings_url + "?tmId=ryxb0z"
