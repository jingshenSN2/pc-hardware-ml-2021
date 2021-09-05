import requests


def get_crypto_data(crypto):
    print(f'Downloading historical data of {crypto}')
    url = f'https://coinmetrics.io/newdata/{crypto}.csv'
    req = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    with open(f'coin_metrics/{crypto}.csv', 'wb') as f:
        f.write(req.content)


for crypto in ['btc', 'eth', 'doge', 'ltc', 'bch', 'etc', 'xmr', 'dash']:
    get_crypto_data(crypto)
