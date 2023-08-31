import requests
mistoken=''
url = "https://www.douyin.com/aweme/v1/web/discover/search/"
params = {
    # 'device_platform': 'webapp',
    # 'aid': '6383',
    # 'channel': 'channel_pc_web',
    # 'search_channel': 'aweme_user_web',
    'keyword': '比亚迪海豹',
    # 'search_source': 'switch_tab',
    # 'query_correct_type': '1',
    # 'is_filter_search': '0',
    # 'offset': '0',
    # 'count': '10',
    # 'pc_client_type': '1',
    # 'version_code': '170400',
    # 'version_name': '17.4.0',
    # 'cookie_enabled': 'true',
    # 'screen_width': '1536',
    # 'screen_height': '864',
    # 'browser_language': 'zh-CN',
    # 'browser_platform': 'Win32',
    # 'browser_name': 'Edge',
    # 'browser_version': '115.0.1901.183',
    # 'browser_online': 'true',
    # 'engine_name': 'Blink',
    # 'engine_version': '115.0.0.0',
    # 'os_name': 'Windows',
    # 'os_version': '10',
    # 'cpu_core_num': '8',
    # 'device_memory': '8',
    # 'platform': 'PC',
    # 'downlink': '10',
    # 'effective_type': '4g',
    # 'round_trip_time': '50',
    # 'webid': '7253998714157630976',
    # 'msToken': 'DJZBIqwY664s8j0tm_VJ8eKjnal5ADg10zHHW6n3JHxqsJd51Eksyjvw9BYQjc49DZexM0WCKzQv4-rEqd_rtQKG0fo0eYvFWUx_Zp6-y4ZK_TZauQ6WGQ==',
    # 'X-Bogus': 'DFSzswVLZuiANruttH-bHQppgiuk',
    'cookie': f'passport_csrf_token=a5a463d89b639104eda3daf01bf37175; passport_csrf_token_default=a5a463d89b639104eda3daf01bf37175; s_v_web_id=verify_ljsvb93h_1dCMUNva_nktV_47Pd_BemO_zZU5mJVvxSZq; __bd_ticket_guard_local_probe=1688751956466; passport_assist_user=CjwB0HArNNeJ5lbLFlXHpJrNAF-tEvxVLEcjL-JfeTa-QtmBvpgF79yJWF17ex87axYgqt8r0tTdBQNuJ5EaSAo80DhhS6Oc_8FzJsKIyGuCg6_hsYd4S0vRudlX7_skafv2b5dldXKcDWh_hNoLWP4Ztd3nc2g5vVlYzm2NENbwtQ0Yia_WVCIBA_QhdFU%3D; n_mh=Jwkk2k_pB7o9GglfgboeGMNnyekRAeWbIMJVBLEmdpU; sso_uid_tt=ad19c6ade9db63870ec4301b963941cd; sso_uid_tt_ss=ad19c6ade9db63870ec4301b963941cd; toutiao_sso_user=1a546660c204587a9b54c9f9c27bfafe; toutiao_sso_user_ss=1a546660c204587a9b54c9f9c27bfafe; sid_ucp_sso_v1=1.0.0-KGU1ZDU5MDM5ZDZkOTFlNmVlNDhjNDFlNDI1YjM5NGI5ODcwNGJhMTgKHQijn8W17AEQj6ChpQYY7zEgDDD76pvLBTgCQO8HGgJobCIgMWE1NDY2NjBjMjA0NTg3YTliNTRjOWY5YzI3YmZhZmU; ssid_ucp_sso_v1=1.0.0-KGU1ZDU5MDM5ZDZkOTFlNmVlNDhjNDFlNDI1YjM5NGI5ODcwNGJhMTgKHQijn8W17AEQj6ChpQYY7zEgDDD76pvLBTgCQO8HGgJobCIgMWE1NDY2NjBjMjA0NTg3YTliNTRjOWY5YzI3YmZhZmU; odin_tt=f90b311fcf98f1031dd3fdf8a1ca8c9e0f94bb722eb3b262f75ac46b640e841e92a701584cb614d044bbb6672d97059e; uid_tt=cf58cb3df72eb93ed8068acd262f8cb0; uid_tt_ss=cf58cb3df72eb93ed8068acd262f8cb0; sid_tt=aa6b2987b064a596d9de06df031d4c23; sessionid=aa6b2987b064a596d9de06df031d4c23; sessionid_ss=aa6b2987b064a596d9de06df031d4c23; LOGIN_STATUS=1; store-region=cn-cq; store-region-src=uid; sid_guard=aa6b2987b064a596d9de06df031d4c23%7C1688752154%7C5183992%7CTue%2C+05-Sep-2023+17%3A49%3A06+GMT; sid_ucp_v1=1.0.0-KDBhYTgyZjZhODZiZTIwOTRhNjg1MWI2MDQ0MDg2ZjFhZmUzMTI0MGEKGQijn8W17AEQmqChpQYY7zEgDDgCQO8HSAQaAmhsIiBhYTZiMjk4N2IwNjRhNTk2ZDlkZTA2ZGYwMzFkNGMyMw; ssid_ucp_v1=1.0.0-KDBhYTgyZjZhODZiZTIwOTRhNjg1MWI2MDQ0MDg2ZjFhZmUzMTI0MGEKGQijn8W17AEQmqChpQYY7zEgDDgCQO8HSAQaAmhsIiBhYTZiMjk4N2IwNjRhNTk2ZDlkZTA2ZGYwMzFkNGMyMw; bd_ticket_guard_server_data=; __security_server_data_status=1; my_rd=1; pwa2=%220%7C0%7C3%7C0%22; ttwid=1%7CqRB3BsR-L7cuhJ8aBYJIYEdbxJrOcEIcOrLx8e_77ow%7C1688953212%7C5abe783349c9c04c6c862fac715285084372eaafa41a4185a2196d1bb7dbedc0; __live_version__=%221.1.1.1250%22; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; webcast_local_quality=null; strategyABtestKey=%221690444103.133%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1691048903867%2C%22type%22%3Anull%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.54%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNzciI6Ii0tLS0tQkVHSU4gQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbk1JSUJEekNCdFFJQkFEQW5NUXN3Q1FZRFZRUUdFd0pEVGpFWU1CWUdBMVVFQXd3UFltUmZkR2xqYTJWMFgyZDFcclxuWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRTk4ZlduVFpSVlNDdTJVVldkcHdIemFrZVxyXG5DdUZLWDJkRkFEMGkzUjdFVWJZRW1XVG1ZNjhldktlcmUyT1NRU2RvYlNpZlFVWkdWMUdEbEpUbXg1RXkwNkFzXHJcbk1Db0dDU3FHU0liM0RRRUpEakVkTUJzd0dRWURWUjBSQkJJd0VJSU9kM2QzTG1SdmRYbHBiaTVqYjIwd0NnWUlcclxuS29aSXpqMEVBd0lEU1FBd1JnSWhBS0IycE8rOGpBSE5mRUQxbS9rZ1NEaXQ0STlwMFJzR0V3VzBkaWdoTnVjelxyXG5BaUVBOW5KbzYyOVVnYTBUSEtJcU5Fai9EYXczMlNwem9TTStpQWlmK3RQK3pKZz1cclxuLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbiJ9; __ac_nonce=064c2214d004cf9d6ed5d; __ac_signature=_02B4Z6wo00f01eEZ1awAAIDAFGY.MHm44iHhOdEAAByGFQPPtq2BJarSYbN1ogz3UZqcrfuKbInFOhnH3xAGZHSBQe4tqWxuF2PjsIoYr7022OmD9OY3rdFU0x3NsldGUJ5SaR1v0xQA4Utvda; SEARCH_RESULT_LIST_TYPE=%22single%22; home_can_add_dy_2_desktop=%221%22; passport_fe_beating_status=true; msToken=kQn5DaTV2FAMuURM6ffe_B3JVYlf472i8JlZgKymstZdqVOLeD2l1r94rcgQbLxOCh1M8qF34QiaplpkNa-_J2z3BVRr_u6YlveKOk2RmrnLGUZaI8HWRA==; tt_scid=SuJTz3er3YrJlPhvA-F9LqWWTknRT2plnqlBSku2UwnMabKArhIZojNM-MFU.rilfe3c; download_guide=%221%2F20230727%2F0%22; csrf_session_id=0a2a3668665e775cdc7cd133bf5285cf; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAqmyknRBubMFKUD8v9QIBzE2RUkvaojgY8zGlbRUOSag%2F1690473600000%2F0%2F0%2F1690444773190%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAqmyknRBubMFKUD8v9QIBzE2RUkvaojgY8zGlbRUOSag%2F1690473600000%2F0%2F1690444173191%2F0%22; publish_badge_show_info=%221%2C0%2C0%2C1690444116205%22; msToken={mistoken}',

}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
}
result = requests.get(url, headers=header, params=params)
result = result.content #FIXME: no result
print(result)
