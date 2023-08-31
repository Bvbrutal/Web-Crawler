# -*- coding: UTF-8 -*-
import requests
import re

def get_data(page,city):
    page = page
    url = f'https://m.ke.com/liverpool/api/webApiProxy/secondhand/resblock/search?cityId=440300&condition=%2F{city}%2Fpg{page}&curPage={page}'
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'lianjia_uuid=23f7c9fe-933a-4352-82a7-22bd40c65c21; select_city=500000; sajssdk_2015_cross_new_user=1; crosSdkDT2019DeviceId=-q47irm-yib4lg-o52loobgkhdm4k4-nshvozmj5; login_ucid=2000000353998767; lianjia_token=2.001490951479206f57053dbc25ea816bff; lianjia_token_secure=2.001490951479206f57053dbc25ea816bff; security_ticket=OVqhnUz7wPJ8YPrhNkXXBJDgz+u56zrFHOqFbUZHVelI/p0K+QsYQdRyNPMRJKfJ77G7tax5MBo0b6upwcWrGo6RFvfrwW2aQmEaPXC9X2YVh8LoVRQhTJGQKZn5QIA+GaLAQLvAgpTHYxBwqj1iPB3EJzTBkZomft2Qhp5/MXg=; ftkrc_=2367b4c5-2ab4-4fac-991b-4a7d4899f938; lfrc_=eda1d6cf-4554-476e-b74f-0ea48b8d189f; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22189f1cdba981296-02e12457b0b631-7c54647e-1327104-189f1cdba99cb5%22%2C%22%24device_id%22%3A%22189f1cdba981296-02e12457b0b631-7c54647e-1327104-189f1cdba99cb5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22360%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22biaoti%22%2C%22%24latest_utm_content%22%3A%22biaoti%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZjg3YWExNzRjZTUzNzYwNmZiNTRhYjNlYmJkZmUwZmZmYTZkNzFiODFiNjExZTIwY2JlMzIzMjk4MjRlMmE0YWQwYjE4MmFlY2UyOTAyMWFiY2RkNTBlZjg5Yzg4MDE1OWQ1YTZhNTRhZGQ1ZjMxNjNjZWZmMmJkZjJmNDgyYmJkN2I3YjAxMDA5NWI4YTViM2U4NmZmMmZkMmMwMWMwY2Y5ZjRhN2NlMzU5YzlhMDRlYjQ3NTE4YjU1NjhmYjRmM2UzOTkyNTMxOGY2M2YzODkxNzI4MTE4MzY3NzdjN2U3NmRmYWJiOWRlNzgwZjVmYzBlMWY3ZTA0YzkxMTViZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwM2QyMmNmZVwifSIsInIiOiJodHRwczovL20ua2UuY29tL215L2luZGV4LyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; digData=%7B%22key%22%3A%22m_pages_xiaoquSearch%22%7D; lianjia_ssid=af97324f-4b63-4c1f-9ddc-de659411c206; beikeBaseData=%7B%22parentSceneId%22%3A%221307053931890390017%22%7D',
        'DUID': '',
        'Host': 'm.ke.com',
        'ORIGINAL-PAGE-URL': 'https://m.ke.com/cq/xiaoqu/pg17',
        'Pragma': 'no-cache',
        'Referer': 'https://m.ke.com/cq/xiaoqu/pg17',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(url, headers=header)
    re1 = response.json()
    return re1

import pandas as pd
count=0
lists = []
city=['luohuqu','futianqu','nanshanqu','yantianqu','baoanqu','longgangqu','longhuaqu','guangmingqu','pingshanqu','dapengxinqu']
for city in city:
    for page in range(1, 101):
        re1 = get_data(page,city)
        for i in re1['data']['data']['list']:
            id = i['id']
            name = i['name']
            districtName = i['districtName']
            bizcircleName = i['bizcircleName']
            if districtName and bizcircleName:
                site = districtName + bizcircleName
            else:
                site=districtName
            price = i['priceUnitAvgStr']
            pointLat = i['pointLat']
            pointLng = i['pointLng']
            buildingCount = i['buildingCount']
            t = [id, name, site, pointLat, pointLng, price, buildingCount]
            lists.append(t)
            count+=1
            print(t)
print("总条数：",count)
cus = ['id', 'name', 'site', 'pointLat', 'pointLng', 'price', 'buildingCount']
result_data = pd.DataFrame(lists)
result_data.to_csv('static/贝壳找房-小区.csv', index=False, header=cus)