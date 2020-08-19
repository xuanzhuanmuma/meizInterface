# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: handler_header.py
@time: 2020/8/18 14:29
"""
import hashlib
from util.handle_json import HandleJson


class HandleHeader(object):
    def get_header(self):
        headers = HandleJson().read_json('header.json')
        return headers

    def header_md5(self):
        header_data = self.get_header()
        value_data = header_data['token']
        # value_data.encode()#变成bytes类型才能加密
        m = hashlib.md5(value_data.encode())
        return m.hexdigest()

if __name__ == '__main__':
    print(HandleHeader().get_header())
    print(HandleHeader().header_md5())

