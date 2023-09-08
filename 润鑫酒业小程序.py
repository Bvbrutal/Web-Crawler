# -*- coding: UTF-8 -*-
import time

import requests

def get_code(i):
    url=f"https://mtlj.jojobm.com/index.php/api/index/get_code_ma?id={int(time.time())}"
    header = {
        'Host': 'mtlj.jojobm.com',
        'Cookie': 'PHPSESSID=g6ap007d5aftn508sufdrsfgb0; path=/',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.33(0x18002129) NetType/WIFI Language/zh_CN',
    }
    re=requests.get(url,headers=header)
    print(re.content)
    with open(f'./static/img/code{i}.jpg','wb') as f:
        f.write(re.content)

def post_data(code):
    url = 'https://mtlj.jojobm.com/index.php/api/baoming/baoming'
    header = {
        'Host': 'mtlj.jojobm.com',
        'Cookie':'PHPSESSID=g6ap007d5aftn508sufdrsfgb0; path=/',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.33(0x18002129) NetType/WIFI Language/zh_CN',
    }
    data = {
        'uid': '38273',
        'uname': '彭松焕',
        'idcard': '500382200006244651',
        'model': 'iPhone XR<iPhone11,8>',
        'address': '重庆市渝北区箭竹路',
        'longitude': '106.493824819617',
        'latitude': '29.619923537514886',
        'code': code,

    }
    re = requests.post(url, headers=header,json=data)
    return re.text

if __name__ == '__main__':
    for i in range(1000):
        get_code(i)