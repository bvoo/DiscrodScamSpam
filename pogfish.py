import requests
from random_word import RandomWords

r = RandomWords()
url = "https://discrod.gift/login/dologin"


headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-CA,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'lumen_session=Md1j2hnPZ6iDX14BRqD4rcUnhOrvNnXaQeuTjc2Y; _TDG=43253e8e66783ce05945b68bfb43b45b; timezoneOffset=-25200,0',
    'Host': 'discrod.gift',
    'Origin': 'https://discrod.gift',
    'Pragma': 'no-cache',
    'Referer': 'https://discrod.gift/vVdsq0xZ8SVbd4a5a8d2TCS9XFgq8DoiVqaw1cv4bjHIEPz2EAKHHsEnA',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

while True:
    username = r.get_random_word()
    password = r.get_random_word()
    
    data = {
        'username': username,
        'password': password
    }

    response = requests.post(url, data=data, headers=headers).text

    print(username, password)
    print(response)