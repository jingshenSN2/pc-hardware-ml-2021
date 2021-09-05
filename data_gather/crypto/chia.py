import time
import pandas as pd
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--lang=zh-CN')
browser = webdriver.Chrome(options=chrome_options)


def get_chia_info(field):
    print(f'Requesting chia {field} history data...')
    browser.get(f'https://xchscan.com/charts/{field}')
    time.sleep(5)
    x_data = browser.execute_script('return this.Highcharts.charts[0].series[0].xData;')  # time
    y_data = browser.execute_script('return this.Highcharts.charts[0].series[0].yData;')  # field
    df = pd.DataFrame([x_data, y_data]).T
    df.columns = ['time', field]
    df.to_csv(f'chia/chia-{field}.csv', index=False)


get_chia_info('netspace')
get_chia_info('chia-price')
get_chia_info('market-cap')
browser.quit()
