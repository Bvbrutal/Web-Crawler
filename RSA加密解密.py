# -*- coding: UTF-8 -*-
import base64
import time
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import datetime
import random
import string
import requests
import time

public_key_pem = b"""
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCq8e9qRpHJCnicpJQL26MMaxkVxSxuRDieHcl/6zCQBZxaicOzMGeArs+OJgDyVcuVpZmJopMRP4xYSycHRPbIuvozJQyC2xbntCnZDkim7N4gJvsuBYEMhHegWUi4EN4Shknko1vAtzQCTBrKuQcgUFiHpz0vAGktjO0RaN2tzwIDAQAB
-----END PUBLIC KEY-----
"""

def get_sequence():
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return current_time + random_digits


def get_nonce(t=32):
    e = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
    n = len(e)
    a = ""
    for i in range(t):
        a += e[random.randint(0, n - 1)]
    return a


def md5_hash(input_string):
    # 创建一个MD5哈希对象
    md5_hasher = hashlib.md5()

    # 更新哈希对象的内容
    md5_hasher.update(input_string.encode('utf-8'))

    # 获取十六进制表示的哈希值
    hash_value = md5_hasher.hexdigest()

    return hash_value

def get_signature(nonce,timestmp):
    # Simulated public key (replace with your actual public key)
    # String to be encrypted 846a15365f614921a5617cd1c2478129
    data_to_encrypt = '''appid=A500120190100001&message={"cityId":"5000","stationId":"210"}'''+f"&nonce={nonce}&timestamp={timestmp}"
    print(data_to_encrypt)
    data_to_encrypt=md5_hash(data_to_encrypt).upper()
    print(data_to_encrypt)
    # Load the public key
    public_key = serialization.load_pem_public_key(public_key_pem, backend=default_backend())

    # Encrypt the data using the public key
    encrypted_data = public_key.encrypt(
        data_to_encrypt.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Encode the encrypted data in Base64
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')

    # Print Base64 encoded encrypted data
    print(encrypted_data_base64)
    return encrypted_data_base64,sequence

def make_request():
    # url = 'https://ycx.cqmetro.cn/bas/ncp/v1/appiont/list'
    url='https://ycx.cqmetro.cn/bas/ncp/v1/appiont/list'
    header = {
        'Host': 'ycx.cqmetro.cn',
        'Referer': 'https://ycx.cqmetro.cn/app-h5/appointment/',
        'appid': 'A500120190100001',
        'Cookie': 'acw_tc=2f624a7b16933740256818517e45dfd2479b392cca015d4cbb542d1ef41054',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BWTJSBridge/1.1.0',
        'app_version': '1.21.0',
        'Origin': 'https://ycx.cqmetro.cn',
        'signature': f'{encrypted_data_base64}',
        'version': '0100',
        'nonce': f'{nonce}',
        'Content-Length': '33',
        'bundleId': 'com.bwton.msx.ycx',
        'token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzZTNhZDI1Yi0yMzg3LTQ2NzgtOWIyOS0wZWFhNzRiYWM1NzciLCJpc3MiOiJZYW5ZYW4iLCJzdWIiOiJ7XCJ1c2VySWRcIjpcIjc5MDExMTI2ODI5MjA5NjBcIixcInVuaW9uSWRcIjpcIjEwMDAwMDE1NzkwMTExMjY4MjkyMDk2MFwiLFwib3BlbmFwaWFjY291bnRcIjpcIjc5MDExMTI2ODI5MjA5NjBcIixcIm5ld0RldmljZUlkXCI6XCIxNGI4N2UxZmQ4NjA5MjI1MDQwNmQxYjViNjAyZTY5N1wiLFwibmV3RGV2aWNlVHlwZVwiOlwiMVwifSIsImlhdCI6MTY5MzI5NDc5MywiZXhwIjoxNjk1ODg2NzkzfQ.FmWvL1K53uz9aHY8sBczsHTCAS1nUA57Vk2-uD-42AY',
        'cityId': '5000',
        'timestamp': f'{timestmp}',
        'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive',
        'X-Ca-Version': 'v1.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
        'sequence': f'{sequence}',
        'X-Ca-Signature-Version': '1',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    data = {"cityId": 5000, "stationId": "210"}
    rea = requests.post(url, header,json=data)
    print(rea.text)
    return rea.text

if __name__ == '__main__':
    sequence = get_sequence()
    nonce = get_nonce()
    timestmp = int(time.time() * 1000)
    print(sequence,nonce,timestmp)
    encrypted_data_base64=get_signature(nonce,timestmp)
    result=make_request()
