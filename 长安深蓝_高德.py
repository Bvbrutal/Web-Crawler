# -*- coding: UTF-8 -*-

import requests

header1 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'app-api.deepal.com.cn',
    'Origin': 'https://deepal.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://deepal.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    'appType': 'android',
    'fingerprint': '78756a92605c15ccb33a5542fe78140c',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
url = 'https://app-api.deepal.com.cn/appapi/v1/support/setting/area'
response = requests.get(url, headers=header1)
result = response.json()


def post(code):
    url = 'https://app-api.deepal.com.cn/iam/appapi/v1/shop/shopAndShowroomsPageListNotRecommended'
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '51',
        'Content-Type': 'application/json',
        'Host': 'app-api.deepal.com.cn',
        'Origin': 'https://deepal.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://deepal.com.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'appType': 'android',
        'fingerprint': '78756a92605c15ccb33a5542fe78140c',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = {"cityCode": code, "channel": "", "page": 1, "size": 9999}
    response = requests.post(url, headers=header, json=data)
    result = response.json()
    return result


import csv

for i in result["data"]:
    code = i['code']
    city = i["fullName"]
    print(code, city)
    result1 = post(code)
    data = result1["data"]["shop"]
    dic = []
    try:
        for i in data:
            name = i["name"]
            addr = i["addr"]
            lng = i["lng"]
            lat = i["lat"]
            belongCityName = i['belongCityName']
            hotline = i['hotline']
            premierContactor = i['premierContactor']
            premierContactorPhone = i['premierContactorPhone']
            type = i['type']
            dic.append(
                [name, addr, lng, lat, belongCityName, city, hotline, premierContactor, premierContactorPhone, type])
        with open('./static/长安深蓝.csv', 'a', newline='\n', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            for data_row in dic:
                csv_writer.writerow(data_row)
    except:
        continue
