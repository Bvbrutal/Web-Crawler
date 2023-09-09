# -*- coding: UTF-8 -*-
import codecs

import requests
import json
import time
import re
mcn_url = "https://xd.newrank.cn/xdnphb/nr/cloud/douyin/accountSearch?xyz=5b656c1bfdad2f2b81ee1c7b7ee8d7a1&nonce=93756e082"
headers = {
            "cookie": "tt_token=true; token=B84BC70398524281A23B32907A923FA3; Hm_lvt_a19fd7224d30e3c8a6558dcb38c4beed=1600998811; UM_distinctid=174c2f7269d8e-018b82af719c7a-5d462912-144000-174c2f7269e2c0; __root_domain_v=.newrank.cn; _qddaz=QD.5qt4ff.423qqb.kfhld1hh; Hm_lvt_e20c9ff085f402c8cfc53a441378ca86=1601003995; Hm_lpvt_e20c9ff085f402c8cfc53a441378ca86=1601003995; _uab_collina=160100400201237841270221; Hm_lpvt_a19fd7224d30e3c8a6558dcb38c4beed=1601176471; tt_token=true",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        }

def create_mcn_body():
    """构建mcn机构请求体"""
    data = {"input": {"keyword": "Mr_nuannan", "type": ""}, "xd_tags": [], "type": "", "nr_range_list": [], "verify": "",
            "contact": "", "mcn": "", "with_fusion_shop_entry": "", "is_live": "",
            "account_info": {"province": "", "city": "", "gender": "",
                             "constellation_name": "", "age_range": ""},
            "data_performance": {"favorited_range_list": [], "follower_range_list": []},
            "relate_goods": {"goods_name": "", "goods_cate1": "", "goods_cate2": "", "price_range": "",
                             "goods_sales_range": "", "visitor_count_range": "", "goods_source": "",
                             "price": {"gte": "", "lt": ""}},
            "fans_info": {"province": "", "city": "", "gender": "", "age_range": "", "constellation_name": ""},
            "sort": "", "size": 20, "start": 1}
    return data

def get_response(url, headers, body):
    time.sleep(5)
    """获取响应"""
    ret = requests.post(url,
                        headers=headers,
                        json=body
                        )
    return ret.text

def get_mcn( page):
        """获取机构信息"""
        data = create_mcn_body(page)
        result = get_response(mcn_url, headers, data)
        response = json.loads(result)
        data = response.get('data')
        mcn_list = data.get('list')
        return mcn_list

def get_video(uid,page):
    data = create_mcn_body(page)
    result = get_response(mcn_url, headers, data)
    response = json.loads(result)


def parse_mcn(mcn_element):
        """解析mcn机构"""
        mcn_item =dict()
        mcn_item['uid'] = mcn_element.get('uid')
        mcn_item['account'] = mcn_element.get('account')
        mcn_item['nickname'] = re.sub("<[^>]*>", "", mcn_element.get('nickname'))
        mcn_item['signature'] = mcn_element.get('signature').replace('\n', '').replace('\r', '')
        mcn_item['follower_count'] = mcn_element.get('follower_count')
        mcn_item['aweme_count'] = mcn_element.get('aweme_count')
        return mcn_item

def userMsg():
        mcn_list = get_mcn(1)
        print(mcn_list)
        # 当前页机构 list
        user_list=[]
        for mcn in mcn_list:
            mcn_item = parse_mcn(mcn)
            user_list.append(mcn_item)
        return user_list

def videoMsg():
    video_list=get_video()


if __name__ == '__main__':
    f = codecs.open('./dy/userMsg.txt', "a", 'utf-8')
    user_list=userMsg()
    for user in user_list:
        print(user)
        f.write(user.get("uid") + "|"+ user.get("account") + "|"+user.get("nickname") + "|"+user.get("signature") + "|"+user.get("follower_count") + "|"+user.get("aweme_count") + "|" +'\r\n')


import codecs
import http

import requests
import json
import time
import re
detail_url="https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/detail/aweme"

