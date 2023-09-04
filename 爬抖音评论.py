import requests
import json
import pandas
from numpy import random

url = 'https://www.douyin.com/aweme/v1/web/comment/list'

header = {
    'authority': 'www.douyin.com',
    'method': 'GET',
    'path': '/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7092308044108827940&cursor=0&count=20&item_type=0&insert_ids=&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=110.0.1587.57&browser_online=true&engine_name=Blink&engine_version=110.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7204858005379991043&msToken=v6YVp4xPaZJTwn8FSNEiS8lQJdIcQ0XsudNB17exHNtF8KfYYEWnNuuQHTxRGBN0rOYoI9h64rghttDlaHPDZyKI62cAd7sqXVdUcLW8sZ8H0C4xnEtW1IsBaJa5Pg==&X-Bogus=DFSzswVuc7iAN985SgPqL2oB6lB0',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bd-ticket-guard-client-cert': 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUNGRENDQWJxZ0F3SUJBZ0lVRG1aMjNGS2hpQVBtaGh6MEYwZ0JrVjEyazlVd0NnWUlLb1pJemowRUF3SXcKTVRFTE1Ba0dBMVVFQmhNQ1EwNHhJakFnQmdOVkJBTU1HWFJwWTJ0bGRGOW5kV0Z5WkY5allWOWxZMlJ6WVY4eQpOVFl3SGhjTk1qTXdNakk0TVRNMU5qSTFXaGNOTXpNd01qSTRNakUxTmpJMVdqQW5NUXN3Q1FZRFZRUUdFd0pEClRqRVlNQllHQTFVRUF3d1BZbVJmZEdsamEyVjBYMmQxWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMEQKQVFjRFFnQUVReTUrY0V6SEs4WVhoUTNYUWNBTm1wejNMQmpvVHlaczU2MEZXc3IzQ0F1bjU1amJ4ajFlRUF4NApHV0RYZjRSdmpSRVU0Mmova1R0UFU2akFQanlsc2FPQnVUQ0J0akFPQmdOVkhROEJBZjhFQkFNQ0JhQXdNUVlEClZSMGxCQ293S0FZSUt3WUJCUVVIQXdFR0NDc0dBUVVGQndNQ0JnZ3JCZ0VGQlFjREF3WUlLd1lCQlFVSEF3UXcKS1FZRFZSME9CQ0lFSUl5VXI2aFlIWnkxamFsUGQ3OEN5ZzNkREcvd01nS0xLeVIweFpWQTZqRzdNQ3NHQTFVZApJd1FrTUNLQUlES2xaK3FPWkVnU2pjeE9UVUI3Y3hTYlIyMVRlcVRSZ05kNWxKZDdJa2VETUJrR0ExVWRFUVFTCk1CQ0NEbmQzZHk1a2IzVjVhVzR1WTI5dE1Bb0dDQ3FHU000OUJBTUNBMGdBTUVVQ0lRQ3dwMG1RQjN0TDNET2kKV3UrdFQ4Um0xWE1ZaWpmaVJxdEJOV2dEelc1SXFnSWdPN3o1Q0lnVmJhWG9qODZHMGtoVXRQNjk3djl3MlFvZwpEQ1J2bFFOVElCTT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=',
    'bd-ticket-guard-client-data': 'eyJ0c19zaWduIjoiY29tcHJlc3NjS3dCMlF6Q01PeFB3cTVLTFdRWUFzUzlaOHdGN24xcnRxY1YzUWtmNXZFPSIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJNRVVDSUVnMld0bzlSUk1NdHlhRlE3SGU1YmVOM1RLZ0V5ZDJaY2dFQ1UyQnBGZHNBaUVBOHk4Z3Z5QXFoeDIwWW12M3plS0M1d2hlSjFNQ0t3anNWT1cyRTZrK3N5OD0iLCJ0aW1lc3RhbXAiOjE2Nzc1OTk3NDJ9',
    'bd-ticket-guard-version': '2',
    'cache-control': 'no-cache',
    'cookie': 'ttwid=1%7CgixaC3yU9l67dHatS6V96DnA3rt5Ov01aEcdIrDCiBQ%7C1677511742%7C88d20e238aeb0257469035767f01e21437a4977dc876c2bcc6d5087ced788e2f; passport_csrf_token=11de526d623d7bbab30bd6fa9abeaf43; passport_csrf_token_default=11de526d623d7bbab30bd6fa9abeaf43; s_v_web_id=verify_lemz6hpd_aB4Ara2m_JXhD_4WXw_9fMf_IotIG2lO0V9m; ttcid=47f7f034a1a74433823f11450d7b297330; strategyABtestKey=%221677515833.98%22; douyin.com; download_guide=%223%2F20230228%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1678197077638%2C%22type%22%3A1%7D; csrf_session_id=ccd363a103ccf133a24f97ee6c5a5280; SEARCH_RESULT_LIST_TYPE=%22single%22; n_mh=b94wPh-8Mw4j9LkdItIRstuPSSIYHiKQ-LGS2t-Syn8; sso_uid_tt=0c98599c6f1d556d24889d64c8666e62; sso_uid_tt_ss=0c98599c6f1d556d24889d64c8666e62; toutiao_sso_user=0024346fe7535304641b09e6531949e3; toutiao_sso_user_ss=0024346fe7535304641b09e6531949e3; passport_auth_status=95b1e9bbe0448617696eb450a8f2bd98%2C; passport_auth_status_ss=95b1e9bbe0448617696eb450a8f2bd98%2C; uid_tt=2647c695ae8168ca4799b2f7e244c63e; uid_tt_ss=2647c695ae8168ca4799b2f7e244c63e; sid_tt=c89d7220b1a8430d470bcc88c7f3f78b; sessionid=c89d7220b1a8430d470bcc88c7f3f78b; sessionid_ss=c89d7220b1a8430d470bcc88c7f3f78b; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWNsaWVudC1jZXJ0IjoiLS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tXG5NSUlDRkRDQ0FicWdBd0lCQWdJVURtWjIzRktoaUFQbWhoejBGMGdCa1YxMms5VXdDZ1lJS29aSXpqMEVBd0l3XG5NVEVMTUFrR0ExVUVCaE1DUTA0eElqQWdCZ05WQkFNTUdYUnBZMnRsZEY5bmRXRnlaRjlqWVY5bFkyUnpZVjh5XG5OVFl3SGhjTk1qTXdNakk0TVRNMU5qSTFXaGNOTXpNd01qSTRNakUxTmpJMVdqQW5NUXN3Q1FZRFZRUUdFd0pEXG5UakVZTUJZR0ExVUVBd3dQWW1SZmRHbGphMlYwWDJkMVlYSmtNRmt3RXdZSEtvWkl6ajBDQVFZSUtvWkl6ajBEXG5BUWNEUWdBRVF5NStjRXpISzhZWGhRM1hRY0FObXB6M0xCam9UeVpzNTYwRldzcjNDQXVuNTVqYnhqMWVFQXg0XG5HV0RYZjRSdmpSRVU0Mmova1R0UFU2akFQanlsc2FPQnVUQ0J0akFPQmdOVkhROEJBZjhFQkFNQ0JhQXdNUVlEXG5WUjBsQkNvd0tBWUlLd1lCQlFVSEF3RUdDQ3NHQVFVRkJ3TUNCZ2dyQmdFRkJRY0RBd1lJS3dZQkJRVUhBd1F3XG5LUVlEVlIwT0JDSUVJSXlVcjZoWUhaeTFqYWxQZDc4Q3lnM2RERy93TWdLTEt5UjB4WlZBNmpHN01Dc0dBMVVkXG5Jd1FrTUNLQUlES2xaK3FPWkVnU2pjeE9UVUI3Y3hTYlIyMVRlcVRSZ05kNWxKZDdJa2VETUJrR0ExVWRFUVFTXG5NQkNDRG5kM2R5NWtiM1Y1YVc0dVkyOXRNQW9HQ0NxR1NNNDlCQU1DQTBnQU1FVUNJUUN3cDBtUUIzdEwzRE9pXG5XdSt0VDhSbTFYTVlpamZpUnF0Qk5XZ0R6VzVJcWdJZ083ejVDSWdWYmFYb2o4Nkcwa2hVdFA2OTd2OXcyUW9nXG5EQ1J2bFFOVElCTT1cbi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS1cbiJ9; bd_ticket_guard_server_data=; odin_tt=f45f1556e7839c2dda6ddd25db7e767f8b55a059f5e6b820b950492d74a35caed012df9b466181258cfed3ee46b1281afcb14b32e3bd62aed282853adde1ca48; passport_assist_user=CkGltMjXBXRrhqxPGmJkCzBTW45nF-VT-T_a18Av4n4kHGGnvfUEKeg3svtb0muPKlgOSHwRcCM4_spwUmsCmfFr3RpICjxTfxjPgTm1Xr9eKXWY6nFCDZGIBYnVUqw-HtSTlQrHqfhmbnq0UtpNuOCiEVuhQu50v3HiigtEomNXz30QlsKqDRiJr9ZUIgEDsiOCJw%3D%3D; sid_ucp_sso_v1=1.0.0-KDY3OGY5NDBjMzVkNzIyZTM5ZDM3YmQ4N2QxNzM3ZTFkODliNDQ2MTMKHwjHuLC2oYyABhCJkPifBhjvMSAMMO3ylIEGOAZA9AcaAmxxIiAwMDI0MzQ2ZmU3NTM1MzA0NjQxYjA5ZTY1MzE5NDllMw; ssid_ucp_sso_v1=1.0.0-KDY3OGY5NDBjMzVkNzIyZTM5ZDM3YmQ4N2QxNzM3ZTFkODliNDQ2MTMKHwjHuLC2oYyABhCJkPifBhjvMSAMMO3ylIEGOAZA9AcaAmxxIiAwMDI0MzQ2ZmU3NTM1MzA0NjQxYjA5ZTY1MzE5NDllMw; LOGIN_STATUS=1; store-region=cn-cq; store-region-src=uid; sid_guard=c89d7220b1a8430d470bcc88c7f3f78b%7C1677592587%7C5183996%7CSat%2C+29-Apr-2023+13%3A56%3A23+GMT; sid_ucp_v1=1.0.0-KDkyNWRkZTViNmMyNjNlN2FiNDE0NWQ3NTg2MGJmOWMzZGQ4NDU0NGQKGwjHuLC2oYyABhCLkPifBhjvMSAMOAZA9AdIBBoCbHEiIGM4OWQ3MjIwYjFhODQzMGQ0NzBiY2M4OGM3ZjNmNzhi; ssid_ucp_v1=1.0.0-KDkyNWRkZTViNmMyNjNlN2FiNDE0NWQ3NTg2MGJmOWMzZGQ4NDU0NGQKGwjHuLC2oYyABhCLkPifBhjvMSAMOAZA9AdIBBoCbHEiIGM4OWQ3MjIwYjFhODQzMGQ0NzBiY2M4OGM3ZjNmNzhi; tt_scid=X1V42USuZSY25EJN0G3ZSJT.Tj-fvQZpAuLpiyYtpum8RfCnccLkgl0zTWljrVIz4d9e; __ac_nonce=063fe23f8003c5d80d39f; __ac_signature=_02B4Z6wo00f01sYSJ7wAAIDD1kzChez9bOLGMiMAANKHI6CAIPtVUljIjRNIhgXI9esCGRt8x2VlCd1JAXr4Dd6xsuyQ6HbA7SSHEf5xvN3GOvKAEXxyTuddaK2mwsrq.2FCt94rBHOcBLRM5b; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAQva6SZKe65yJDAea3O3rGNBvhw2rGNqfUcL6A8HQE1i2zGZPNm1uJGVaaNtMCJ4D%2F1677600000000%2F0%2F0%2F1677600339062%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAQva6SZKe65yJDAea3O3rGNBvhw2rGNqfUcL6A8HQE1i2zGZPNm1uJGVaaNtMCJ4D%2F1677600000000%2F0%2F1677599739063%2F0%22; msToken=jtjNh0nS5oqEgeGA1XsmQJnGNKQ8Nn3yUgQX3-LNIB-vt-ROlQ33lfq-JXfbQcUNpqhZdhFWrL6qP9LqRvZOUO8YYsrSSjU-rML7kE8SYzZP_3t1jgyT4KARVicxzg==; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; msToken=v6YVp4xPaZJTwn8FSNEiS8lQJdIcQ0XsudNB17exHNtF8KfYYEWnNuuQHTxRGBN0rOYoI9h64rghttDlaHPDZyKI62cAd7sqXVdUcLW8sZ8H0C4xnEtW1IsBaJa5Pg==',
    'pragma': 'no-cache',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAPCnTQLqza4Xqu-uO7KZHcKuILkO7RRz2oapyOC04AQ0?modal_id=7092308044108827940',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
}

param = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'aweme_id': '7092308044108827940',
    'cursor': '0',
    'count': '20',
    'item_type': '0',
    'insert_ids': '',
    'rcFT': '',
    'pc_client_type': '1',
    'version_code': '170400',
    'version_name': '17.4.0',
    'cookie_enabled': 'true',
    'screen_width': '1536',
    'screen_height': '864',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Edge',
    'browser_version': '110.0.1587.57',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '110.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '8',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '50',
    'webid': '7204858005379991043',
    'msToken': 'v6YVp4xPaZJTwn8FSNEiS8lQJdIcQ0XsudNB17exHNtF8KfYYEWnNuuQHTxRGBN0rOYoI9h64rghttDlaHPDZyKI62cAd7sqXVdUcLW8sZ8H0C4xnEtW1IsBaJa5Pg==',
    'X-Bogus': '',
}

respone = requests.get(url=url, headers=header, params=param)
print(respone)
print(respone.text)
