# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: base_request.py
@time: 2020/8/13 9:45
"""
import requests

from util.handle_ini import HandleIni


class BaseRequest(object):
    def send_post(self, url, data):
        '''发送post请求'''
        headers = {'token': '12345hzzxkj67890'}
        res = requests.post(url=url, data=data, headers=headers)
        return res

    def send_get(self, url, data):
        '''发送get请求'''
        headers = {'token': '12345hzzxkj67890'}
        res = requests.get(url=url, params=data, headers=headers)
        return res

    def run_main(self, method, url, data):
        '''执行方法，传递method, url, data参数'''
        base_url = HandleIni().get_value('server', 'host')
        if 'http' not in url or 'https' not in url:
            url = base_url + url
        if method == 'get':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
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


