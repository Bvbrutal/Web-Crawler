# -*- coding: UTF-8 -*-
import requests
import pandas as pd
from lxml import etree
import re
import time


def get_data(page):
    di = []
    url = f'https://h5.m.jia.com/JiaZhuangxiu/ajax_shop_list_201907/?areaflag=chongqing&page={page}&lat1=29.622799480219&lng1=106.50423680208&type=total_score&tag=&area=&action=page&genre=&price=&area_num=&tplv=2020&shop_store_photo=1&active_shop_filter_type=&gao_id=100068,100032&extra_data=1&show_tjj_position=ZXCompanylist&package=com.qeeka.o2o.pro0'

    header = {
        'Host': 'h5.m.jia.com',
        'from-app': 'Y',
        'Accept': '*/*',
        'idfa': '46131968-2942-43AD-87BF-FA038E463400',
        'X-Requested-With': 'XMLHttpRequest',
        'userId': '136405727',
        'appVersion': '3.9.3',
        'devicePlatform': 'iOS',
        'packageName': 'com.qeeka.o2o.pro',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'deviceId': '87E11302-20D3-4B3F-BCD7-8A9D164EA6CA',
        'sessionId': 'session-user-47487366adc04528b9f6b37f7938325c',
        'User-Agent': '%E9%BD%90%E5%AE%B6%E6%9E%81%E9%80%9F%E7%89%88/1 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Connection': 'keep-alive',
        'appId': '802',
        'appChannel': 'AppStore',
        'Cookie': 'Hm_lvt_0ef6d34be86061f1e88b15621d1fef05=1693796822,1693797067,1693797388,1693797929; TJJID2=2-1xramy1vdma2nv7w-1693795317741---1693797082899-1693795317741-1693797084206-1693797928386-5; referrer=https%3A%2F%2Fh5.m.jia.com%2Fzx%2Fshop%2F215230404%2F%3Fpos%3D2%26area_id%3D0; LOGIN_AREAFLAG=chongqing; www_jia_user_id=136405727; PHPSESSID=mvqnvlgnkoqremen6j19aust31',
        'deviceIMEI': '87E11302-20D3-4B3F-BCD7-8A9D164EA6CA',
    }

    response = requests.get(url, headers=header)
    for i in range(1, 11):
        tree = etree.HTML(response.text)
        xpath = f'//div[{i}]/a/div[2]/div[1]/div/span//text()'
        name = tree.xpath(xpath)[0]
        xpath = f'/html/body/div[{i}]/a/@href'
        re1 = tree.xpath(xpath)[0]
        match = re.search(r"/shop/([0-9]*)/?", re1)
        uid = match[1]
        phone = get_phone(uid)
        t = [name, uid, phone]
        print(t)
        di.append(t)
    return di


def get_phone(uid):
    url = f'https://h5.m.jia.com/zx/shop/{uid}/'

    header = {
        'Host': 'h5.m.jia.com',
        'appId': '802',
        'wk_header': 'Y',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 /87E11302-20D3-4B3F-BCD7-8A9D164EA6CA/828*1792/46011/iPhone XR/QJZX/3.9.3/AppStore/VersionMark3.9.3',
        'Cookie': 'www_jia_user_id=136405727;HMACCOUNT=61ECB32470EFE0C6;ab_bid=8fc37bc1eb8abcf487b5395c68df7e09f680;LOGIN_AREAFLAG=chongqing;BAIDUID=EDB39D6FBA64D4E361B50D86924BD739:FG=1;Hm_lvt_0ef6d34be86061f1e88b15621d1fef05=1693798099,1693799275,1693801253,1693806804;PHPSESSID=atssmdkhs6rvap169q3gpifav7;referrer=https%3A%2F%2Fh5.m.jia.com%2F%2Fzx%2Ftoutiao%2Fchongqing%2F;SECKEY_ABVK=P8e9feeM4OQNhsW6PGy4kCBIUyCF800qEgv3aCsJYmo%3D;TJJID2=2-1xramy1vdma2nv7w-1693795317741---1693808998415-1693806803516-1693806807441-1693808998415-10;ab_sr=1.0.1_YWVlNjI3NGY0ZDBlMGE3OGI2NWQzZmIyODc4Mzg3NWY0Mjk4ZWFiYzg3OGYwNmE4MzBhODA0OWNmZDEzMGQwNGU4MmY3YjAyNzk5NjlhNGU0Yzg0NTBkY2VmMjFiZmViODc3OTA1ODQ4ZmUyMTJjY2E5ZDUxN2FjODEzZWJmNjgwNDdhMzNkNWJhMTI1ZGM2NWViMzAzYTJmNWI3ZDMzNA==;traceid=b32e92cdce;UId=DSmNa9Qb++fsV8EbR94gFw;session_id=session-user-47487366adc04528b9f6b37f7938325c;ab_jid=84a7b42ac95541cc8fc37bc1eb8abcf487b4;BMAP_SECKEY=lXWzznEROmG2kBwEElgmNXJ5FImNuDzaxU0i2avg4uK31hEjXAX-5-Gxu3ON7hJD6s9n06RzQnft_AAz0UzumzmaSCNM0zcQbMB6sE5Ok0AEv_RPilTb05v2bdAXeAr1k9IMxRkySX1B7FNiFXqxUZ2R9dzXeCl8m19w8qjYLpk;',
        'devicePlatform': 'iOS',
        'userId': '136405727',
        'deviceIMEI': '87E11302-20D3-4B3F-BCD7-8A9D164EA6CA',
        'appVersion': '3.9.3',
        'appChannel': 'AppStore',
        'from-app': 'Y',
        'packageName': 'com.qeeka.o2o.pro',
        'substation-py': 'chongqing',
        'deviceId': '87E11302-20D3-4B3F-BCD7-8A9D164EA6CA',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-cn',
        'sessionId': 'session-user-47487366adc04528b9f6b37f7938325c',
        'substation-cn': '',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'idfa': '46131968-2942-43AD-87BF-FA038E463400',
    }

    response = requests.get(url, headers=header)
    tree = etree.HTML(response.text)
    xpath1 = '//*[@id="shop_tel"]/@value'
    phone = tree.xpath(xpath1)[0]

    return phone


dic = []
for page in range(0, 57):
    time.sleep(1)
    t = get_data(page)
    print(t)
    dic += t

res = pd.DataFrame(dic)
cus = ['name', 'uid', 'phone']
res.to_csv('齐家.csv', index=False, header=cus)