#%%
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


DRIVER_PATH = './chromedriver_win32/chromedriver.exe'

GET_URL = 'https://shopee.tw/buyer/login'
ACCOUNT_ELEMENT_NAME = 'loginKey'
PASSWORD_ELEMENT_NAME = 'password'
BUTTON_CLASS_NAME = 'wyhvVD _1EApiB hq6WM5 L-VL8Q cepDQ1 _7w24N1'
                    #wyhvVD _1EApiB hq6WM5 L-VL8Q cepDQ1 _7w24N1

ACCOUNT_NUMBER = '0972820475'
PASSWORD = 'Elvis951753'

#%%
#heads = requests.get(GET_URL)
#print(heads.text)

#%%
headers = {
    'accept' : "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def login():
    opt = webdriver.ChromeOptions()
    opt.add_argument('--accept=%s' % headers['accept'])
    opt.add_argument('--accept-encoding=%s' % headers['accept-encoding'])
    opt.add_argument('--accept-language=%s' % headers['accept-language'])
    opt.add_argument('--user-agent=%s' % headers['User-Agent'])
    
    driver = webdriver.Chrome(DRIVER_PATH,options=opt)
    #driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(GET_URL)

    time.sleep(3)


    account = driver.find_element(By.NAME, ACCOUNT_ELEMENT_NAME)
    password = driver.find_element(By.NAME, PASSWORD_ELEMENT_NAME)

    account.send_keys(ACCOUNT_NUMBER)
    password.send_keys(PASSWORD)

    time.sleep(2)
    
    button_tag = driver.find_elements(By.TAG_NAME,'button')
    button = None
    for it in button_tag:
        if it.get_attribute('class') == BUTTON_CLASS_NAME :
            print('找得到...')
            button = it
            print(it.get_attribute('class'))
    
    #button = driver.find_element(By.CLASS_NAME, BUTTON_CLASS_NAME)
    if button == None:
        raise('沒有找到按鈕')
    button.click()
    time.sleep(10)
    '''html_code = driver.page_source
    with open('./page_source.html', 'w', encoding='utf-8') as w:
        w.write(html_code)'''

    #cookie = ';'.join(['{}={}'.format(item.get('name'), item.get('value')) for item in driver.get_cookies()])


if __name__ == '__main__':
    login()

