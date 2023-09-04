# -*- coding: utf-8 -*-
import random
import time

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def fetchUrl(pid, uid, max_id):
    url = "https://weibo.com/ajax/statuses/buildComments"

    headers = {
        "user-agent": UserAgent().random,
        "Cookie": "自己的cookie"
    }
    proxies = [{
        "http": "http://111.225.153.66:8089",
        "http": "http://171.92.21.83:9000",
        "http": "http://182.139.110.30:9000",
        "http": "http://171.92.20.71:9000",
        "http": "http://171.92.21.43:9000",
        "http": "http://115.211.47.137:9000",
        "http": "http://115.223.237.229:9000",
        "http": "http://117.28.95.138:57114",
        "http": "http://115.211.35.237:9000",
        "http": "http://171.92.21.230:9000",
        "http": "http://103.59.151.99:30001",
        "http": "http://115.205.122.27:7891",
        "http": "http://171.92.21.154:9000",
        "http": "http://49.71.159.239:9000",
        "http": "http://171.92.20.8:9000",
        "http": "http://117.94.114.39:9000",
        "http": "http://115.211.33.131:9000",
        "http": "http://111.250.131.111:3128",
        "http": "http://115.211.45.26:9000",
        "http": "http://121.37.227.255:8888",
        "http": "http://171.92.21.135:9000",
        "http": "http://115.218.220.11:9000",
        "http": "http://183.147.28.22:9000",
        "http": "http://171.92.21.104:9000",
        "http": "http://182.139.110.15:9000",
        "http": "http://122.243.14.207:9000",
        "http": "http://182.139.111.107:9000",
        "http": "http://115.210.31.0:9000",
        "http": "http://171.92.20.55:9000","http": "http://171.92.20.32:9000","http": "http://59.38.60.118:9797","http": "http://111.225.153.66:8089","http": "http://171.92.21.83:9000","http": "http://182.139.110.30:9000","http": "http://171.92.20.71:9000","http": "http://171.92.21.43:9000","http": "http://115.211.47.137:9000","http": "http://115.223.237.229:9000","http": "http://117.28.95.138:57114","http": "http://115.211.35.237:9000","http": "http://171.92.21.230:9000","http": "http://103.59.151.99:30001","http": "http://115.205.122.27:7891","http": "http://171.92.21.154:9000","http": "http://49.71.159.239:9000","http": "http://171.92.20.8:9000","http": "http://117.94.114.39:9000","http": "http://115.211.33.131:9000","http": "http://111.250.131.111:3128","http": "http://115.211.45.26:9000","http": "http://121.37.227.255:8888","http": "http://171.92.21.135:9000","http": "http://115.218.220.11:9000","http": "http://183.147.28.22:9000","http": "http://171.92.21.104:9000","http": "http://182.139.110.15:9000","http": "http://122.243.14.207:9000","http": "http://182.139.111.107:9000"
    }]
    params = {
        "flow": 0,
        "is_reload": 1,
        "id": pid,
        "is_show_bulletin": 2,
        "is_mix": 0,
        "max_id": max_id,
        "count": 20,
        "uid": uid,
    }
    proxy = random.choice(proxies)
    r = requests.get(url, headers=headers, params=params,
                     proxies=proxy).json()  # Only convert to Json when status is OK.
    return r


def parseJson(jsonObj):
    data = jsonObj["data"]
    max_id = jsonObj["max_id"]

    commentData = []
    for item in data:
        # 评论id
        datas = {'-1': '普通用户', '0': '名人', '1': '政府', '2': '企业', '3': '媒体', '4': '校园', '5': '网站', '6': '应用', '7': '团体机构',
                 '8': '待审企业', '200': '初级达人', '220': '中高级达人', '400': '已故v用户'}
        comment_Id = item["id"]
        # 评论内容
        content = BeautifulSoup(item["text"], "html.parser").text
        # 评论时间
        created_at = item["created_at"]
        # 点赞数
        like_counts = item["like_counts"]
        # 评论数
        total_number = item["total_number"]
        next = "微博内容"
        # 评论者 id，name，city
        user = item["user"]
        userID = user["id"]
        userName = user["name"]
        userCity = user["location"]
        gender = user["gender"]
        statuses_count = user["statuses_count"]
        v = user["verified_type"]
        vr = datas.get("{}".format(v))
        age = user["created_at"]

        dataItem = [next, comment_Id, created_at, userID, userName, gender, age, userCity, like_counts, total_number,
                    content, vr, statuses_count]
        commentData.append(dataItem)
    return commentData, max_id


def save_data(data, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)

    dataframe = pd.DataFrame(data)
    dataframe.to_csv(path + filename, encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)


if __name__ == "__main__":
    s = 0
    pid =4774830090226681# 用户id，固定，想要爬的博主id
    uid =1263406744 # 微博id，固定，想要爬的微博id
    path = "//"  # 保存的路径
    filename = "beiyong.csv"
    max_id = 0

    while (True):
        s += 1
        html = fetchUrl(pid, uid, max_id)
        comments, max_id = parseJson(html)
        save_data(comments, path, filename)
        print(s)
        time.sleep(0.5)
        if max_id==0:
            break
