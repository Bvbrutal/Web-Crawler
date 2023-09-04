# -*- coding: utf-8 -*-
# import time
#
# import requests
#
# url = 'https://ycx.cqmetro.cn/bas/ncp/v1/appiont/submit'
#
# header = {
#     'Host': 'ycx.cqmetro.cn',
#     'Referer': 'https://ycx.cqmetro.cn/app-h5/appointment/',
#     'appid': 'A500120190100001',
#     'Cookie': 'acw_tc=2f61f27c16932013512411888e5cf056bcd1659d0751cdce2a68c557c024b4',
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BWTJSBridge/1.1.0',
#     'app_version': '1.21.0',
#     'Origin': 'https://ycx.cqmetro.cn',
#     'signature': 'E4xUMqbn30OUqSn815Aj47jjhEC+kQDhle6ATTAsrIeQZNJGLefGnNyu0UwgKS9xSJqUIWxQ8w/Wo0DGUBejXfz4th3fP9kdczEYl4u26csEU0HM5kNzSdRBw5OuBkTb5JoJp6+SdAcCq0QfURMZnwemiKGDBvCDtbUewiuOyPQ=',
#     'version': '0100',
#     'nonce': 'KWasGwpHX7bn3Zipx8mEj3MyAmwT57mG',
#     'Content-Length': '41',
#     'bundleId': 'com.bwton.msx.ycx',
#     'token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjMzk4YWNhMS01ZmJjLTRhY2QtODAzMS0xN2RhZjZhNmE1YTYiLCJpc3MiOiJZYW5ZYW4iLCJzdWIiOiJ7XCJ1c2VySWRcIjpcIjc5MDExMTI2ODI5MjA5NjBcIixcInVuaW9uSWRcIjpcIjEwMDAwMDE1NzkwMTExMjY4MjkyMDk2MFwiLFwib3BlbmFwaWFjY291bnRcIjpcIjc5MDExMTI2ODI5MjA5NjBcIixcIm5ld0RldmljZUlkXCI6XCIxNGI4N2UxZmQ4NjA5MjI1MDQwNmQxYjViNjAyZTY5N1wiLFwibmV3RGV2aWNlVHlwZVwiOlwiMVwifSIsImlhdCI6MTY5MjcwMDQyMywiZXhwIjoxNjk1MjkyNDIzfQ.4y1bfxivuFHQNn5CVQWH9UQbXHE-YOfebzNwAfSwahw',
#     'cityId': '5000',
#     'timestamp': f'{int(time.time()*1000)}',
#     # 1693202466621
#     'Accept-Language': 'zh-cn',
#     'Connection': 'keep-alive',
#     'X-Ca-Version': 'v1.0',
#     'Accept': 'application/json',
#     'Content-Type': 'application/json;charset=utf-8',
#     'sequence': '202308281401064728860019',
#     'X-Ca-Signature-Version': '1',
#     'Accept-Encoding': 'gzip, deflate, br',
# }
#
# print(int(time.time()*1000))
#
# data = {"instationRuleId": 138781, "tripMode": "1"}
# res = requests.get(url, headers=header,json=data)
# print(res.content.decode('utf-8'))


import datetime
import random


def get_sequence():
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return current_time + random_digits


# # 示例使用
# sequence = get_sequence()
# print("Generated Sequence:", sequence)

import random
import string


def get_nonce(length=32):
    characters = string.ascii_letters + string.digits
    nonce = ''.join(random.choice(characters) for _ in range(length))
    return nonce


# # 示例使用
# nonce = get_nonce()
# print("Generated Nonce:", nonce)
#

import time


def get_timestamp():
    return int(time.time() * 1000)  # Convert seconds to milliseconds


# 示例使用
# timestamp = get_timestamp()
# print("Current Timestamp:", timestamp)


# import hashlib
#
#
# def get_signature(message, isRequest, nonce, timestamp):
#     # 初始化 appInfo，这部分需要根据你的具体实现进行修改
#     app_info = {
#         "appId": "846a15365f614921a5617cd1c2478129",
#         "appKey": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCq8e9qRpHJCnicpJQL26MMaxkVxSxuRDieHcl/6zCQBZxaicOzMGeArs+OJgDyVcuVpZmJopMRP4xYSycHRPbIuvozJQyC2xbntCnZDkim7N4gJvsuBYEMhHegWUi4EN4Shknko1vAtzQCTBrKuQcgUFiHpz0vAGktjO0RaN2tzwIDAQAB"
#     }
#
#     # 构建签名字符串
#     signature_str = f"appid={app_info['appId']}&message={message}&nonce={nonce}&timestamp={timestamp}"
#
#     if isRequest:
#         signature_str += "&requestType=1"  # 仅在请求时添加此参数
#
#     print("签名字符串:", signature_str)
#
#     # 计算签名
#     signature = hashlib.md5(signature_str.encode()).hexdigest().upper()
#     print("计算得到的签名:", signature)
#
#     return signature
#


