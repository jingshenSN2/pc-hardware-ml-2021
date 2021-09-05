import time
import random
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--lang=zh-CN')
browser = webdriver.Chrome(options=chrome_options)

'''
Important!
When we requests history sold items from ebay, there will be a hCaptcha check.
So we can first pass the check once, and then input any character to resume this program.
'''
browser.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=gtx&_sacat=175673&LH_TitleDesc=0&_odkw=gtx&_osacat=175673&Chipset%252FGPU%2520Model=NVIDIA%2520GeForce%2520GTX%2520970&LH_Complete=1&_ipg=200&LH_Sold=1')
input('Finish captcha, then enter any character to resume:')


def get_gpu(keyword, model):
    print(f'Start fetching {model}')
    model_url = model.replace(' ', '%2520')
    i = 1
    flag = True
    while flag:
        browser.get(f'https://www.ebay.com/sch/i.html?_nkw={keyword}&Chipset%252FGPU%2520Model={model_url}&rt=nc&LH_Sold=1&LH_Complete=1&_ipg=200&_pgn={i}')
        time.sleep(5 + random.random() * 5)
        try:
            # check the Next page button exists or pause the program
            element = browser.find_element_by_xpath("//a[@aria-label='Next page']")
            # the Next page button at the last page has an attribute aria-disabled='true'
            is_last_page = element.get_attribute('aria-disabled')
            if is_last_page == 'true':
                flag = False
        except Exception:
            # BUG HERE: if the total number of sold items are lower than _ipg, the program will keep showing this line
            input('Something went wrong! Finish captcha, then enter any character to resume:')
        # save html
        with open(f'gpu/{model}-{i}.html', 'wb') as f:
            f.write(browser.page_source.encode('utf-8'))
        print(f'\tSaved page {i}')
        i = i + 1
    print(f'End fetching {model}')
    time.sleep(10)


# NVIDIA
get_gpu('gtx+970', 'NVIDIA GeForce GTX 970')
get_gpu('gtx+980', 'NVIDIA GeForce GTX 980')
get_gpu('gtx+1060', 'NVIDIA GeForce GTX 1060')
get_gpu('gtx+1660', 'NVIDIA GeForce GTX 1660')
get_gpu('rtx+2060', 'NVIDIA GeForce RTX 2060')
get_gpu('rtx+2070', 'NVIDIA GeForce RTX 2070')
get_gpu('rtx+2080+ti', 'NVIDIA GeForce RTX 2080 Ti')
get_gpu('rtx+3060', 'NVIDIA GeForce RTX 3060')
get_gpu('rtx+3060+ti', 'NVIDIA GeForce RTX 3060 Ti')
get_gpu('rtx+3070', 'NVIDIA GeForce RTX 3070')
get_gpu('rtx+3080', 'NVIDIA GeForce RTX 3080')
get_gpu('rtx+3090', 'NVIDIA GeForce RTX 3090')


# AMD
get_gpu('rx+570', 'AMD Radeon RX 570')
get_gpu('rx+580', 'AMD Radeon RX 580')
get_gpu('rx+5700+xt', 'AMD Radeon RX 5700 XT')
get_gpu('rx+6800', 'AMD Radeon RX 6800 XT')
get_gpu('rx+6800+xt', 'AMD Radeon RX 6800 XT')
get_gpu('rx+6900+xt', 'AMD Radeon RX 6900 XT')
