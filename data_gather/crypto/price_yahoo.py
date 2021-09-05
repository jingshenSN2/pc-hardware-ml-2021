import requests
import time


def get_crypto_price(crypto):
    print(f'Downloading historical price of {crypto}-USD')
    ts = int(time.time())
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{crypto}-USD?period1=0&period2={ts}&interval=1d&events=history&includeAdjustedClose=true'
    req = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    with open(f'yahoo_finance/{crypto}-USD.csv', 'wb') as f:
        f.write(req.content)


for crypto in ['BTC', 'ETH', 'Doge', 'LTC', 'BCH', 'ETC', 'XMR', 'Dash']:
    get_crypto_price(crypto)
