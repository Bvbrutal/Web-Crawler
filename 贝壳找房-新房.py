# -*- coding: UTF-8 -*-
import pandas as pd
import requests
def get_data(page):
    url = f'https://m.ke.com/sz/loupan/pg{page}/?_t=1&source=list'
    header = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'lianjia_uuid=23f7c9fe-933a-4352-82a7-22bd40c65c21; sajssdk_2015_cross_new_user=1; crosSdkDT2019DeviceId=-q47irm-yib4lg-o52loobgkhdm4k4-nshvozmj5; ftkrc_=2367b4c5-2ab4-4fac-991b-4a7d4899f938; lfrc_=eda1d6cf-4554-476e-b74f-0ea48b8d189f; hy_data_2020_id=189f2683915806-0f938c233e0b0b-7c54647e-1327104-189f268391613c8; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22189f2683915806-0f938c233e0b0b-7c54647e-1327104-189f268391613c8%22%2C%22site_id%22%3A341%2C%22user_company%22%3A236%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22189f2683915806-0f938c233e0b0b-7c54647e-1327104-189f268391613c8%22%7D; sajssdk_2020_cross_new_user=1; lianjia_ssid=076acd4f-0b21-40bb-81cb-5ef89578e010; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22189f1cdba981296-02e12457b0b631-7c54647e-1327104-189f1cdba99cb5%22%2C%22%24device_id%22%3A%22189f1cdba981296-02e12457b0b631-7c54647e-1327104-189f1cdba99cb5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wychongqing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNTE4ZTA5NDhmYjRjYzljM2RlZDZjM2JhMDA1Y2M0NmEwNTgyYWU4MTg0MjJiZjAyMTUwNDU3MDhmN2JjMzM1ODQxMzg0NWY1NmNjN2FhOWJhYmVhZDA4YjgwOTViODdhYjIyOGJhY2JhYjhlOTA3NWQ1M2M3OWY1ZjQ0OThhOTcyNzI3NzU1NTliYjcyOTA0MzY4MDgwNTZhNDExNjRkMWJmNjMwNmNhYWM3ZjM1ZGJmY2JlYTI3MGExMDZlZTAyY2NkMjFlMjdkNTY2YjRhYjI2ODc0YmZhMGZiYTEyYTQxZWQxYTc1ZTkyM2Q4NTI5ZDU1YWMwZjA3NDNiOTliZVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI5NDk5MzdkZlwifSIsInIiOiJodHRwczovL20ua2UuY29tL2NpdHkvc2VhcmNoIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; select_city=440300; beikeBaseData=%7B%22parentSceneId%22%3A%221308107441066922497%22%7D; digData=%7B%22key%22%3A%22m_pages_xinfangResblockList%22%7D; digv_extends={"utmTrackId":null}',
        'Host': 'm.ke.com',
        'Pragma': 'no-cache',
        'Referer': 'https://m.ke.com/sz/loupan/futianqu/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/115.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    response = requests.get(url, headers=header)
    re2 = response.json()
    return re2
count=0
lists=[]
for page in range(1, 64):
    re1 = get_data(page)
    print(page)
    for i in re1['data']['body']['_resblock_list']:
        id = i['id']
        name = i['resblock_name']
        districtName = i['district_name']
        bizcircleName = i['bizcircle_name']
        if districtName and bizcircleName:
            site = districtName + bizcircleName
        else:
            site = districtName
        average_price = i['average_price']
        avg_price_start_unit=i['avg_price_start_unit']
        price=average_price+avg_price_start_unit
        if average_price=="0":
            price="价格待定"
        pointLat = i['latitude']
        pointLng = i['longitude']
        house_type=i['house_type']
        t = [id, name, site, pointLat, pointLng, price,house_type]
        lists.append(t)
        count += 1
        print(t)
print("总条数：", count)
cus = ['id', 'name', 'site', 'pointLat', 'pointLng', 'price','house_type']
result_data = pd.DataFrame(lists)
result_data.to_csv('static/贝壳找房-新房.csv', index=False, header=cus)