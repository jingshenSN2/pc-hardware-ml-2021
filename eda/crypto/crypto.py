import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import minmax_scale

com = pd.read_csv('../../data/coin_metrics/PriceUSD.csv')
com['date'] = pd.to_datetime(com['date'])

plt.figure(figsize=(20, 10))
for col in ['btc','eth','doge','ltc','bch','etc','xmr','dash']:
    com[col] = minmax_scale([com[col]], axis=1)[0]
    plt.plot(com['date'], com[col], label=col)

plt.legend()
plt.ylabel('Normalized Price')
plt.title('Normalized Historical Prices of 8 Cryptocurrencies in 2017-2021')
plt.savefig('crypto.png', bbox_inches='tight')

