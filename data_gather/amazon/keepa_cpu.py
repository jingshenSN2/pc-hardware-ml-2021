import requests
# subscribe on https://keepa.com/#!api to get access key
access_key = 'cju3topabp5hdq28hn3jhod62fb7noiitniam32kd71f76v9nta6t4or5qms00gv'


def get_cpu(manufacturer, product, ASIN_list):
    """
    :param manufacturer: 'intel' or 'amd',  manufacturer of cpu, as part of save path
    :param product: cpu product name
    :param ASIN_list: single ASIN or list of ASINs
    :return:
    """
    if isinstance(ASIN_list, str):
        ASIN_list = [ASIN_list]
    for ASIN in ASIN_list:
        print(f'Requesting information of manufacturer: {manufacturer}, product: {product}, ASIN: {ASIN}')
        url = f'https://api.keepa.com/product?key={access_key}&domain=1&asin={ASIN}&history=1&buybox=1'
        req = requests.get(url)
        with open(f'cpu/{manufacturer}/{product}-{ASIN}.json', 'wb') as f:
            f.write(req.content)


# X-series
# get_cpu('intel', 'core i9-10940X', 'B07YP67PFV')
# get_cpu('intel', 'core i9-10920X', 'B07YP6Y9VY')
# get_cpu('intel', 'core i9-10900X', 'B07YP69HTM')
# get_cpu('intel', 'core i9-9980XE', 'B07JGCMQY8')
# get_cpu('intel', 'core i9-9940X', 'B07JFH771Y')
# get_cpu('intel', 'core i9-9920X', 'B07JGCV5KN')
# get_cpu('intel', 'core i9-9900X', 'B07JDV1MMR')
# get_cpu('intel', 'core i9-9820X', 'B07KCCH7JL')

# i9
# get_cpu('intel', 'core i9-11900K', 'B08X6PPTTH')
# get_cpu('intel', 'core i9-11900', 'B08X5XVLL9')
# get_cpu('intel', 'core i9-10900K', ['B086MHSTVD', 'B08H2DRCWZ'])
# get_cpu('intel', 'core i9-10900KF', 'B086MG1C7D')
# get_cpu('intel', 'core i9-10900', 'B086ML4XSD')
# get_cpu('intel', 'core i9-10900F', 'B086MHTK5C')
# get_cpu('intel', 'core i9-10850K', 'B08DHRG2X9')
# get_cpu('intel', 'core i9-9900KS', 'B07YP3J7ZM')
# get_cpu('intel', 'core i9-9900K', ['B089J731BX', 'B005404P9I'])
# get_cpu('intel', 'core i9-9900KF', 'B07MGBZWDZ')
# get_cpu('intel', 'core i9-9900', 'B07RXX3Y2T')

# i7
# get_cpu('intel', 'core i7-11700K', 'B08X6ND3WP')
# get_cpu('intel', 'core i7-11700KF', 'B08X6NXNX7')
# get_cpu('intel', 'core i7-11700', 'B08X6QHYDL')
# get_cpu('intel', 'core i7-11700F', 'B08X6V4WTF')
# get_cpu('intel', 'core i7-10700K', 'B086ML4XSB')
# get_cpu('intel', 'core i7-10700KF', 'B086MMS6FV')
# get_cpu('intel', 'core i7-10700', 'B086MG1C7C')
# get_cpu('intel', 'core i7-10700F', 'B086MN2XYL')
# get_cpu('intel', 'core i7-9700K', 'B07HHN6KBZ')
# get_cpu('intel', 'core i7-9700KF', 'B07MJXYX62')
# get_cpu('intel', 'core i7-9700', 'B07S6CRLVD')
# get_cpu('intel', 'core i7-9700F', 'B07S8DWXT3')
# get_cpu('intel', 'core i7-8086K', 'B07DGDWJ3P')
# get_cpu('intel', 'core i7-8700K', 'B07598VZR8')
# get_cpu('intel', 'core i7-8700', 'B07598HLB4')
# get_cpu('intel', 'core i7-7700K', 'B01MXSI216')
# get_cpu('intel', 'core i7-7700', 'B01N0L41N7')

