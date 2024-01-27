import requests as req


url = 'https://coinbase.com/v2/exchange-rates'
params = {
    'currency': 'EUR',
}
response = req.get(url, params=params)
r_json = response.json()
rates = r_json['data']['rates']

for currency, rate in rates.items():
    print(currency, rate)


print(response.url)
from_currency = input('Insert currency code: ').upper()
amount = int(input('Insert amount: '))
print(f'{amount} {params["currency"]} in {from_currency} is {amount * float(rates[from_currency])}')


