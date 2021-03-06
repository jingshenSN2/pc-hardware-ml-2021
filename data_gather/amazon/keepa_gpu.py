import time

import requests
from data_gather.api_key import *

days = 66


def get_gpu(manufacturer, product, ASIN_list):
    """
    :param manufacturer: manufacturer of gpu, as part of save path
    :param product: gpu product name
    :param ASIN_list: list of ASINs
    :return:
    """
    for ASIN in ASIN_list:
        print(f'Requesting information of manufacturer: {manufacturer}, product: {product}, ASIN: {ASIN}')
        url = f'https://api.keepa.com/product?key={keepa_access_key}&domain=1&asin={ASIN}&history=1&buybox=1&days={days}'
        req = requests.get(url)
        with open(f'gpu/{manufacturer}/{product}-{ASIN}.json', 'wb') as f:
            f.write(req.content)
        time.sleep(45)


# MSI
get_gpu('MSI', 'NVIDIA Geforce GTX 1050 Ti', ['B01MAZ357B', 'B01N683IAQ'])
get_gpu('MSI', 'NVIDIA Geforce GTX 1650', ['B086VR4VHX', 'B086VQPW2T', 'B08GL81369'])
get_gpu('MSI', 'NVIDIA Geforce GTX 1660', ['B07PBLDV3D', 'B07P9G4QK1'])
get_gpu('MSI', 'NVIDIA Geforce GTX 1660 Super', ['B07ZK69HDK', 'B07ZHDZ1K6'])
get_gpu('MSI', 'NVIDIA Geforce GTX 1660 Ti', ['B07N824KNV', 'B07N825Y1L'])
get_gpu('MSI', 'NVIDIA Geforce RTX 2060', ['B07MC23VS4', 'B07MQ36Z6L'])
get_gpu('MSI', 'NVIDIA Geforce RTX 2060 Super', ['B07YXQ19NC'])
get_gpu('MSI', 'NVIDIA Geforce RTX 2070', ['B07J4VJX6L', 'B081YJPKTM', 'B082P1BF7H', 'B07JCD8GQN'])
get_gpu('MSI', 'NVIDIA Geforce RTX 2070 Super', ['B0856BVRFL', 'B07J4VJX6L'])
get_gpu('MSI', 'NVIDIA Geforce RTX 2080', ['B07GHXQTGZ'])
get_gpu('MSI', 'NVIDIA Geforce RTX 2080 Super', ['B07Y8NP7X7', 'B07VDMGYGZ'])
get_gpu('MSI', 'NVIDIA Geforce RTX 2080 Ti', ['B07GJ3ZD69'])
get_gpu('MSI', 'NVIDIA Geforce RTX 3060', ['B08WPJ5P4R', 'B08WPRMVWB'])
get_gpu('MSI', 'NVIDIA Geforce RTX 3070', ['B0956WYQ1B', 'B08KWPDXJZ', 'B08KWN2LZG'])
get_gpu('MSI', 'NVIDIA Geforce RTX 3070 Ti', ['B096HJC18P', 'B096HQC9Y5'])
get_gpu('MSI', 'NVIDIA Geforce RTX 3080', ['B0932CTHP6'])
get_gpu('MSI', 'NVIDIA Geforce RTX 3080 Ti', ['B095VZ6F73'])
get_gpu('MSI', 'NVIDIA Geforce RTX 3090', ['B08HRBW6VB'])
get_gpu('MSI', 'AMD Radeon RX 580', ['B06XZQMMHJ', 'B06Y19NMP3'])
get_gpu('MSI', 'AMD Radeon RX 5500 XT', ['B082G34GSL', 'B082G2XDLL'])
get_gpu('MSI', 'AMD Radeon RX 5600 XT', ['B08CKDLN91', 'B0843VSJ7D', 'B083VPXN78'])
get_gpu('MSI', 'AMD Radeon RX 5700 XT', ['B07WNSP41M'])
get_gpu('MSI', 'AMD Radeon RX 6700 XT', ['B08Z72P3R9'])
get_gpu('MSI', 'AMD Radeon RX 6800', ['B08RHQC4KQ'])
get_gpu('MSI', 'AMD Radeon RX 6800 XT', ['B08RJ6YBH5'])
get_gpu('MSI', 'AMD Radeon RX 6900 XT', ['B08W2GPR62'])

