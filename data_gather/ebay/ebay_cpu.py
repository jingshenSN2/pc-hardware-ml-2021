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
So we can first open a history sold items page and pass the check once.
Then we input any character to resume this program.
'''
browser.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311&_nkw=amd+ryzen+7+2700x&_sacat=0&LH_TitleDesc=0&_fsrp=1&_odkw=amd+ryzen+5+2700&_osacat=0&LH_Complete=1&LH_Sold=1')
input('Finish captcha, then enter any character to resume:')


def get_cpu(model, num_per_page=100):
    print(f'Start fetching {model}')
    model_url = model.replace(' ', '+')
    i = 1
    flag = True
    while flag:
        browser.get(f'https://www.ebay.com/sch/164/i.html?_nkw={model_url}&rt=nc&LH_Sold=1&LH_Complete=1&_ipg={num_per_page}&_pgn={i}')
        time.sleep(5 + random.random() * 4)
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
        with open(f'cpu/{model}-{i}.html', 'wb') as f:
            f.write(browser.page_source.encode('utf-8'))
        print(f'\tSaved page {i}')
        i = i + 1
    print(f'End fetching {model}')
    time.sleep(10)


# Intel
get_cpu('intel core i7-7700')
get_cpu('intel core i3-8100')
get_cpu('intel core i5-9400')
get_cpu('intel core i7-9700k')
get_cpu('intel core i9-9900k')
get_cpu('intel core i3-10100')
get_cpu('intel core i5-10400', 50)
get_cpu('intel core i7-10700k')
get_cpu('intel core i9-10900k')
get_cpu('intel core i5-11400', 50)
get_cpu('intel core i7-11700k', 50)
get_cpu('intel core i9-11900k')

# AMD
get_cpu('amd ryzen 5 2600')
get_cpu('amd ryzen 7 2700x')
get_cpu('amd ryzen 5 3600')
get_cpu('amd ryzen 7 3700x')
get_cpu('amd ryzen 9 3900x')
get_cpu('amd ryzen 9 3950x')
get_cpu('amd ryzen 5 5600x')
get_cpu('amd ryzen 7 5800x')
get_cpu('amd ryzen 9 5900x')
get_cpu('amd ryzen 9 5950x')

