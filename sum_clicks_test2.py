import requests

my_token_2 = '0a51e1f49ff29fed3abc1a6ec9960775da5f2d66'
my_token = '01642008264703bec1fc7f3060481e901c225929'
vlink = input('Введите ссылку: ')
url = 'https://api-ssl.bitly.com/v4/shorten'
headers = {'Authorization': my_token_2}
data = {'long_url': vlink}


def shorten_link(url, headers, data):    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200: 
        response.raise_for_status()  
        return (response.json().get('link'))
    else: 
        return (requests.exceptions.HTTPError('error'))
    
bitlink = None    
try:
    bitlink = shorten_link(url, headers, data)       
except requests.exceptions.HTTPError:
    print("Ошибка:", bitlink)
else:
    print('Битлинк:', bitlink)

url_2 = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks'
params = (
    ('unit', 'day'),
    ('units', '1')
    )

def count_clicks(url_2, headers):
    response = requests.get(url_2, headers=headers, params=params)
    print(response.text)
    try:
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        print("Ошибка при запросе данных:", e)

count_clicks(url_2, headers)
 

def is_bitlink(url, headers):
    if 'bit.ly' in url:
        url_3 = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks'
        params = (
            ('unit', 'day'),
            ('units', '1')
        )
        
        response = requests.get(url_3, headers=headers, params=params)
        
        try:
            response.raise_for_status()
            print(response.json())
        except requests.exceptions.HTTPError as e:
            print("Ошибка при запросе данных:", e)
    else:
        data = {'long_url': url}
        bitlink = shorten_link(url, headers, data)
        print('Битлинк:', bitlink)

# Пример использования функции is_bitlink
vlink = input('Введите ссылку: ')
is_bitlink(vlink, headers)