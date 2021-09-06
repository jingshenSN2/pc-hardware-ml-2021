import requests
# subscribe on https://keepa.com/#!api to get access key
access_key = 'cju3topabp5hdq28hn3jhod62fb7noiitniam32kd71f76v9nta6t4or5qms00gv'


def get_drive(manufacturer, drive_type, sub_type, product, ASIN_dict):
    """
    :param manufacturer: manufacturer of ssd, as part of save path
    :param product: ssd product name
    :param drive_type: type of drive, 'hdd' or 'ssd'
    :param sub_type: subtype of drive, 'nvme', 'm2' or 'sata' for ssd, '25' or '35' for hdd
    :param ASIN_dict: dict of ASIN, key is capacity and value is ASIN
    :return:
    """
    for capacity, ASIN in ASIN_dict.items():
        print(f'Requesting ssd information of manufacturer: {manufacturer}, type: {drive_type}, sub_type: {sub_type}, product: {product}, capacity: {capacity}, ASIN: {ASIN}')
        url = f'https://api.keepa.com/product?key={access_key}&domain=1&asin={ASIN}&history=1&buybox=1'
        req = requests.get(url)
        with open(f'{drive_type}/{manufacturer}/{sub_type}-{product}-{capacity}-{ASIN}.json', 'wb') as f:
            f.write(req.content)


def get_ssd(manufacturer, ssd_type, product, ASIN_dict):
    """
    :param manufacturer: manufacturer of ssd, as part of save path
    :param product: ssd product name
    :param ssd_type: type of ssd, 'nvme', 'm2' or 'sata'; as part of filename; 'm2' refers to m.2 SATA, 'nvme' refers to m.2 nvme
    :param ASIN_dict: dict of ASIN, key is capacity and value is ASIN, capacity should be multiple of 128gb
    :return:
    """
    get_drive(manufacturer, 'ssd', ssd_type, product, ASIN_dict)


def get_hdd(manufacturer, hdd_size, product, ASIN_dict):
    """
    :param manufacturer: manufacturer of hdd, as part of save path
    :param hdd_size: disk size, '25' or '35'
    :param product: hdd product name
    :param ASIN_dict: dict of ASIN, key is capacity and value is ASIN, capacity should be multiple of 500gb
    :return:
    """
    get_drive(manufacturer, 'hdd', hdd_size, product, ASIN_dict)


# SSD dict_template: {'128gb': '', '256gb': '', '512gb': '', '1tb': '', '2tb': ''}
# ADATA
# get_ssd('ADATA', 'sata', 'su800', {'128gb': 'B01K8A29BE', '256gb': 'B01K8A2A0E', '512gb': 'B01K8A2A0E', '1tb': 'B01K8A29E6', '2tb': 'B07GBRG2G8'})
# get_ssd('ADATA', 'sata', 'su760', {'256gb': 'B07TDW8Z3M', '512gb': 'B07TBQ637W', '1tb': 'B07TBQ637W'})
# get_ssd('ADATA', 'sata', 'su740', {'512gb': 'B08BFF1NZZ', '1tb': 'B08BF7R11F', '2tb': 'B08BF7R11F'})
# get_ssd('ADATA', 'sata', 'su720', {'1tb': 'B088JT3M1R', '2tb': 'B08F9QGRQQ'})
# get_ssd('ADATA', 'sata', 'su635', {'256gb': 'B07PLNNDL2', '512gb': 'B07PGC3JKQ', '1tb': 'B07PQNHZ7Y', '2tb': 'B07Y3YP7WF'})
# get_ssd('ADATA', 'm2', 'su800', {'256gb': 'B01M3Z46FQ', '512gb': 'B01M3Z3UC2', '1tb': 'B01MR7FVM9'})
# get_ssd('ADATA', 'm2', 'su650', {'128gb': 'B07V1KHPKK', '256gb': 'B07TYGQJ45', '512gb': 'B085LTNV9M'})
# get_ssd('ADATA', 'nvme', 'sx8200 pro', {'256gb': 'B07K1MDMF3', '512gb': 'B07K1HMMJC', '1tb': 'B07K1J3C23', '2tb': 'B07TY2TN64'})
# get_ssd('ADATA', 'nvme', 'sx6000 pro', {'256gb': 'B07H53JT77', '512gb': 'B07H5355JF', '1tb': 'B07H52ML35'})
# get_ssd('ADATA', 'nvme', 'sx6000 lite', {'128gb': 'B07MTVVXG7', '512gb': 'B07N23BSZM'})

