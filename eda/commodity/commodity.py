import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import minmax_scale

com = pd.read_csv('../../data/commodity.csv')
com['Date'] = pd.to_datetime(com['Date'])

plt.figure(figsize=(20, 10))
for col in ['aluminum', 'copper', 'gold', 'silver', 'crude_oil']:
    com[col] = minmax_scale([com[col]], axis=1)[0]
    plt.plot(com['Date'], com[col], label=col)

plt.legend()
plt.ylabel('Normalized Price')
plt.title('Normalized Historical Prices of 5 Commodities in 2015-2021')
plt.savefig('commodity.png', bbox_inches='tight')

