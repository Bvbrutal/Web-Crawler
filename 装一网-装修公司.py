import requests

url = 'https://cq.zhuangyi.com/zsgs/pn-2/'

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'ASP.NET_SessionId=qzy5zjpn4dige1l01sesnugl; ZYW_Home=cq; ZYW_HomeName=%e9%87%8d%e5%ba%86; route=480c78b420084f73716b746bf39ccea4; ZYW_UUID=16935520200376914413; __root_domain_v=.zhuangyi.com; _qddaz=QD.761793552020456; _qdda=3-1.1; _qddab=3-lzrwto.lm095a8h; ASP.NET_SessionId=cv5apbarsulspkcuhsnay4aj; ZYW_M0_City=nSL1TEg7H7FuDIs2T4idN5B5jb+etFcZpAeMyxRRlgo=; zyw_user_info=0',
    'Host': 'cq.zhuangyi.com',
    'Referer': 'https://cq.zhuangyi.com/zsgs/pn-2/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',

}

xpath = '//*[@id="aspnetForm"]/div[6]/div[3]/div[1]/ul/li[1]/span[2]/p[3]/i[1]'

response=requests.get(url,header)
print(response.text)