# Crucial
# get_ssd('Crucial', 'sata', 'mx500', {'256gb': 'B0781VSXBP', '512gb': 'B0786QNS9B', '1tb': 'B078211KBB', '2tb': 'B003J5JB12'})
# get_ssd('Crucial', 'sata', 'bx500', {'256gb': 'B07G3YNLJB', '512gb': 'B07G3KGYZQ', '1tb': 'B07YD579WM', '2tb': 'B07YD5F561'})
# get_ssd('Crucial', 'nvme', 'p5 plus', {'512gb': 'B098W1NDV2', '1tb': 'B098WL46RS', '2tb': 'B098WKQRDL'})
# get_ssd('Crucial', 'nvme', 'p5', {'256gb': 'B0892TH611', '512gb': 'B087QTMXS7', '1tb': 'B087QRVVVH', '2tb': 'B0892TWDP1'})
# get_ssd('Crucial', 'nvme', 'p2', {'256gb': 'B086BKGSC1', '512gb': 'B086BGWNY8', '1tb': 'B089DNM8LR', '2tb': 'B08GVDNTGJ'})

# Kingston
# get_ssd('Kingston', 'sata', 'kc600', {'256gb': 'B07ZDBZDR9', '512gb': 'B07ZDBT15M', '1tb': 'B07ZGWM58Q', '2tb': 'B08485J48C'})
# get_ssd('Kingston', 'sata', 'q500', {'128gb': 'B07KCJFBTR', '256gb': 'B07KCGPRMQ', '512gb': 'B07KCP5NT9', '1tb': 'B07QFNN3KS', '2tb': 'B08HRB31QC'})
# get_ssd('Kingston', 'sata', 'a400', {'128gb': 'B01N6JQS8C', '256gb': 'B01N5IB20Q', '512gb': 'B01N0TQPQB', '1tb': 'B079XC5PVV', '2tb': 'B07YQJSGWY'})
# get_ssd('Kingston', 'm2', 'a400', {'128gb': 'B07P22T3VD', '256gb': 'B07P22RK1G', '512gb': 'B083WNX8H6'})
# get_ssd('Kingston', 'nvme', 'nv1', {'512gb': 'B091BCQK7B', '1tb': 'B091BDQ2B6', '2tb': 'B091BG4HDW'})
# get_ssd('Kingston', 'nvme', 'kc2500', {'256gb': 'B087QZ4PXW', '512gb': 'B087QXDTMN', '1tb': 'B087QYC363', '2tb': 'B089TMNMDT'})
# get_ssd('Kingston', 'nvme', 'a2000', {'256gb': 'B07VYG5HQD', '512gb': 'B07VXCFNVS', '1tb': 'B07VXC9QMH'})

