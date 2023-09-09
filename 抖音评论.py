# -*- coding: UTF-8 -*-
import requests

mistoken = ''
url = "https://www.douyin.com/aweme/v1/web/comment/list/"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Host': 'www.douyin.com',
    'cookie': 's_v_web_id=verify_llnh9hxk_6K0kuOeN_1Mnq_4RgC_BXUt_vriiv6ADFRVd; ttwid=1%7Cz5FA4JclgTonQjvduobRYhWfhF6mKiouNfrjX7AaLCc%7C1692779601%7C7258a1a68b1e424d2c855c5f6ad40e805589e847f34e9666f27b0c124d84b474; passport_csrf_token=716ed7f47d87ac2b7d92a50e54b5ab2e; passport_csrf_token_default=716ed7f47d87ac2b7d92a50e54b5ab2e; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRFlkMGFQeTNSREM0aU5Hei90dW9qcUdPRHl5ejJydjRMSm5HQnh5VDUxWmJhUTJVWkZibzMxckdFRmlGS3doeFVEenQ1eWlWNzlaWHFIaWpyMms1dUU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ==; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; strategyABtestKey=%221694229509.97%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; ttcid=30122cb695ef44c1a59b198bfcba3fdc23; tt_scid=IFxbh6Mji.VPIo7.SgU92TlDs7aTgBOn0xaOJrd8.CgFDZGWnEowUS.LR8LVg6O9ea0e; csrf_session_id=6255493ed280535128010cbbfea44032; download_guide=%221%2F20230909%2F0%22; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1694834472832%2C%22type%22%3A1%7D; home_can_add_dy_2_desktop=%221%22; msToken=anhReIysiYSmO9PG7Y0wL3oWO15QsWyp8FyraLlLu6E62HBE0yU7VWb7ZujsqVsSgkbp0Z88gNFImYxi7Eov847FpO6njGwKyWsLwGgWFVVKoxMvpNzau0ZJZN4=; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; msToken=iW4MXft7e_6aS4CtGMnLr7WU_Tcp8U-dmKtw7bXNmKDM-z8ikb-Z2Xdtx_MJ9l84TUUQUbHh7DtwuyxBfnsV-UtEjoCczBwP0PtIWyQdOX3Dsov9FFeLiEr59fA=',

}
data = {
    'aweme_id': '7273459778611924280',
    'count': '20',
    'msToken': 'iW4MXft7e_6aS4CtGMnLr7WU_Tcp8U-dmKtw7bXNmKDM-z8ikb-Z2Xdtx_MJ9l84TUUQUbHh7DtwuyxBfnsV-UtEjoCczBwP0PtIWyQdOX3Dsov9FFeLiEr59fA=',
    'X-Bogus': 'DFSzswVudZUANcTOtySEJM9WX7rr',

}
result = requests.get(url, headers=header, params=data).text
print(result.encode('utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