# EVGA
get_gpu('EVGA', 'NVIDIA Geforce GTX 960', ['B00SL2TQ2C'])
get_gpu('EVGA', 'NVIDIA Geforce GTX 1050 ti', ['B01MEFABEL'])
get_gpu('EVGA', 'NVIDIA Geforce GTX 1060', ['B01KU2CIIY', 'B01N683IAQ'])
get_gpu('EVGA', 'NVIDIA Geforce GTX 1650', ['B085WV18XN', 'B08CPL5BB1'])
get_gpu('EVGA', 'NVIDIA Geforce GTX 1660', ['B07RJGL33C'])
get_gpu('EVGA', 'NVIDIA Geforce GTX 1660 Super', ['B07ZHZL2JB'])
get_gpu('EVGA', 'NVIDIA Geforce GTX 1660 Ti', ['B07NBHXKK6'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 2060', ['B083GH7LXW', 'B07P11QHZG'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 2060 Super', ['B07VM9Q9R8', 'B07TLPWBJ4'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 2070', ['B07J63W42X'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 2070 Super', ['B07YMPZCPT'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 2080', ['B07GHVK4KN', 'B07GHVWMBS'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 2080 Super', ['B07VJPNG1M', 'B07VCH31N9'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 2080 Ti', ['B07KSPW8HQ', 'B07KVKRLG2', 'B07GHW9VJZ'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 3060', ['B08WM28PVH'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 3070 Ti', ['B096WM6JFS'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 3080 Ti', ['B09622N253'])
get_gpu('EVGA', 'NVIDIA Geforce RTX 3090', ['B08J61SS5R', 'B08J5F3G18'])

# ASUS
get_gpu('ASUS', 'NVIDIA Geforce GTX 1050 Ti', ['B01M360WG6', 'B01MG9AKKZ', 'B079JSKCW3'])
get_gpu('ASUS', 'NVIDIA Geforce GTX 1650 Super', ['B081L1JHGT', 'B081KY5L57'])
get_gpu('ASUS', 'NVIDIA Geforce GTX 1660', ['B07PFM57FL'])
get_gpu('ASUS', 'NVIDIA Geforce GTX 1660 Super', ['B07ZHWQ81N', 'B07ZGXG8GM', 'B081SPGMBD'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 2060', ['B07R18TH1X', 'B07MSK1H93'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 2060 Super', ['B085CP6W5Y'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 2070', ['B07JFYT2KD'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 2070 Super', ['B07TXRW3HX', 'B07TYWQ1SW'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 2080', ['B07GKD7DND', 'B083R2SCRL'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 2080 Super', ['B07VFKM4VQ'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 2080 Ti', ['B07HY6QWXN'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 3060', ['B08WHJPBFX', 'B08WGTL4CW'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 3070', ['B08L8LG4M3', 'B08MT6B58K'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 3070 Ti', ['B096YQ6WVW'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 3080', ['B08J6F174Z', 'B08HH5WF97'])
get_gpu('ASUS', 'NVIDIA Geforce RTX 3090', ['B08J6GMWCQ', 'B08HJGNJ81'])
get_gpu('ASUS', 'AMD Radeon RX 570', ['B06Y5WGXX3'])
get_gpu('ASUS', 'AMD Radeon RX 580', ['B071L1VGQW', 'B071D8YQJD'])
get_gpu('ASUS', 'AMD Radeon RX 5500 XT', ['B083FM3XPJ', 'B082G4J2WG'])
get_gpu('ASUS', 'AMD Radeon RX 5600 XT', ['B083WFK6M4'])
get_gpu('ASUS', 'AMD Radeon RX 5700 XT', ['B07XC5CQDK'])
get_gpu('ASUS', 'AMD Radeon RX 6700 XT', ['B08YWZHJDZ', 'B08YX8D8ST'])
get_gpu('ASUS', 'AMD Radeon RX 6800', ['B08NWJ29NB'])
get_gpu('ASUS', 'AMD Radeon RX 6900 XT', ['B08S6Z2HGW', 'B08R81J62G'])

# XFX
get_gpu('XFX', 'AMD Radeon RX 570', ['B077VX31FZ'])
get_gpu('XFX', 'AMD Radeon RX 580', ['B06Y66K3XD'])
get_gpu('XFX', 'AMD Radeon RX 5500 XT', ['B082KYFDYC'])
get_gpu('XFX', 'AMD Radeon RX 5600 XT', ['B086PZGTHZ'])
get_gpu('XFX', 'AMD Radeon RX 5700 XT', ['B082MQ4QTZ', 'B07WRYC3MT'])
get_gpu('XFX', 'AMD Radeon RX 6700 XT', ['B08YK97LKC', 'B08YKH7VMN'])
get_gpu('XFX', 'AMD Radeon RX 6800', ['B08NN76VJD'])
get_gpu('XFX', 'AMD Radeon RX 6800 XT', ['B08NX14LV1', 'B08N6ZLX9B'])
get_gpu('XFX', 'AMD Radeon RX 6900 XT', ['B08SVZNFWR', 'B08Q9SCPGD'])

# Sapphire
get_gpu('Sapphire', 'AMD Radeon RX 570', ['B079VSD38Y', 'B089V8D54S', 'B083R4XQSH', 'B071CF1JFV', 'B071XNH5BC'])
get_gpu('Sapphire', 'AMD Radeon RX 580', ['B083W2JP4W', 'B06ZZ6FMF8', 'B071QX74F9'])
get_gpu('Sapphire', 'AMD Radeon RX 5500 XT', ['B082G2YY99', 'B00JRKKSTC'])
get_gpu('Sapphire', 'AMD Radeon RX 5600 XT', ['B083R25Z94'])
get_gpu('Sapphire', 'AMD Radeon RX 5700 XT', ['B07WC7683C', 'B07XMNGVVD', 'B081KRC1H2'])
get_gpu('Sapphire', 'AMD Radeon RX 6700 XT', ['B08YN79ZW2', 'B08YNQ4ZM1'])
get_gpu('Sapphire', 'AMD Radeon RX 6800', ['B08NXYBVDB'])
get_gpu('Sapphire', 'AMD Radeon RX 6800 XT', ['B08NXXT7WN'])
get_gpu('Sapphire', 'AMD Radeon RX 6900 XT', ['B08QQFW9YS'])

# Gigabyte
get_gpu('Gigabyte', 'NVIDIA Geforce GTX 1030', ['B071DY2VJR'])
get_gpu('Gigabyte', 'NVIDIA Geforce GTX 1050 Ti', ['B01M25X363', 'B01M4KGTNI', 'B06WWLWWJM'])
get_gpu('Gigabyte', 'NVIDIA Geforce GTX 1650', ['B07QHGKC2D', 'B086T6W63R'])
get_gpu('Gigabyte', 'NVIDIA Geforce GTX 1660', ['B07P76G428'])
get_gpu('Gigabyte', 'NVIDIA Geforce GTX 1660 Ti', ['B07NJPKZQG'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 2060', ['B07NYKD5FT'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 2060 Super', ['B085CP6W5Y'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 2070', ['B08K3B3VPF', 'B07WGQT52X', 'B07R726461'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 2070 Super', ['B07WN6RVHH', 'B07WN6WB4G'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 2080 Super', ['B07WQG7S5S'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 2080 Ti', ['B07YLDH9KT', 'B07GJKR7RW'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 3060', ['B08X4V8N5Q', 'B0971BG25M'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 3070', ['B098Q4M4WH', 'B096YM573B'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 3080 Ti', ['B083HZF4GV'])
get_gpu('Gigabyte', 'NVIDIA Geforce RTX 3090', ['B08KTWVHQP', 'B08R5D3374', 'B08HJRF2CN'])
get_gpu('Gigabyte', 'AMD Radeon RX 570', ['B06Y3RT952'])
get_gpu('Gigabyte', 'AMD Radeon RX 580', ['B0842VMKM5', 'B06Y3ZQPY6'])
get_gpu('Gigabyte', 'AMD Radeon RX 5500 XT', ['B082BXNYCQ'])
get_gpu('Gigabyte', 'AMD Radeon RX 5600 XT', ['B083YJFHFH'])
get_gpu('Gigabyte', 'AMD Radeon RX 5700 XT', ['B0842SCK5T', 'B07W95D5V3'])
get_gpu('Gigabyte', 'AMD Radeon RX 6700 XT', ['B08Z5M4KFM'])
get_gpu('Gigabyte', 'AMD Radeon RX 6800', ['B08NYLMBJY'])
get_gpu('Gigabyte', 'AMD Radeon RX 6800 XT', ['B08PFX6PZ6'])
get_gpu('Gigabyte', 'AMD Radeon RX 6900 XT', ['B083HZ3M1X'])

# ZOTAC
get_gpu('ZOTAC', 'NVIDIA Geforce GTX 1030', ['B0711NWFJX'])
get_gpu('ZOTAC', 'NVIDIA Geforce GTX 1050 ti', ['B01MCU1ERO', 'B01M27X994'])
get_gpu('ZOTAC', 'NVIDIA Geforce GTX 1060', ['B01KKJAJM4'])
get_gpu('ZOTAC', 'NVIDIA Geforce GTX 1650', ['B07QF1H9YR', 'B0881YZJ45'])
get_gpu('ZOTAC', 'NVIDIA Geforce GTX 1650 Super', ['B07ZKSZ5LF'])
get_gpu('ZOTAC', 'NVIDIA Geforce GTX 1660', ['B07XV7FNR2', 'B07PF8YTCX', 'B07PD2LG7Z'])
get_gpu('ZOTAC', 'NVIDIA Geforce GTX 1660 Super', ['B07Z8PWC6R'])
get_gpu('ZOTAC', 'NVIDIA Geforce GTX 1660 Ti', ['B07NMWQXLR'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 2060', ['B07TDN1SC5'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 2060 Super', ['B07TMJJVQ1'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 2070', ['B07JB9YY8V', 'B07JCRHKCL'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 2070 Super', ['B07XSPWMP9'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 2080', ['B07NC8J9YF', 'B07K9SCJRK', 'B07GG9L5X1', 'B07KB9S34G'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 2080 Super', ['B07TKFMHB4', 'B07WZFXVGT'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 2080 Ti', ['B07KB1RFPW', 'B07KB86GYZ'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 3060', ['B08W8DGK3X'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 3070', ['B08W44ZLRP'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 3070 Ti', ['B096TZHXYN'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 3080 Ti', ['B0971RHNLP', 'B0964DB2P9'])
get_gpu('ZOTAC', 'NVIDIA Geforce RTX 3090', ['B08ZL6XD9H', 'B095V4SNXB'])