headers2 = {
            "cookie": "vtoken=1;token=890CBCEEF50E43D7AB241F0BE3E892F7",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        }


def create_aweme_body():
    data={"uid":"110563717491","sort":"create_time"}
    return data


def get_aweme_response(detailurl, headers, body):
    time.sleep(5)
    """获取响应"""
    ret = requests.post(detailurl,
                        headers=headers,
                        json=body
                        )
    return ret.text


def get_aweme( ):
        """获取视频信息"""
        data = create_aweme_body()
        result = get_aweme_response(detail_url, headers2, data)
        response = json.loads(result)
        print(response)
        data = response.get('data')
        mcn_list = data.get('list')
        return mcn_list

def parse_mcn(mcn_element):
        """解析mcn机构"""
        mcn_item =dict()
        mcn_item['uid'] = mcn_element.get('uid')
        mcn_item['account'] = mcn_element.get('account')
        mcn_item['nickname'] = re.sub("<[^>]*>", "", mcn_element.get('nickname'))
        mcn_item['signature'] = mcn_element.get('signature').replace('\n', '').replace('\r', '')
        mcn_item['follower_count'] = mcn_element.get('follower_count')
        mcn_item['aweme_count'] = mcn_element.get('aweme_count')
        return mcn_item

def parse_aweme(aweme_element):
    """解析mcn机构"""
    aweme_item = dict()
    aweme_item['aweme_id'] = aweme_element.get('aweme_id')
    aweme_item['aweme_desc'] = aweme_element.get('aweme_desc')
    aweme_item['comment_count'] = re.sub("<[^>]*>", "", aweme_element.get('comment_count'))
    aweme_item['digg_count'] = aweme_element.get('digg_count').replace('\n', '').replace('\r', '')
    aweme_item['create_time'] = aweme_element.get('create_time')
    aweme_item['share_url'] = aweme_element.get('share_url')
    return aweme_item

def parse_detail(aweme_element):
        """解析mcn机构"""
        detail_item = dict()
        detail_item['aweme_id'] = aweme_element.get('aweme_id')
        detail_item['play_addr'] = aweme_element.get('video').get('play_addr').get('url_list')[0]
        detail_item['desc'] =aweme_element.get('desc')
        detail_item['author_user_id'] = aweme_element.get('author_user_id')
        return detail_item


def awemeListMsg():
        aweme_list = get_aweme(1)
        # print(aweme_list)
        # 当前页机构 list
        user_list=[]
        for aweme in aweme_list:
            aweme_item = parse_aweme(aweme)
            user_list.append(aweme_item)
        return user_list

# 发送给aria2开始下载
def SendDownloadInfo(id, url, referer, savePath,vname):
    jsonreq = json.dumps({"jsonrpc": "2.0", "id": id, "method": "aria2.addUri",
                          "params": [[url], {"referer": referer, "dir": savePath,"out":vname}]})
    resp = requests.post("http://localhost:6800/jsonrpc", data=jsonreq)
    print(jsonreq)
    if resp.status_code == 200:
        return True
    return False

if __name__ == '__main__':

    f = codecs.open('./dy/awemeMsg.txt', "a", 'utf-8')
    aweme_list=awemeListMsg()
    for aweme in aweme_list:
        url="https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids="+aweme.get("aweme_id")
        response = requests.get(url=url)
        detailmsg= dict()
        if response.status_code >= 200 and response.status_code < 300:
            data = response.json()
            print(data)
            detail_list = data['item_list']
            for detail in detail_list:
                detailmsg=parse_detail(detail)
                print(detailmsg.get("play_addr"))
                SendDownloadInfo(detailmsg.get("aweme_id"), detailmsg.get("play_addr"), 'https://www.iesdouyin.com', './dy',detailmsg.get("aweme_id")+'.mp4')
        f.write(aweme.get("aweme_id") + "|"+ aweme.get("aweme_desc") + "|"+aweme.get("comment_count") + "|"+aweme.get("digg_count") + "|"+aweme.get("create_time") + "|"+aweme.get("share_url") + "|" +'\r\n')