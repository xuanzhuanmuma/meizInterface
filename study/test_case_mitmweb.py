# encoding: utf-8
"""
@author: yanNa
@software: PyCharm
@file: test_case_mitmweb.py
@time: 2020/8/21 14:49
"""
from mitmproxy import http
from util.handle_json import HandleJson
import json

class GetData():
    def request(self, flow):
        request_data = flow.request
        self.request_url = request_data.url
        request_pr = request_data.query
        request_form = request_data.urlencoded_form
        print('url=========', self.request_url)
        print('pr===========', request_pr)
        print('form=========', request_form)

    def response(self, flow):
        if 'meis' in self.request_url:
            response_data = flow.response
            host = self.request_url.split('meis')[0]
            print(host)
            base_url = host[0]
            url = host[1]
            if '?' in host[1]:
                url = url.split('?')[0]
            data = HandleJson().get_value(url)
            print('=========data:', data)
            response_data.set_text(json.dumps(data))

            '''
            response_header = response_data.headers
            content_type = response_header['Content-Type']
            if 'image/jpeg' in content_type:
                print('这个返回的是图片')
            elif 'application/json' in content_type:
                status_code = response_data.status_code
                text = response_data.text
                print('code===========', status_code)
                print('text===========', text)
            else:
                print('格式不是我们预期的')
            '''


addons = [
    GetData()
]
