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




#if __name__ == '__main__':
 #   main()'''
