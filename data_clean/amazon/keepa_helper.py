"""
keepa API definition of response: https://keepa.com/#!discuss/t/product-object/116
keepa API timestamp conversion:
    utc_time = (keepa_time + 21564000) * 60
"""
import json


def read_json(json_file):
    with open(json_file, 'r') as f:
        product = json.load(f)
    return product


response_json = read_json('../../data_gather/amazon/cpu/amd/ryzen threadripper 1900X-B0754JNQBP.json')

print(1)
