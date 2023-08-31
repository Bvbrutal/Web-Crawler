import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

import hashlib


def md5_hash(input_string):
    # ����һ��MD5��ϣ����
    md5_hasher = hashlib.md5()

    # ���¹�ϣ���������
    md5_hasher.update(input_string.encode('utf-8'))

    # ��ȡʮ�����Ʊ�ʾ�Ĺ�ϣֵ
    hash_value = md5_hasher.hexdigest()

    return hash_value
# Simulated public key (replace with your actual public key)
public_key_pem = b"""
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCq8e9qRpHJCnicpJQL26MMaxkVxSxuRDieHcl/6zCQBZxaicOzMGeArs+OJgDyVcuVpZmJopMRP4xYSycHRPbIuvozJQyC2xbntCnZDkim7N4gJvsuBYEMhHegWUi4EN4Shknko1vAtzQCTBrKuQcgUFiHpz0vAGktjO0RaN2tzwIDAQAB
-----END PUBLIC KEY-----
"""

# String to be encrypted
data_to_encrypt = "appid=846a15365f614921a5617cd1c2478129&message={}&nonce=v642jqv17c0nOfk1sDsX2Kv5y7JfJD9F&timestamp=1693288502573"
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
print("Encrypted Data (Base64):", encrypted_data_base64)
