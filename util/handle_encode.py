# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: handle_encode.py
@time: 2020/8/14 14:42
"""
import base64
from Crypto.Cipher import AES
# 密钥（key）, 密斯偏移量（iv） CBC模式加密


class HandleEncode(object):
    def AES_Encrypt(key, data):
        '''加密'''
        vi = '0102030405060708'
        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        data = pad(data)
        # 字符串补位
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
        encryptedbytes = cipher.encrypt(data.encode('utf8'))
        # 加密后得到的是bytes类型的数据
        encodestrs = base64.b64encode(encryptedbytes)
        # 使用Base64进行编码,返回byte字符串
        enctext = encodestrs.decode('utf8')
        # 对byte字符串按utf-8进行解码
        return enctext

    def AES_Decrypt(key, data):
        '''解密'''
        vi = '0102030405060708'
        data = data.encode('utf8')
        encodebytes = base64.decodebytes(data)
        # 将加密数据转换位bytes类型数据
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
        text_decrypted = cipher.decrypt(encodebytes)
        unpad = lambda s: s[0:-s[-1]]
        text_decrypted = unpad(text_decrypted)
        # 去补位
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted