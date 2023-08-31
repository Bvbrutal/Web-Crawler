# -*- coding: UTF-8 -*-


import requests
import pandas as pd


def post1():
    url = 'https://www.xiaopeng.com/api/store/queryAll'
    hearder = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Content-Length': '0',
        'Cookie': 'deviceId=179df.1da548dfe_1689927879773; gdp_user_id=gioenc-b1baed47%2Cbgga%2C560b%2Cab60%2C7bcd14bbg47b; __snaker__id=vdM06ttW5c2rcMf9; YD00458597415740%3AWM_TID=2yJqb6%2F%2BGuNFFUVERVPBgj8%2FxfcCVY5w; acw_tc=775434ab16914632004782101ebae95a8dd904125aa3f85ad8f71f4f87; csrfToken=g3wfbGkWZ-veOfgskBLHQS0K; 84eafaa69d23412f_gdp_session_id=2243ff1e-b82d-49fa-b1de-137e2dbaa5db; 84eafaa69d23412f_gdp_session_id_sent=2243ff1e-b82d-49fa-b1de-137e2dbaa5db; gdxidpyhxdE=BpiMB4xW1%2BJMNvivLpGaMqDDoiB2tGjB%5CJkZ6sLUqLzuJ%5CGg%2FHRb%5C7G6zEeriiUBhsuAYQypBU93pUfwx%2BPM5dRRr%2B5ygtbRvNue%2BckkXWYMDgzkpPArSaRfedUGqw4O6ednLQA2UwQS%2BbQ4q%2B3vXjN%2FZ2uGJxkBysCnb66eti4VAZaQ%3A1691464103058; YD00458597415740%3AWM_NI=Jwa3AtK0kX3ih9F2lUkbY84B4mLbtGB%2Bfs5WAIaZ%2Bov4GS25BYSgi5YURbT5jLWw381PojeW0ymDQQT1ZutRe%2F0ufGxJqoZ9CU60ww27Un%2FJNdbA4EPygEnFzRmpvcFNVnc%3D; YD00458597415740%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee98e821aaa796b1ea3d898a8eb3c44a868f8e87d161b78784a7ea4ea6bb8d94c62af0fea7c3b92a8aa9afd4c48089f0a5b9b263ace78ad3ef5fa9be97d9b74af8b38483f74d82f5aa94b85d8397afbbaa65b6ec89b4b13f82879d88ec3f9b8b9e83d73faa949998b234f390a18be85df4a7a3a5d45b98ef9696f75aa7f10096e54dbc96bf90d933818bfad1f67df2e99b8fae428ebcaea2b74f94a7a9a6ed4eba8ea391f56986929a8fe237e2a3; 84eafaa69d23412f_gdp_sequence_ids={%22globalKey%22:254%2C%22VISIT%22:4%2C%22PAGE%22:19%2C%22CUSTOM%22:113%2C%22VIEW_CLICK%22:106%2C%22VIEW_CHANGE%22:16}',
        'Origin': 'https://www.xiaopeng.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.xiaopeng.com/pengmetta.html',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'X-Csrf-Token': '2BD1yXON-Jv_DsvPjLYFUjYkogZV8H9BX-qU',
    }

    response=requests.post(url,headers=hearder)
    re1=response.json()
    return re1
dic=[]
re1=post1()
for i in re1['data']:
    address=i['address']
    cityName=i['cityName']
    cityCode=i['cityCode']
    lat=i['lat']
    lng=i['lng']
    provinceName=i['provinceName']
    provinceCode=i['provinceCode']
    storeCode=i['storeCode']
    storeName=i['storeName']
    serviceMobile=i['serviceMobile']
    storeTypeName=i['storeTypeName']
    mobile=i['mobile']
    t=[address,cityName,cityCode,lat,lng,provinceName,provinceCode,storeCode,storeName,serviceMobile,storeTypeName,mobile]
    dic.append(t)
    print(t)
cus=['address','cityName','cityCode','lat','lng','provinceName','provinceCode','storeCode','storeName','serviceMobile','storeTypeName','mobile']
result=pd.DataFrame(dic)
result.to_csv('./static/小鹏.csv',index=False,header=cus,encoding='utf-8')