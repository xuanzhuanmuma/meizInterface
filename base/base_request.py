# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: base_request.py
@time: 2020/8/13 9:45
"""
import requests

from util.handle_ini import HandleIni
from util.handle_cookie import HandleCookie


class BaseRequest(object):
    def send_post(self, url, data, headers=None, cookie=None, get_cookie=None):
        '''发送post请求'''
        response = requests.post(url=url, data=data, headers=headers, cookies=cookie)
        if get_cookie is not None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            # 是app或者web
            HandleCookie().write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response
        return res

    def send_get(self, url, data, headers=None, cookie=None, get_cookie=None):
        '''发送get请求'''
        response = requests.get(url=url, params=data, headers=headers, cookies=cookie)
        if get_cookie is not None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            # 是app或者web
            HandleCookie().write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response
        return res

    def run_main(self, method, url, data, headers=None, cookie=None, get_cookie=None):
        '''执行方法，传递method, url, data参数'''
        base_url = HandleIni().get_value('server', 'host')
        if 'http' not in url or 'https' not in url:
            url = base_url + url
        if method == 'get':
            res = self.send_get(url, data, headers, cookie, get_cookie)
        else:
            res = self.send_post(url, data, headers, cookie, get_cookie)
        return res

    def get_text(self, res):
        '''通过文本的形式获取响应内容'''
        return res.text

    def get_content(self, res):
        '''通过content获取的内容便是二进制类型的'''
        return res.content

    def get_json_(self, res):
        '''json响应数据'''
        return res.json()

    def get_respost_encoding(self, res):
        '''通过encoding获取响应内容的编码及修改编码'''
        return res.encoding

    def get_respose_code(self, res):
        '''获取响应状态码'''
        return res.status_code

    def get_respost_head(self, res):
        '''获取响应头'''
        return res.headers

'''单例'''
request = BaseRequest()


