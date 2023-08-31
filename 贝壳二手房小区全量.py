# -*- coding: UTF-8 -*-
import requests
from requests.adapters import HTTPAdapter, Retry
import requests
import pandas as pd

url = 'https://map.ke.com/proxyApi/i.c-pc-webapi.ke.com/map/initdata?cityId=110000&dataSource=ESF'
header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'lianjia_uuid=23f7c9fe-933a-4352-82a7-22bd40c65c21; crosSdkDT2019DeviceId=-q47irm-yib4lg-o52loobgkhdm4k4-nshvozmj5; ftkrc_=2367b4c5-2ab4-4fac-991b-4a7d4899f938; lfrc_=eda1d6cf-4554-476e-b74f-0ea48b8d189f; hy_data_2020_id=189f2683915806-0f938c233e0b0b-7c54647e-1327104-189f268391613c8; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22189f2683915806-0f938c233e0b0b-7c54647e-1327104-189f268391613c8%22%2C%22site_id%22%3A341%2C%22user_company%22%3A236%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22189f2683915806-0f938c233e0b0b-7c54647e-1327104-189f268391613c8%22%7D; ke_uuid=f38576560a5d857bbeec3e42cbc2fe3b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22189f1cdba981296-02e12457b0b631-7c54647e-1327104-189f1cdba99cb5%22%2C%22%24device_id%22%3A%22189f1cdba981296-02e12457b0b631-7c54647e-1327104-189f1cdba99cb5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%E6%89%BE%E6%88%BF%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wychongqing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; select_city=110000; lianjia_ssid=11d630df-99d3-41e5-a4fb-3f68624dd4c1',
    'Host': 'map.ke.com',
    'Pragma': 'no-cache',
    'Referer': 'https://map.ke.com/map/110000/ESF',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'X-Requested-With': 'XMLHttpRequest',
    'plat': 'KE',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(url, header).json()
print('dict_list')
dict_list = {}
list_cityid = []
for i in response['data']['cityList']:
    for m in i['list']:
        province = m['name']
        for h in m['list']:
            ids = h['id']
            name = h['name']
            t = [ids, name]
            dict_list[ids] = province
            list_cityid.append(t)
print('mapping_table')
for_list = []
for i in list_cityid:
    for_list.append(i[0])
for_list_name = []
for i in list_cityid:
    for_list_name.append(i[1])
mapping_table = {item[0]: item[1] for item in list_cityid}

session = requests.Session()
session.headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'lianjia_ssid=438e1265-0f74-4bea-b699-2f23c4123732; lianjia_uuid=fbe5517a-e4e6-4774-9759-ba3bb1c4d4f0; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218a1fe73674260-0190dc98d1e956-26031f51-1327104-18a1fe73675c65%22%2C%22%24device_id%22%3A%2218a1fe73674260-0190dc98d1e956-26031f51-1327104-18a1fe73675c65%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    'Host': 'map.ke.com',
    'Referer': 'https://map.ke.com/map/500000/ESF',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'plat': 'KE',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
pool_connections = 100
pool_maxsize = 100

retry_strategy = Retry(
    total=5,
    status_forcelist=[500, 502, 503, 504],
    backoff_factor=0.1,
)
adapter = HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize, max_retries=retry_strategy)

# 为特定的 URL 前缀关联连接池适配器
session.mount('http://', adapter)
session.mount('https://', adapter)


def deal_lat_lng(ids, types, maxLatitude, minLatitude, maxLongitude, minLongitude):
    url = f'https://map.ke.com/proxyApi/i.c-pc-webapi.ke.com/map/bubblelist?cityId={ids}&dataSource=ESF&condition=&id=&groupType={types}&maxLatitude={maxLatitude}&minLatitude={minLatitude}&maxLongitude={maxLongitude}&minLongitude={minLongitude}'
    response = session.get(url)
    re1 = response.json()
    return re1


def deal_data(res, dics, counts, city, city_id):
    for i in res['data']['bubbleList']:
        id_ = i['id']
        border = i['border']
        name = i['name']
        latitude = i['latitude']
        longitude = i['longitude']
        count = i['count']
        priceStr = i['priceStr']
        priceUnit = i['priceUnit']
        price = priceStr + priceUnit
        province = dict_list[f'{city_id}']
        t = [id_, name, border, price, latitude, longitude, count, city, province]
        dics.append(t)
        counts += count
    return dics, counts


def spider_main(city_id):
    try:
        print(f"{mapping_table[f'{city_id}']}:{city_id} 开始")
        re1 = deal_lat_lng(city_id, 'district', 54, 3, 135, 73)
        city = mapping_table[f'{city_id}']
        lng = []
        lat = []
        for i in re1['data']['bubbleList']:
            for li in i['border'].split(';'):
                lng.append(float(li.split(',')[0]))
                lat.append(float(li.split(',')[1]))
        maxLatitude_all = max(lat)
        minLatitude_all = min(lat)
        maxLongitude_all = max(lng)
        minLongitude_all = min(lng)
        lat_m = 0.025
        lng_m = 0.025
        minLongitude_all_while = minLongitude_all - lat_m
        counts = 0
        dics = []
        while True:
            minLatitude_all_while = minLatitude_all - lng_m
            while True:
                res = deal_lat_lng(city_id, "community", minLatitude_all_while + lat_m, minLatitude_all_while,
                                   minLongitude_all_while + lng_m, minLongitude_all_while)
                minLatitude_all_while = minLatitude_all_while + lat_m
                if minLatitude_all_while - lat_m >= maxLatitude_all:
                    break
                if res['data']['totalCount'] == 0:
                    continue
                dics, counts = deal_data(res, dics, counts, city, city_id)
            minLongitude_all_while = minLongitude_all_while + lng_m
            if minLongitude_all_while - lng_m >= maxLongitude_all:
                break
        print(f"{mapping_table[f'{city_id}']}：{city_id} 结束  总套数：", counts)
        return dics
    except Exception as e:
        print(f"{mapping_table[f'{city_id}']}:{city_id} 爬取失败 ")
        return [0, city_id]



from multiprocessing.dummy import Pool


def thread(for_list_1):
    dics = []
    dics_fall = []
    # 定义三个线程池
    pool = Pool(50)
    # 利用map让线程池中的所有线程‘同时’执行calc_power2函数
    result = pool.map(spider_main, for_list_1)
    pool.close()
    pool.join()
    for i in result:
        try:
            if i[0] == 0:
                dics_fall.append(i[1])
                continue
            dics += i
        except:
            print(f"{i}出错了")
            continue

    print(len(dics), len(result))
    cus = ['id', 'name', 'border', 'price', 'latitude', 'longitude', 'count', 'city', 'province']
    data_result = pd.DataFrame(dics)
    data_result.to_excel(f'sp_6_{for_list_1[0]}.xlsx', index=False, header=cus)
    print("失败的id", [mapping_table[f"{i}"] for i in dics_fall])


import multiprocessing

if __name__ == '__main__':
    multiprocessing.freeze_support()
    processes = []
    for i in range(3):
        print("start......")
        ag = for_list[i * 50:50 + i * 50]
        process = multiprocessing.Process(target=thread, args=(ag,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print("All Processes Finished")
