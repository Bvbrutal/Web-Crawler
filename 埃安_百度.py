# -*- coding: UTF-8 -*-
import pandas as pd
import requests


def post1():
    url = 'https://www.aion.com.cn/Home/api/area'

    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Content-Length': '0',
        'Cookie': 'PHPSESSID=tccjflhn3gtdj7a2irlmdd08g9',
        'Origin': 'https://www.aion.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://www.aion.com.cn/show/25hours',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'X-Requested-With': 'XMLHttpRequest',
    }

    response = requests.post(url, headers=header)
    re1 = response.json()
    return re1


def post2(cid):
    url = 'https://www.aion.com.cn/Home/api/area'

    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Content-Length': '10',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'PHPSESSID=tccjflhn3gtdj7a2irlmdd08g9',
        'Origin': 'https://www.aion.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://www.aion.com.cn/show/25hours',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {'cid': cid}
    response = requests.post(url, headers=header, data=data)
    re2 = response.json()
    return re2


def post3(province, city):
    url = 'https://www.aion.com.cn/Home/api/search'
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Content-Length': '27',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'PHPSESSID=tccjflhn3gtdj7a2irlmdd08g9',
        'Origin': 'https://www.aion.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://www.aion.com.cn/show/25hours',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'province': province,
        'city': city
    }
    response = requests.post(url, headers=header, data=data)
    re3 = response.json()
    return re3


re1 = post1()
print(re1)
dic = []
for i in re1['data']:
    cid_province = i['cid']
    name_province = i['name']
    re2 = post2(cid_province)
    for j in re2['data']:
        cid_city = j['cid']
        name_city = j['name']
        re3 = post3(cid_province, cid_city)
        for m in re3['data']:
            address = m['address']
            code = m['code']
            fullname = m['fullname']
            phone_seal = m['phone_seal']
            phone_service = m['phone_service']
            lat = m['lat']
            lng = m['lng']
            region = m['region']
            t = [fullname, address, code, name_province, cid_province, name_city, cid_city, phone_seal, phone_service,
                 lat, lng, region]
            dic.append(t)
            print(t)

cus = ['fullname', 'address', 'code', 'name_province', 'cid_province', 'name_city', 'cid_city', 'phone_seal',
       'phone_service', 'lat', 'lng', 'region']
result = pd.DataFrame(dic)
result.to_csv('./static/埃安.csv', index=False, header=cus)

