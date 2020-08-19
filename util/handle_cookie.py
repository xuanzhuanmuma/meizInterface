# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: handle_cookie.py
@time: 2020/8/17 16:42
"""
import time

from util.handle_json import HandleJson


# {
#   "app_cookie": {
#      "appid": "aaaa"
#   },
#   "web": {
#     "cookie": "bbbbb"
#   }
# }


class HandleCookie(object):

    def get_cookies(self):
        json_data = HandleJson().read_json('cookie.json')
        return json_data

    # 获取cookie
    def get_cookie_value(self, cookie_key):
        json_data = self.get_cookies()
        return json_data[cookie_key]

    # 写入cookie
    def write_cookie(self, data, cookie_key):
        json_data = self.get_cookie_value(cookie_key)
        json_data[cookie_key] = data
        HandleJson().write_value('cookie.json', json_data)

if __name__ == '__main__':
    update_data = {
        "appid": "qwerttyutuy"
    }
    print(HandleCookie().write_cookie(update_data, 'app_cookie'))
    time.sleep(3)
    print(HandleCookie().get_cookie_value('app_cookie'))

