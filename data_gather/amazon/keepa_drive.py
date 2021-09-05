import requests
# subscribe on https://keepa.com/#!api to get access key
access_key = 'cju3topabp5hdq28hn3jhod62fb7noiitniam32kd71f76v9nta6t4or5qms00gv'


def get_ssd(manufacturer, product, ssd_type, ASIN_dict):
    """
    :param manufacturer: manufacturer of ssd, as part of save path
    :param product: ssd product name
    :param ssd_type: 'm.2' or '2.5in', type of ssd, as part of save path
    :param ASIN_dict: dict of ASIN, key is capacity and value is ASIN
    :return:
    """
    for capacity, ASIN in ASIN_dict.items():
        print(f'Requesting ssd information of manufacturer: {manufacturer}, product: {product}, capacity: {capacity}, ASIN: {ASIN}')
        url = f'https://api.keepa.com/product?key={access_key}&domain=1&asin={ASIN}&history=1&buybox=1'
        req = requests.get(url)
        with open(f'ssd/{ssd_type}/{manufacturer}/{product}-{capacity}-{ASIN}.json', 'wb') as f:
            f.write(req.content)


def get_hdd(manufacturer, product, ASIN_dict):
    """
    :param manufacturer: manufacturer of hdd, as part of save path
    :param product: hdd product name
    :param ASIN_dict: key is capacity and value is ASIN
    :return:
    """
    for capacity, ASIN in ASIN_dict.items():
        print(f'Requesting hdd information of manufacturer: {manufacturer}, product: {product}, capacity: {capacity}, ASIN: {ASIN}')
        url = f'https://api.keepa.com/product?key={access_key}&domain=1&asin={ASIN}&history=1&buybox=1'
        req = requests.get(url)
        with open(f'hdd/{manufacturer}/{product}-{capacity}-{ASIN}.json', 'wb') as f:
            f.write(req.content)


# SSD
# ADATA

# Crucial

# Hikvision

# Kingston

# Kioxia(Toshiba)

# Samsung

# SanDisk

# Seagate

# SK hynix

# Western Digital

# HDD
# Toshiba

# Seagate

# Western Digital


