# -*- coding: UTF-8 -*-
import pandas as pd
import requests


def post1():
    url = f'https://www.tesla.cn/cua-api/tesla-locations?translate=zh_CN&map=baidu&usetrt=true'
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Cookie': 'gdp_user_id=gioenc-4dgd6794%2Cae8d%2C5cg3%2C9866%2C6196746d3c39; AKA_A2=A; b0e25bc027704bfe_gdp_session_id=02eced48-bcd9-4497-84b4-1aa35ea71afa; ak_bmsc=5F1DA5139EE9CF531B9DE77F1FF26A99~000000000000000000000000000000~YAAQN2l7djTmUL6JAQAAYoPB0hTmNrA9M3hz69VTwJHiSng+7MX/NyLhbs/AwA7l8bmyWku8kFNrpjWvgAm487RJR4goaeFQgF6BRo5O+7eGAisTZfIHtwVipLWLoH77SbL60dyBTIDzCZsCKjleixkVubxPoChAFZq6fHrSPVgB1cSxHwHq0p/KprsZPagg0YTVpgvSp5eozIl7NngGh9iPnJZZgl6HTHpG4Yt3K81u7nL/AG7M84zveOLxT3K81neeThIJNelMgM2hjQz0UztETlkFcgrNiPrXP6tHljHD/DdtX9FzKBylyFb15KSXhVLqTLK9NKAbJktMOsY1ZzDnc/1Bgw+V8hZX25ORGnOIuhvgRtW4TjY/l3w6F590RYkDSnOVRCb+rVzf05I+RNdcbTZsJ4f6qpoU1ctqiV3LcWyBs2ZEiZ1alblv1nZMQR9aszTQSG3DBWCOuPXpASmD09gfyAZKTh9pNipV9UmvgXbYcN/8uNI=; cua_sess=12afced137ce161d8a8bc2c92cf6525f; returning_user=1; has_js=1; buy_flow_locale=zh_CN; webchat-channel=chatbot; bm_sv=FE18679548329E5152986DC4FECC7981~YAAQN2l7dj6eUb6JAQAA3RPX0hQbEEdc8WvL2yf7NVVUgxW0XUO3nn92XDRluIZV56ItWyRKB4zaQQZwGwPO/UofnWCpb6NaCBHXOFMKEC8LadJs6UXPxq63vIhD+ES5J9oih0OefhOuKQpnob0TdISxyKTEjSNmGi0nAzznHeYEXzoswt8gH22rRsQBxskUKnbk/sGOZC/rNOe/JDFMK1vY/C4jDQkpnefGaoVuCcmmaHbv0JrOYoJ7StxKMDQ=~1; SECKEY_ABVK=TJQu6ZQiydy8dGAtx2ViK9T25l3U2xTcbemBtV3nAb0%3D; BMAP_SECKEY=dVuvVIY4R2nAN3MpGpqIBhMlhQNgTxh5JkuVdTtTiVdIEsDKqNyi6guu-fhBy20Pm7JLRFRf0AkeIR8V9SjdWlU34JhAybHFzbYOYJa7Jtwme8KVUcb5EpAe2DAd-nZ52VYLSnrkOGWnHkHIyQqFFe583m2y6IxzrHRjmjlniqg5vJpZxF76Ptmim084SDGX; b0e25bc027704bfe_gdp_sequence_ids=%7B%22globalKey%22%3A258%2C%22VISIT%22%3A4%2C%22PAGE%22%3A57%2C%22VIEW_CLICK%22%3A148%2C%22VIEW_CHANGE%22%3A14%2C%22FORM_SUBMIT%22%3A3%2C%22CUSTOM%22%3A37%7D; b0e25bc027704bfe_gdp_session_id_02eced48-bcd9-4497-84b4-1aa35ea71afa=true',
        'Pragma': 'no-cache',
        'Referer': 'https://www.tesla.cn/findus?filters=store%2Cservice%2Csupercharger%2Cdestination%20charger%2Cbodyshop&location=beijingwestjoycity',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    }

    response = requests.get(url, headers=header)
    re1 = response.json()
    return re1


