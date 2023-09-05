import re
import time
import requests
from numpy import random


class kuaishou():
    def __init__(self):
        self.url = "https://www.kuaishou.com/graphql"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57",
            "Cookie": "did=web_dd1895ad8c492c8e0e8ccdfca79472a3; didv=1677668522826; kpf=PC_WEB; clientid=3; userId=2939205029; kpn=KUAISHOU_VISION; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABljEn7CSTFF3bZTKeU_lBp9j0z-RGoJRPpGaWOid7hl4adq91slCkWbVDfZOgIhlShUIY4J8OJkQBlvec8wvCFZ7A3nis7FuO0dTToJaPMF8I_HtPyL2Bztc3_osSKsArkIMTh_up01I_POmPm73YgHD3ACXXFiDlwgsMZ54CfdvxFduRGGWw6GaNgA6otd0Q2Cr4AQR_kyasIa4AFyr82BoS5Uf6LooXNTrpm4StA9DDXaoVIiB2m8TSA5T7OPJdJajwHu-G-VNKdRm3y6QQzVOCc0qmsCgFMAE; kuaishou.server.web_ph=2c254ff4c915e00b97534f63bd0a97db6e49", }

    def get_information(self, userId):
        datas = {}
        json = {
            "operationName": "visionProfile",
            "variables": {
                "userId": userId
            },
            "query": "query visionProfile($userId: String) {\n  visionProfile(userId: $userId) {\n    result\n    hostName\n    userProfile {\n      ownerCount {\n        fan\n        photo\n        follow\n        photo_public\n        __typename\n      }\n      profile {\n        gender\n        user_name\n        user_id\n        headurl\n        user_text\n        user_profile_bg_url\n        __typename\n      }\n      isFollowing\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        response = requests.post(url=self.url, headers=self.header, json=json)
        data = response.json()['data']['visionProfile']['userProfile']
        fan = data['ownerCount']['fan']
        datas['fan'] = fan
        follow = data['ownerCount']['follow']
        datas['follow'] = follow
        photo_public = data['ownerCount']['photo_public']
        datas['photo_public'] = photo_public
        user_name = data['profile']['user_name']
        datas['user_name'] = user_name
        user_id = data['profile']['user_id']
        datas['user_id'] = user_id
        user_text = data['profile']['user_text']
        datas['user_text'] = user_text
        return datas

    def get_vide(self, userId):
        datas = {}
        json = {
            "operationName": "visionProfilePhotoList",
            "variables": {
                "userId": userId,
                "pcursor": "",
                "page": "profile"
            },
            "query": "fragment photoContent on PhotoEntity {\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  __typename\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n"
        }
        response = requests.post(url=self.url, headers=self.header, json=json)
        for i in range(3):
            data = response.json()['data']["visionProfilePhotoList"]["feeds"][i]["photo"]
            caption = data["caption"]
            datas[f'caption{i}'] = caption
            likeCount = data["likeCount"]
            datas[f'likeCount{i}'] = likeCount
            viewCount = data["viewCount"]
            datas[f'viewCount{i}'] = viewCount
            realLikeCount = data["realLikeCount"]
            datas[f'realLikeCount{i}'] = realLikeCount
            photoUrl = data["photoUrl"]
            datas[f'photoUrl{i}'] = photoUrl
            id = data['id']
            datas[f'id{i}'] = id
        return datas

    def get_comment(self, photoId, pcursor):
        dict = []
        json = {
            "operationName": "commentListQuery",
            "variables": {
                "photoId": photoId,
                "pcursor": pcursor
            },
            "query": "query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      authorLiked\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        authorLiked\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        response = requests.post(url=self.url, headers=self.header, json=json)
        pcursor = response.json()['data']["visionCommentList"]['pcursor']
        data = response.json()['data']["visionCommentList"]["rootComments"]
        for d in data:
            name = d["authorName"]
            content = re.sub('[(]O3x[a-z0-9]{13}[)]', '', d['content'])
            dict.append(name)
            dict.append(content)
            f = "{0}:{1}".format(name, content)
            print(f)
        return pcursor, dict


if __name__ == '__main__':
    kua = kuaishou()
    inf = kua.get_vide("3xwrbnfsfzpq83k")
    photoId = inf['id1']
    pcursor = ''
    with open('message3333.txt', 'w', encoding='utf-8') as f:
        while pcursor != "no_more":
            pcursor,dict = kua.get_comment(photoId, pcursor)
            f.write(str(dict))