# Samsung
# get_ssd('Samsung', 'sata', '870 qvo', {'1tb': 'B089C73T72', '2tb': 'B089C6LZ42', '4tb': 'B089C5P5SX', '8tb': 'B089C3TZL9'})
# get_ssd('Samsung', 'sata', '870 evo', {'256gb': 'B08QBN5J9B', '512gb': 'B08QBMD6P4', '1tb': 'B08QBJ2YMG', '2tb': 'B08QB93S6R', '4tb': 'B08QBL36GF'})
# get_ssd('Samsung', 'sata', '860 pro', {'256gb': 'B07864XMTK', '512gb': 'B07836C6YV', '1tb': 'B078211KCN', '2tb': 'B07879KC15', '4tb': 'B0786ZQ1PJ'})
# get_ssd('Samsung', 'sata', '860 qvo', {'1tb': 'B07L3D19MY'})
# get_ssd('Samsung', 'sata', '860 evo', {'256gb': 'B07864WMK8', '512gb': 'B0781Z7Y3S', '1tb': 'B078DPCY3T', '2tb': 'B0786QNSBD', '4tb': 'B07864XY8B'})
# get_ssd('Samsung', 'm2', '860 evo', {'256gb': 'B07864V6CK', '512gb': 'B078218TWQ', '1tb': 'B07822Z77M', '2tb': 'B07822SVMS'})
# get_ssd('Samsung', 'nvme', '980 pro', {'256gb': 'B08GL52C3V', '512gb': 'B08GL575DB', '1tb': 'B08GLX7TNT', '2tb': 'B08RK2SR23'})
# get_ssd('Samsung', 'nvme', '980', {'256gb': 'B08V7P3SKS', '512gb': 'B08V7GT6F3', '1tb': 'B08V83JZH4'})
# get_ssd('Samsung', 'nvme', '970 pro', {'512gb': 'B07C8Y31G2', '1tb': 'B07BYHGNB5'})
# get_ssd('Samsung', 'nvme', '970 evo plus', {'256gb': 'B07MG119KG', '512gb': 'B07M7Q21N7', '1tb': 'B07MFZY2F2', '2tb': 'B07MFZXR1B'})
# get_ssd('Samsung', 'nvme', '970 evo', {'512gb': 'B07BN4NJ2J', '1tb': 'B07BN217QG', '2tb': 'B07C8Y31G1'})

# SanDisk
# get_ssd('SanDisk', 'sata', 'ssd plus', {'256gb': 'B01F9G43WU', '512gb': 'B01F9G46Q8', '1tb': 'B07D998212', '2tb': 'B07YFFJK2Q'})
# get_ssd('SanDisk', 'sata', 'ultra 3d nand', {'256gb': 'B071KGRXRH', '512gb': 'B072R78B6Q', '1tb': 'B071KGRXRG', '2tb': 'B071KGS72Q', '4tb': 'B07W1SYTTT'})


# Seagate
# get_ssd('Seagate', 'sata', 'firecuda 120', {'512gb': 'B088D6VBG6', '1tb': 'B088D6WBVR', '2tb': 'B088CTFBW8', '4tb': 'B088GCWTRX'})
# get_ssd('Seagate', 'sata', 'barracuda 120', {'256gb': 'B07ZPRD5VM', '512gb': 'B07ZPRK6KD', '1tb': 'B07ZPRJFV1', '2tb': 'B07ZPRS2Z7'})
# get_ssd('Seagate', 'sata', 'barracuda q1', {'512gb': 'B087NYT1M1', '1tb': 'B087NYH678'})
# get_ssd('Seagate', 'nvme', 'firecuda 530', {'512gb': 'B08Q4X1HRJ', '1tb': 'B08Q54CHS6'})
# get_ssd('Seagate', 'nvme', 'firecuda 520', {'512gb': 'B07ZPRQ4YM', '1tb': 'B07ZPRMLJP', '2tb': 'B07ZPRPFQY'})
# get_ssd('Seagate', 'nvme', 'firecuda 510', {'512gb': 'B07ZPRRSPX', '1tb': 'B07QRC1Z94', '2tb': 'B07QQ95CBZ'})
# get_ssd('Seagate', 'nvme', 'barracuda 510', {'256gb': 'B07ZPRRRBH', '512gb': 'B07ZPRV8JY', '1tb': 'B07ZPRK68X'})
# get_ssd('Seagate', 'nvme', 'barracuda q5', {'512gb': 'B08LB86XJW', '1tb': 'B08LB5LQ65', '2tb': 'B08LB9TMYK'})

# SK hynix
# get_ssd('SK hynix', 'sata', 'gold s31', {'256gb': 'B07SL9WBCR', '512gb': 'B07SK5BNM1', '1tb': 'B07SNHB4RC'})
# get_ssd('SK hynix', 'nvme', 'gold p31', {'512gb': 'B08DK2FB7G', '1tb': 'B08DKB5LWY', '2tb': 'B099RHVB42'})

