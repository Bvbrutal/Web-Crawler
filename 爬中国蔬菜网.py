import pandas as pd
import requests
from lxml import etree


class Response:  # 定义类Respone
    def __init__(self, url, data=None):
        self.url = url
        self.data = data
        self.headers = {  # 模拟电脑访问
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    def requests_req(self):  # post请求
        if self.data:
            response = requests.post(url=self.url, headers=self.headers, data=self.data)
            response.encoding = 'utf-8'
            return response
        else:
            response = requests.get(url=self.url, headers=self.headers)
            response.encoding = 'utf-8'
            return response

    def analy(self):  # 通过lxml库中的etree.HTML来解析这个网页的结构
        html = etree.HTML(self.requests_req().text)
        return html

    def par_data(self):
        Data = []
        info = self.analy().xpath('//div[@class="pri_k"]/p')
        for i in info:
            # 根据xpath爬取数据
            date = i.xpath('./span[1]/text()')[0][1:][:-1]  # 日期
            varity = i.xpath('./span[2]/text()')[0]  # 蔬菜种类
            market = i.xpath('./span[3]/a/text()')[0]  # 批发市场
            price_min = i.xpath('./span[4]/text()')[0][1:]  # 最低价格
            price_max = i.xpath('./span[5]/text()')[0][1:]  # 最高价格
            price_average = i.xpath('./span[6]/text()')[0][1:]  # 平均价格
            unit = i.xpath('./span[7]/text()')[0]  # 计量单位
            date = pd.to_datetime(date)  # 转换时间类型
            datas = [date, varity, market, price_min, price_max, price_average, unit]
            print(datas)
            Data.append(datas)
        return Data

    def save_data(self):  # 保存为csv文件
        dataframe = pd.DataFrame(self.par_data())
        dataframe.to_csv('data.csv', encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)


if __name__ == '__main__':
    # 输入爬取页数
    pages = int(input('请输入想要爬取多少页数据\n'))
    # 设置表头名字
    header = [['日期', '品种', '批发市场', '最低价格', '最高价格', '平均价格', '计量单位']]
    header = pd.DataFrame(header)
    header.to_csv('data.csv', encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)
    # 循环爬取网页数据
    for page in range(1, pages):
        url = 'http://www.vegnet.com.cn/Price/List_ar500000_p' + str(page) + '.html?marketID=0'  # 网页地址
        response = Response(url)  # 实例
        response.save_data()
