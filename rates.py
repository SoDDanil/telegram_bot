from weakref import proxy
import requests
from bs4 import BeautifulSoup
import lxml
import re

proxies = {
    'https':'http://29ChNA:PPdJJQ@176.53.143.215:8000',
    'https':'http://29ChNA:PPdJJQ@45.10.81.141:8000',
    'https':'http://29ChNA:PPdJJQ@45.10.80.242:8000'
}

cookies = {
    '__ddg1_': 'GklxZioE3l59nXRsO3h7',
    '_ym_uid': '1660205455292780087',
    '_ym_d': '1660205455',
    '_ym_isad': '2',
    'accept': '1',
    '_ym_visorc': 'b',
}

headers = {
    'authority': 'www.cbr.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}


def get_rates(url):
    rates_dict = {
}
    response = requests.get(url, cookies=cookies, headers=headers,timeout=30, proxies=proxies)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('td', class_='')
    data1 = ''
    data2 = ''
    for value in data: 
        code = re.fullmatch('\D{3}', str(value.text))
        if code:
            data1 = value.text
        count = re.fullmatch('[0-1]+' , str(value.text))
        if count:
            data2 = value.text
        exchange = re.fullmatch('\d+,\d+', str(value.text))
        if exchange:
            rates_dict[data1] = dict([(data2,value.text)])
        
    return rates_dict    


def main():
    url = 'https://www.cbr.ru/currency_base/daily/'
    rates_dict = get_rates(url = url)
    
    strings = []
    for key,value in rates_dict.items():
        for key1,value1 in value.items():
            strings.append('{} - {} - {} \n'.format(key, key1, value1 ))
    rates_string = ' '.join(strings)

    return rates_string


