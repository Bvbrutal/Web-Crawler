import time
import json
import base64
import datetime
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; TECNO CD8) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.61 Mobile Safari/537.36'
}


# 学生信息存储
class StudentInfo:

    def __init__(self, openid, xh, account, passwd, location, wecom):
        self.lat = None
        self.lng = None
        self.location_title = None
        self.location_big = None
        self.location_small = None
        self.location_szdq = None
        self.location_xxdz = None
        self.gender = None
        self.name = None
        self.wecom = wecom
        self.openid = openid
        self.xh = xh
        self.account = account
        self.passwd = passwd
        self.location = location
        self.get_info()  # 获取name gender
        self.get_location()  # 获取地址详情

    # 获取学生信息
    def get_info(self):
        url = 'https://be-prod.redrock.cqupt.edu.cn/magipoke-text/search/people'
        data = {'stu': self.xh}
        response = requests.get(url, data, headers=headers)
        # print(response.json())
        name = response.json()['data'][0]['name']
        gender = response.json()['data'][0]['gender']
        self.name = name
        self.gender = gender

    # 获取地址经纬度
    def get_location(self):
        url = 'https://apis.map.qq.com/ws/geocoder/v1'
        data = {
            'address': self.location,
            'key': '7IMBZ-XWMWW-D4FR5-R3NAG-G7A7S-FMBFN'
        }
        response = requests.get(url, data, headers=headers)
        # print(response.json())
        self.location_title = response.json()['result']['title']
        from operator import itemgetter
        location_temp = response.json()['result']['address_components']
        location_szdq = itemgetter(*('province', 'city', 'district'))(location_temp)
        # 中国,重庆市,重庆市,南岸区
        self.location_big = '中国,' + ','.join(location_szdq)
        # print(self.location_big)
        # 重庆市重庆市南岸区崇文路2号
        if location_temp['street_number']:
            self.location_small = \
                ''.join(itemgetter(*('province', 'city', 'district', 'street', 'street_number'))(location_temp)) + '号'
        else:
            self.location_small = \
                ''.join(itemgetter(*('province', 'city', 'district', 'street'))(location_temp))
        # print(self.location_small)
        # 重庆市,重庆市,南岸区
        self.location_szdq = ','.join(location_szdq)
        # print(self.location_szdq)
        # 崇文路2号重庆邮电大学
        if location_temp['street_number']:
            self.location_xxdz = \
                ''.join(itemgetter(*('street', 'street_number'))(location_temp)) + '号'
        else:
            self.location_xxdz = \
                ''.join(itemgetter('street')(location_temp))
        # print(self.location_xxdz)
        self.lng = response.json()['result']['location']['lng']
        self.lat = response.json()['result']['location']['lat']


class CQUPTClockIn(StudentInfo):

    def __init__(self, openid, xh, account, passwd, location, wecom):
        super().__init__(openid, xh, account, passwd, location, wecom)
        self.mrdkkey = self.get_mrdkkey()

    # 企业微信通知
    def wecom_notification(self, text):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a9f2c44e-96a6-4b30-9a16-bfd94bd9f142'
        data = {
            'msgtype': 'text',
            'text': {
                'content': text,
                'mentioned_list': [self.wecom]
            }
        }
        requests.post(url, headers=headers, json=data)

    # 检查打卡次数判断打卡状态 0：未打卡 1：已打卡
    # 此处不检测openid
    def check_count(self):
        url = 'https://we.cqupt.edu.cn/api/mrdk/get_mrdk_flag.php'
        data = {"xh": self.xh, "openid": self.openid, "timestamp": round(time.time())}
        data = self.data_process(data)
        response = requests.post(url, data, headers=headers)

        return int(response.json()['data']['count'])

    # 获得mrdkkey
    @staticmethod
    def get_mrdkkey():
        day = ["s9ZS", "jQkB", "RuQM", "O0_L", "Buxf", "LepV", "Ec6w", "zPLD", "eZry", "QjBF", "XPB0", "zlTr", "YDr2",
               "Mfdu",
               "HSoi", "frhT", "GOdB", "AEN0", "zX0T", "wJg1", "fCmn", "SM3z", "2U5I", "LI3u", "3rAY", "aoa4", "Jf9u",
               "M69T",
               "XCea", "63gc", "6_Kf", "s9ZS"]
        hour = ["89KC", "pzTS", "wgte", "29_3", "GpdG", "FDYl", "vsE9", "SPJk", "_buC", "GPHN", "OKax", "_Kk4", "hYxa",
                "1BC5",
                "oBk_", "JgUW", "0CPR", "jlEh", "gBGg", "frS6", "4ads", "Iwfk", "TCgR", "wbjP"]

        now_day = datetime.datetime.now().day
        now_hour = datetime.datetime.now().hour

        return day[now_day] + hour[now_hour]

    # 处理post数据成key value字典格式
    @staticmethod
    def data_process(_data):
        _json_data = json.dumps(_data)
        _bytes_data = _json_data.encode('utf-8')
        _bs64_data = base64.b64encode(_bytes_data).decode('utf8')
        _data_dict = {
            'key': _bs64_data
        }
        _data_json = json.dumps(_data_dict)

        return _data_json

    # 打卡主程序
    def clock_in(self):
        url = 'https://we.cqupt.edu.cn/api/mrdk/post_mrdk_info.php'
        data = {'name': self.name, 'xh': self.xh, 'xb': self.gender, 'openid': self.openid,
                'locationBig': f'{self.location_big}', 'locationSmall': f'{self.location_small}',
                'latitude': self.lat, 'longitude': self.lng,
                'szdq': f'{self.location_szdq}', 'xxdz': f'{self.location_xxdz}', 'ywjcqzbl': '低风险',
                'ywjchblj': '无', 'xjzdywqzbl': '无', 'twsfzc': '是', 'ywytdzz': '无', 'jkmresult': '绿色',
                'beizhu': '无', 'mrdkkey': self.mrdkkey, 'timestamp': round(time.time())}
        data = self.data_process(data)
        response = requests.post(url, data, headers=headers)

        return response.json()['status']

    def main_process(self):
        # 检查openid是否绑定
        # self.check_bind()
        # 检查打卡状态 0：未打卡 1：已打卡
        if self.check_count():
            print('您已打卡！')
            print(f'\n定位地点：{self.location_szdq}{self.location_xxdz}\n意愿地点：{self.location}'.replace(',', ''))
            # self.wecom_notification(f'We重邮：您已打卡！\n\n定位地点：{self.location_title}\n意愿地点：{self.location}')
        else:
            # 进入打卡流程
            print('开始打卡......')
            if self.clock_in() == 200:
                print('打卡成功！')
                self.wecom_notification(f'We重邮：打卡成功！\n\n定位地点：{self.location_big}\n意愿地点：{self.location}')
                self.check_count()
            else:
                print('Error')
                self.wecom_notification(f'We重邮：打卡失败，请检查！\n\n定位地点：{self.location_big}\n意愿地点：{self.location}')


if __name__ == '__main__':
    # 填写openid 学号 统一认证码 密码 意愿打卡地址 企业微信用户名
    info = ('oIaII0WB-9ZWa1ZxPyeC0W5YyUB0', '2020212118', '1668238', '4639.psh', '重庆市重庆市合川区龙市镇', 'PengSongHuan')
    yuesir = CQUPTClockIn(*info)
    yuesir.main_process()