# i5
# get_cpu('intel', 'core i5-11600K', 'B08X67YZBL')
# get_cpu('intel', 'core i5-11600KF', 'B08X62BTJD')
# get_cpu('intel', 'core i5-11600', 'B08X5XWNTB')
# get_cpu('intel', 'core i5-11500', 'B08X6BCPGD')
# get_cpu('intel', 'core i5-11400', 'B08X6JPK4K')
# get_cpu('intel', 'core i5-11400F', 'B08X6SZ184')
# get_cpu('intel', 'core i5-10600K', 'B086MHSH2C')
# get_cpu('intel', 'core i5-10600KF', 'B086M8441R')
# get_cpu('intel', 'core i5-10600', 'B086MG2B41')
# get_cpu('intel', 'core i5-10500', 'B086MW76DW')
# get_cpu('intel', 'core i5-10400', 'B086MN38Q2')
# get_cpu('intel', 'core i5-10400F', 'B086MHSTWN')
# get_cpu('intel', 'core i5-9600KF', 'B07MQP5LNM')
# get_cpu('intel', 'core i5-9600', 'B07S1Q396F')
# get_cpu('intel', 'core i5-9500', 'B07S4MSXJL')
# get_cpu('intel', 'core i5-9400', 'B07MGZ9FJZ')
# get_cpu('intel', 'core i5-9400F', 'B07MRCGQQ4')
# get_cpu('intel', 'core i5-8500', 'B07938SNBB')
# get_cpu('intel', 'core i5-8400', 'B0759FGJ3Q')

# i3
# get_cpu('intel', 'core i3-10300', 'B086M8V695')
# get_cpu('intel', 'core i3-10100', 'B086MMRW87')
# get_cpu('intel', 'core i3-10100F', 'B08LKJPR5X')
# get_cpu('intel', 'core i3-9100', 'B07RXW4Y2K')
# get_cpu('intel', 'core i3-9100F', 'B07R7Q3JZH')
# get_cpu('intel', 'core i3-8350K', 'B0759FWJDK')
# get_cpu('intel', 'core i3-8300', 'B0793DCQLG')
# get_cpu('intel', 'core i3-8100', 'B0759FTRZL')

# threadripper
# get_cpu('amd', 'ryzen threadripper 3990X', 'B0815SBQ9W')
# get_cpu('amd', 'ryzen threadripper 3970X', 'B0815JJQQ8')
# get_cpu('amd', 'ryzen threadripper 3960X', 'B0815JGCXP')
# get_cpu('amd', 'ryzen threadripper 2990WX', 'B07G25SD1P')
# get_cpu('amd', 'ryzen threadripper 2970WX', 'B07JBQJ1D9')
# get_cpu('amd', 'ryzen threadripper 2950X', 'B07GFN6CVF')
# get_cpu('amd', 'ryzen threadripper 2920X', 'B07JDF4QP2')
# get_cpu('amd', 'ryzen threadripper 1950X', 'B074CBH3R4')
# get_cpu('amd', 'ryzen threadripper 1920X', 'B074CBJHCT')
# get_cpu('amd', 'ryzen threadripper 1900X', 'B0754JNQBP')

# zen 3
# get_cpu('amd', 'ryzen 9 5950X', 'B0815Y8J9N')
# get_cpu('amd', 'ryzen 9 5900X', 'B08164VTWH')
# get_cpu('amd', 'ryzen 7 5800X', 'B0815XFSGK')
# get_cpu('amd', 'ryzen 5 5600X', 'B08166SLDF')
# get_cpu('amd', 'ryzen 7 5700G', 'B091J3NYVF')
# get_cpu('amd', 'ryzen 5 5600G', 'B092L9GF5N')

# zen 2
# get_cpu('amd', 'ryzen 9 3950X', 'B07ZTYKLZW')
# get_cpu('amd', 'ryzen 9 3900XT', 'B089WD454D')
# get_cpu('amd', 'ryzen 9 3900X', 'B07SXMZLP9')
# get_cpu('amd', 'ryzen 7 3800XT', 'B089WCXZJC')
# get_cpu('amd', 'ryzen 7 3800X', 'B07SXMZLPJ')
# get_cpu('amd', 'ryzen 7 3700X', 'B07SXMZLPK')
# get_cpu('amd', 'ryzen 5 3600XT', 'B089WC4VWF')
# get_cpu('amd', 'ryzen 5 3600X', 'B07SQBFN2D')
# get_cpu('amd', 'ryzen 5 3600', 'B07STGGQ18')
# get_cpu('amd', 'ryzen 3 3300X', 'B0876YS2T4')
# get_cpu('amd', 'ryzen 3 3100', 'B0876Y2TMZ')

# zen +
# get_cpu('amd', 'ryzen 7 2700X', 'B07B428M7F')
# get_cpu('amd', 'ryzen 7 2700', 'B07B41717Z')
# get_cpu('amd', 'ryzen 5 2600X', 'B07B428V2L')
# get_cpu('amd', 'ryzen 5 2600', 'B07B41WS48')
# get_cpu('amd', 'ryzen 5 3400G', 'B07SXNDKNM')
# get_cpu('amd', 'ryzen 3 3200G', 'B07STGHZK8')