def post2(id):
    url = f'https://www.tesla.cn/cua-api/tesla-location?id={id}&map=baidu'
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Cookie': 'gdp_user_id=gioenc-4dgd6794%2Cae8d%2C5cg3%2C9866%2C6196746d3c39; AKA_A2=A; b0e25bc027704bfe_gdp_session_id=02eced48-bcd9-4497-84b4-1aa35ea71afa; ak_bmsc=5F1DA5139EE9CF531B9DE77F1FF26A99~000000000000000000000000000000~YAAQN2l7djTmUL6JAQAAYoPB0hTmNrA9M3hz69VTwJHiSng+7MX/NyLhbs/AwA7l8bmyWku8kFNrpjWvgAm487RJR4goaeFQgF6BRo5O+7eGAisTZfIHtwVipLWLoH77SbL60dyBTIDzCZsCKjleixkVubxPoChAFZq6fHrSPVgB1cSxHwHq0p/KprsZPagg0YTVpgvSp5eozIl7NngGh9iPnJZZgl6HTHpG4Yt3K81u7nL/AG7M84zveOLxT3K81neeThIJNelMgM2hjQz0UztETlkFcgrNiPrXP6tHljHD/DdtX9FzKBylyFb15KSXhVLqTLK9NKAbJktMOsY1ZzDnc/1Bgw+V8hZX25ORGnOIuhvgRtW4TjY/l3w6F590RYkDSnOVRCb+rVzf05I+RNdcbTZsJ4f6qpoU1ctqiV3LcWyBs2ZEiZ1alblv1nZMQR9aszTQSG3DBWCOuPXpASmD09gfyAZKTh9pNipV9UmvgXbYcN/8uNI=; cua_sess=12afced137ce161d8a8bc2c92cf6525f; returning_user=1; has_js=1; buy_flow_locale=zh_CN; webchat-channel=chatbot; bm_sv=FE18679548329E5152986DC4FECC7981~YAAQN2l7dj6eUb6JAQAA3RPX0hQbEEdc8WvL2yf7NVVUgxW0XUO3nn92XDRluIZV56ItWyRKB4zaQQZwGwPO/UofnWCpb6NaCBHXOFMKEC8LadJs6UXPxq63vIhD+ES5J9oih0OefhOuKQpnob0TdISxyKTEjSNmGi0nAzznHeYEXzoswt8gH22rRsQBxskUKnbk/sGOZC/rNOe/JDFMK1vY/C4jDQkpnefGaoVuCcmmaHbv0JrOYoJ7StxKMDQ=~1; SECKEY_ABVK=TJQu6ZQiydy8dGAtx2ViK9T25l3U2xTcbemBtV3nAb0%3D; BMAP_SECKEY=dVuvVIY4R2nAN3MpGpqIBhMlhQNgTxh5JkuVdTtTiVdIEsDKqNyi6guu-fhBy20Pm7JLRFRf0AkeIR8V9SjdWlU34JhAybHFzbYOYJa7Jtwme8KVUcb5EpAe2DAd-nZ52VYLSnrkOGWnHkHIyQqFFe583m2y6IxzrHRjmjlniqg5vJpZxF76Ptmim084SDGX; b0e25bc027704bfe_gdp_sequence_ids=%7B%22globalKey%22%3A258%2C%22VISIT%22%3A4%2C%22PAGE%22%3A57%2C%22VIEW_CLICK%22%3A148%2C%22VIEW_CHANGE%22%3A14%2C%22FORM_SUBMIT%22%3A3%2C%22CUSTOM%22%3A37%7D; b0e25bc027704bfe_gdp_session_id_02eced48-bcd9-4497-84b4-1aa35ea71afa=true',
        'Pragma': 'no-cache',
        'Referer': 'https://www.tesla.cn/findus?filters=store%2Cservice%2Csupercharger%2Cdestination%20charger%2Cbodyshop&location=beijingwestjoycity',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    }

    response = requests.get(url, headers=header)
    re2 = response.json()
    return re2


re1 = post1()
dic = []
for i in re1:
    try:
        location_id = i['location_id']
        location_type = i['location_type']
        re2 = post2(location_id)
        address = re2['address']
        baidu_lat = re2['baidu_lat']
        baidu_lng = re2['baidu_lng']
        city = re2['city']
        title = re2['title']
        province_state = re2['province_state']
        region = re2['region']
        sales_phone = re2['sales_phone'][0]['number']
        trt_id = re2['trt_id']
        country = re2['country']
        t=[location_id, location_type, address, baidu_lat, baidu_lng, city, title, province_state, region,sales_phone, trt_id, country]
        dic.append(t)
        print(t)
    except Exception as e:
        # 捕获异常并打印原始数据
        print(re2)
        print("An error occurred:", e)

cus = ['location_id', 'location_type', 'address', 'baidu_lat', 'baidu_lng', 'city', 'title', 'province_state',
       'region', 'sales_phone', 'trt_id', 'country']
result = pd.DataFrame(dic)
result.to_csv('./static/特斯拉.csv', index=False, header=cus,encoding='utf-8')