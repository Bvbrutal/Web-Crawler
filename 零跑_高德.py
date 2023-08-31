# -*- coding: UTF-8 -*-
import pandas as pd
import requests

def post1():
    url = 'https://store-center.leapmotor.com/leap-store/storeDrainage/getAllProvinceCityStore'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=header)
    re1 = response.json()
    return re1


def post2(provinceCode, cityCode):
    url = f'https://store-center.leapmotor.com/leap-store/storeDrainage/getLastStoreInfo?storeType=0&longitudeLatitude=120.223901,30.209219&provinceCode={provinceCode}&cityCode={cityCode}'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=header)
    re2 = response.json()
    return re2

re1 = post1()
dic = []
for i in re1['data']['cityList']:
    areaShopCity = i['areaShopCity']
    areaShopCityCode = i['areaShopCityCode']
    areaShopProvince = i['areaShopProvince']
    areaShopProvinceCode = i['areaShopProvinceCode']
    re2 = post2(areaShopProvinceCode,areaShopCityCode)
    for j in re2['data']['recommend']:
        areaShopLocation = j['areaShopLocation']
        name=j['name']
        site=j['site']
        areaShopTell=j['areaShopTell']
        areaAbbreviation=j['areaAbbreviation']
        shopServiceCategory=j['shopServiceCategory']
        storeName=j['storeName']
        name=name+areaAbbreviation
        print(areaShopLocation)
        lng=areaShopLocation.split(',')[0]
        lat=areaShopLocation.split(',')[1]
        t = [name, site,lat,lng, areaShopTell, areaShopCity,areaShopCityCode,areaShopProvince,areaShopProvinceCode,shopServiceCategory,storeName]
        dic.append(t)
        print(t)

cus=['name', 'site','lat','lng', 'areaShopTell', 'areaShopCity','areaShopCityCode','areaShopProvince','areaShopProvinceCode','shopServiceCategory','storeName']
result=pd.DataFrame(dic)
result.to_csv('./static/零跑2.csv',index=False,header=cus)
