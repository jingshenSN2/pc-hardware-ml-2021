import pandas as pd
from functools import reduce
from datetime import datetime

price = pd.read_csv('../../data_gather/crypto/chia/chia-chia-price.csv')
market_cap = pd.read_csv('../../data_gather/crypto/chia/chia-market-cap.csv')
net_space = pd.read_csv('../../data_gather/crypto/chia/chia-netspace.csv')

price['Date'] = price['time'].apply(lambda ts: datetime.fromtimestamp(int(ts/1000)).date())
market_cap['Date'] = market_cap['time'].apply(lambda ts: datetime.fromtimestamp(int(ts/1000)).date())
net_space['Date'] = net_space['time'].apply(lambda ts: datetime.fromtimestamp(int(ts/1000)).date())

price.drop('time', axis=1, inplace=True)
market_cap.drop('time', axis=1, inplace=True)
net_space.drop('time', axis=1, inplace=True)

chia_df = reduce(lambda df1, df2: pd.merge(df1, df2, on=['Date'], how='inner'), [price, market_cap, net_space])

chia_df = chia_df[['Date', 'chia-price', 'market-cap', 'netspace']]

print(chia_df.describe())

#         chia-price    market-cap      netspace
# count   170.000000  1.700000e+02  1.700000e+02
# mean    335.451406  2.241181e+08  2.071583e+19
# std     348.246477  1.913704e+08  1.614025e+19
# min       0.000000  0.000000e+00  1.308328e+17
# 25%       0.000000  0.000000e+00  1.544806e+18
# 50%     255.137120  2.725670e+08  2.507439e+19
# 75%     417.706855  3.652890e+08  3.632367e+19
# max    1551.248311  5.835614e+08  4.094060e+19

chia_df.to_csv('../../data/chia.csv', index=False)

print(1)
