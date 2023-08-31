import pandas as pd

import requests
import time
timestamp=int(time.time()*1000)

keyword1='比亚迪'
url1 = f'https://dyapi.huitun.com/search/user?_t={timestamp}&from=1&userType=&sortField=follower_count_total&sortMod=desc&keyword={keyword1}&cids=&contentTag=&cat0=&cat1=&gmvRange=&gmvRangeAvg=&userRangeAvg=&gpmRangeAvg=&priceRange=&dsrRange=&scoreRange=&followerRange=&diggRange=&incFans=&isOpenWindow=&isEarnest=&company=&customVerify=&gender=&ageRange=&province=&region=&fansGroup=&hasMcn=&contactWay=&isLive=&maxGender=&maxAge=&maxArea=&maxCity=&maxCg=&maxCl=&tag=0&tryIt=&liveGmv=&type='
header1 = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '__root_domain_v=.huitun.com; _qddaz=QD.976189066613776; _clck=1b6lyj5|2|fdn|0|1287; SESSION=YzlhNDcwYTctMTY4Ny00OGIzLWIwYmItYTJjMWNlNjQ3MTc4; _clsk=f50wdy|1690458132036|8|1|k.clarity.ms/collect',
    'Host': 'dyapi.huitun.com',
    'Origin': 'https://dy.huitun.com',
    'Pragma': 'no-cache',
    'Referer': 'https://dy.huitun.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
response1 = requests.get(url1, headers=header1)
result1 = response1.json()
list2=[]
for data in result1['data']:
    nickname=data['nickname']
    authorId=data['authorId']
    uid=data['uid']
    followerCountTotal=data['followerCountTotal']
    list3=[uid,authorId,nickname,followerCountTotal]
    print(authorId)
    list2.append(list3)

print(list2)
list=[]
for i in range(len(list2)):
    uid=list2[i][0]
    nickname=list2[i][1]
    followerCountTotal=list2[i][2]
    url = f'https://dyapi.huitun.com/live/v2/record?_t={timestamp}&from=1&time=&has=&keyword=&mod=DESC&sort=&start=2023-04-29&end=2023-07-27&filterMap=&uid={uid}&example='
    header = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '__root_domain_v=.huitun.com; _qddaz=QD.976189066613776; _clck=1b6lyj5|2|fdn|0|1287; SESSION=YzlhNDcwYTctMTY4Ny00OGIzLWIwYmItYTJjMWNlNjQ3MTc4; _clsk=f50wdy|1690458132036|8|1|k.clarity.ms/collect',
        'Host': 'dyapi.huitun.com',
        'Origin': 'https://dy.huitun.com',
        'Pragma': 'no-cache',
        'Referer': 'https://dy.huitun.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(url, headers=header)
    result=response.json()
    for data in result['data']:
        title=data['title']
        livetime=data['liveTime']
        digg=data['digg']
        totalUser=data['totalUser']
        userNum=data['userNum']
        roomid=data['roomId']
        startLive=data['startLive']
        list1=[nickname,followerCountTotal,roomid,title,startLive,livetime,totalUser,userNum,digg]
        list.append(list1)
        print('直播id：{:<}'.format(roomid))

df = pd.DataFrame(list2)
df.to_csv('static/data1.csv', mode='a', index=False, header=False, encoding='utf-8-sig')