# # 示例使用
# message = ""
# is_request = True  # 在请求时为 True，响应时为 False
# nonce = get_nonce(length=32)
# timestamp = get_timestamp()
#
# signature = get_signature(message, is_request, nonce, timestamp)
# print("Final Signature:", signature)


#
# import hashlib
# import random
# import time
# from Crypto.Cipher import AES
#
# class YourClass:
#     def getSignature(self, data, needSignature, nonce, timestamp):
#         self.initAppInfo()
#
#         self.signatureInfo = self.appInfo
#         e = hashlib.md5(data.encode()).hexdigest()
#         n = ""
#
#         if needSignature:
#             n = "appid=" + self.signatureInfo['appId'] + "&message=" + e + "&nonce=" + nonce + "&timestamp=" + timestamp
#         else:
#             n = e
#
#         print(n)
#         a = n.upper()
#
#         print("公钥是：")
#         print(self.signatureInfo['appKey'])
#
#         cipher = AES.new(self.signatureInfo['appKey'].encode(), AES.MODE_ECB)
#         encrypted = cipher.encrypt(a.encode())
#         encrypted_hex = encrypted.hex()
#
#         return encrypted_hex
#
#     def initAppInfo(self):
#         # Your code to fetch and decrypt appInfo
#         # For example:
#         self.appInfo = {
#             'appId': '846a15365f614921a5617cd1c2478129',
#             'appKey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCq8e9qRpHJCnicpJQL26MMaxkVxSxuRDieHcl/6zCQBZxaicOzMGeArs+OJgDyVcuVpZmJopMRP4xYSycHRPbIuvozJQyC2xbntCnZDkim7N4gJvsuBYEMhHegWUi4EN4Shknko1vAtzQCTBrKuQcgUFiHpz0vAGktjO0RaN2tzwIDAQAB'
#         }
#
# # Usage
# your_instance = YourClass()
# data = ""
# need_signature = True
# nonce = get_nonce(length=32)
# timestamp = str(int(time.time())*1000)
#
# signature = your_instance.getSignature(data, need_signature, nonce, timestamp)
# print("Signature:", signature)

# import execjs
# from urllib import parse
#
#
# with open('static/js/ycx.js', 'r', encoding='utf-8') as f:
#     fu_ = f.read()
# ctx = execjs.compile(fu_)
# t={}
# time_ = ctx.call('getHeaders',t)
# print(time_)


import hashlib
import hmac
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


class SignatureHelper:
    def __init__(self):
        self.app_info = {
            'appId': 'A500120190100001',
            'appKey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCq8e9qRpHJCnicpJQL26MMaxkVxSxuRDieHcl/6zCQBZxaicOzMGeArs+OJgDyVcuVpZmJopMRP4xYSycHRPbIuvozJQyC2xbntCnZDkim7N4gJvsuBYEMhHegWUi4EN4Shknko1vAtzQCTBrKuQcgUFiHpz0vAGktjO0RaN2tzwIDAQAB'
        }
        self.signature_info = self.app_info

    def generate_signature(self, message, nonce, timestamp):
        app_id = self.signature_info['appId']
        # data = f'appid={app_id}&message={message}&nonce={nonce}&timestamp={timestamp}'
        data = 'appid=846a15365f614921a5617cd1c2478129&message=&nonce=v642jqv17c0nOfk1sDsX2Kv5y7JfJD9F&timestamp=1693288502573'
        encrypted_signature = self.rsa_encrypt(data)
        return encrypted_signature

    def rsa_encrypt(self, data):
        public_key_pem = """
        -----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCq8e9qRpHJCnicpJQL26MMaxkV
        xSxuRDieHcl/6zCQBZxaicOzMGeArs+OJgDyVcuVpZmJopMRP4xYSycHRPbIuvoz
        JQyC2xbntCnZDkim7N4gJvsuBYEMhHegWUi4EN4Shknko1vAtzQCTBrKuQcgUFiH
        pz0vAGktjO0RaN2tzwIDAQAB
        -----END PUBLIC KEY-----
        """
        with open("../public.pem", "rb") as public_pem_file:
            print(public_pem_file.read())
            public_key = serialization.load_pem_public_key(
                public_pem_file.read(),
                backend=default_backend()
            )
        # # 从 PEM 格式的公钥加载公钥对象
        # public_key = serialization.load_pem_public_key(
        #     public_key_pem.encode("utf-8"),
        #     backend=default_backend()
        # )

        # 使用公钥进行加密
        ciphertext = public_key.encrypt(
            plaintext=data.encode('utf-8'),
            padding=padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext


# Example usage
helper = SignatureHelper()
message = ""
nonce = get_nonce()
timestamp = get_timestamp()

encrypted_signature = helper.generate_signature(message, nonce, timestamp)
print("Encrypted Signature:", encrypted_signature)