# Western Digital
# get_ssd('WD', 'sata', 'wd gold', {'1tb': 'B085WBMNV4', '2tb': 'B085WBDPL9', '4tb': 'B085WBV64J', '8tb': 'B085WBH1BZ'})
# get_ssd('WD', 'sata', 'wd red', {'512gb': 'B07YFGQLYK', '1tb': 'B07YFG3R5N', '2tb': 'B07YFGG261', '4tb': 'B07YFGTXHT'})
# get_ssd('WD', 'sata', 'wd blue', {'256gb': 'B073SB2MXW', '512gb': 'B073SBZ8YH', '1tb': 'B073SBQMCX', '2tb': 'B073SBRHH6', '4tb': 'B07QV3XGCP'})
# get_ssd('WD', 'sata', 'wd green', {'128gb': 'B076XWDN6V', '256gb': 'B076Y374ZH', '512gb': 'B01M3POPK3', '1tb': 'B07NNRTTCM', '2tb': 'B086NKQ389'})
# get_ssd('WD', 'm2', 'wd red', {'512gb': 'B07YFG1N7Q', '1tb': 'B07YFGXPQ2', '2tb': 'B07YFG451Q'})
# get_ssd('WD', 'm2', 'wd blue', {'256gb': 'B073SBV3XX', '512gb': 'B073SBX6TY', '1tb': 'B073SB2MXT', '2tb': 'B073SBW3VD'})
# get_ssd('WD', 'nvme', 'an1500', {'1tb': 'B08HBZCSHW', '2tb': 'B08HBXDX8R', '4tb': 'B08HBPMPZ2'})
# get_ssd('WD', 'nvme', 'sn850', {'512gb': 'B08KFN1KT1', '1tb': 'B08KFS6THF', '2tb': 'B08KFRFL8F'})
# get_ssd('WD', 'nvme', 'sn750', {'256gb': 'B07M64R4CR', '512gb': 'B07MH2P5ZD', '1tb': 'B07M64QXMN', '2tb': 'B07M9VXSXG', '4tb': 'B08QZ879V5'})
# get_ssd('WD', 'nvme', 'sn550', {'256gb': 'B07YFF8879', '512gb': 'B07YFF3JCN', '1tb': 'B07YFFX5MD', '2tb': 'B08K4NP5DQ'})

# HDD
# Seagate
# get_hdd('Seagate', '35', 'barracuda', {'1tb': 'B07D99KFPK', '2tb': 'B07H2RR55Q', '3tb': 'B07D9C7SQH', '4tb': 'B07D9C7SQH', '6tb': 'B07H28SY39', '8tb': 'B07H289S7C'})
# get_hdd('Seagate', '25', 'barracuda', {'500gb': 'B07H1VZ4CT', '1tb': 'B07H28QRKN', '2tb': 'B07D99S8Z7'})
# get_hdd('Seagate', '35', 'firecuda', {'1tb': 'B01N6MHWZH', '2tb': 'B01IEKG2HM'})
# get_hdd('Seagate', '25', 'firecuda', {'500gb': 'B07H28QRKS', '1tb': 'B01LWRTRZU', '2tb': 'B01M1NHCZT'})
# get_hdd('Seagate', '35', 'ironwolf', {'1tb': 'B07H28PKLX', '2tb': 'B07H2GY8ZV', '3tb': 'B07H289S7B', '4tb': 'B07H289S79', '6tb': 'B085Z4P89R', '8tb': 'B084ZV4DXB', '10tb': 'B085ZB51HW', '12tb': 'B084ZTSMWF', '14tb': 'B07H4VBRKW', '16tb': 'B07SGGWYC1'})
# get_hdd('Seagate', '35', 'ironwolf pro', {'2tb': 'B07H23VGPH', '4tb': 'B084ZV8YW8', '8tb': 'B084ZV1DN8', '10tb': 'B085Z423DR', '12tb': 'B084ZV1DN6', '14tb': 'B07H57WY2Z', '16tb': 'B07SLPTK17', '18tb': 'B08FY88FNG'})
# get_hdd('Seagate', '35', 'skyhawk', {'1tb': 'B07H2FPFW9', '2tb': 'B07H2F3744', '4tb': 'B07H231394', '6tb': 'B07H28M89D', '8tb': 'B07N33PYN4'})
# get_hdd('Seagate', '35', 'skyhawk ai', {'8tb': 'B0776XWX8N', '10tb': 'B085RH2FR7', '12tb': 'B07VFRGDSW', '16tb': 'B07XBTS8S1'})

