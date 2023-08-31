# -*- coding: UTF-8 -*-
import pandas as pd
import requests

def post():
    url = 'https://www.bydauto.com.cn/api/index/showProvinceShop'
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '25',
        'Content-Type': 'application/json',
        'Cookie': 'referUrl=https%3A%2F%2Fwww.bydauto.com.cn%2Fpc%2FbuyCarSupport%2F; _pykey_=28a07868-8b00-510a-ad82-c6693ae6f129; _gscu_860813076=88960745n9gbwg11; Hm_lvt_1851a2613a0030cf442d59e8a51494a7=1688960746; Hm_lvt_c3eadf618f9b5e24794bf7aae93ff45d=1688960746; Hm_lvt_3ff4ba069adcd13c93982bb0011a50ef=1688960746; Hm_lvt_1564e5d163ac886419eba6220df2404e=1688960746; HWWAFSESID=9e4e0a659d9a870024; HWWAFSESTIME=1691395868128; referUrl=https%3A%2F%2Fwww.so.com%2Flink%3Fm%3DeMWlcvuVdUlHlkfTfzGpz3W26Nw1HrIp2J6QUpBPYr6oyEisW0FELuLztDRKvXfEK2EiHav2RuApTxQUZs3jR01oJzOnuFvUt7MP3HOpAZtW2vTip%252FpZJM11ma8Ol9cgVFoFC9ApS5x4%253D; 0995c630008c48eda2c1310db70a4da3=WyIyMDMwNDI1ODE1Il0',
        'Host': 'www.bydauto.com.cn',
        'Origin': 'https://www.bydauto.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://www.bydauto.com.cn/pc/buyCarSupport/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {"level_type": 1, "type": 1}

    response = requests.post(url, headers=header, json=data)
    re=response.json()
    return re
def post1(pid):
    url = 'https://www.bydauto.com.cn/api/index/getCityByPidShop'
    header = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Origin': 'https://www.bydauto.com.cn',
        'Cookie': 'referUrl=https%3A%2F%2Fwww.bydauto.com.cn%2Fpc%2FbuyCarSupport%2F; Hm_lpvt_1564e5d163ac886419eba6220df2404e=1691425571; Hm_lpvt_3ff4ba069adcd13c93982bb0011a50ef=1691425571; Hm_lvt_1564e5d163ac886419eba6220df2404e=1691425557; Hm_lvt_3ff4ba069adcd13c93982bb0011a50ef=1691425557; _gscbrs_860813076=1; _gscs_860813076=91425556gu0ehg15|pv:2; _gscu_860813076=91425556g8z7tl15; _pykey_=2c17b49a-7ff1-5012-9553-8a0402b0f999; Hm_lpvt_1851a2613a0030cf442d59e8a51494a7=1691425571; Hm_lpvt_c3eadf618f9b5e24794bf7aae93ff45d=1691425571; Hm_lvt_1851a2613a0030cf442d59e8a51494a7=1691425557; Hm_lvt_c3eadf618f9b5e24794bf7aae93ff45d=1691425557; __clickidc=169142555743277053; 0995c630008c48eda2c1310db70a4da3=WyIzNTgyNjkzMzQyIl0; HWWAFSESID=9210273b1bfa741b41; HWWAFSESTIME=1691425556254',
        'Content-Length': '23',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Host': 'www.bydauto.com.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
        'Referer': 'https://www.bydauto.com.cn/pc/buyCarSupport/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    data = {"pid": pid, "type": 1}
    response = requests.post(url, headers=header, json=data)
    result = response.json()
    return result

def post2(province,city):
    url = 'https://www.bydauto.com.cn/api/comom/search_join_shop'
    header = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Origin': 'https://www.bydauto.com.cn',
        'Cookie': 'referUrl=https%3A%2F%2Fwww.bydauto.com.cn%2Fpc%2FbuyCarSupport%2F; Hm_lpvt_1564e5d163ac886419eba6220df2404e=1691425571; Hm_lpvt_3ff4ba069adcd13c93982bb0011a50ef=1691425571; Hm_lvt_1564e5d163ac886419eba6220df2404e=1691425557; Hm_lvt_3ff4ba069adcd13c93982bb0011a50ef=1691425557; _gscbrs_860813076=1; _gscs_860813076=91425556gu0ehg15|pv:2; _gscu_860813076=91425556g8z7tl15; _pykey_=2c17b49a-7ff1-5012-9553-8a0402b0f999; Hm_lpvt_1851a2613a0030cf442d59e8a51494a7=1691425571; Hm_lpvt_c3eadf618f9b5e24794bf7aae93ff45d=1691425571; Hm_lvt_1851a2613a0030cf442d59e8a51494a7=1691425557; Hm_lvt_c3eadf618f9b5e24794bf7aae93ff45d=1691425557; __clickidc=169142555743277053; 0995c630008c48eda2c1310db70a4da3=WyIzNTgyNjkzMzQyIl0; HWWAFSESID=9210273b1bfa741b41; HWWAFSESTIME=1691425556254',
        'Content-Length': '23',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Host': 'www.bydauto.com.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
        'Referer': 'https://www.bydauto.com.cn/pc/buyCarSupport/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    data = {"type":2,"lat":29.599979,"lng":106.495288,"province":province,"city":city,"network":'null'}
    response = requests.post(url, headers=header, json=data)
    result = response.json()
    return result


dic=[]
re=post()
for i in re['data']:
    id1 = i['id']
    name1 = i['name']
    re1=post1(id1)
    for j in re1['data']:
        id2=j['id']
        name2=j['name']
        re2=post2(id1,id2)
        for m in re2['data']:
            id=m['id']
            short_name=m['short_name']
            buy_car_type=m['buy_car_type']
            lng=m['lng']
            lat=m['lat']
            address=m['address']
            tel=m['tel']
            jsd_type=m['jsd_type']
            join_shop_code=m['join_shop_code']
            join_shop_name=m['join_shop_name']
            province=name1
            province_code=id1
            city=name2
            city_code=id2
            t=[id,short_name,buy_car_type,lng,lat,address,tel,jsd_type,join_shop_code,join_shop_name,province,province_code,city,city_code]
            print(t[0:2])
            dic.append(t)
custom_header=['id','short_name','buy_car_type','lng','lat','address','tel','jsd_type','join_shop_code','join_shop_name','province','province_code','city','city_code']
dic_result=pd.DataFrame(dic)
dic_result.to_csv("./static/比亚迪.csv",index=False,header=custom_header,encoding='utf-8')