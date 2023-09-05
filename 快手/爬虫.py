import json
import random
import time

import pandas as pd
import requests
import re


# photoId：视频id
# pcursor：页数传递
# userId：博主id

class kuaishou():
    def __init__(self):
        self.header = {
            "referer": 'https://www.kuaishou.com/profile/3xx4nngake7pnmg',
            "Cookie": 'did=web_dd1895ad8c492c8e0e8ccdfca79472a3; didv=1677668522826; kpf=PC_WEB; clientid=3; userId=2939205029; ktrace-context=1|MS43NjQ1ODM2OTgyODY2OTgyLjg3NTkzNjUyLjE2NzgwMDA1Nzk1MTIuNzI2MzY=|MS43NjQ1ODM2OTgyODY2OTgyLjM5NTE4Mzg4LjE2NzgwMDA1Nzk1MTIuNzI2Mzc=|0|graphql-server|webservice|false|NA; kpn=KUAISHOU_VISION; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABvUBanrPBz-dryvq-04bHe2ITaPXHCvm5RGAe1VAT8xJHH6UM2xwChs-i88xWCj6oq51S_K-VQNZc5ANl0JuOQIhKC-t5HL8Ib8ZjgczWHcuPGbr_F8kddW-sKCdHQBY2LDkK3g3NY2Fd3mH3HPkVTpXLVcgBules4DFzrVeA70Mc1seROgGcai9Ujt-wHQi47qFQO4NLkNPQUJ-LCVjQNBoSzFZBnBL4suA5hQVn0dPKLsMxIiCtYDxfdrXDnNlg9bH5Yjtu7t1afj5odmW5ki5U4iyBkygFMAE; kuaishou.server.web_ph=abc9532cc3347f7309aa11a82d4775e97d10',
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'
        }
        proxies = [{'http': 'http:/114.99.2.57:8089', 'http': 'http://114.102.47.191:8089',
                    'http': 'http://110.82.250.167:8089', 'http': 'http://111.224.213.238:8089',
                    'http': 'http://223.247.47.228:8089', 'http': 'http://111.224.213.37:8089',
                    'http': 'http://114.102.47.152:8089', 'http': 'http://114.102.47.176:8089',
                    'http': 'http://117.94.117.143:9000', 'http': 'http://121.233.226.190:8089',
                    'http': 'http://117.69.230.61:8089', 'http': 'http://120.40.213.209:8089',
                    'http': 'http://117.57.97.136:8089', 'http': 'http://59.59.6.214:8089',
                    'http': 'http://111.175.81.57:8443', 'http': 'http://183.164.244.151:8089',
                    'http': 'http://47.92.155.21:8118', 'http': 'http://114.231.82.161:8089',
                    'http': 'http://117.57.112.45:8089', 'http': 'http://117.95.192.231:8089',
                    'http': 'http://117.95.199.224:8089', 'http': 'http://123.245.249.144:8089',
                    'http': 'http://114.43.118.170:3128', 'http': 'http://111.225.153.37:8089',
                    'http': 'http://222.190.208.79:8089', 'http': 'http://117.57.118.203:8089',
                    'http': 'http://114.233.70.79:9000', 'http': 'http://180.105.119.4:8089',
                    'http': 'http://114.106.134.202:8089', 'http': 'http://114.233.70.97:9000'
                    }]
        self.proxy = random.choice(proxies)
        self.url = 'https://www.kuaishou.com/graphql'

    def get_myid(self):
        data = {
            "operationName": "userInfoQuery",
            "variables": {},
            "query": "query userInfoQuery {\n  visionOwnerInfo {\n    id\n    name\n    avatar\n    eid\n    userId\n    __typename\n  }\n}\n"
        }
        response = requests.post(url=self.url, headers=self.header, json=data,proxies=self.proxy)
        data_result = response.json()
        return data_result

    def get_upid(self, userId):
        data = {
            "operationName": "visionProfile",
            "variables": {
                "userId": userId
            },
            "query": "query visionProfile($userId: String) {\n  visionProfile(userId: $userId) {\n    result\n    hostName\n    userProfile {\n      ownerCount {\n        fan\n        photo\n        follow\n        photo_public\n        __typename\n      }\n      profile {\n        gender\n        user_name\n        user_id\n        headurl\n        user_text\n        user_profile_bg_url\n        __typename\n      }\n      isFollowing\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        response = requests.post(url=self.url, headers=self.header, json=data,proxies=self.proxy)
        data_result=response.json()
        return data_result

    def get_information(self, userId, pcursor):
        data = {
            "operationName": "visionProfilePhotoList",
            "variables": {
                "userId": userId,
                "pcursor": pcursor,
                "page": "profile"
            },
            "query": "fragment photoContent on PhotoEntity {\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  __typename\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n"
        }
        response = requests.post(url=self.url, headers=self.header, json=data,proxies=self.proxy)
        data_result = response.json()
        return data_result

    def ger_comment(self, photoId, pcursor):
        data = {
            "operationName": "commentListQuery",
            "variables": {
                "photoId": photoId,
                "pcursor": pcursor
            },
            "query": "query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      authorLiked\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        authorLiked\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        response = requests.post(url=self.url, headers=self.header, json=data,proxies=self.proxy)
        # with open('message3333.txt', 'wb') as f:
        #     f.write(response.content)
        data_result = response.json()
        return data_result

    def commentout(self, data):
        visionCommentList = data['data']['visionCommentList']
        pcursor = visionCommentList['pcursor']
        commentCount = visionCommentList['commentCount']
        rootComments = visionCommentList['rootComments']
        for i in rootComments:
            authorName = i["authorName"]
            content = re.sub('[(]O3x[a-z0-9]{13}[)]', '', i['content'])
            subCommentCount = i['subCommentCount']
            likedCount = i['likedCount']
            print("昵称：{0} 评论内容：{1} 回复数：{2} 点赞数:{3}".format(authorName, content, subCommentCount, likedCount))
        return pcursor, commentCount

    # def idout(self):
    def analyzingdata(self, data):
        result=[]
        for i in range(0,3):
            data_result = []
            datas = data['data']['visionProfilePhotoList']['feeds'][i]['photo']['id']
            title=data['data']['visionProfilePhotoList']['feeds'][i]['photo']['caption']
            data_result.append(datas)
            data_result.append(title)
            result.append(data_result)
        return result


if __name__ == '__main__':
    pcursor = ''
    userId = '3xhgmexpjbmbtck'
    filename = "数据.text"
    ks = kuaishou()
    # for ph in photoId:
    #     # while pcursor!='no more':
    #     #     data = ks.ger_comment(ph,pcursor)
    #     #     pcursor,commentcount=ks.commentout(data)
    #     #     print(pcursor)

    data = ks.get_information(userId, pcursor)
    photoId = ks.analyzingdata(data)
    ist = 1
    for i in photoId:
        r = 1
        pcursors = ''
        names = []
        dicts = []
        title=i[1]
        print(i[1])
        with open(f'标题：{title}.txt', 'a', encoding='utf-8') as f:
            while pcursors != "no_more":
                result = ks.ger_comment(i[0], pcursors)
                pcursors = result['data']["visionCommentList"]['pcursor']
                data = result['data']["visionCommentList"]["rootComments"]
                for d in data:
                    name = d["authorName"]
                    names.append(name)
                    content = re.sub('[(]O3x[a-z0-9]{13}[)]', '', d['content'])
                    dicts.append(content)
                    fs = "{0}:{1}   {2}".format(name, content, r)
                    print(fs)
                    f.write(content)
                    r += 1
                time.sleep(random.randint(1,5))
            df = pd.DataFrame({'姓名': names, '评论内容': dicts})
            df.to_csv(f"标题：{title}.csv", index=False, sep=',',encoding='utf-8-sig')
    print(data)