# Toshiba
# get_hdd('Toshiba', '35', 'x300', {'4tb': 'B013JPKUU2', '5tb': 'B013JPLKQK', '6tb': 'B013JPLKJC', '8tb': 'B074BTZ2YJ'})
# get_hdd('Toshiba', '35', 'p300', {'500gb': 'B013JPKUHA', '2tb': 'B013JPKT9O', '3tb': 'B013JPLOQQ'})
# get_hdd('Toshiba', '25', 'l200', {'500gb': 'B013JPKYNK', '1tb': 'B013JPLM68', '2tb': 'B07CT5RDDX'})
# get_hdd('Toshiba', '35', 'n300', {'4tb': 'B06Y2VCQ31', '6tb': 'B06Y2KCXCM', '8tb': 'B06Y2TSZBV'})
# get_hdd('Toshiba', '35', 's300', {'4tb': 'B07NTC8G12', '5tb': 'B07NTC92RL', '8tb': 'B07NTDWDGL'})

# Western Digital
# get_hdd('WD', '35', 'wd blue', {'2tb': 'B07JC1TQ7N', '3tb': 'B08XDG9ND6', '4tb': 'B087QTVCHH', '6tb': 'B07MYKZGVX'})
# get_hdd('WD', '25', 'wd blue', {'500gb': 'B013QFRZL2', '1tb': 'B071F9MLJJ', '2tb': 'B079BQS5WQ'})
# get_hdd('WD', '35', 'wd red', {'2tb': 'B07PGWXQCM', '3tb': 'B083XVD1FP', '4tb': 'B083XVY99B', '6tb': 'B07MYL7KVK'})
# get_hdd('WD', '35', 'wd red plus', {'2tb': 'B008JJLZ7G', '3tb': 'B008JJLW4M', '4tb': 'B00EHBERSE', '6tb': 'B00LO3KR96', '8tb': 'B07D3MWMNZ', '10tb': 'B083JXTH5L', '12tb': 'B07RQ99XJH', '14tb': 'B07YFGMZVV'})
# get_hdd('WD', '35', 'wd red pro', {'2tb': 'B01FYXPGT2', '4tb': 'B01FYXPGT2', '6tb': 'B07B1HX5KN', '8tb': 'B07D3N95GS', '10tb': 'B084F34HZ6', '12tb': 'B07RTMPWD8', '14tb': 'B07YFGW736', '16tb': 'B08K3VVKSW', '18tb': 'B08K3TFM92'})
# get_hdd('WD', '35', 'wd purple', {'1tb': 'B072L175ZW', '2tb': 'B071RM2HS7', '3tb': 'B0718XQQJ9', '4tb': 'B071KVB4F8', '6tb': 'B071V6SVK2', '8tb': 'B07RRCQVN1', '10tb': 'B082LNS4JZ', '12tb': 'B07DYNG3N8', '14tb': 'B082LTQG89', '18tb': 'B08P2JRD9L'})
# get_hdd('WD', '35', 'wd black', {'500gb': 'B008968L6M', '1tb': 'B00FJRS6FU', '2tb': 'B00FJRS628', '4tb': 'B0792G331G', '6tb': 'B0792GSD6N', '8tb': '', '10tb': 'B08MKJPFZ7'})
# get_hdd('WD', '35', 'wd gold', {'1tb': 'B01IY9USY6', '2tb': 'B01IY9UTMM', '4tb': 'B07XDD6GD3', '6tb': 'B07XHCT33G', '8tb': 'B07XGDNZXT', '10tb': 'B07XDD5MV8', '12tb': 'B075L6FJH8', '14tb': 'B07XC95Y28', '16tb': 'B089S33PR3', '18tb': 'B089S3CZ41'})
