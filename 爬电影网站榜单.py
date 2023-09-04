import requests
import re
import prettytable as pd
import csv



for i in range(10):
    url = 'https://movie.douban.com/top250?start='+str(25*i)+'&filter=' # 评分排行榜的网址
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36'
    }# 修饰请求头

    response = requests.get(url, headers=headers) #发送请求 获取网站数据

    result = response.text

    p = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp;'
                   r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                   r'.*?<span>(?P<num>.*?)</span>', re.S)
    # 格式化输出
    table = pd.PrettyTable()
    # 设置表头
    table.field_names = ['电影名', '年份', '评分', '评分人数']
    for it in p.finditer(result):
        # 添加表数据
        table.add_row([it.group('name'), it.group('year').strip(), it.group('score'), it.group('num')])
    print(table)
    # 以追加的形式打开文件
    f = open('../../爬微博/data.csv', mode='a')
    csv_write = csv.writer(f)
    for it in p.finditer(result):
        # 将迭代器it转换为字典
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csv_write.writerow(dic.values())
    print('写入完成')

